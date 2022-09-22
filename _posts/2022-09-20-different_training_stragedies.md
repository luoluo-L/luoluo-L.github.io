---
title: 'Different training testing set split stragedy: randomly vs by speakers'
permalink: /audio-mnist-tutorial/different_training_stragedies/
date: 2022-09-20
tags:
    - audio signal processing
    - classification
---

---

<!--
Audio MNIST data description and statistic analysis on durations
---
-->
We first download audio MNIST (digits) data from [here](https://www.kaggle.com/datasets/alanchn31/free-spoken-digits).  This is a balanced dataset in terms of labels/digits and speakers, with 6 male speakers and each person has 500 recordings for digits, 50 recordings per digits per person. Each digits have then 50 x 6 = 300 files.
We here describe the result of different training test fold split stragedy.

1. random split: we split training and test data by random split 
2. Split based on speakers: this senario is closer to real-world case applications where the data from the same speaker goes either training fold or test fold but not both.

Result of two different train test fold split stragedies
---


We plot the performance metric F1 score (micro) for multi-class classification, which is commonly used when all classes are balanced. For imbalanced problems, different weighted scheme for F1 scores can be found [here](https://towardsdatascience.com/micro-macro-weighted-averages-of-f1-score-clearly-explained-b603420b292f). We use 2/3 data for training and 2/3 data for testing. The max length was set to 0.8 seconds to preserve most data.

Here is the training performance (Top) and testing performance (Bottom). Training performances for two splitting scheme are relatively similar, especially around stable performance with increasing number of epochs. However, the testing performance for split for speakers suffers much more compared to random splitting. For split randomly, stable testing performance is around 0.85 whereas for split by speakers, the stable test performance is around 0.6 for the same number of total 40 epochs.

<img src='/images/audio_mnist_posts/figures/two_train_test_split_methods_train.png' width = '600'>



<img src='/images/audio_mnist_posts/figures/two_train_test_split_methods_test.png' width = '600'>



The main implementation for these two methods is as follows:
<img src='/images/audio_mnist_posts/figures/train_test_split_methods.PNG' width = '600'>

