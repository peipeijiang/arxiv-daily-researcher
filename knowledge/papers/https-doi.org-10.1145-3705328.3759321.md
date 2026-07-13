---
title: "The Hidden Cost of Defaults in Recommender System Evaluation"
paper_id: "https://doi.org/10.1145/3705328.3759321"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 20.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Image Retrieval and Classification Techniques"]
---

# The Hidden Cost of Defaults in Recommender System Evaluation

[查看原文](https://dblp.org/rec/conf/recsys/BerlingSS25) · [ArXiv](https://arxiv.org/abs/2508.21180) · [Semantic Scholar](https://www.semanticscholar.org/paper/899d493542175efc29f4362850001d279474f03b)

## 一句话结论

> 论文揭示了推荐系统框架RecBole中隐藏的默认提前停止策略会显著影响超参数优化结果，导致性能差异与搜索策略间的差异相当，强调了框架透明性和可复现性的重要性。

## 论文信息

- **作者**：Hannah Berling, Robin Svahn, Alan Said
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：20.0
- **DOI**：[https://doi.org/10.1145/3705328.3759321](https://doi.org/10.1145/3705328.3759321)

<details open>
<summary><strong>中文摘要</strong></summary>

超参数优化对于提升推荐系统性能至关重要，但其实现常被视为中性或次要问题。本研究将关注点从模型基准测试转向对广泛使用的推荐框架RecBole的行为审计。我们证明，RecBole的内部默认设置（尤其是未文档化的早停策略）会提前终止随机搜索与贝叶斯优化，从而以用户不可见的方式限制搜索覆盖范围。通过使用六个模型和两个数据集，我们比较了不同搜索策略，并量化了性能方差与搜索路径不稳定性。研究结果表明，隐藏的框架逻辑可能引入与搜索策略间差异相当的变异性。这些结果凸显了将框架视为实验设计主动组成部分的重要性，并呼吁推荐系统研究领域采用更透明、更注重可复现性的工具。我们为研究人员和开发者提供了可操作的建议，以减轻隐藏配置行为的影响，并提升超参数调优工作流的透明度。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Hyperparameter optimization is critical for improving the performance of recommender systems, yet its implementation is often treated as a neutral or secondary concern. In this work, we shift focus from model benchmarking to auditing the behavior of RecBole, a widely used recommendation framework. We show that RecBole's internal defaults, particularly an undocumented early-stopping policy, can prematurely terminate Random Search and Bayesian Optimization. This limits search coverage in ways that are not visible to users. Using six models and two datasets, we compare search strategies and quantify both performance variance and search path instability. Our findings reveal that hidden framework logic can introduce variability comparable to the differences between search strategies. These results highlight the importance of treating frameworks as active components of experimental design and call for more transparent, reproducibility-aware tooling in recommender systems research. We provide actionable recommendations for researchers and developers to mitigate hidden configuration behaviors and improve the transparency of hyperparameter tuning workflows.

</details>

---

_知识库更新时间：2026-07-13T06:43:12.873796_
