---
title: "Hierarchical Graph Information Bottleneck for Multi-Behavior Recommendation"
paper_id: "https://doi.org/10.1145/3705328.3748073"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Complex Network Analysis Techniques"]
---

# Hierarchical Graph Information Bottleneck for Multi-Behavior Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/0001SS0T00Y25) · [ArXiv](https://arxiv.org/abs/2507.15395)

## 一句话结论

> 针对多行为推荐中行为分布差异和辅助行为噪声问题，提出层次化图信息瓶颈框架HGIB，通过信息瓶颈和边剪枝学习紧凑表示，在公开和工业数据集上显著提升目标行为预测性能。

## 论文信息

- **作者**：Hengyu Zhang, Chunxu Shen, Xiangguo Sun, Jie Tan, Yanchao Tan, Yu Rong, Hong Cheng, Lingling Yi
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3705328.3748073](https://doi.org/10.1145/3705328.3748073)

<details open>
<summary><strong>中文摘要</strong></summary>

在现实推荐场景中，用户通常通过多种类型的行为交互与平台互动。多行为推荐算法旨在利用各种辅助用户行为来增强对主要关注目标行为（如购买）的预测，从而克服目标行为记录中数据稀疏性导致的性能限制。当前最先进的方法通常采用层级设计，遵循级联（例如，浏览→加入购物车→购买）或并行（统一→行为→特定组件）范式来捕捉行为关系。然而，这些方法仍面临两个关键挑战：（1）不同行为之间存在严重的分布差异，以及（2）辅助行为中的噪声导致的负迁移效应。在本文中，我们提出了一种新颖的、模型无关的层级图信息瓶颈（Hierarchical Graph Information Bottleneck, HGIB）框架，用于多行为推荐，以有效应对这些挑战。遵循信息瓶颈原理，我们的框架优化了紧凑且充分表示的习得过程，这些表示在保留目标行为预测所需关键信息的同时，消除了与任务无关的冗余。为进一步减轻交互噪声，我们引入了一个图精炼编码器（Graph Refinement Encoder, GRE），通过可学习的边丢弃机制动态剪枝冗余边。我们在三个真实世界公开数据集上进行了全面实验，结果表明我们的框架具有卓越的有效性。除了学术界广泛使用的这些数据集外，我们进一步在多个真实工业场景中扩展了评估，并进行了在线A/B测试，再次显示出在多行为推荐中的显著改进。我们提出的HGIB的源代码可在https://github.com/zhy99426/HGIB获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In real-world recommendation scenarios, users typically engage with platforms through multiple types of behavioral interactions. Multi-behavior recommendation algorithms aim to leverage various auxiliary user behaviors to enhance prediction for target behaviors of primary interest (e.g., buy), thereby overcoming performance limitations caused by data sparsity in target behavior records. Current state-of-the-art approaches typically employ hierarchical design following either cascading (e.g., view$\rightarrow$cart$\rightarrow$buy) or parallel (unified$\rightarrow$behavior$\rightarrow$specific components) paradigms, to capture behavioral relationships. However, these methods still face two critical challenges: (1) severe distribution disparities across behaviors, and (2) negative transfer effects caused by noise in auxiliary behaviors. In this paper, we propose a novel model-agnostic Hierarchical Graph Information Bottleneck (HGIB) framework for multi-behavior recommendation to effectively address these challenges. Following information bottleneck principles, our framework optimizes the learning of compact yet sufficient representations that preserve essential information for target behavior prediction while eliminating task-irrelevant redundancies. To further mitigate interaction noise, we introduce a Graph Refinement Encoder (GRE) that dynamically prunes redundant edges through learnable edge dropout mechanisms. We conduct comprehensive experiments on three real-world public datasets, which demonstrate the superior effectiveness of our framework. Beyond these widely used datasets in the academic community, we further expand our evaluation on several real industrial scenarios and conduct an online A/B testing, showing again a significant improvement in multi-behavior recommendations. The source code of our proposed HGIB is available at https://github.com/zhy99426/HGIB.

</details>

---

_知识库更新时间：2026-07-14T04:41:25.081762_
