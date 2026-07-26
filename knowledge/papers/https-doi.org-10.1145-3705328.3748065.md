---
title: "LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders"
paper_id: "https://doi.org/10.1145/3705328.3748065"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Topic Modeling"]
---

# LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders

[查看原文](https://dblp.org/rec/conf/recsys/ChaiRXYHZCLZYXR25) · [ArXiv](https://arxiv.org/abs/2505.04421) · [Semantic Scholar](https://www.semanticscholar.org/paper/6620f99ca8e6c4ef088f31f28ae3c74503c492ba)

## 一句话结论

> 评分失败，无法生成摘要

## 论文信息

- **作者**：Zheng Chai, Qin Ren, Xijun Xiao, Huizhi Yang, Bo Han, Sijun Zhang, Di Chen, Hui Lu, Wenlin Zhao, Lele Yu, Xionghang Xie, Shiru Ren, Xiang Sun, Y. X. Tan, Peng Xu, Yuchao Zheng, Di Wu
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3705328.3748065](https://doi.org/10.1145/3705328.3748065)

<details>
<summary><strong>英文摘要</strong></summary>

Modeling ultra-long user behavior sequences is critical for capturing both long- and short-term preferences in industrial recommender systems. Existing solutions typically rely on two-stage or indirect modeling paradigms, incurring upstream-downstream inconsistency and computational inefficiency. In this paper, we present LONGER, a Long-sequence Optimized traNsformer for GPU-Efficient Recommenders. LONGER incorporates (i) a global token mechanism for stabilizing attention over long contexts, (ii) a token merge module with lightweight InnerTransformers and hybrid attention strategy to reduce quadratic complexity, and (iii) a series of engineering optimizations, including training with mixed-precision and activation recomputation, KV cache serving, and the fully synchronous model training and serving framework for unified GPU-based dense and sparse parameter updates. LONGER consistently outperforms strong baselines in both offline metrics and online A/B testing in both advertising and e-commerce services at ByteDance, validating its consistent effectiveness and industrial-level scaling laws. Currently, LONGER has been validated and fully deployed across dozens of real-world influential scenarios at ByteDance, serving billions of users.

</details>

---

_知识库更新时间：2026-07-26T04:14:36.136385_
