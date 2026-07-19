---
title: "Improved Recurrent Neural Networks for Session-based Recommendations"
paper_id: "https://doi.org/10.1145/2988450.2988452"
source: "citation"
published: "2016-09-15T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Machine Learning in Healthcare"]
---

# Improved Recurrent Neural Networks for Session-based Recommendations

[查看原文](https://doi.org/10.1145/2988450.2988452)

## 一句话结论

> 该论文通过数据增强和输入分布偏移校正技术改进了RNN模型在会话推荐中的性能，在RecSys Challenge 2015数据集上取得了显著提升。

## 论文信息

- **作者**：Yong Tan, Xinxing Xu, Yong Liu
- **来源**：Proceedings of the 1st Workshop on Deep Learning for Recommender Systems
- **发布时间**：2016-09-15
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/2988450.2988452](https://doi.org/10.1145/2988450.2988452)

<details open>
<summary><strong>中文摘要</strong></summary>

近年来，循环神经网络（RNN）被提出用于基于会话的推荐任务。相较于传统推荐方法，该模型展现出显著的性能提升。本研究进一步探索了基于RNN的会话推荐模型，提出应用两种技术以改进模型性能：数据增强（data augmentation）以及应对输入数据分布偏移的方法。此外，我们通过实验研究了广义蒸馏（generalised distillation）技术，并提出了一种直接预测项目嵌入（item embeddings）的新型替代模型。在RecSys Challenge 2015数据集上的实验表明，相较于先前报告的结果，本模型在[email protected]和平均倒数排名（Mean Reciprocal [email protected]）指标上分别实现了12.8%和14.8%的相对提升。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recurrent neural networks (RNNs) were recently proposed for the session-based recommendation task. The models showed promising improvements over traditional recommendation approaches. In this work, we further study RNN-based models for session-based recommendations. We propose the application of two techniques to improve model performance, namely, data augmentation, and a method to account for shifts in the input data distribution. We also empirically study the use of generalised distillation, and a novel alternative model that directly predicts item embeddings. Experiments on the RecSys Challenge 2015 dataset demonstrate relative improvements of 12.8% and 14.8% over previously reported results on the [email protected] and Mean Reciprocal [email protected] metrics respectively.

</details>

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3746252.3761384
- **seed_title**：Autonomous Reasoning-Retrieval for Large Language Model Based Recommendation
- **seed_score**：83.0

</details>

---

_知识库更新时间：2026-07-19T04:08:52.140150_
