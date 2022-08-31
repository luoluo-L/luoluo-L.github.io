---
title: 'time series clustering using tslearn'
date: 2021-08-01
permalink: /posts/2021/08/tsclustering
tags:
  - time series
  - clustering
  - k-means
  - dynamic time wrapping

---



TSlearn package for classic timeseries clustering methods.

Follow this [demo](https://tslearn.readthedocs.io/en/stable/auto_examples/clustering/plot_kmeans.html). With some small modifications (parameters stated in last section, and we generate the following results with number of clusters set to ```nc = 3```.

<img src='/images/blog_tsclustering/example_three_ts_clustering_numClusters3.png'>


**Methods:**

  $\bullet$ Euclidean k-means,

  $\bullet$ DTW (Dynamic Time Wrapping), Soft-DTW.

Remarks:
---
One needs to fill in missing data (if there are) first before using those algorithms.

Clustering series needs to have **equal length**. 
If not, resampling needs to be done before applying those algorithms.

timeseries k-means clustering center is a smoothed/low-passed version of signals in each cluster.

DTW deals with time-invariance better, therefore DTW clustering centers are more indicative of shape.

Comparison of DTW vs Soft-DTW: 
According to this example, soft-DTW cluster center captures the actual signal center in time domain, whereas DTW pick the first template.

Cluster size changes with different number of clusters
---

Below image shows how cluster size changes with various numnber of clusters.
The sample size is ```n=100``` to train cluster algorithms, and time dimension is ```t = 40```. In this dataset, the number of labels in the dataset is 4.


Among three methods, k-means generates more imbalanced clusters, where the majority class tends to take over minority classes while increasing the number of clusters. 

<img src='/images/blog_tsclustering/diff_methods_cluster_sizes.png'>
