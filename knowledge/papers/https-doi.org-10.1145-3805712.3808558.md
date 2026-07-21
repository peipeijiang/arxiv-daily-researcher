---
title: "Where Relevance Emerges: A Layer-Wise Study of Internal Attention for Zero-Shot Re-Ranking"
paper_id: "https://doi.org/10.1145/3805712.3808558"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 10.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Sentiment Analysis and Opinion Mining", "Text and Document Classification Technologies"]
---

# Where Relevance Emerges: A Layer-Wise Study of Internal Attention for Zero-Shot Re-Ranking

[查看原文](https://dblp.org/rec/conf/sigir/ChenZYZL26) · [ArXiv](https://arxiv.org/abs/2602.22591) · [Semantic Scholar](https://www.semanticscholar.org/paper/f860c64a7a9a614e47a8af4e67299cbed500fac3)

## 一句话结论

> 论文通过分层研究大语言模型的内部注意力机制，提出了一种无需生成文本的零样本重排序方法，并分析了不同层注意力信号的一致性和有效性。

## 论文信息

- **作者**：Haodong Chen, Shengyao Zhuang, Zheng Yao, Guido Zuccon, Teerapong Leelanupab
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：10.0
- **DOI**：[https://doi.org/10.1145/3805712.3808558](https://doi.org/10.1145/3805712.3808558)

<details open>
<summary><strong>中文摘要</strong></summary>

基于大语言模型（LLMs）的零样本文档重排序已从逐点方法（Pointwise）发展为列表式（Listwise）和集合式（Setwise）方法，以优化计算效率。尽管这些方法取得了成功，但它们主要依赖生成式评分或输出对数几率（logits），在推理延迟和结果一致性方面面临瓶颈。上下文重排序（In-Context Re-ranking, ICR）最近被提出作为一种O(1)的替代方法。ICR直接提取内部注意力信号，避免了文本生成的开销。然而，现有ICR方法仅简单聚合所有层的信号；各层贡献及其在不同架构间的一致性尚未被探索。此外，目前尚无统一研究在一致条件下，将内部注意力与传统生成式及基于似然（likelihood）的机制在不同排序框架中进行比较。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Zero-shot document re-ranking with Large Language Models (LLMs) has evolved from Pointwise methods to Listwise and Setwise approaches that optimize computational efficiency. Despite their success, these methods predominantly rely on generative scoring or output logits, which face bottlenecks in inference latency and result consistency. In-Context Re-ranking (ICR) has recently been proposed as an O(1) alternative method. ICR extracts internal attention signals directly, avoiding the overhead of text generation. However, existing ICR methods simply aggregate signals across all layers; layer-wise contributions and their consistency across architectures have been left unexplored. Furthermore, no unified study has compared internal attention with traditional generative and likelihood-based mechanisms across diverse ranking frameworks under consistent conditions.

</details>

---

_知识库更新时间：2026-07-21T04:03:10.445973_
