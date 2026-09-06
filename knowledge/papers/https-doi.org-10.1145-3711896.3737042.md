---
title: "MDVT: Enhancing Multimodal Recommendation with Model-Agnostic Multimodal-Driven Virtual Triplets"
paper_id: "https://doi.org/10.1145/3711896.3737042"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Speech and dialogue systems"]
---

# MDVT: Enhancing Multimodal Recommendation with Model-Agnostic Multimodal-Driven Virtual Triplets

[查看原文](https://dblp.org/rec/conf/kdd/0003000000WN25) · [ArXiv](https://arxiv.org/abs/2505.16665) · [Semantic Scholar](https://www.semanticscholar.org/paper/9bd3e61e17ffcbb51cfdbcfc2a28f897b1775689)

## 一句话结论

> 该论文提出一种模型无关的多模态驱动虚拟三元组方法MDVT，通过动态和静态结合的热身阈值策略生成高质量虚拟三元组，有效缓解多模态推荐中的数据稀疏问题，提升推荐性能。

## 论文信息

- **作者**：Jinfeng Xu, Zheyu Chen, Jinze Li, Shuo Yang, Hewei Wang, Yijie Li, Mengran Li, Puzhen Wu, Edith C.‐H. Ngai
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3711896.3737042](https://doi.org/10.1145/3711896.3737042)

<details open>
<summary><strong>中文摘要</strong></summary>

数据稀疏问题严重制约了推荐系统的性能，因为传统模型依赖有限的历史交互来学习用户偏好和物品属性。尽管引入多模态信息能够显式地表示这些偏好和属性，但现有工作往往仅将其作为辅助信息使用，未能充分发挥其潜力。在本文中，我们提出MDVT，一种模型无关的方法，通过构建多模态驱动的虚拟三元组来提供有价值的监督信号，从而有效缓解多模态推荐系统中的数据稀疏问题。为确保虚拟三元组的高质量，我们引入了三种定制化的预热阈值策略：静态、动态和混合策略。静态预热阈值策略通过穷举搜索最优预热轮数，但耗时且计算开销大。动态预热阈值策略根据损失趋势调整预热周期，提高了效率，但可能无法达到最优性能。混合策略结合了两者，先使用动态策略近似确定最优预热轮数，再在较窄的超参数空间中通过静态策略进行细化。一旦满足预热阈值，虚拟三元组便通过我们增强的成对损失函数用于联合模型优化，而不会引起显著的梯度偏斜。在多个真实世界数据集上的大量实验表明，将MDVT集成到先进的多模态推荐模型中，能够有效缓解数据稀疏问题并提升推荐性能，尤其在稀疏数据场景下效果显著。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

The data sparsity problem significantly hinders the performance of recommender systems, as traditional models rely on limited historical interactions to learn user preferences and item properties. While incorporating multimodal information can explicitly represent these preferences and properties, existing works often use it only as side information, failing to fully leverage its potential. In this paper, we propose MDVT, a model-agnostic approach that constructs multimodal-driven virtual triplets to provide valuable supervision signals, effectively mitigating the data sparsity problem in multimodal recommendation systems. To ensure high-quality virtual triplets, we introduce three tailored warm-up threshold strategies: static, dynamic, and hybrid. The static warm-up threshold strategy exhaustively searches for the optimal number of warm-up epochs but is time-consuming and computationally intensive. The dynamic warm-up threshold strategy adjusts the warm-up period based on loss trends, improving efficiency but potentially missing optimal performance. The hybrid strategy combines both, using the dynamic strategy to find the approximate optimal number of warm-up epochs and then refining it with the static strategy in a narrow hyper-parameter space. Once the warm-up threshold is satisfied, the virtual triplets are used for joint model optimization by our enhanced pair-wise loss function without causing significant gradient skew. Extensive experiments on multiple real-world datasets demonstrate that integrating MDVT into advanced multimodal recommendation models effectively alleviates the data sparsity problem and improves recommendation performance, particularly in sparse data scenarios.

</details>

---

_知识库更新时间：2026-09-06T04:59:26.701820_
