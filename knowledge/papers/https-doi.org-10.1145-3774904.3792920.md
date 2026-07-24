---
title: "序列感知可解释推荐中的文本上下文审计"
paper_id: "https://doi.org/10.1145/3774904.3792920"
source: "www"
published: "2026-01-01T00:00:00"
score: 48.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)", "Topic Modeling"]
---

# 序列感知可解释推荐中的文本上下文审计

> **英文原标题**：Auditing Textual Context in Sequence-Aware Explainable Recommendation

[查看原文](https://dblp.org/rec/conf/www/Ariza-CasabonaS26) · [Semantic Scholar](https://www.semanticscholar.org/paper/b7f5b149adc536b5d0a4b44d90b1a04c0ae1eb7e)

## 一句话结论

> 该论文研究了在序列感知可解释推荐中，如何通过多种文本聚合、融合机制和训练策略将用户历史交互的文本信息注入物品嵌入，以提升推荐性能和解释质量。

## 论文信息

- **作者**：Alejandro Ariza-Casabona, María Salamó, Ludovico Boratto
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：48.0
- **DOI**：[https://doi.org/10.1145/3774904.3792920](https://doi.org/10.1145/3774904.3792920)

<details open>
<summary><strong>中文摘要</strong></summary>

自解释推荐系统通过提供推荐理由来增强用户信任。序列感知模型利用用户交互历史实现个性化推荐与解释，推动了该领域的发展。然而，生成模型在处理稀疏数据时往往会产生重复或无关的解释。本文探索了将用户历史交互中的丰富文本信息直接注入项目嵌入（item embeddings）的最优方法，以构建用户推理路径，从而生成个性化解释。我们对多种技术进行了全面分析，包括：(1) 多种文本聚合策略，将细粒度的属性级用户观点汇聚为用户聚合的项目文本表示（user-aggregated item text representations）；(2) 多种融合机制，用于结合文本模态与协同模态（collaborative modalities），涵盖从早期融合（early fusion）到Transformer架构中的晚期融合（late fusion）方法；(3) 不同的解释生成训练范式。在三个真实数据集上的实验表明，为成功将文本信息融入序列感知可解释推荐模型，并提升推荐性能与解释质量，应遵循的具体步骤。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Self-explaining recommenders enhance user trust by providing justifications for their suggestions. Sequence-aware models have advanced the field by leveraging user interaction history to personalize recommendations and explanations. However, generative models often struggle with sparse data, producing repetitive or irrelevant explanations. This paper explores the optimal methods for infusing rich textual information from past user interactions directly into the item embeddings to feed a user reasoning path leading to personalized explanations. We conduct a comprehensive analysis of various techniques, including: (1) multiple text aggregation strategies to pool fine-grained attributed item opinions into user-aggregated item text representations; (2) several fusion mechanisms to combine text and collaborative modalities, from early fusion to a late fusion approach within the Transformer architecture; and (3) different training regimes for explanation generation. Experiments on three real-world datasets demonstrate which steps to follow in order to successfully leverage textual information into a sequence-aware explainable recommendation model and boost recommendation performance as well as explanation quality.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文研究如何有效利用用户交互历史中的丰富文本信息来提升序列感知可解释推荐系统的性能。针对生成模型在稀疏数据下产生重复或无关解释的问题，作者探索了多种文本注入方法：包括多种文本聚合策略将细粒度属性意见整合为用户聚合的文本表示；多种融合机制（从早期融合到Transformer架构中的晚期融合）结合文本与协同模态；以及不同的解释生成训练策略。在三个真实数据集上的实验表明，遵循所提出的步骤能成功利用文本信息，提升推荐性能和解释质量。

### 主要创新

- 系统比较了多种文本聚合策略以从用户交互中提取细粒度属性意见
- 探索了从早期融合到晚期融合的多种文本与协同模态融合机制
- 研究了不同训练策略对解释生成的影响
- 提供了在序列感知可解释推荐中有效利用文本信息的完整步骤指南

### 研究方法

论文采用实验研究方法，在三个真实数据集上比较不同文本聚合策略、融合机制和训练策略。文本聚合策略用于将用户交互中的属性意见整合为文本表示；融合机制包括早期融合和Transformer架构中的晚期融合；训练策略针对解释生成进行优化。通过推荐性能和解释质量指标评估各方法效果。

### 关键结果

实验结果表明，遵循所提出的步骤能够成功利用文本信息，提升推荐性能和解释质量。具体数值和指标摘要未提供。

### 技术栈

- 摘要未提供具体算法、工具或数学方法名称。

### 方法优势

- 聚焦于序列感知可解释推荐中文本信息利用的关键问题
- 系统性地比较了多种文本聚合、融合和训练策略
- 在多个真实数据集上进行实验，结果具有可靠性

### 主要局限

- **论文局限**：摘要未提及具体局限性，如可能对稀疏数据敏感或计算开销较大。
- **当前证据局限**：仅基于摘要，无法评估实验细节、基线对比、消融研究等，结论的泛化性需进一步验证。

### 与当前研究方向的关联

论文与序列推荐、生成式推荐、多模态推荐高度相关，涉及用户交互历史中的文本信息利用，属于推荐系统与自然语言处理交叉领域。

---

_知识库更新时间：2026-07-24T04:05:55.202267_
