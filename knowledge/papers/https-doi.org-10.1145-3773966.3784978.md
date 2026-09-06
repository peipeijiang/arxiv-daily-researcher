---
title: "RankGraph-Context：赋能不同工业推荐系统阶段"
paper_id: "https://doi.org/10.1145/3773966.3784978"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Advanced Graph Neural Networks", "Recommender Systems and Techniques", "Graph Theory and Algorithms"]
---

# RankGraph-Context：赋能不同工业推荐系统阶段

> **英文原标题**：RankGraph-Context: Empowering Different Industrial Recommendation System Stages

[查看原文](https://dblp.org/rec/conf/wsdm/FuXLY26) · [Semantic Scholar](https://www.semanticscholar.org/paper/c4bfb2daaaab850c27f13fed12de37338a5ff904)

## 一句话结论

> 本文提出RankGraph-Context，一个图上下文框架，通过统一数据构建、训练和推理阶段来提升工业推荐系统的性能，在冷启动、长尾覆盖和跨面数据方面取得一致改进。

## 论文信息

- **作者**：Dongqi Fu, Yinglong Xia, H Li, Hong Yan
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3773966.3784978](https://doi.org/10.1145/3773966.3784978)

<details open>
<summary><strong>中文摘要</strong></summary>

工业推荐系统日益在异构产品、用户旅程和反馈回路中运行，然而大多数系统仍然在很大程度上孤立地优化各个阶段——数据整理、模型训练和推理。我们提出了RankGraph-Context，不同于图神经网络模型，它是一种知识丰富且敏捷的以图为中心的上下文框架，通过以下方式统一这些阶段：(i) 在数据构建过程中捕捉隐式关系信号，(ii) 在结构化关系上下文中调节训练，以及(iii) 在推理阶段通过训练后或测试时学习进行适应。在多个生产级场景中，RankGraph-Context在冷启动检索、长尾覆盖和跨面数据整理方面带来了一致的改进，同时通过测试时更新实现了安全的在线适应。我们详细阐述了该框架，在多个面和用例上进行了实例化，并报告了离线和在线结果，表明RankGraph-Context能够以可承受的工程开销赋能不同推荐系统阶段。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Industrial recommendation systems increasingly operate across heterogeneous products, user journeys, and feedback loops, yet most systems still optimize each stage—data curation, model training, and inference—largely in isolation. We present RankGraph-Context, different from a graph neural network model, which is a knowledgeable and agile graph-centric context framework that unifies these stages by (i) catching implicit relational signals during data construction, (ii) conditioning training on structured relational context, and (iii) adapting at inference time through post-training or test-time learning. Across several production-scale scenarios, RankGraph-Context delivers consistent improvements on cold-start retrieval, long-tail coverage, and cross-surface data curation, while enabling safe online adaptation through test-time updates. We detail the framework, instantiate it on multiple surfaces and use cases, and report offline and online results, showing that RankGraph-Context can empower different recommendation system stages with affordable engineering overhead.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

工业推荐系统通常涉及异构产品、用户旅程和反馈循环，但多数系统仍将数据整理、模型训练和推理等阶段孤立优化。本文提出RankGraph-Context，一个区别于图神经网络模型的知识型、敏捷的图中心上下文框架，通过（i）在数据构建时捕获隐式关系信号，（ii）在训练时基于结构化关系上下文进行条件化，（iii）在推理时通过训练后或测试时学习进行自适应，统一这些阶段。在多个生产规模场景中，RankGraph-Context在冷启动检索、长尾覆盖和跨面数据整理方面持续改进，同时通过测试时更新实现安全在线自适应。文章详述了框架，在多个面和用例上实例化，并报告离线和在线结果，表明RankGraph-Context能以可承受的工程开销赋能不同推荐系统阶段。

### 主要创新

- 提出一个统一的图中心上下文框架，连接数据构建、模型训练和推理阶段。
- 在数据构建时捕获隐式关系信号，丰富上下文信息。
- 在训练时利用结构化关系上下文进行条件化，提升模型泛化能力。
- 在推理时通过训练后或测试时学习实现安全在线自适应。
- 在多个生产规模场景中验证了冷启动检索、长尾覆盖和跨面数据整理的改进。

### 研究方法

论文提出RankGraph-Context框架，具体方法包括：（i）在数据构建阶段，通过图结构捕获用户和物品间的隐式关系信号；（ii）在训练阶段，将结构化关系上下文作为条件输入到模型训练中；（iii）在推理阶段，采用训练后调整或测试时学习机制，使模型能够适应新数据。框架在多个推荐表面和用例上实例化，并通过离线评估和在线实验验证效果。

### 关键结果

在多个生产规模场景中，RankGraph-Context在冷启动检索、长尾覆盖和跨面数据整理方面带来持续改进，并支持通过测试时更新实现安全在线自适应。离线与在线结果均表明其有效性。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 提出一个统一框架，解决推荐系统各阶段孤立优化的问题。
- 强调隐式关系信号的捕获和利用，增强上下文感知。
- 支持在线自适应，适应动态环境。
- 在多个生产场景中验证，具有实际应用价值。
- 工程开销可控，易于部署。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：由于仅提供摘要，无法评估方法的细节、对比实验、可复现性等，需全文进一步分析。

### 与当前研究方向的关联

该论文与推荐系统领域高度相关，涉及工业推荐系统、图上下文、数据构建、训练与推理统一、冷启动、长尾覆盖、在线自适应等关键词，对排序与重排、用户建模、CTR/CVR预测等方向有潜在贡献。

---

_知识库更新时间：2026-09-06T04:59:26.701294_
