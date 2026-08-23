---
title: "未来是稀疏的：面向可扩展检索的推荐系统嵌入压缩"
paper_id: "https://doi.org/10.1145/3705328.3748147"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 68.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Advanced Image and Video Retrieval Techniques"]
---

# 未来是稀疏的：面向可扩展检索的推荐系统嵌入压缩

> **英文原标题**：The Future is Sparse: Embedding Compression for Scalable Retrieval in Recommender Systems

[查看原文](https://dblp.org/rec/conf/recsys/KasalickySVBAK25)

## 一句话结论

> 该论文提出了一种嵌入压缩方法，在保持推荐性能的同时大幅减少内存占用，实现了可扩展的推荐检索。

## 论文信息

- **作者**：Petr Kasalický, Martin Spišák, Vojtěch Vančura, Daniel Bohuněk, Rodrigo Alves, Pavel Kordík
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：68.0
- **DOI**：[https://doi.org/10.1145/3705328.3748147](https://doi.org/10.1145/3705328.3748147)

<details open>
<summary><strong>中文摘要</strong></summary>

模型嵌入 每1亿次点击的CTR大小（压缩） 维度 提升 嵌入模型 SBERT [18] 512（基线） 204.8 GB Nomic [14] 768 +4.86% 307.2 GB Nomic（Matryoshka） 64 +1.89% 25.6 GB Nomic（CompresSAE） 4096* +3.44% 25.6 GB *稀疏嵌入，具有32个非零条目。图1：用于候选检索的嵌入模型比较。我们报告了在下游任务上的在线推荐性能，相对于SBERT [18]，并给出了任意有效的99%置信区间。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Model Embedding CTR Size per 100M (Compression) Dimension Lift Embeddings SBERT [18] 512 (baseline) 204.8 GB Nomic [14] 768 +4.86% 307.2 GB Nomic (Matryoshka) 64 +1.89% 25.6 GB Nomic (CompresSAE) 4096* +3.44% 25.6 GB *Sparse embeddings with 32 nonzero entries.Figure 1: Comparison of embedding models used for candidate retrieval.We report online recommendation performance on a downstream task, relative to SBERT [18], with anytime-valid 99% confidence intervals.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出了一种名为CompresSAE的稀疏自编码器，用于压缩推荐系统中的稠密嵌入向量，以解决嵌入表随维度和基数增长导致的内存和计算开销问题。CompresSAE将稠密嵌入映射为高维稀疏向量，仅保留k个非零元素，并通过线性无偏解码器重建原始向量，使用余弦相似度作为训练目标。该方法在离线实验中表现出快速收敛和良好的压缩-精度平衡，在在线A/B测试中，CompresSAE在12倍压缩下仅损失1.35%的点击率，并优于同等大小的Matryoshka模型。此外，论文还探讨了从稀疏空间直接检索和从重建空间检索两种策略，后者利用核技巧在保持精度的同时提高效率。

### 主要创新

- 提出CompresSAE，一种用于嵌入压缩的稀疏自编码器，将稠密向量映射为高维稀疏向量。
- 使用TopK激活函数同时实现稀疏化和非线性，替代常用的ReLU。
- 解码器采用线性无偏设计，支持核技巧，实现从重建空间的高效检索。
- 在在线A/B测试中验证了CompresSAE在12倍压缩下仅损失1.35% CTR，并优于同等大小的Matryoshka模型。

### 研究方法

CompresSAE由编码器和解码器组成。编码器将归一化的稠密嵌入通过线性变换和TopK激活函数映射为k稀疏向量；解码器为线性无偏层，将稀疏向量重建为原始维度。训练使用余弦重建损失，在预计算嵌入上优化，无需原始数据。检索时可采用直接稀疏检索或通过核技巧从重建空间检索。

### 关键结果

CompresSAE在离线实验中快速收敛，约15秒内超越Matryoshka。；在压缩-精度权衡上表现更优，尤其在高压缩率下。；在线A/B测试中，CompresSAE达到12倍压缩，CTR仅下降1.35%。；CompresSAE相比同等大小的Matryoshka模型CTR提升1.52%，且统计显著。

### 技术栈

- 稀疏自编码器（SAE）
- TopK激活函数
- 余弦相似度损失
- 核技巧
- CSR格式稀疏矩阵
- NVIDIA H100 SXM 80GB GPU

### 方法优势

- 提出了一种新颖的嵌入压缩方法，有效解决内存和计算瓶颈。
- 方法简单高效，训练速度快（约100秒）。
- 提供了两种检索策略，兼顾精度和速度。
- 在线实验验证了实际效果，具有工业应用价值。

### 主要局限

- 输入内容未提供关于方法局限性的明确讨论。
- 输入内容未提供与其他压缩方法的详细对比。
- 输入内容未提供在不同数据集上的泛化性分析。

### 与当前研究方向的关联

推荐系统：论文聚焦于推荐系统中的嵌入压缩，直接相关。；嵌入压缩：核心主题。；稀疏表示：方法基于稀疏自编码器。；可扩展检索：目标是为大规模检索提供高效方案。；工业落地：在线A/B测试验证了实际应用。

## 代码与复现

- [recombee/CompresSAE](https://github.com/recombee/CompresSAE)：likely，置信度 69，Stars 39
- [alopatenko/LLMSearchRecommender](https://github.com/alopatenko/LLMSearchRecommender)：possible，置信度 30，Stars 104

---

_知识库更新时间：2026-08-23T02:16:26.101288_
