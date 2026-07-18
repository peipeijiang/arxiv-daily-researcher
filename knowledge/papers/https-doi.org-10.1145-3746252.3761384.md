---
title: "面向大语言模型推荐的自洽推理-检索方法"
paper_id: "https://doi.org/10.1145/3746252.3761384"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 83.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Sentiment Analysis and Opinion Mining", "Multimodal Machine Learning Applications"]
---

# 面向大语言模型推荐的自洽推理-检索方法

> **英文原标题**：Autonomous Reasoning-Retrieval for Large Language Model Based Recommendation

[查看原文](https://dblp.org/rec/conf/cikm/000500WLCZW25) · [Semantic Scholar](https://www.semanticscholar.org/paper/4da3ff3d0db1d215e33514a97a47d401a039e35a)

## 一句话结论

> 该论文提出DeepRec，一种基于LLM的推荐方法，通过强化学习驱动的多轮交互机制，让LLM与传统推荐模型协同探索物品空间，显著提升推荐性能。

## 论文信息

- **作者**：Bowen Zheng, Xiaolei Wang, Enze Liu, Xi Wang, Hongyu Lu, Yu Chen, Wayne Xin Zhao, Ji-Rong Wen
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：83.0
- **DOI**：[https://doi.org/10.1145/3746252.3761384](https://doi.org/10.1145/3746252.3761384)

<details open>
<summary><strong>中文摘要</strong></summary>

近期，大语言模型（LLMs）已被引入推荐系统（RSs），用作推荐主干或增强传统推荐模型（TRMs）。然而，现有的基于LLM的推荐系统未能充分利用LLMs（如世界知识与推理能力）与TRMs（如推荐特定知识与计算效率）的互补优势，导致对物品空间的探索较为浅层。为解决这一局限，我们提出DeepRec，一种新颖的基于LLM的推荐方法，它促进LLMs与TRMs之间自主的多轮交互，以实现对物品空间的深度探索。在每一轮交互中，LLMs对用户偏好进行推理，并与TRMs协作检索候选物品。经过多轮交互后，LLMs对聚合后的候选物品进行排序，生成最终推荐。我们利用强化学习（RL）进行优化，并在三个关键方面提出创新贡献：基于推荐模型的数据展开、面向推荐的分层奖励以及两阶段RL训练策略。在数据展开方面，我们设计了一种偏好感知的TRM，LLMs与之交互以构建轨迹数据。在奖励设计方面，我们提出一种分层奖励函数，包含过程级奖励与结果级奖励，分别用于优化交互过程与推荐质量。在RL训练方面，我们的两阶段RL策略首先引导LLMs学习与TRMs的有效交互，随后进行面向推荐的RL以提升性能。在公开数据集上的实验表明，DeepRec显著优于传统及现有基于LLM的基线方法，为推荐系统中的深度探索建立了新范式。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recently, large language models (LLMs) have been introduced into recommender systems (RSs) as recommendation backbones or to enhance traditional recommendation models (TRMs). However, existing LLM-based RSs fail to fully leverage the complementary strengths of LLMs (e.g., world knowledge and reasoning capabilities) and TRMs (e.g., recommendation-specific knowledge and computational efficiency), resulting in shallow exploration of the item space. To address this limitation, we propose DeepRec, a novel LLM-based RS approach that facilitates autonomous multi-turn interactions between LLMs and TRMs for deep item space exploration. In each interaction turn, LLMs reason over user preferences and collaborate with TRMs to retrieve candidate items. After multi-turn interaction, LLMs rank the aggregated candidates to generate the final recommendations. We utilize reinforcement learning (RL) for optimization and introduce novel contributions in three key aspects: recommendation model based data rollout, recommendation-oriented hierarchical rewards, and a two-stage RL training strategy. For data rollout, we design a preference-aware TRM, with which LLMs interact to construct trajectory data. For reward design, we propose a hierarchical reward function that comprises both process-level and outcome-level rewards to optimize the interaction process and recommendation quality, respectively. For RL training, our two-stage RL strategy first guides LLMs to learn effective interactions with TRMs, followed by recommendation-oriented RL for performance enhancement. Experiments on public datasets show that DeepRec substantially outperforms both traditional and existing LLM-based baselines, establishing a new paradigm for deep exploration in recommender systems.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出DeepRec，一种基于大语言模型（LLM）的推荐系统方法，通过LLM与传统推荐模型（TRM）之间的自主多轮交互实现深度物品空间探索。每轮交互中，LLM推理用户偏好并与TRM协作检索候选物品，多轮后聚合候选并排序生成最终推荐。采用强化学习优化，创新包括：偏好感知TRM的数据展开、推荐导向的分层奖励（过程级和结果级）、两阶段RL训练策略。实验表明DeepRec显著优于传统和现有LLM基线，为推荐系统深度探索建立新范式。

### 主要创新

- 提出LLM与TRM自主多轮交互机制，实现深度物品空间探索
- 设计偏好感知TRM用于数据展开，构建轨迹数据
- 提出推荐导向的分层奖励函数，包含过程级和结果级奖励
- 采用两阶段RL训练策略，先学习有效交互再优化推荐性能

### 研究方法

使用强化学习（RL）优化，具体包括：1）偏好感知TRM与LLM交互生成轨迹数据；2）分层奖励函数（过程级+结果级）指导优化；3）两阶段RL训练：第一阶段学习交互，第二阶段面向推荐性能优化。

### 关键结果

在公开数据集上，DeepRec显著优于传统和现有LLM基线，建立推荐系统深度探索新范式。

### 技术栈

- 大语言模型（LLM）
- 传统推荐模型（TRM）
- 强化学习（RL）
- 分层奖励函数

### 方法优势

- 充分利用LLM的世界知识和推理能力与TRM的推荐知识和计算效率，通过多轮交互实现深度探索；强化学习优化框架设计新颖，包含数据展开、分层奖励和两阶段训练。

### 主要局限

- 论文局限：摘要未提供具体数据集、基线模型、实验设置及消融结果，无法评估泛化性和计算开销。当前证据局限：仅基于摘要，缺乏方法细节和实验数据。

### 与当前研究方向的关联

高度相关：涉及LLM与推荐系统结合、推荐智能体（多轮交互）、强化学习优化，属于生成式推荐和推荐智能体方向。

---

_知识库更新时间：2026-07-18T03:48:20.893617_
