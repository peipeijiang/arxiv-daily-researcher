---
title: "Flights Pricelock Fee Recommendation on Online Travel Agent Platform"
paper_id: "https://doi.org/10.1145/3705328.3759339"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 33.0
tags: ["paper", "recommender-systems", "Data Management and Algorithms", "Autonomous Vehicle Technology and Safety", "Traffic Prediction and Management Techniques"]
---

# Flights Pricelock Fee Recommendation on Online Travel Agent Platform

[查看原文](https://dblp.org/rec/conf/recsys/KhetanMYP25) · [Semantic Scholar](https://www.semanticscholar.org/paper/1f310c616de25937effb1e5e556f50f50c3b7efa)

## 一句话结论

> The paper proposes a neural network-based recommender system with a novel loss function (L-SORD) to recommend fees for flight pricelock products, improving predictive accuracy and revenue.

## 论文信息

- **作者**：Akash Khetan, Narasimha Medeme, Deepak Yadav, Anmol Porwal
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：33.0
- **DOI**：[https://doi.org/10.1145/3705328.3759339](https://doi.org/10.1145/3705328.3759339)

<details open>
<summary><strong>中文摘要</strong></summary>

在本研究中，我们提出了一种基于神经网络（NN）的推荐系统，并开发了一种新颖的自定义损失函数，用于为其价格锁定产品推荐费用。该产品是一种广受欢迎的附加产品，允许用户锁定航班价格，并在之后以相同的锁定价格进行预订，即使在预订期间价格上涨也是如此。实现该产品的核心挑战在于预测未来价格在不同时间范围内的变化幅度。我们将此问题构建为多任务学习（MTL）框架，其中价格变化幅度被建模为有序类别，并在多个时间区间上分别作为任务头进行建模。关键的是，我们通过引入一种名为可学习软序回归（L-SORD）的新颖损失函数，来处理价格变化分箱的有序性质。我们的演示展示了该系统如何提升预测准确性和收入表现，从而在高风险的真实环境中实现更有效的价格推荐。这项工作凸显了在生产级定价推荐系统中，将MTL架构与自定义损失函数相结合的潜力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In this study, we present a neural network (NN) based recommender system with novel custom loss function developed to recommend fee for its pricelock product.It is a popular add-on product that allows users to lock a flight price and book it later at the same locked price, even if the price increases while flight booking.The core challenge in enabling this product lies in predicting the magnitude of future price changes over time horizons.We formulate this problem as a multi-task learning (MTL) setup, where price change magnitudes are modeled as ordinal categories across several time intervals modeled as heads.Crucially, we address the ordinal nature of price change buckets by introducing a novel loss function called Learnable Soft Ordinal Regression (L-SORD).Our demo showcases how this system improves both predictive accuracy and revenue performance, enabling more effective price recommendations in a high stakes, real world environment.This work highlights the potential of combining MTL architectures with custom loss functions in production grade pricing recommender systems.

</details>

---

_知识库更新时间：2026-08-24T02:13:54.085289_
