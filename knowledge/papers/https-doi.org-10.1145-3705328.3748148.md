---
title: "Informfully推荐器——面向多样性感知会话内推荐的可复现性框架"
paper_id: "https://doi.org/10.1145/3705328.3748148"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Information Retrieval and Search Behavior"]
---

# Informfully推荐器——面向多样性感知会话内推荐的可复现性框架

> **英文原标题**：Informfully Recommenders - Reproducibility Framework for Diversity-aware Intra-session Recommendations

[查看原文](https://dblp.org/rec/conf/recsys/HeitzLIB25) · [ArXiv](https://arxiv.org/abs/2508.13019)

## 一句话结论

> The paper presents Informfully Recommenders, a reproducibility framework for diversity-aware intra-session recommendations, providing an end-to-end solution for implementing and experimenting with normative and diverse recommender systems.

## 论文信息

- **作者**：Lucien Heitz, Runze Li, Oana Inel, Abraham Bernstein
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3705328.3748148](https://doi.org/10.1145/3705328.3748148)

<details open>
<summary><strong>中文摘要</strong></summary>

规范感知的推荐系统已获得越来越多的关注，尤其是在多样性优化方面。推荐系统社区已建立了成熟的实验流程，通过促进模型基准测试及与最先进方法的比较，支持可复现的评估。然而，据我们所知，目前尚无一个可复现性框架能够在推荐流程的预处理、处理中、后处理及评估阶段支持全面的规范驱动实验。为填补这一空白，我们提出了Informfully Recommenders，这是迈向规范性可复现性框架的第一步，该框架聚焦于基于Cornac构建的多样性感知设计。我们的扩展提供了一个端到端的解决方案，用于实现和实验规范性与通用型多样化推荐系统，涵盖：1）数据集预处理，2）多样性优化模型，3）专门的会话内项目重排序，以及4）一套广泛的多样性度量指标。我们通过在新闻领域进行的大规模离线实验，展示了我们扩展的能力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Norm-aware recommender systems have gained increased attention, especially for diversity optimization. The recommender systems community has well-established experimentation pipelines that support reproducible evaluations by facilitating models' benchmarking and comparisons against state-of-the-art methods. However, to the best of our knowledge, there is currently no reproducibility framework to support thorough norm-driven experimentation at the pre-processing, in-processing, post-processing, and evaluation stages of the recommender pipeline. To address this gap, we present Informfully Recommenders, a first step towards a normative reproducibility framework that focuses on diversity-aware design built on Cornac. Our extension provides an end-to-end solution for implementing and experimenting with normative and general-purpose diverse recommender systems that cover 1) dataset pre-processing, 2) diversity-optimized models, 3) dedicated intrasession item re-ranking, and 4) an extensive set of diversity metrics. We demonstrate the capabilities of our extension through an extensive offline experiment in the news domain.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出了Informfully Recommenders，一个基于Cornac框架的扩展，旨在为规范性推荐系统（NRS）提供端到端的可复现性框架，特别关注多样性优化。该框架覆盖推荐管道的四个阶段：预处理（数据增强）、处理中（模型选择）、后处理（重排序）和评估（多样性指标）。它提供了六种数据增强功能、多种多样性优化模型（包括随机游走和过滤算法）、静态和动态重排序器、用户模拟器以及多种传统和规范性多样性指标。通过三个新闻数据集（EB-NeRD、MIND、NeMig）的实验，展示了框架在评估多样性感知推荐系统方面的能力，并比较了不同模型和重排序策略在多样性和准确性上的权衡。

### 主要创新

- 首次提出一个统一的、端到端的规范性推荐系统可复现性框架，覆盖预处理、处理中、后处理和评估四个阶段。
- 提供了六种数据增强功能，支持多语言，用于添加规范性相关属性（如政治派别、情感等）。
- 引入了三种随机游走模型和两种轻量级规范性过滤算法，以及三种静态重排序器和两种动态会话内重排序器。
- 集成了五种传统多样性指标和五种规范性RADio指标，用于全面评估推荐多样性。
- 与Informfully研究平台兼容，支持在线用户研究的可视化。

### 研究方法

论文采用基于Cornac框架的扩展方法，构建了模块化的推荐管道。通过数据增强（如命名实体识别、情感分析、政治角色识别等）丰富数据集，然后使用多种模型（包括神经网络、随机游走、过滤算法）生成候选列表，再通过静态或动态重排序优化多样性，最后使用传统和规范性多样性指标进行评估。实验在三个新闻数据集上进行，比较了不同模型和重排序策略的性能。

### 关键结果

实验结果显示，基于目标分布（NTD）的模型和重排序器在传统多样性指标（如Gini系数和ILD）上表现最佳，接近理论最优值。在RADio指标上，NTD优化模型在EB-NeRD和MIND上表现突出，但在NeMig上动态重排序效果更好。随机游走模型在数据稀疏时性能下降。整体上，框架能够有效评估多样性感知推荐系统的性能。

### 技术栈

- Cornac框架
- RoBERTa（情感分析）
- spaCy（命名实体识别）
- Wikidata（政治角色增强）
- Textstat（文本复杂度）
- NetworkX（故事聚类）
- BART（文章分类）
- GloVe和fastText（词嵌入）
- Sentence Transformers（文章相似度）
- Greedy-KL、PM-2、MMR（静态重排序）
- 动态属性惩罚（DAP）
- RADio指标
- Gini系数、ILD等传统多样性指标

### 方法优势

- 提供了一个全面的、模块化的框架，覆盖推荐管道的所有关键阶段，便于研究人员进行系统性实验。
- 支持多种数据增强功能，能够为规范性推荐系统添加必要的属性信息。
- 集成了多种模型和重排序策略，包括规范性算法，便于比较不同方法。
- 提供了用户模拟器，支持动态会话内重排序的评估。
- 与Informfully平台兼容，支持在线用户研究。

### 主要局限

- 实验仅基于新闻领域，可能不适用于其他领域。
- 数据增强功能可能依赖于外部库和API，可能影响可复现性。
- 用户模拟器较为简单，可能无法完全模拟真实用户行为。
- 部分模型（如随机游走）在数据稀疏时性能不佳。
- 论文未提供详细的代码示例或教程，可能影响框架的易用性。

### 与当前研究方向的关联

推荐系统：论文提出了一个推荐系统框架，属于推荐系统研究。；多样性：论文聚焦于多样性感知的推荐，包括传统和规范性多样性指标。；可复现性：论文强调框架的可复现性，提供了端到端的实验流程。；新闻推荐：实验在新闻数据集上进行，与新闻推荐相关。；重排序：论文实现了静态和动态重排序策略。；用户模拟：论文提供了用户模拟器，用于评估动态重排序。

## 代码与复现

- [Informfully/Recommenders](https://github.com/Informfully/Recommenders)：likely，置信度 69，Stars 5

---

_知识库更新时间：2026-08-16T02:20:30.029896_
