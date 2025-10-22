import torch
import torch.nn as nn
from transformers import InformerForPrediction, InformerConfig

class CNNInformerWrapper(nn.Module):
    def __init__(self, cnn_input_dim, cnn_out_dim, informer_model_name="huggingface/informer"):
        super().__init__()

        # 1. CNN Preprocessor
        self.cnn = nn.Sequential(
            nn.Conv1d(cnn_input_dim, cnn_out_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(cnn_out_dim, cnn_out_dim, kernel_size=3, padding=1),
            nn.ReLU()
        )

        # 2. Load Pretrained Informer
        self.informer = InformerForPrediction.from_pretrained(informer_model_name)

        # Check that cnn_out_dim matches Informer's expected input size
        assert self.informer.config.enc_in == cnn_out_dim, \
            f"cnn_out_dim ({cnn_out_dim}) must match Informer input dim ({self.informer.config.enc_in})"

    def forward(self, x):
        # x: (B, L, F_in)
        x = x.permute(0, 2, 1)        # → (B, F_in, L)
        x = self.cnn(x)               # → (B, F_cnn, L)
        x = x.permute(0, 2, 1)        # → (B, L, F_cnn)

        # Pass to Informer
        output = self.informer(inputs_embeds=x)
        return output.logits  # (B, pred_len, D_out)


# Input: batch of 96-length sequences with 7 features
x = torch.randn(32, 96, 7)

model = CNNInformerWrapper(
    cnn_input_dim=7,
    cnn_out_dim=512  # Must match Informer config.enc_in
)

y_pred = model(x)
print(y_pred.shape)
