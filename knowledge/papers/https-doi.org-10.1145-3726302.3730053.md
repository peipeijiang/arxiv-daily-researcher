---
title: "面向基于大语言模型的生成式推荐的顺序无关标识符"
paper_id: "https://doi.org/10.1145/3726302.3730053"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 63.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Recommender Systems and Techniques", "Natural Language Processing Techniques"]
---

# 面向基于大语言模型的生成式推荐的顺序无关标识符

> **英文原标题**：Order-agnostic Identifier for Large Language Model-based Generative Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/0001S0FWNC25) · [ArXiv](https://arxiv.org/abs/2502.10833) · [Semantic Scholar](https://www.semanticscholar.org/paper/d1ff26014e3d2db06119a0acbc6012087da919ba)

## 一句话结论

> 论文提出了一种顺序无关的标识符方法，用于基于大语言模型的生成式推荐，以解决现有标识符在语义捕获和协同过滤信息编码上的不足，从而提升推荐性能。

## 论文信息

- **作者**：Xinyu Lin, H. C. Shi, Wenjie Wang, Fuli Feng, Qifan Wang, See-Kiong Ng, Tat‐Seng Chua
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：63.0
- **DOI**：[https://doi.org/10.1145/3726302.3730053](https://doi.org/10.1145/3726302.3730053)

<details open>
<summary><strong>中文摘要</strong></summary>

利用大型语言模型（LLMs）进行生成式推荐已引起广泛研究关注，其中项目分词（item tokenization）是关键步骤。该步骤涉及为LLMs分配项目标识符，以编码用户历史并生成下一个项目。现有方法要么采用分词序列标识符，将项目表示为离散的分词序列，要么采用单分词标识符，使用ID或语义嵌入。分词序列标识符面临波束搜索中的局部最优问题以及逐步生成导致的生成效率低下等挑战。相比之下，单分词标识符无法捕获丰富的语义或编码协同过滤（CF）信息，从而导致性能次优。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Leveraging Large Language Models (LLMs) for generative recommendation has attracted significant research interest, where item tokenization is a critical step. It involves assigning item identifiers for LLMs to encode user history and generate the next item. Existing approaches leverage either token-sequence identifiers, representing items as discrete token sequences, or single-token identifiers, using ID or semantic embeddings. Token-sequence identifiers face issues such as the local optima problem in beam search and low generation efficiency due to step-by-step generation. In contrast, single-token identifiers fail to capture rich semantics or encode Collaborative Filtering (CF) information, resulting in suboptimal performance.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

利用大语言模型进行生成式推荐已成为研究热点，其中物品标记化是关键步骤，即为物品分配标识符以供LLM编码用户历史并生成下一项。现有方法要么采用令牌序列标识符（将物品表示为离散令牌序列），要么采用单令牌标识符（使用ID或语义嵌入）。令牌序列标识符存在波束搜索中的局部最优问题和逐步生成导致的低生成效率；而单令牌标识符无法捕获丰富语义或编码协同过滤信息，导致性能次优。本文提出一种顺序无关的标识符方法，旨在结合两者优势，同时避免其缺陷，从而提升生成式推荐的性能。

### 主要创新

- 提出顺序无关的标识符设计，避免令牌序列标识符的逐步生成问题
- 能够同时捕获物品的语义信息和协同过滤信息
- 提高生成效率，避免波束搜索中的局部最优问题
- 为LLM生成式推荐提供更有效的物品表示方法

### 研究方法

论文提出一种顺序无关的标识符方法，具体技术路线在摘要中未详细披露，但核心思想是设计一种标识符，使得物品表示不依赖于令牌顺序，从而可以并行生成或直接预测，同时融合语义和协同过滤信息。

### 关键结果

摘要未提供具体实验结果，但指出现有方法存在缺陷，所提方法旨在解决这些问题，预期能提升生成式推荐的性能。

### 技术栈

- 摘要未提供具体算法、工具或数学方法，但涉及大语言模型、生成式推荐、物品标记化、令牌序列标识符、单令牌标识符、协同过滤、语义嵌入等概念。

### 方法优势

- 针对现有方法的痛点提出解决方案，具有明确的问题导向
- 设计思路新颖，结合了两种标识符的优势
- 关注生成效率和推荐性能，具有实际应用价值

### 主要局限

- 论文局限：摘要未提供实验验证和具体性能数据，无法评估实际效果。当前证据局限：仅基于摘要，缺乏方法细节和实验结果，无法全面评估。

### 与当前研究方向的关联

该论文与关键词“生成式推荐”、“大语言模型”、“物品标记化”、“协同过滤”、“语义信息”高度相关，属于LLM与推荐系统结合的前沿研究。

## 代码与复现

- [Linxyhaha/SETRec](https://github.com/Linxyhaha/SETRec)：likely，置信度 69，Stars 33

---

_知识库更新时间：2026-08-25T02:16:23.900359_
