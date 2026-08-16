---
title: "EARN：通过寄存器令牌实现基于LLM的生成式推荐的高效推理加速"
paper_id: "https://doi.org/10.1145/3711896.3736919"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 95.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Machine Learning in Healthcare"]
---

# EARN：通过寄存器令牌实现基于LLM的生成式推荐的高效推理加速

> **英文原标题**：EARN: Efficient Inference Acceleration for LLM-based Generative Recommendation by Register Tokens

[查看原文](https://dblp.org/rec/conf/kdd/0002000SHC25)

## 一句话结论

> 本文提出EARN框架，利用早期层的注意力模式将信息压缩到注册令牌中，以加速基于LLM的生成式推荐，实现高达3.79倍加速和80.8%的KV缓存减少，同时保持或提升准确性。

## 论文信息

- **作者**：Chaoqun Yang, Xinyu Lin, Wenjie Wang, Yongqi Li, Teng Sun, Xianjing Han, Tat‐Seng Chua
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：95.0
- **DOI**：[https://doi.org/10.1145/3711896.3736919](https://doi.org/10.1145/3711896.3736919)

<details open>
<summary><strong>中文摘要</strong></summary>

基于大语言模型的生成式推荐（LLMRec）已取得显著成功，但其因巨大的计算开销和KV缓存的内存压力而面临高推理延迟问题。现有的KV缓存缩减方法存在关键局限性：鉴于推荐任务解码步骤较短，缓存压缩带来的加速效果有限；而提示压缩则可能丢失重要的交互历史信息。通过对LLMRec中注意力模式的系统分析，我们揭示了两个关键发现：1）逐层注意力稀疏性反转现象，即早期层保留密集的信息模式，而后期层表现出高度冗余；2）双重注意力汇聚点现象，即注意力分数同时集中于输入序列的首尾标记。基于这些发现，我们提出了EARN，一种高效推理框架，利用早期层将信息压缩至置于输入序列边界的寄存器标记中，并在后续层中仅关注这些标记。在三个数据集、两种LLMRec方法和两种LLM架构上的大量实验表明，EARN具有优越性，实现了最高3.79倍的加速和80.8%的KV缓存缩减，同时精度优于通用微调方法。我们的工作弥合了LLMRec中效率与效果之间的差距，为工业场景提供了实用的部署优势。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Model-based generative recommendation (LLMRec) has achieved notable success, but it suffers from high inference latency due to massive computational overhead and memory pressure of KV Cache. Existing KV Cache reduction methods face critical limitations: cache compression offers marginal acceleration given recommendation tasks' short decoding steps, while prompt compression risks discarding vital interaction history. Through systematic analysis of attention patterns in LLMRec, we uncover two pivotal insights: 1) layer-wise attention sparsity inversion where early layers retain dense informative patterns while later layers exhibit high redundancy, and 2) dual attention sinks phenomenon where attention scores concentrate on both head and tail tokens of input sequences. Motivated by these insights, we propose EARN, an efficient inference framework that leverages the early layers to compress information into register tokens placed at the input sequence boundaries, then focuses solely on these tokens in the subsequent layers. Extensive experiments on three datasets, two LLMRec methods and two LLM architectures demonstrate EARN's superiority, achieving up to 3.79x speedup and 80.8% KV Cache reduction with better accuracy than the general finetuning approach. Our work bridges the efficiency-effectiveness gap in LLMRec, offering practical deployment advantages for industrial scenarios.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

基于大语言模型的生成式推荐（LLMRec）虽取得显著成功，但存在高推理延迟问题，源于大量计算开销和KV缓存的内存压力。现有KV缓存缩减方法面临关键限制：缓存压缩因推荐任务解码步骤短而加速效果有限，提示压缩则可能丢失重要的交互历史。通过对LLMRec中注意力模式的系统分析，作者发现两个关键洞察：1）逐层注意力稀疏性反转，即早期层保留密集信息模式，而后期层高度冗余；2）双重注意力汇聚现象，即注意力分数集中在输入序列的首尾令牌上。基于这些洞察，提出EARN高效推理框架，利用早期层将信息压缩到置于输入序列边界的寄存器令牌中，后续层仅关注这些令牌。在三个数据集、两种LLMRec方法和两种LLM架构上的大量实验表明，EARN实现了高达3.79倍加速和80.8%的KV缓存缩减，且准确率优于通用微调方法。该工作弥合了LLMRec中的效率与效果差距，为工业场景提供了实际部署优势。

### 主要创新

- 发现LLMRec中逐层注意力稀疏性反转现象，即早期层密集、后期层冗余。
- 发现双重注意力汇聚现象，注意力集中在输入序列首尾令牌。
- 提出EARN框架，利用早期层将信息压缩到寄存器令牌，后续层仅处理这些令牌。
- 在多个数据集和模型上实现显著加速和KV缓存缩减，同时保持或提升准确率。

### 研究方法

论文通过系统分析LLMRec中的注意力模式，提出两个关键洞察，并据此设计EARN框架。该框架在输入序列边界放置寄存器令牌，利用早期层压缩信息，后续层仅关注这些令牌，从而减少计算和KV缓存。实验在三个数据集、两种LLMRec方法和两种LLM架构上进行，对比通用微调方法。

### 关键结果

EARN实现了高达3.79倍加速和80.8%的KV缓存缩减，同时准确率优于通用微调方法。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 提出新颖的注意力模式洞察，为高效推理提供理论基础。
- 方法在多个数据集和模型上验证，具有泛化性。
- 显著提升推理速度并减少内存占用，有利于工业部署。
- 在加速的同时保持或提升准确率，实现效率与效果的双赢。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法的细节、潜在缺陷或适用范围。

### 与当前研究方向的关联

该论文与推荐系统、生成式推荐、LLM与推荐结合、效率优化等关键词高度相关，属于LLMRec领域的前沿研究，关注推理效率与部署可行性。

---

_知识库更新时间：2026-08-16T02:20:30.031362_
