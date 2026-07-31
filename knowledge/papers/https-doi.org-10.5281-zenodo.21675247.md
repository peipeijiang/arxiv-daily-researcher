---
title: "fishFingers: Bioconcentration factor (BCF) and fish species bioaccumulation distribution prediction for chemicals detected by HRMS using recommender system machine learning"
paper_id: "https://doi.org/10.5281/zenodo.21675247"
source: "openalex"
published: "2026-07-30T00:00:00"
score: 16.0
tags: ["paper", "recommender-systems", "Computational Drug Discovery Methods", "Metabolomics and Mass Spectrometry Studies", "Environmental Toxicology and Ecotoxicology"]
---

# fishFingers: Bioconcentration factor (BCF) and fish species bioaccumulation distribution prediction for chemicals detected by HRMS using recommender system machine learning

[查看原文](https://doi.org/10.5281/zenodo.21675247)

## 一句话结论

> 该论文提出了一种利用推荐系统机器学习方法，从高分辨率质谱数据中预测化学物质生物富集因子（BCF）的新方法，无需预先结构注释，并验证了其性能优于传统模型。

## 论文信息

- **作者**：Drew Szabo
- **来源**：Zenodo (CERN European Organization for Nuclear Research)
- **发布时间**：2026-07-30
- **相关度评分**：16.0
- **DOI**：[https://doi.org/10.5281/zenodo.21675247](https://doi.org/10.5281/zenodo.21675247)

<details open>
<summary><strong>中文摘要</strong></summary>

摘要 环境中新型化学物质的暴露量现已超出我们在传统框架下评估每种化学品风险的能力。化学品被生物体吸收的速率与其被排泄的速率之比，即生物富集因子（BCF），是评估化学风险的重要终点指标，常被用于监管面向市场开发的化学品。遗憾的是，所有已知的可靠BCF预测方法均需确切的化学结构信息。本文将展示如何在不进行先验结构注释的情况下，利用高分辨质谱（HRMS）特征预测BCF，并借助高质量串联质谱（MS2）阐明关键结构指纹。这种用于非靶向筛查的离线优先排序方法可快速将特征按生物累积风险递减顺序排列。我们获取并整理了一个包含1000多种化学品实测BCF值的数据集，用于训练和测试。对于每种化学品，使用rcdk包计算了2691个结构指纹矩阵，涵盖MACCS、PubChem、Klekota-Roth以及若干自定义SMARTS。采用推荐系统方法，以来自100多种鱼类的结构指纹为输入对BCF进行建模。比较了线性回归、决策树和随机失活决策树算法的性能，并对表现最佳的模型进行优化和测试，以获得最高的平衡准确率（计算公式为（TPR+TNR）/2）。随后，利用MassBank谱库中具有高质量MS2数据的化学品，通过SIRIUS CSI:FingerID v5.8基于平均峰列表生成结构指纹来验证模型。最后，将模型性能与文献中描述的方法进行比较，包括基于疏水性的模型（log Kow）以及使用已知结构注释的最新机器学习模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Abstract Exposure to novel entities in the environment now exceeds our capacity to evaluate the risk of each chemical under traditional frameworks. The rate at which a chemical is absorbed into an organism compared to the rate it is excreted, known as the bioconcentration factor (BCF), is an important endpoint for evaluating chemical risk and is often used to regulate chemicals developed for market. Unfortunately, all known methods of reliable BCF prediction require a confident chemical structure. The prediction of BCF from high-resolution mass spectrometry (HRMS) features without a priori structural annotation will be demonstrated, using high-quality tandem mass spectrometry (MS2) to elucidate key structural fingerprints. This offline prioritisation method for non-targeted screening can quickly rank features in order of decreasing risk of bioaccumulation. A dataset containing measured BCF values for more than 1000 chemicals was obtained and curated for training and testing. For each chemical, a matrix of 2691 structural fingerprints were calculated using the rcdk package, incorporating MACCS, PubChem, Klekota-Roth, and a number of custom SMARTS. A recommender system approach was applied to model BCF with inputs from structural fingerprints from over 100 species of fish. The performance of linear regression, decision tree and dropout tree algorithms were compared, and the best performing model was optimised and tested to achieve the highest balanced accuracy, calculated as (TPR+TNR)/2. Chemicals with high-quality MS2 in the MassBank spectral library were then used to validate the model using SIRIUS CSI:FingerID v5.8 to generate the structural fingerprints using the averaged peak lists. The performance of the model was compared with methods described in the literature, including hydrophobicity-based models (log Kow) and more recent machine learning models that use known structural annotations.

</details>

---

_知识库更新时间：2026-07-31T04:07:10.054581_
