---
title: 'Predict unit-level LoS using time-series modelling'
date: 2022-05-30
permalink: /posts/2022/04/blog-post-4/
tags:
  - unit-level Length of Stay(LoS)
  - predictive model
  - time series
  - LSTM
---

We propose to a dynamic, real-time, lightweight, end-to-end next day median ED-LoS prediction algorithm using time-series LSTM modelling. Similar method can be extended to unit-level KPI prediction.  [Summary](http://luoluo-l.github.io/files/amia_cic.pdf)


Background
--
Length of Stay (LoS) is an important indicator for operational efficiency in Emergency Departments (ED), as
reducing ED LoS can potentially reduce health care costs and improve patients' satisfaction. We develop a method
of predicting the next-day median ED-LoS, and it will provide an early warning to ED managers to take proactive
actions to reduce future ED-LoS.


In recent years, there have been many literature works that focus on predicting the remaining LoS and ED workflow.
In a recent review 1 on this topic, three major gaps are identified from exisitng relavent works: i) patient level LoS
prediction models require massive data elements, and some of features may not be easily accessible; ii) two-step
approaches which predict supply and demand first and then LoS based on their predictions, are not end-to-end LoS
prediction solutions; iii) static models which are commonly used lack the ability to dynamically update in real time.

To address these gaps, we propose a real-time end-to-end ED LoS prediction method on the unit level based on only a few aggregated features. The data elements required are easily vailable, and this lightweight model is suitable for practical deployment.

Method: 
--
We first calculate daily median ED-LoS on a unit level, as target values.

Inputs variables:
* the number of daily ED arrival cases,
 * the number of daily placed imaging orders including ultrasound,
CT, MRI and X-rays modalities. 
* previous day median ED-LoS.

Prediction:
* the next day median ED-LoS

Model: 
long short-term memory (LSTM) network2. 

The LSTM main parameter unit/inner dimension is 100. The model is trained on a single CPU machine for 50 epochs. Note, resource
related features such as the number of staff has been shown to be predictive in previous works1, however our dataset
does not contain this information, and therefore we do not include resource information in our model.


We use one-year historical data from one hospital with around 300-500 ED cases daily. The first half-year is used as training, and the second half-year as prediction. Figure 1 shows the input features and the results of the
prediction. The predicted ED-LoS is smoother than the true ED-LoS but has strong correlation with the ground truth. 


Our LSTM model performs resonably well with prediction root mean squared error=0.1. The model successfully
predicts both the trend and the peak of median ED-LoS in early December. ED managers can potentially react based
on predicted ED-LoS peaks and take proactive actions.


Conclusion
---
We propose to a dynamic, real-time, lightweight, end-to-end next day median ED-LoS prediction algorithm using
time-series LSTM modelling. The model behaves well with low prediction error, predicting both trends and high
median ED-LoS events well. The output of the model provides early warning information to ED managers to take proactive actions for reducing future ED-LoS.


[Download Summary](http://luoluo-l.github.io/files/amia_cic.pdf)
