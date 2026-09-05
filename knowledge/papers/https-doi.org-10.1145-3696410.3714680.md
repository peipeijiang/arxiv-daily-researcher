---
title: "Does Weighting Improve Matrix Factorization for Recommender Systems?"
paper_id: "https://doi.org/10.1145/3696410.3714680"
source: "www"
published: "2025-01-01T00:00:00"
score: 20.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Image Retrieval and Classification Techniques"]
---

# Does Weighting Improve Matrix Factorization for Recommender Systems?

[查看原文](https://dblp.org/rec/conf/www/AyoubRLSK25) · [ArXiv](https://arxiv.org/abs/2510.10440)

## 一句话结论

> 该论文系统研究了矩阵分解中加权方案对推荐性能的影响，发现未加权训练在大型模型上表现相当甚至更好，挑战了传统加权观点，并提出了高效优化加权目标的方法。

## 论文信息

- **作者**：Alex Ayoub, Sam Robertson, Dawen Liang, Harald Steck, Nathan Kallus
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：20.0
- **DOI**：[https://doi.org/10.1145/3696410.3714680](https://doi.org/10.1145/3696410.3714680)

<details open>
<summary><strong>中文摘要</strong></summary>

矩阵分解是用于top-N推荐和协同过滤的一种广泛采用的方法。当在隐式反馈数据（如点击）上实现时，一种常见的启发式方法是提高已观测交互的权重。这一策略已被证明能够提升某些算法的性能。在本文中，我们对各种加权方案和矩阵分解算法进行了系统性研究。有点出乎意料的是，我们发现使用未加权数据进行训练可以达到与加权数据训练相当的性能——有时甚至更优，尤其是对于大型模型而言。这一观察结果挑战了传统认知。尽管如此，我们识别出加权可能有益的情形，特别是对于容量较低的模型和特定的正则化方案。我们还推导出了用于精确最小化若干加权目标的高效算法，而这些目标此前被认为在计算上是难以处理的。我们的工作为推荐系统中矩阵分解的加权、正则化与模型容量之间的相互作用提供了全面的分析。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Matrix factorization is a widely used approach for top-N recommendation and collaborative filtering. When implemented on implicit feedback data (such as clicks), a common heuristic is to upweight the observed interactions. This strategy has been shown to improve performance for certain algorithms. In this paper, we conduct a systematic study of various weighting schemes and matrix factorization algorithms. Somewhat surprisingly, we find that training with unweighted data can perform comparably to-and sometimes outperform-training with weighted data, especially for large models. This observation challenges the conventional wisdom. Nevertheless, we identify cases where weighting can be beneficial, particularly for models with lower capacity and specific regularization schemes. We also derive efficient algorithms for exactly minimizing several weighted objectives that were previously considered computationally intractable. Our work provides a comprehensive analysis of the interplay between weighting, regularization, and model capacity in matrix factorization for recommender systems.

</details>

---

_知识库更新时间：2026-09-05T04:50:29.987758_
