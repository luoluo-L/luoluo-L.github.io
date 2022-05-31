---
layout: single
title:  "Reading notes of Deep Learning book by Goodfellow et al."
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
categories: 
  - Jekyll
tags:
  - python
---

Reading notes of book: Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville

---

Chapter 10: Sequence Modelling: Recurrent and Recursive Nets
---

**Recurrent Neural Networks(RNNs)** processes sequential data $\boldsymbol{x}^{(1)}, \boldsymbol{x}^{(2)}, ..., \boldsymbol{x}^{(\tau)}$.


Take advantage of the benefits of **shared parameters**: 
- generalize to varience length
- share statistical stregth across different sequence length and positions in time.
  
  Local time/location-invariant property is prefered for some task. Example: Say task is to identify time to go to Nepal, then we want to learn similar features from sentences: setence 1: I went to Nepal in 2009; Setence 2: in 2009, I went to Nepal. We want to identify the year in either locations of the sentence.


Unfolding Computational Graphs
---

A classical form of a dynamical system: 
$\boldsymbol{s}^{(t)} = f ( \boldsymbol{s}^{(t-1)}; \theta)$, where $s$ is the state of system, and $\theta$ is parameter. This is recurrent because the definition of state $s$ at $t$ referes back to the same definition at time $t - 1$.

Unfold a finite step dynamical system:
$\boldsymbol{s}^{(T)} = f( \boldsymbol{s}^{(T-1)}; \theta ) = f (f (\boldsymbol{s}^{(T-2)} ; \theta) ; \theta)$.

Classical form of a dynamical system with external input signal $\boldsymbol{x}$: $\boldsymbol{s}^{(t)} = f ( \boldsymbol{s}^{(t-1)}, \boldsymbol{x}^{(t)}; \theta)$.

Recurrent Neural Network notations commonly use $\boldsymbol{h}$ to denote hidden states: 

$\boldsymbol{h}^{(t)} = f ( \boldsymbol{h}^{(t-1)}, \boldsymbol{x}^{(t)}; \theta)$.

Two representations of RNNs: the recurrent graph and the unfolded graph. The recurrent graph is a succinct/brief notation. Unfolded graph provides explict description and flow (useful for cases like bi-directional RNNs).

Recurrent Neural Networks (RNNs)
----



Recursive Neural Networks
---
Main difference to Recurrent Neural Networks: **Recursive neural networks** are structured as **deep tree**, whereas **Recurrent neural networks** have  **chain-like structure**.

Previous work has succesfully applied recursive neural networks in NLP and CV fields. 




