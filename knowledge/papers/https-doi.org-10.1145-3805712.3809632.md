---
title: "Bi-Level Optimization for Generative Recommendation: Bridging Tokenization and Generation"
paper_id: "https://doi.org/10.1145/3805712.3809632"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Generative Adversarial Networks and Image Synthesis", "Advanced Technologies in Various Fields"]
---

# Bi-Level Optimization for Generative Recommendation: Bridging Tokenization and Generation

[查看原文](https://dblp.org/rec/conf/sigir/BaiLZWYRRF26) · [ArXiv](https://arxiv.org/abs/2510.21242)

## 一句话结论

> 针对生成式推荐中tokenizer与推荐模型分离导致次优标识符的问题，提出双层次优化框架BLOGER，通过元学习联合优化两者，在多个数据集上超越现有方法。

## 论文信息

- **作者**：Yimeng Bai, Chang Liu, Yang Zhang, Dingxian Wang, Frank Yang, Andrew Rabinovich, Wenge Rong, Fuli Feng
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3805712.3809632](https://doi.org/10.1145/3805712.3809632)

<details open>
<summary><strong>中文摘要</strong></summary>

生成式推荐正作为一种变革性范式兴起，它直接生成推荐项目，而非依赖匹配。构建此类系统通常涉及两个关键组成部分：（1）优化分词器以获取合适的项目标识符，以及（2）基于这些标识符训练推荐器。现有方法往往将这两个组成部分分开处理——要么顺序执行，要么交替进行——从而忽视了它们之间的相互依赖关系。这种分离可能导致不匹配：分词器在没有推荐目标直接指导的情况下进行训练，可能产生次优的标识符，进而降低推荐性能。为解决此问题，我们提出BLOGER——一种面向生成式推荐的双层优化框架，该框架在统一的优化过程中显式建模分词器与推荐器之间的相互依赖关系。下层使用分词后的序列训练推荐器，而上层则基于分词损失和推荐损失共同优化分词器。我们采用元学习方法高效求解该双层优化问题，并引入梯度修正技术以缓解上层更新中的梯度冲突，从而确保项目标识符既信息丰富又与推荐目标对齐。在多个真实世界数据集上的大量实验表明，BLOGER在持续优于最先进的生成式推荐方法的同时，保持了实际效率且未引入显著额外计算开销，有效弥合了项目分词与自回归生成之间的鸿沟。我们已在https://github.com/Ten-Mao/BLOGER 公开代码。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Generative recommendation is emerging as a transformative paradigm by directly generating recommended items, rather than relying on matching. Building such a system typically involves two key components: (1) optimizing the tokenizer to derive suitable item identifiers, and (2) training the recommender based on those identifiers. Existing approaches often treat these components separately--either sequentially or in alternation--overlooking their interdependence. This separation can lead to misalignment: the tokenizer is trained without direct guidance from the recommendation objective, potentially yielding suboptimal identifiers that degrade recommendation performance. To address this, we propose BLOGER, a Bi-Level Optimization for GEnerative Recommendation framework, which explicitly models the interdependence between the tokenizer and the recommender in a unified optimization process. The lower level trains the recommender using tokenized sequences, while the upper level optimizes the tokenizer based on both the tokenization loss and recommendation loss. We adopt a meta-learning approach to solve this bi-level optimization efficiently, and introduce gradient surgery to mitigate gradient conflicts in the upper-level updates, thereby ensuring that item identifiers are both informative and recommendation-aligned. Extensive experiments on multiple real-world datasets demonstrate that BLOGER consistently outperforms state-of-the-art generative recommendation methods while maintaining practical efficiency with no significant additional computational overhead, effectively bridging the gap between item tokenization and autoregressive generation. We release our code at https://github.com/Ten-Mao/BLOGER.

</details>

---

_知识库更新时间：2026-07-14T04:41:25.082230_
