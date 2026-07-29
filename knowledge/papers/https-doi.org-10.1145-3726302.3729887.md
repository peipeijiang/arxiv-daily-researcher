---
title: "Adaptive Structure Learning with Partial Parameter Sharing for Post-Click Conversion Rate Prediction"
paper_id: "https://doi.org/10.1145/3726302.3729887"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 22.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Gene expression and cancer classification", "Advanced Computing and Algorithms"]
---

# Adaptive Structure Learning with Partial Parameter Sharing for Post-Click Conversion Rate Prediction

[查看原文](https://dblp.org/rec/conf/sigir/000100025)

## 一句话结论

> 该论文提出自适应结构学习方法Adap-SL，通过部分参数共享解决CVR预测中的选择偏差和数据稀疏问题，在三个真实数据集上提升了性能并减少了参数。

## 论文信息

- **作者**：Chunyuan Zheng, Hang Pan, Yang Zhang, Haoxuan Li
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：22.0
- **DOI**：[https://doi.org/10.1145/3726302.3729887](https://doi.org/10.1145/3726302.3729887)

<details open>
<summary><strong>中文摘要</strong></summary>

点击后转化率（CVR）预测任务旨在预测点击后发生转化的概率，这在众多领域中至关重要。CVR预测面临两个公认的挑战：选择性偏差和数据稀疏性。许多先前的方法通过基于双重稳健估计器（doubly robust estimator）无偏估计理想损失来应对选择性偏差，该估计器结合了误差插补模型（error imputation model）和倾向性模型（propensity model）以辅助CVR预测模型的学习。然而，这些方法在预测模型与插补模型之间的知识迁移不合理，以及在稀疏数据下网络结构设计缺乏灵活性方面存在困难。为此，我们提出了一种新颖的原则性自适应结构学习方法，命名为Adap-SL，该方法能够自适应地学习最优网络结构、调整激活（非零）参数的数量，并决定预测模型与插补模型之间需要迁移哪些知识。具体而言，我们从过参数化的基础网络出发，自适应地为插补模型和预测模型提取部分重叠的子网络。在三个真实世界推荐数据集上进行了大量实验，结果表明，我们的方法在持续提升性能的同时，所需参数更少。代码可在 https://github.com/ChunyuanZheng/sigir25-sparse-sharing 获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

The post-click conversion rate (CVR) prediction task aims to predict the probability of a conversion after a click, which is essential in many fields. There are two widely-recognized challenges for CVR prediction: selection bias and data sparsity. Many previous methods focus on addressing selection bias by unbiasedly estimating the ideal loss based on the doubly robust estimator, which incorporates the error imputation model and propensity model to help CVR prediction model learning. However, they struggle with unreasonable knowledge transfer between the prediction model and imputation model and inflexible network structure design under sparse data. To this end, we introduce a novel principled adaptive structure learning approach, named Adap-SL, to adaptively learn the optimal network structure, adjust the number of activated (non-zero) parameters, and determine which knowledge needs to be transferred between the prediction model and the imputation model. Specifically, we start with an over-parameterized base network, where we adaptively extract partially overlapped subnetworks for the imputation model and the prediction model. Extensive experiments are conducted on three real-world recommendation datasets, demonstrating that our method consistently improves performance while requiring fewer parameters. The code is available at https://github.com/ChunyuanZheng/sigir25-sparse-sharing.

</details>

---

_知识库更新时间：2026-07-29T03:56:18.946804_
