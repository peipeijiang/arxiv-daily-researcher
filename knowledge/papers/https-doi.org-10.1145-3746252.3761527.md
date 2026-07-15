---
title: "InterFormer: 面向点击率预测的有效异构交互学习"
paper_id: "https://doi.org/10.1145/3746252.3761527"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Image and Video Quality Assessment", "Emotion and Mood Recognition", "Visual Attention and Saliency Detection"]
---

# InterFormer: 面向点击率预测的有效异构交互学习

> **英文原标题**：InterFormer: Effective Heterogeneous Interaction Learning for Click-Through Rate Prediction

[查看原文](https://dblp.org/rec/conf/cikm/0001LHLZYLRCCHX25) · [ArXiv](https://arxiv.org/abs/2411.09852) · [Semantic Scholar](https://www.semanticscholar.org/paper/d37c61c568798928bf42152def0c8480177d9dd1)

## 一句话结论

> 论文提出InterFormer模块，通过交错式双向信息流和完整信息保留，有效学习异构信息交互，提升CTR预测性能，并在Meta Ads平台部署取得线上收益。

## 论文信息

- **作者**：Zhichen Zeng, Xiaolong Liu, Mengyue Hang, Xiaoyi Liu, Qinghai Zhou, Chaofei Yang, Yiqun Liu, Yichen Ruan, Laming Chen, Yuxin Chen, Yanxu Hao, Jiaqi Xu, Jade Nie, Xi Liu, Buyun Zhang, Wei Wen, Siyang Yuan, Hang Yin, Xin Zhang, Kai Ying Wang
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3746252.3761527](https://doi.org/10.1145/3746252.3761527)

<details open>
<summary><strong>中文摘要</strong></summary>

点击率（CTR）预测，即预测用户点击广告的概率，是推荐系统中的一项基础任务。用户画像与行为序列等异构信息的出现，从不同角度描绘了用户兴趣。异构信息的互利整合是CTR预测成功的关键。然而，现有大多数方法存在两个根本性局限：（1）由于模态间信息流的单向性，导致模态间交互不足；（2）早期汇总导致的激进信息聚合，造成过多信息损失。为解决这些问题，我们提出名为InterFormer的新型模块，以交错方式学习异构信息交互。为实现更优的交互学习，InterFormer支持双向信息流，促进不同模态间的互利学习。为避免激进信息聚合，我们在每个数据模态中保留完整信息，并使用独立的Cross Arch进行有效的信息选择与汇总。InterFormer已在Meta Ads的多个平台部署，相较于先前最先进模型实现了0.15%的性能提升与24%的QPS增益，并产生了显著的线上影响。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Click-through rate (CTR) prediction, which predicts the probability of a user clicking an ad, is a fundamental task in recommender systems. The emergence of heterogeneous information, such as user profile and behavior sequences, depicts user interests from different aspects. A mutually beneficial integration of heterogeneous information is the cornerstone towards the success of CTR prediction. However, most of the existing methods suffer from two fundamental limitations, including (1) insufficient inter-mode interaction due to the unidirectional information flow between modes, and (2) aggressive information aggregation caused by early summarization, resulting in excessive information loss. To address these limitations, we propose a novel module named InterFormer to learn heterogeneous information interaction in an interleaving style. To achieve better interaction learning, InterFormer enables bidirectional information flow for mutually beneficial learning across different modes. To avoid aggressive information aggregation, we retain complete information in each data mode and use a separate Cross Arch for effective information selection and summarization. InterFormer has been deployed across multiple platforms at Meta Ads, achieving 0.15% performance gain and 24% QPS gain compared to prior state-of-the-art models and yielding sizable online impact.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

点击率预测是推荐系统中的基础任务，异构信息（如用户画像和行为序列）从不同角度描述用户兴趣，其有效整合至关重要。现有方法存在两个局限：模式间单向信息流导致交互不足，以及早期汇总导致信息丢失。为此，本文提出InterFormer模块，以交错方式学习异构信息交互。InterFormer通过双向信息流实现模式间的互利学习，并通过保留各模式的完整信息、使用独立的Cross Arch进行信息选择和汇总，避免激进的信息聚合。InterFormer已在Meta Ads多个平台部署，相比先前最优模型取得0.15%性能提升和24% QPS提升，并带来显著的线上收益。

### 主要创新

- 提出InterFormer模块，实现异构信息交互的交错式学习。
- 采用双向信息流，促进不同模式间的互利学习。
- 保留各数据模式的完整信息，避免早期汇总导致的信息损失。
- 设计独立的Cross Arch用于有效的信息选择和汇总。

### 研究方法

摘要未提供具体技术路线，仅概述了InterFormer模块的设计思想：通过双向信息流实现模式间交互，并利用独立的Cross Arch进行信息选择与汇总，以交错方式学习异构信息。

### 关键结果

在Meta Ads多个平台部署，相比先前最优模型获得0.15%性能提升。；获得24%的QPS提升。；带来显著的线上收益。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 针对现有方法的两大局限提出了明确解决方案。
- 双向信息流设计增强了模式间交互。
- 保留完整信息避免了早期汇总的信息损失。
- 工业部署验证了实际效果，性能与效率均有提升。

### 主要局限

- **论文局限**：摘要未提供，可能包括对更多模式或更复杂场景的适用性等。
- **当前证据局限**：仅基于摘要，缺乏模型细节、实验设置、数据集、基线对比等具体信息。

### 与当前研究方向的关联

论文聚焦于CTR预测中的异构信息交互学习，与CTR/CVR预测、用户建模、排序与重排等关键词高度相关，同时涉及工业落地，与推荐系统的工业实践相关。

---

_知识库更新时间：2026-07-15T03:52:18.777756_
