---
title: "RMBRec: Robust Multi-Behavior Recommendation towards Target Behaviors"
paper_id: "https://doi.org/10.1145/3774904.3792617"
source: "www"
published: "2026-01-01T00:00:00"
score: 25.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Mobile Crowdsensing and Crowdsourcing"]
---

# RMBRec: Robust Multi-Behavior Recommendation towards Target Behaviors

[查看原文](https://dblp.org/rec/conf/www/CaiZFCWW26) · [ArXiv](https://arxiv.org/abs/2601.08705) · [Semantic Scholar](https://www.semanticscholar.org/paper/0f75c20c26e8608ccb327cf65a4bc5755b8ae05c)

## 一句话结论

> The paper proposes RMBRec, a robust multi-behavior recommendation framework that enhances robustness against noisy auxiliary behaviors by maximizing mutual information between representations and minimizing predictive risk variance, achieving superior accuracy and stability.

## 论文信息

- **作者**：Miaomiao Cai, Zhijie Zhang, Junfeng Fang, Huilin Chen, Xiang Wang, Meng Wang
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：25.0
- **DOI**：[https://doi.org/10.1145/3774904.3792617](https://doi.org/10.1145/3774904.3792617)

<details open>
<summary><strong>中文摘要</strong></summary>

多行为推荐在实践中面临一个关键挑战：辅助行为（如点击、加入购物车）往往带有噪声、与目标行为（如购买）相关性较弱或语义上不一致，从而导致偏好学习产生偏差并降低推荐性能。尽管现有方法尝试融合这些异构信号，但它们本质上缺乏一种原则性机制来确保对此类行为不一致性的鲁棒性。在本工作中，我们提出面向目标行为的鲁棒多行为推荐（RMBRec），这是一种基于信息论鲁棒性原则的鲁棒多行为推荐框架。我们将鲁棒性解释为一个联合过程，即在最大化预测信息的同时，最小化其在异构行为环境中的方差。在此视角下，表示鲁棒模块（RRM）通过最大化用户辅助表示与目标表示之间的互信息来增强局部语义一致性，而优化鲁棒模块（ORM）则通过最小化各行为间预测风险的方差来实现全局稳定性，这是对不变风险最小化的一种高效近似。这种局部-全局协作在理论上以一致的方式将表示净化与优化不变性联系起来。在三个真实数据集上的大量实验表明，RMBRec不仅在准确性上优于最先进的方法，而且在各种噪声扰动下仍保持显著的稳定性。为便于复现，我们的代码可在 https://github.com/miaomiao-cai2/RMBRec/ 获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multi-behavior recommendation faces a critical challenge in practice: auxiliary behaviors (e.g., clicks, carts) are often noisy, weakly correlated, or semantically misaligned with the target behavior (e.g., purchase), which leads to biased preference learning and suboptimal performance. While existing methods attempt to fuse these heterogeneous signals, they inherently lack a principled mechanism to ensure robustness against such behavioral inconsistency. In this work, we propose Robust Multi-Behavior Recommendation towards Target Behaviors (RMBRec), a robust multi-behavior recommendation framework grounded in an information-theoretic robustness principle. We interpret robustness as a joint process of maximizing predictive information while minimizing its variance across heterogeneous behavioral environments. Under this perspective, the Representation Robustness Module (RRM) enhances local semantic consistency by maximizing the mutual information between users' auxiliary and target representations, whereas the Optimization Robustness Module (ORM) enforces global stability by minimizing the variance of predictive risks across behaviors, which is an efficient approximation to invariant risk minimization. This local-global collaboration bridges representation purification and optimization invariance in a theoretically coherent way. Extensive experiments on three real-world datasets demonstrate that RMBRec not only outperforms state-of-the-art methods in accuracy but also maintains remarkable stability under various noise perturbations. For reproducibility, our code is available at https://github.com/miaomiao-cai2/RMBRec/.

</details>

---

_知识库更新时间：2026-08-01T04:05:05.967149_
