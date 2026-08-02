---
title: "SELM-CTR: a stacking ensemble deep learning model with SHAP-based analysis for large-scale click-through rate prediction"
paper_id: "https://doi.org/10.1108/ijicc-04-2026-0403"
source: "openalex"
published: "2026-08-01T00:00:00"
score: 36.0
tags: ["paper", "recommender-systems", "Consumer Market Behavior and Pricing", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research"]
---

# SELM-CTR: a stacking ensemble deep learning model with SHAP-based analysis for large-scale click-through rate prediction

[查看原文](https://doi.org/10.1108/ijicc-04-2026-0403)

## 一句话结论

> 该论文提出了一种基于堆叠集成深度学习模型（SELM-CTR）的点击率预测方法，结合DNN、DeepFM、GDCN和XGBoost，并利用SHAP进行特征解释，在公开数据集上取得了优于基线的性能。

## 论文信息

- **作者**：Zeeshan Ali, Hassan Ahmed, Abdullah Khan, Shahrzad Saremi, Rania Shibl, Mansooreh Mirzaei, Parvin Rastegari, Mingzhong Wang
- **来源**：International Journal of Intelligent Computing and Cybernetics
- **发布时间**：2026-08-01
- **相关度评分**：36.0
- **DOI**：[https://doi.org/10.1108/ijicc-04-2026-0403](https://doi.org/10.1108/ijicc-04-2026-0403)

<details open>
<summary><strong>中文摘要</strong></summary>

目的：点击率（CTR）预测是数字广告中的核心挑战，因为预测用户是否会点击广告直接决定了广告投放决策和收入结果。标准机器学习和深度学习方法能够实现合理的预测精度，但大多不透明，难以确定哪些特征驱动了预测及其原因。深度神经网络（DNN）、深度因子分解机（DeepFM）和深度交叉网络（DCN）各自捕捉特征交互的不同方面，但单独使用均无法全面应对大规模稀疏数据的复杂性。设计/方法/途径：本文提出了一种基于堆叠集成的点击率预测模型（SELM-CTR），该堆叠集成以DNN、DeepFM和门控深度交叉网络（GDCN）作为基模型，并以XGBoost作为元模型。我们并未将这些架构视为可互换的替代方案，而是利用其互补优势：DNN学习非线性表示，DeepFM通过因子分解捕捉低阶和高阶交互，GDCN则应用门控交叉层交互。元模型基于基模型的折外预测进行训练，从而学习针对不同输入模式应信任哪种架构。发现：使用公开可用的AVAZU数据集进行评估表明，所提方法实现了89%的准确率、94%的曲线下面积（AUC）以及0.25的对数损失。这些结果相较于现有基线方法具有可衡量的改进。此外，SHAP的应用阐明了特定特征如何影响模型预测，为实际决策提供了实用见解。原创性/价值：本研究的主要贡献在于将堆叠集成架构（使用DNN、DeepFM、GDCN和XGBoost）与基于SHAP的特征分析相结合。这解决了深度学习中常见的“黑箱”局限性，在广告领域确保了高预测性能的同时，提高了特征贡献的透明度。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Purpose Click-through rate (CTR) prediction is a core challenge in digital advertising, as forecasting whether a user will click on an advertisement directly determines ad placement decisions and revenue outcomes. Standard machine learning and deep learning approaches achieve reasonable predictive accuracy but are largely opaque, making it difficult to determine which features drive predictions and why. Deep Neural Networks (DNN), Deep Factorization Machines (DeepFM), and Deep Cross Networks (DCN) each capture different aspects of feature interaction, yet none alone addresses the full complexity of large-scale sparse data. Design/methodology/approach This paper proposes a stacking ensemble learning model for click-through rate (SELM-CTR) prediction, a stacking ensemble that combines DNN, DeepFM, and a Gated Deep Cross Network (GDCN) as base models, with XGBoost serving as the meta-model. Rather than treating these architectures as interchangeable alternatives, we exploit their complementary strengths: the DNN learns nonlinear representations, DeepFM captures low- and high-order interactions through factorization, and GDCN applies gated cross-layer interactions. The meta-model is trained on out-of-fold predictions from the base models, allowing it to learn which architecture to trust for different input patterns. Findings Evaluation using the publicly available AVAZU dataset indicates that the proposed method achieves an accuracy of 89%, an Area Under the Curve (AUC) of 94%, and a log loss of 0.25. These results represent a measurable improvement over existing baseline approaches. Furthermore, the application of SHAP clarifies how specific features influence the model's predictions, providing practical insights for real-world decision-making. Originality/value The primary contribution of this work is the integration of a stacking ensemble architecture (using DNN, DeepFM, GDCN, and XGBoost) with SHAP-based feature analysis. This addresses the common “black-box” limitations of deep learning in advertising, ensuring both high predictive performance and greater transparency regarding feature contributions.

</details>

---

_知识库更新时间：2026-08-02T04:11:29.698638_
