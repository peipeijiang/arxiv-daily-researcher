---
title: "超越静态最佳N：基于贝叶斯列表级对齐的LLM推荐"
paper_id: "https://doi.org/10.1145/3805712.3809535"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 66.0
tags: ["paper", "recommender-systems"]
---

# 超越静态最佳N：基于贝叶斯列表级对齐的LLM推荐

> **英文原标题**：Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/ChenGCYH26) · [ArXiv](https://arxiv.org/abs/2605.04559)

## 一句话结论

> 论文针对LLM推荐中列表级指标优化困难的问题，提出贝叶斯列表级对齐方法，通过动态参考和梯度修正克服现有Best-of-N对齐的不足。

## 论文信息

- **作者**：Ruijun Chen, Chongming Gao, Jiawei Chen, Weiqin Yang, Xiangnan He
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：66.0
- **DOI**：[https://doi.org/10.1145/3805712.3809535](https://doi.org/10.1145/3805712.3809535)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型通过利用其生成能力对复杂用户偏好进行建模，彻底革新了推荐系统（LLM4Rec）。然而，现有的LLM4Rec方法主要依赖基于词元（token）级别的目标函数，难以优化定义实际推荐质量的列表级（list-level）及不可微分指标（如NDCG、公平性）。尽管最优N选（Best-of-N, BoN）方法在推理过程中直接优化这些指标，但其高昂的计算成本阻碍了实际部署。为此，BoN对齐（BoN Alignment）旨在将搜索能力蒸馏至模型自身，但当前方法存在两个关键局限：（1）无差别监督（Indiscriminate Supervision），即静态参考无法区分超出其经验范围的候选样本的相对质量，导致排序引导信息丢失；（2）梯度衰减（Gradient Decay），即随着策略持续优化，有效监督信号迅速减弱，导致优化效率低下。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models have revolutionized recommender systems (LLM4Rec) by leveraging their generative capabilities to model complex user preferences. However, existing LLM4Rec methods primarily rely on token-level objectives, making it difficult to optimize list-level and non-differentiable metrics (e.g., NDCG, fairness) that define actual recommendation quality. While Best-of-N (BoN) directly optimizes these metrics during inference, its high computational cost hinders real-world deployment. To address this, BoN Alignment aims to distill the search capability into the model itself, yet current approaches suffer from two critical limitations: (1) Indiscriminate Supervision, where the static reference fails to distinguish the relative quality of candidates exceeding its empirical range, leading to a loss of ranking guidance; and (2) Gradient Decay, where the effective supervision signal rapidly diminishes as the evolving policy improves, resulting in inefficient optimization.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

论文针对LLM推荐系统中列表级指标（如NDCG、公平性）优化困难的问题，提出BLADE框架。现有方法如Best-of-N（BoN）推理代价高，而BoN对齐存在静态参考导致的监督无区分和梯度衰减问题。BLADE通过贝叶斯框架动态融合静态先验与当前策略的在线证据，构建自进化目标分布，持续提供有效训练信号。实验表明，BLADE在三个真实数据集上显著优于基线，突破了静态性能上限，在排序准确性和列表级指标上均取得提升。

### 主要创新

- 识别静态BoN对齐的两个关键瓶颈：监督无区分和梯度衰减。
- 提出贝叶斯动态估计框架，融合静态先验与动态证据构建自进化目标。
- 通过共享采样机制实现零额外开销的目标估计与策略优化。
- 在多个列表级指标（公平性、多样性）上展示通用优化能力。

### 研究方法

采用贝叶斯框架，将静态参考分布作为先验，当前策略的在线采样作为动态证据，通过Beta分布建模并更新后验，得到动态CDF估计。将估计的CDF转化为代理奖励，结合GRPO进行策略优化。训练中共享同一批采样用于目标估计和梯度计算。

### 关键结果

BLADE在Amazon CDs数据集上NDCG@5比最强列表级基线BoN Alignment提升23.1%。；BLADE在三个数据集上均取得最佳或次佳结果，突破静态性能上限。；动态系数τ=0.3时训练曲线持续上升，而静态基线（τ=0）早期停滞。；在公平性和多样性优化中，BLADE实现帕累托占优，同时保持高准确率。

### 技术栈

- Llama-3.2-1B-Instruct
- GRPO (Group Relative Policy Optimization)
- Beta分布与贝叶斯更新
- AdamW优化器
- 线性学习率衰减

### 方法优势

- 理论分析深入，清晰指出静态对齐的缺陷。
- 方法设计简洁有效，贝叶斯更新公式闭合可解。
- 共享采样机制使计算开销与静态对齐相当。
- 实验全面，覆盖多个数据集和列表级指标。

### 主要局限

- 动态系数τ需要手动调参，对性能敏感。
- 仅使用1B参数模型，更大模型上的效果未验证。
- 复合奖励中的权重λ需针对不同目标调整。
- 输入内容未提供与更多基线（如PPO）的对比。

### 与当前研究方向的关联

LLM与推荐系统结合：核心研究LLM4Rec中的对齐问题。；生成式推荐：将推荐建模为序列生成任务。；排序与重排：直接优化列表级排序指标NDCG。；推荐系统的公平性：实验部分优化了公平性指标MGU。

---

_知识库更新时间：2026-07-18T03:48:20.892936_
