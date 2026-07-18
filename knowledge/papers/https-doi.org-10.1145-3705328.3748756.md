---
title: "通过社会选择解决推荐系统中的多利益相关者公平性问题"
paper_id: "https://doi.org/10.1145/3705328.3748756"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Mobile Crowdsensing and Crowdsourcing", "Advanced Bandit Algorithms Research", "Recommender Systems and Techniques"]
---

# 通过社会选择解决推荐系统中的多利益相关者公平性问题

> **英文原标题**：Addressing Multi-stakeholder Fairness Concerns in Recommender Systems Through Social Choice

[查看原文](https://dblp.org/rec/conf/recsys/Aird25) · [Semantic Scholar](https://www.semanticscholar.org/paper/e198c0c7f0e5184e0ae87f5816240d1491c8d808)

## 一句话结论

> 该研究提出基于社会选择的SCRUF-D架构，通过重排序推荐列表来同时处理多个公平性定义，并评估了准确性与公平性之间的权衡。

## 论文信息

- **作者**：Amanda Aird
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3705328.3748756](https://doi.org/10.1145/3705328.3748756)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统中的公平性已在群体和个体层面展开讨论，涉及提供方与消费方的双重关切。但当前许多提升推荐系统公平性的解决方案仅能应对单一公平性问题，或对公平性的定义存在局限。我的研究致力于通过一种能够处理多重复杂公平性问题的方案来改进推荐系统的公平性。我采用基于多智能体社会选择架构的SCRUF-D（动态公平性推荐社会选择）方法，对推荐结果进行重排序，以提升多维度公平性。已完成的研究评估了在提供方侧针对多种公平性定义进行重排序时，准确性与公平性之间的权衡关系，包括探索不同社会选择规则与智能体分配机制对此权衡的影响。目前，我正在将研究扩展至包含个体与消费方侧的公平性指标。正在进行的研究旨在纳入消费方侧公平性指标，评估准确性与公平性之间的权衡。未来计划开展处理不同类型公平性之间矛盾的研究，并通过人类研究验证SCRUF的价值。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Fairness in recommender systems has been discussed on the group and individual level with concerns for both providers and consumers. But many current solutions to improving fairness in recommender systems can only address one fairness concern or have limited definitions of fairness. My research revolves around improving fairness in recommender systems with an approach that addresses multiple and complex fairness concerns. I use SCRUF-D (Social Choice for Recommendation Under Fairness - Dynamic), a multi-agent social choice-based architecture, for reranking recommendations to improve fairness across multiple dimensions. My completed research has evaluated trade-offs between accuracy and fairness when reranking for multiple fairness definitions on the provider side. This includes exploring how different social choice rules and agent allocation mechanisms impact this trade-off. Currently, I am focused on expanding these studies to include individual and consumer-side fairness metrics. My ongoing research aims to evaluate the trade-offs between accuracy and fairness, incorporating consumer-side fairness metrics. Research to handle tensions between different types of fairness and human research to demonstrate the value of SCRUF is being planned.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

该论文提出了一种基于社会选择的多智能体架构SCRUF-D，用于在推荐系统中重排序推荐结果，以改善多个维度的公平性。研究评估了在提供者侧针对多种公平定义进行重排序时，准确性与公平性之间的权衡，并探索了不同社会选择规则和智能体分配机制对此权衡的影响。当前研究正在扩展至个体和消费者侧的公平性指标，并计划处理不同类型公平性之间的张力以及进行人类研究以展示SCRUF的价值。

### 主要创新

- 提出SCRUF-D架构，基于多智能体社会选择方法解决推荐系统中的多利益相关者公平性问题
- 同时处理多个公平性定义，超越单一公平性关注
- 探索不同社会选择规则和智能体分配机制对准确性与公平性权衡的影响
- 将公平性研究从提供者侧扩展至消费者侧和个体层面

### 研究方法

采用SCRUF-D（Social Choice for Recommendation Under Fairness - Dynamic）架构，通过多智能体社会选择方法对推荐结果进行重排序，以改善多个维度的公平性。研究通过实验评估不同社会选择规则和智能体分配机制下准确性与公平性的权衡。

### 关键结果

摘要未提供具体实验结果，但指出已完成的研究评估了提供者侧重排序时准确性与公平性的权衡，并探索了不同社会选择规则和智能体分配机制的影响。

### 技术栈

- SCRUF-D架构、社会选择规则、智能体分配机制

### 方法优势

- 提出了一种新颖的多智能体社会选择方法，能够同时处理多个公平性定义；研究覆盖提供者、消费者和个体多个利益相关者视角；计划进行人类研究以验证实际价值。

### 主要局限

- 论文局限：当前研究主要聚焦提供者侧公平性，消费者侧和个体公平性研究尚在进行中；未提供具体实验数据和结果。当前证据局限：仅基于摘要，缺乏具体方法细节、数据集、基线、实验结果和代码可用性信息。

### 与当前研究方向的关联

与推荐系统公平性高度相关，涉及多利益相关者公平、重排序方法；与排序与重排、推荐系统鲁棒性相关；未涉及序列推荐、生成式推荐、LLM、多模态、对话式推荐、CTR/CVR预测等关键词。

---

_知识库更新时间：2026-07-18T03:48:20.892359_
