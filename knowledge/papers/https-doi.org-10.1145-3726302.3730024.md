---
title: "Linear Item-Item Models with Neural Knowledge for Session-based Recommendation"
paper_id: "https://doi.org/10.1145/3726302.3730024"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# Linear Item-Item Models with Neural Knowledge for Session-based Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/000100L25) · [ArXiv](https://arxiv.org/abs/2504.15057)

## 一句话结论

> 论文提出LINK模型，通过线性框架融合线性知识和神经网络知识，提升会话推荐性能，在六个数据集上Recall@20和MRR@20分别提升高达14.78%和11.04%，且推理FLOPs减少813倍。

## 论文信息

- **作者**：Minjin Choi, Sunkyung Lee, Seongmin Park, Jongwuk Lee
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3726302.3730024](https://doi.org/10.1145/3726302.3730024)

<details open>
<summary><strong>中文摘要</strong></summary>

基于会话的推荐（Session-based Recommendation, SBR）旨在通过建模会话内的短期交互来预测用户的后续行为。现有神经模型主要关注捕捉序列项目转换中的复杂依赖关系。作为替代方案，线性项目-项目模型主要识别项目间的强共现模式，并支持更快的推理速度。尽管每种范式在SBR中均得到了积极研究，但它们在捕捉项目关系方面的根本差异，以及如何有效弥合这些不同建模范式的问题，仍未得到探索。本文提出了一种新颖的SBR模型，即融合神经知识的线性项目-项目模型（Linear Item-Item model with Neural Knowledge, LINK），该模型将两种类型的知识整合到一个统一的线性框架中。具体而言，我们设计了LINK的两个专门组件：（i）线性知识增强的项目-项目相似度模型（Linear knowledge-enhanced Item-item Similarity model, LIS），通过自蒸馏优化项目相似度关联；（ii）神经知识增强的项目-项目转换模型（Neural knowledge-enhanced Item-item Transition model, NIT），无缝融合从现成神经模型中蒸馏出的复杂神经知识。大量实验表明，LINK在六个真实世界数据集上均优于最先进的线性SBR模型，在Recall@20和MRR@20指标上分别实现了最高14.78%和11.04%的提升，同时推理FLOPs（浮点运算次数）减少了多达813倍。我们的代码可在https://github.com/jin530/LINK获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Session-based recommendation (SBR) aims to predict users' subsequent actions by modeling short-term interactions within sessions. Existing neural models primarily focus on capturing complex dependencies for sequential item transitions. As an alternative solution, linear item-item models mainly identify strong co-occurrence patterns across items and support faster inference speed. Although each paradigm has been actively studied in SBR, their fundamental differences in capturing item relationships and how to bridge these distinct modeling paradigms effectively remain unexplored. In this paper, we propose a novel SBR model, namely Linear Item-Item model with Neural Knowledge (LINK), which integrates both types of knowledge into a unified linear framework. Specifically, we design two specialized components of LINK: (i) Linear knowledge-enhanced Item-item Similarity model (LIS), which refines the item similarity correlation via self-distillation, and (ii) Neural knowledge-enhanced Item-item Transition model (NIT), which seamlessly incorporates complicated neural knowledge distilled from the off-the-shelf neural model. Extensive experiments demonstrate that LINK outperforms state-of-the-art linear SBR models across six real-world datasets, achieving improvements of up to 14.78% and 11.04% in Recall@20 and MRR@20 while showing up to 813x fewer inference FLOPs. Our code is available at https://github.com/jin530/LINK.

</details>

---

_知识库更新时间：2026-07-29T03:56:18.946955_
