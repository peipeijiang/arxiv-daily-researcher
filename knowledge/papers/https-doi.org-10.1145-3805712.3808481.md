---
title: "多任务排序中相关性与参与度的联合优化：基于高效LLM监督的电商应用"
paper_id: "https://doi.org/10.1145/3805712.3808481"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 53.0
tags: ["paper", "recommender-systems", "Information Retrieval and Search Behavior", "Expert finding and Q&A systems", "Text and Document Classification Technologies"]
---

# 多任务排序中相关性与参与度的联合优化：基于高效LLM监督的电商应用

> **英文原标题**：Joint Optimization of Relevance and Engagement in Multi-Task Ranking for E-Commerce with Efficient LLM Supervision

[查看原文](https://dblp.org/rec/conf/sigir/ChenXSWD26) · [ArXiv](https://arxiv.org/abs/2605.27704) · [Semantic Scholar](https://www.semanticscholar.org/paper/db095f859e4f01cca667d95ca0c59d5ca1631b08)

## 一句话结论

> 该论文提出一个工业多任务排序系统，通过轻量级LLM生成相关性标签，联合优化相关性和用户参与度，显著提升语义对齐效果。

## 论文信息

- **作者**：Luming Chen, Jiaqi Xi, Raghav Saboo, Kenny Chi, Martin Wang
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：53.0
- **DOI**：[https://doi.org/10.1145/3805712.3808481](https://doi.org/10.1145/3805712.3808481)

<details open>
<summary><strong>中文摘要</strong></summary>

优化工业搜索排序模型仅针对用户参与信号往往会导致系统性偏差，优先展示热门或价格锚定商品，而这些商品可能无法满足语义意图。我们提出了一套生产级多任务排序系统，将语义相关性作为主要优化目标，实现了显式且可控的相关性-参与度权衡。该架构采用有序相关性预测头，可预测各相关性阈值上的累积概率，从而保留标签的固有排序。这些输出通过统一的价值模型评分函数与参与度预测头集成，实现了语义质量与短期行为信号之间的系统性平衡。为了为该多任务框架提供高质量监督，我们利用经过微调的轻量级大语言模型（LLMs）生成三级有序相关性标签：不相关、中度相关和高度相关。我们解决了标签分布敏感性问题，并确保与人工标注高度一致，从而实现对超过1亿个查询-商品对的高效标注。离线指标（包括NDCG@10）评估及在线A/B实验均表明，我们的方法在保持核心参与目标的同时显著提升了语义对齐效果。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Optimizing industrial search ranking models solely for user engagement signals often introduces systematic biases, prioritizing popular or price-anchored items that may not satisfy semantic intent. We present a production-scale multi-task ranking system that integrates semantic relevance as a primary optimization objective, enabling explicit and controllable relevance--engagement trade-offs. Our architecture employs an ordinal relevance head that predicts cumulative probabilities over relevance thresholds, preserving the inherent ordering of labels. These outputs are integrated with engagement heads through a unified value model scoring function, enabling systematic balancing of semantic quality and short-term behavioral signals. To provide high-quality supervision for this multi-task framework, we utilize fine-tuned lightweight Large Language Models (LLMs) to generate three-level ordinal relevance labels: irrelevant, moderately relevant, and highly relevant. We address challenges regarding label distribution sensitivity and ensure high alignment with human annotations to enable efficient labeling for over 100 million query--item pairs. Evaluation across offline metrics, including NDCG@10, and online A/B experiments demonstrates that our approach significantly improves semantic alignment while preserving core engagement objectives.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出一个生产级多任务排序系统，将语义相关性作为主要优化目标，实现相关性与参与度之间的显式可控权衡。系统采用序数相关性头预测累积概率，并通过统一价值模型评分函数与参与度头集成。为提供高质量监督，利用微调轻量级LLM生成三级序数相关性标签（不相关、中等相关、高度相关），并解决标签分布敏感性问题，确保与人工标注高度对齐，为超过1亿查询-物品对高效生成标签。离线指标（NDCG@10）和在线A/B实验表明，该方法显著提升语义对齐，同时保持核心参与度目标。

### 主要创新

- 设计可扩展的LLM相关性监督流水线，生成与生产查询分布对齐的高质量序数标签。
- 将序数语义相关性直接集成到多任务排序目标中，实现相关性与参与度的可控权衡。
- 在大规模生产搜索系统中展示离线相关性改进和正向在线影响。
- 序数相关性头相比标准分类和回归基线，在相关性NDCG上表现更优。

### 研究方法

采用多任务深度神经网络架构，共享底层处理查询、物品和用户特征，分别通过任务特定塔预测CTR、ATCR、CVR和相关性。相关性头使用序数预测，输出两个概率（至少相关和高度相关）。LLM标签通过微调gpt-4o-mini生成，基于约60万人工标注，经审计和冲突解决后，对超过1亿查询-物品对生成标签。最终排序分数通过线性加权组合参与度预测和相关性得分。

### 关键结果

离线实验显示，序数相关性头在相关性NDCG@10上达到0.962，优于基线（0.812）和软max（0.961）及回归（0.959）变体。在线A/B实验显示ATCR提升1.16%（p=0.01），CVR提升1.10%（p=0.01），GOV提升0.50%（p=0.03）。

### 技术栈

- 多任务学习
- 深度神经网络
- 序数分类
- LLM微调（gpt-4o-mini）
- BM25
- NDCG@10
- AUC
- 价值模型评分函数

### 方法优势

- 将LLM监督高效集成到生产排序系统，无需在线LLM推理。
- 序数相关性头保持标签自然顺序，提升排序质量。
- 统一价值函数允许在服务时显式控制相关性与参与度权衡。
- 离线与在线实验均验证有效性，包括显著业务指标提升。

### 主要局限

- LLM标签生成依赖人工标注和审计，成本较高。
- 标签分布敏感性需精心采样策略，可能影响泛化。
- 未探索查询自适应权重或长期用户满意度指标。
- 实验仅在单一电商平台进行，通用性待验证。

### 与当前研究方向的关联

论文直接涉及LLM与推荐系统结合、多任务排序、相关性优化、CTR/CVR预测，以及工业落地，与序列推荐、生成式推荐、推荐智能体等关键词部分相关，但未涉及多模态或对话式推荐。

---

_知识库更新时间：2026-07-21T04:03:10.446258_
