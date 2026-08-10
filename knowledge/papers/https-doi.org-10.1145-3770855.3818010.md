---
title: "G²PRO：基于梯度引导的图提示优化用于基于LLM的POI推荐"
paper_id: "https://doi.org/10.1145/3770855.3818010"
source: "citation"
published: "2026-08-07T00:00:00"
score: 98.0
tags: ["paper", "recommender-systems"]
---

# G²PRO：基于梯度引导的图提示优化用于基于LLM的POI推荐

> **英文原标题**：G²PRO: Gradient-guided Graph Prompt Optimization for LLM-based POI Recommendation

[查看原文](https://doi.org/10.1145/3770855.3818010)

## 一句话结论

> 提出G2PRO框架，通过梯度引导的图提示优化，结合GNN和LLM，有效提升基于LLM的POI推荐性能。

## 论文信息

- **作者**：Nan Jiang, Haitao Yuan, Tianjun Wei, Yingpeng Du, Jianing Si, Minxiao Chen, Jie Zhang, Zhu Sun
- **来源**：Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2
- **发布时间**：2026-08-07
- **相关度评分**：98.0
- **DOI**：[https://doi.org/10.1145/3770855.3818010](https://doi.org/10.1145/3770855.3818010)

<details open>
<summary><strong>中文摘要</strong></summary>

大型语言模型（LLMs）在序列推理方面展现出强大的潜力，为下一兴趣点（POI）推荐带来了新的机遇。然而，由于文本语义与连续时空信号之间的模态差异，将LLMs应用于POI预测仍面临挑战。现有的基于规则的提示方法在弥合这一差异时往往引入冗余上下文。为解决这一问题，我们提出了G2PRO，一种将图神经网络（GNNs）的结构感知能力与LLMs的推理能力相结合的协作框架。具体而言，我们构建了用户行为时空知识图谱（UST-KG）以捕捉POI关系与转移动态，并训练了一个轻量级基于GNN的提示选择器（GPS），用于选择信息丰富的POI节点以构建提示。我们进一步引入了一种梯度引导的正提示标注策略，通过提示嵌入上的梯度估计每个POI对目标预测的贡献，将提示选择转化为可优化的学习目标，而非手工设计的启发式规则。在四个真实数据集上的实验表明，G2PRO持续优于最先进的传统方法和基于LLM的基线方法。消融研究和分解研究进一步验证了各组件的有效性，并展示了结构感知、归因引导的提示方法对基于LLM的POI推荐的益处。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models (LLMs) have shown strong potential for sequential reasoning, creating new opportunities for next Point-of-Interest (POI) recommendation. However, applying LLMs to POI prediction remains challenging due to the modality gap between textual semantics and continuous spatio-temporal signals. Existing rule-based prompting methods often introduce redundant context when bridging this gap. To address this issue, we propose G2PRO, a collaborative framework that combines the structural perception of Graph Neural Networks (GNNs) with the reasoning capability of LLMs. Specifically, we construct a User-Behavior Spatio-Temporal Knowledge Graph (UST-KG) to capture POI relations and transition dynamics, and train a lightweight GNN-based Prompt Selector (GPS) to select informative POI nodes for prompt construction. We further introduce a gradient-guided positive prompt labeling strategy that estimates each POI's contribution to the target prediction through gradients over prompt embeddings, turning prompt selection into an optimizable learning objective rather than a hand-crafted heuristic. Experiments on four real-world datasets show that G2PRO consistently outperforms state-of-the-art traditional and LLM-based baselines. Ablation and breakdown studies further validate the effectiveness of each component and demonstrate the benefits of structure-aware, attribution-guided prompting for LLM-based POI recommendation.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出G²PRO框架，结合图神经网络的结构感知与大语言模型的推理能力，用于下一兴趣点推荐。针对文本语义与连续时空信号之间的模态差距，以及现有规则提示方法引入冗余上下文的问题，G²PRO构建用户行为时空知识图谱，并训练轻量级图提示选择器以选择信息丰富的POI节点构建提示。同时，引入梯度引导的正提示标注策略，通过提示嵌入的梯度估计每个POI对目标预测的贡献，将提示选择转化为可优化的学习目标。在四个真实数据集上的实验表明，G²PRO优于最先进的传统和基于LLM的基线，消融和分解研究验证了各组件的有效性。

### 主要创新

- 提出G²PRO协作框架，融合GNN的结构感知与LLM的推理能力，用于POI推荐。
- 构建用户行为时空知识图谱（UST-KG），捕获POI关系和转换动态。
- 设计轻量级图提示选择器（GPS），自动选择信息丰富的POI节点构建提示。
- 引入梯度引导的正提示标注策略，将提示选择转化为可优化的学习目标。

### 研究方法

构建用户行为时空知识图谱（UST-KG）以建模POI关系和转换动态；训练轻量级图神经网络（GNN）作为提示选择器（GPS），从知识图谱中选择信息丰富的POI节点；采用梯度引导的正提示标注策略，通过计算提示嵌入的梯度来估计每个POI对目标预测的贡献，从而优化提示选择；将选中的POI节点用于构建LLM的提示，利用LLM的推理能力进行最终推荐。

### 关键结果

在四个真实世界数据集上，G²PRO一致优于最先进的传统和基于LLM的基线。消融和分解研究进一步验证了每个组件的有效性，并展示了结构感知、属性引导的提示对基于LLM的POI推荐的好处。

### 技术栈

- 摘要未提供具体技术栈，但涉及大语言模型（LLM）、图神经网络（GNN）、知识图谱、梯度计算、提示学习等。

### 方法优势

- 提出新颖的协作框架，有效结合GNN和LLM的优势。
- 通过梯度引导的提示标注，将提示选择转化为可优化目标，避免手工启发式。
- 在多个真实数据集上验证了方法的有效性。

### 主要局限

- 摘要未提供明确的局限性讨论。当前证据仅基于摘要，无法评估方法的潜在缺点，如计算开销、对知识图谱质量的依赖等。

### 与当前研究方向的关联

论文与序列推荐、生成式推荐、LLM与推荐系统结合、推荐智能体等关键词高度相关，聚焦于利用LLM进行POI推荐，并创新性地结合GNN和梯度优化提示，属于LLM在推荐系统中的前沿应用。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3626772.3657828
- **seed_title**：Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning
- **seed_score**：90.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.671354_
