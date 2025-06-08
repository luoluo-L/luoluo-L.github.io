---
title: 'Wearable EDA Quality Model improves SOTA'
date: 2025-06-08
tags:
permalink: /posts/2026/06/blog-post-4/
  - Electrodermal activity
  - Wearables
---
Electrodermal activity (EDA) is a key indicator of sympathetic nervous system activation and a reliable marker of emotional arousal or stress. However, motion artifacts and connectivity issues often degrade EDA signal quality. To enable meaningful interpretation, it is essential to distinguish between high- and low-quality EDA signals.
We propose an EDA signal quality index system leveraging unsupervised pre-training—a strategy widely used in natural language processing models such as GPT.  Our approach achieve approximately $8\%$ in ROCAUC improvement compared to SOTA, while requiring only half the training epochs. This demonstrates that even with limited labeled data and a lightweight model, pre-training can significantly enhance EDA quality assessment, making it practical for real-time, wearable health applications.
