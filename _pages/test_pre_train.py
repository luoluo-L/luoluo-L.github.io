import torch
import torch.nn as nn
import torch.optim as optim


# ----- 1. Placeholder CNN Feature Extractor -----
class CNNFeatureExtractor(nn.Module):
    def __init__(self, input_dim, feature_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, feature_dim)

    def forward(self, x):
        # x: [batch_size, seq_len, input_dim]
        return self.linear(x)  # [batch_size, seq_len, feature_dim]


# ----- 2. Decoder-Only Transformer -----
class DecoderOnlyTransformer(nn.Module):
    def __init__(self, feature_dim, nhead=4, num_layers=2, max_len=512):
        super().__init__()
        self.pos_embedding = nn.Embedding(max_len, feature_dim)
        decoder_layer = nn.TransformerDecoderLayer(d_model=feature_dim, nhead=nhead)
        self.transformer = nn.TransformerDecoder(decoder_layer, num_layers=num_layers)
        self.output_head = nn.Linear(feature_dim, feature_dim)

    def forward(self, x, mask):
        batch_size, seq_len, _ = x.size()
        pos_ids = torch.arange(seq_len, device=x.device).unsqueeze(0)
        pos_embed = self.pos_embedding(pos_ids)  # [1, seq_len, feature_dim]
        x = x + pos_embed

        x = x.transpose(0, 1)  # [seq_len, batch, feature_dim]
        output = self.transformer(tgt=x, memory=x, tgt_mask=mask)
        return self.output_head(output.transpose(0, 1))  # [batch, seq_len, feature_dim]


# ----- 3. Causal Mask (Upper Triangular) -----
def generate_causal_mask(seq_len, device):
    mask = torch.triu(torch.full((seq_len, seq_len), float('-inf'), device=device), diagonal=1)
    return mask


# ----- 4. Training Config -----
batch_size = 8
seq_len = 10
input_dim = 16
feature_dim = 64
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----- 5. Simulated Data -----
x_data = torch.randn(batch_size, seq_len, input_dim).to(device)

# ----- 6. Model Setup -----
cnn = CNNFeatureExtractor(input_dim, feature_dim).to(device)
transformer = DecoderOnlyTransformer(feature_dim).to(device)
optimizer = optim.Adam(list(cnn.parameters()) + list(transformer.parameters()), lr=1e-4)
criterion = nn.MSELoss()

# ----- 7. Training Loop -----
cnn.train()
transformer.train()
train_loss_list = []

for epoch in range(10):
    # Step 1: Feature extraction
    features = cnn(x_data)  # [batch, seq_len, feature_dim]

    # Step 2: Prepare targets (shift left) and pad last position
    target = features[:, 1:, :]  # next-step targets
    pad = torch.zeros_like(target[:, :1, :])  # dummy last target
    target_padded = torch.cat([target, pad], dim=1)  # [batch, seq_len, feature_dim]

    # Step 3: Generate causal mask for Transformer
    causal_mask = generate_causal_mask(seq_len, x_data.device)

    # Step 4: Forward pass
    preds = transformer(features, mask=causal_mask)  # [batch, seq_len, feature_dim]

    # Step 5: Create loss mask to ignore last timestep
    loss_mask = torch.ones(seq_len, dtype=torch.bool, device=device)
    loss_mask[-1] = False  # ignore last token
    loss_mask = loss_mask.unsqueeze(0).expand(batch_size, -1)  # [batch, seq_len]
    #print(target_padded.shape)
    # Step 6: Masked loss computation
    masked_preds = preds[loss_mask]
    masked_targets = target_padded[loss_mask]
    #print(masked_targets.shape)

    loss = criterion(masked_preds, masked_targets)
    train_loss_list.append(loss)
    # Step 7: Backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch + 1} | Loss: {loss.item():.6f}")
