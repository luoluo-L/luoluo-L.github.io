---
title: 'notes for contrastive learning'
date: 2199-01-01
permalink: /posts/2022/03/blog-post-1/
tags:
  - AI
  - contrastive learning
  - unsupervised learning
  - in progress
---

Contrastive learning
----

Contrastive learnining is a unsupervised technique that enables encoder to generate good representations by 
encoraging embeddings from similar inputs toghether and increase distance of dissimilar pairs.

Learnings: transformation of data augmentation should be composed of at least $2$ transformations.
Even though augmentated data have larger variances than using one transformation (commomly used for supervised learning tasks) and makes discriminative tasks harder, it improves results of contrastive learning. 



a good code implementation tutorial is here:
https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial17/SimCLR.html

a good summary of contrastive learning for visual and sentence application is here:

https://lilianweng.github.io/posts/2021-05-31-contrastive/