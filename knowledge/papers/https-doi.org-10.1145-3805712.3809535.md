---
title: "超越静态Best-of-N：面向LLM推荐系统的贝叶斯列表级对齐"
paper_id: "https://doi.org/10.1145/3805712.3809535"
source: "citation"
published: "2026-07-15T00:00:00"
score: 88.0
tags: ["paper", "recommender-systems"]
---

# 超越静态Best-of-N：面向LLM推荐系统的贝叶斯列表级对齐

> **英文原标题**：Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation

[查看原文](https://doi.org/10.1145/3805712.3809535)

## 一句话结论

> 本文针对LLM推荐系统中静态Best-of-N对齐的不足，提出贝叶斯列表级对齐方法，通过动态参考和梯度修正提升列表级指标（如NDCG和公平性）的优化效果。

## 论文信息

- **作者**：Ruijun Chen, Chongming Gao, Jiawei Chen, Weiqin Yang, Xiangnan He
- **来源**：Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval
- **发布时间**：2026-07-15
- **相关度评分**：88.0
- **DOI**：[https://doi.org/10.1145/3805712.3809535](https://doi.org/10.1145/3805712.3809535)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型通过利用其生成能力对复杂用户偏好进行建模，彻底革新了推荐系统（LLM4Rec）。然而，现有的LLM4Rec方法主要依赖词元级目标，难以优化定义实际推荐质量的列表级和不可微指标（如NDCG、公平性）。尽管Best-of-N（BoN）在推理过程中直接优化这些指标，但其高昂的计算成本阻碍了实际部署。为解决这一问题，BoN对齐旨在将搜索能力蒸馏到模型自身，但现有方法存在两个关键局限：（1）无差别监督，即静态参考无法区分超出其经验范围的候选相对质量，导致排序指导信息丢失；（2）梯度衰减，即随着策略不断进化，有效监督信号迅速减弱，导致优化效率低下。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models have revolutionized recommender systems (LLM4Rec) by leveraging their generative capabilities to model complex user preferences. However, existing LLM4Rec methods primarily rely on token-level objectives, making it difficult to optimize list-level and non-differentiable metrics (e.g., NDCG, fairness) that define actual recommendation quality. While Best-of-N (BoN) directly optimizes these metrics during inference, its high computational cost hinders real-world deployment. To address this, BoN Alignment aims to distill the search capability into the model itself, yet current approaches suffer from two critical limitations: (1) Indiscriminate Supervision, where the static reference fails to distinguish the relative quality of candidates exceeding its empirical range, leading to a loss of ranking guidance; and (2) Gradient Decay, where the effective supervision signal rapidly diminishes as the evolving policy improves, resulting in inefficient optimization.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

大型语言模型（LLM）通过生成能力建模复杂用户偏好，推动了推荐系统（LLM4Rec）的发展。然而，现有方法主要依赖token级目标，难以优化列表级且不可微的指标（如NDCG、公平性）。Best-of-N（BoN）在推理时直接优化这些指标，但计算成本高。BoN对齐旨在将搜索能力蒸馏到模型中，但现有方法存在两个关键限制：静态参考无法区分超出其经验范围的候选相对质量，导致排序指导丢失；以及随着策略改进，有效监督信号迅速减弱，导致优化效率低下。本文提出贝叶斯列表级对齐方法，以解决上述问题。

### 主要创新

- 提出贝叶斯列表级对齐框架，超越静态Best-of-N，动态调整监督信号。
- 针对静态参考的局限性，引入贝叶斯方法以区分候选相对质量。
- 缓解梯度衰减问题，保持优化过程中的有效监督。
- 直接优化列表级指标，提升推荐质量。

### 研究方法

摘要未提供具体方法细节，但可推断采用贝叶斯推断和列表级对齐策略，可能涉及动态参考模型或不确定性估计。

### 关键结果

摘要未提供具体实验结果，但指出现有方法的两个限制，并暗示所提方法能解决这些问题。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 针对现有BoN对齐方法的两个关键缺陷提出解决方案。
- 直接优化列表级指标，更符合推荐系统实际评估。
- 贝叶斯方法可能提供更稳健的监督信号。

### 主要局限

- 论文局限：摘要未提供实验验证和具体性能数据。当前证据局限：仅基于摘要，无法评估方法有效性和实现细节。

### 与当前研究方向的关联

与LLM与推荐系统结合、生成式推荐、排序与重排、用户建模等关键词高度相关。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.668788_
