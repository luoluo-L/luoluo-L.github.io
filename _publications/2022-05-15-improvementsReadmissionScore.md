---
title: "Improvements of LACE+ Readmission Risk Score"
collection: publications
permalink: /publication/2022-improveLACEPlus
excerpt: 'Improvements of LACE+ readmission risk score. These bring 17% AUC improvement.'
date: 2022-05-15
tags:
    - 30-day readmission
    - XGBoost
    - Clinical Categories

---
Improvements of LACE+ Readmission Risk Score

work by Eran Simhon, and Luoluo Liu

Background
--
Although the literature on 30-days readmission risk scores is rich and several scores have been developed over the years, predicting readmission during a hospital stay for general population remains a key challenge. Most models either perform poorly or requires data elements that are not easily accessible in real-time.

Main improvements of the well-known Canadian [LACE+](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3659212/) model
---
- train a XGBoost model on US data of about half a million inpatients of a large multi-states healthcare network 
- use a composite two-step prediction model, where in the first step we map ICD codes to clinical categories and predict risk of readmission solely based on clinical categories. The prediction is added as a feature in the next step, replacing Case-mix score suggested in the original LACE+ model
- the ability to deal with missing input data elements

the improved LACE+ algorithm:
---
Here is an illuatration of the improved LACE+ algorithm:
<img src='/images/readmission/flowchart_30day_readmission.png' width='1800'>

**Main results:**
- the weighted erformance across different hospitals with 600K inpatient encounters, LACE+ AUC=0.66, Improved LACE+ AUC=0.772, with about **17% improvement on AUC**.  

- Using feature importance analysis, the added Clinical cateogries is the top feature.




