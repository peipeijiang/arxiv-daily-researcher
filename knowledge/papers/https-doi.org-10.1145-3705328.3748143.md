---
title: "基于层次序列转换器的上下文并行扩展生成式推荐"
paper_id: "https://doi.org/10.1145/3705328.3748143"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 45.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Generative Adversarial Networks and Image Synthesis", "Caching and Content Delivery"]
---

# 基于层次序列转换器的上下文并行扩展生成式推荐

> **英文原标题**：Scaling Generative Recommendations with Context Parallelism on Hierarchical Sequential Transducers

[查看原文](https://dblp.org/rec/conf/recsys/DongLLPLWZ25)

## 一句话结论

> 该论文提出了一种支持上下文并行的层次序列转换器（HSTU），通过处理锯齿张量实现更长的用户交互序列，从而提升生成式推荐系统的性能。

## 论文信息

- **作者**：Yan Dong, Han Li, Shen Li, Nikhil Patel, Xing Liu, Xiaodong Wang, Chuanhao Zhuge
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：45.0
- **DOI**：[https://doi.org/10.1145/3705328.3748143](https://doi.org/10.1145/3705328.3748143)

<details open>
<summary><strong>中文摘要</strong></summary>

大规模推荐系统对于处理海量的日常用户交互至关重要，需要对高基数和异构特征进行有效建模，以确保预测的准确性。在先前的工作中，我们引入了层次化序列换能器（Hierarchical Sequential Transducers, HSTU），这是一种基于注意力机制的架构，用于对高基数、非平稳的流式推荐数据进行建模，并在生成式推荐器框架（Generative Recommender, GR）中展现了良好的扩展规律。近期研究和实验表明，关注更长的用户历史序列能够带来显著的指标提升。然而，扩展序列长度会带来较高的激活内存开销，因此需要并行化解决方案来有效切分激活内存。在基于Transformer的大语言模型（LLM）中，上下文并行（Context Parallelism, CP）是一种常用技术，它将计算沿序列长度维度分布到多个GPU上，从而有效降低由注意力激活产生的内存占用。相比之下，生产级排序模型通常使用锯齿状输入张量（jagged input tensors）来表示用户交互特征，这给CP的实现带来了独特的挑战。在本工作中，我们引入了支持锯齿状张量的上下文并行机制，用于HSTU注意力计算，为扩展序列维度奠定了基本能力。我们的方法使得支持的用户交互序列长度提升了5.3倍，同时在与分布式数据并行（Distributed Data Parallelism, DDP）结合时，实现了1.55倍的扩展因子。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large-scale recommendation systems are pivotal to process an immense volume of daily user interactions, requiring the effective modeling of high cardinality and heterogeneous features to ensure accurate predictions.In prior work, we introduced Hierarchical Sequential Transducers (HSTU), an attention-based architecture for modeling high cardinality, non-stationary streaming recommendation data, providing good scaling law in the generative recommender framework (GR).Recent studies and experiments demonstrate that attending to longer user history sequences yields significant metric improvements.However, scaling sequence length is activation-heavy, necessitating parallelism solutions to effectively shard activation memory.In transformer-based LLMs, context parallelism (CP) is a commonly used technique that distributes computation along the sequence-length dimension across multiple GPUs, effectively reducing memory usage from attention activations.In contrast, production ranking models typically utilize jagged input tensors to represent user interaction features, introducing unique CP implementation challenges.In this work, we introduce context parallelism with jagged tensor support for HSTU attention, establishing foundational capabilities for scaling up sequence dimensions.Our approach enables a 5.3 increase in supported user interaction sequence length, while achieving a 1.55 scaling factor when combined with Distributed Data Parallelism (DDP).

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

大规模推荐系统需要处理海量用户交互数据，并有效建模高基数、异构特征。先前工作提出了层次序列转换器（HSTU），一种基于注意力的架构，用于建模高基数、非平稳的流式推荐数据，在生成式推荐框架中展现出良好的扩展性。近期研究表明，增加用户历史序列长度能显著提升指标。然而，长序列导致激活内存过高，需要并行化方案。在基于Transformer的LLM中，上下文并行（CP）是一种常用技术，沿序列长度维度在多个GPU上分配计算，有效降低注意力激活的内存占用。相比之下，生产级排序模型通常使用不规则张量表示用户交互特征，给CP实现带来独特挑战。本文针对HSTU注意力引入支持不规则张量的上下文并行，为扩展序列维度奠定基础。该方法将支持的用户交互序列长度提升5.3倍，并与分布式数据并行（DDP）结合时实现1.55倍的扩展因子。

### 主要创新

- 首次为HSTU注意力引入支持不规则张量的上下文并行，解决生产级排序模型中不规则输入带来的并行化难题。
- 实现了用户交互序列长度5.3倍的提升，显著扩展了模型可处理的历史序列范围。
- 与分布式数据并行（DDP）结合，实现了1.55倍的扩展因子，展示了并行策略的有效组合。
- 为生成式推荐系统中长序列建模提供了可扩展的并行方案，推动了该领域的发展。

### 研究方法

论文主要采用上下文并行（CP）技术，将序列长度维度上的计算分布到多个GPU上，以减少注意力激活的内存占用。针对生产级排序模型中的不规则张量输入，设计了专门的CP实现，以支持HSTU注意力。通过实验验证了该方法在扩展序列长度和提升扩展因子方面的有效性。

### 关键结果

论文提出的方法使支持的用户交互序列长度增加了5.3倍，并在与分布式数据并行（DDP）结合时实现了1.55倍的扩展因子。

### 技术栈

- 层次序列转换器（HSTU）
- 上下文并行（CP）
- 分布式数据并行（DDP）
- 不规则张量（jagged tensors）
- 注意力机制

### 方法优势

- 针对生产级推荐系统的实际挑战（不规则输入）提出了有效的并行方案，具有实用价值。
- 显著提升了序列长度支持能力，有助于利用更长历史序列提升推荐性能。
- 与DDP结合展示了良好的扩展性，为大规模部署提供了可能。
- 基于先前工作HSTU，延续了生成式推荐的研究方向，具有连贯性。

### 主要局限

- 论文局限：摘要未提及具体实验设置、数据集、基线对比或消融研究，无法全面评估方法的普适性和优势。
- 当前证据局限：仅基于摘要，缺乏对方法细节、性能对比和潜在缺点的深入分析。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、LLM与推荐系统结合、用户建模、CTR/CVR预测等关键词高度相关。它聚焦于扩展用户历史序列长度，属于序列推荐和用户建模的核心问题；采用生成式推荐框架（GR）和HSTU架构，与生成式推荐和LLM结合方向一致；同时涉及工业落地中的并行化挑战，与工业推荐系统紧密相关。

---

_知识库更新时间：2026-08-02T04:11:29.699526_
