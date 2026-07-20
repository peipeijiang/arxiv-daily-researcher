---
title: "Social Relation Meets Recommendation: Augmentation and Alignment"
paper_id: "https://doi.org/10.1145/3746252.3760873"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 28.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Sentiment Analysis and Opinion Mining"]
---

# Social Relation Meets Recommendation: Augmentation and Alignment

[查看原文](https://dblp.org/rec/conf/cikm/0040WXL25) · [ArXiv](https://arxiv.org/abs/2502.15695) · [Semantic Scholar](https://www.semanticscholar.org/paper/9e44a1d28ac6c90fe09f9b161044eded2ec292f1)

## 一句话结论

> 该论文提出利用社交关系图增强行为推荐模型，通过双视图去噪和互蒸馏技术解决噪声和兴趣不一致问题，有效提升冷用户推荐效果。

## 论文信息

- **作者**：Lin Wang, Weisong Wang, Xuanji Xiao, Qing Li
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：28.0
- **DOI**：[https://doi.org/10.1145/3746252.3760873](https://doi.org/10.1145/3746252.3760873)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统对于现代内容平台至关重要，然而传统的基于行为的模型在处理交互数据有限的冷启动用户时往往面临困难。吸引这些用户对于平台增长至关重要。为弥补这一不足，我们提出利用社交关系图来丰富基于行为模型的兴趣表示。然而，由于关系噪声和跨领域不一致性，从社交图中提取价值颇具挑战。为解决噪声传播问题并获取准确的社交兴趣，我们采用了一种双视角去噪策略：对用户-物品交互矩阵应用低秩奇异值分解（SVD）以生成去噪后的社交图，并通过对比学习对齐原始社交图与重构社交图。针对社交兴趣与行为兴趣之间的不一致性，我们采用“相互蒸馏”技术，将原始兴趣分离为对齐的社交/行为兴趣以及社交/行为特有兴趣，从而最大化两者的效用。在广泛采用的工业数据集上的实验结果验证了该方法的有效性，尤其对于冷启动用户，为未来研究提供了全新视角。相关实现代码可访问 https://github.com/WANGLin0126/CLSRec。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recommender systems are essential for modern content platforms, yet traditional behavior-based models often struggle with cold users who have limited interaction data. Engaging these users is crucial for platform growth. To bridge this gap, we propose leveraging the social-relation graph to enrich interest representations from behavior-based models. However, extracting value from social graphs is challenging due to relation noise and cross-domain inconsistency. To address the noise propagation and obtain accurate social interest, we employ a dual-view denoising strategy, employing low-rank SVD to the user-item interaction matrix for a denoised social graph and contrastive learning to align the original and reconstructed social graphs. Addressing the interest inconsistency between social and behavioral interests, we adopt a ''mutual distillation'' technique to isolate the original interests into aligned social/behavior interests and social/behavior specific interests, maximizing the utility of both. Experimental results on widely adopted industry datasets verify the method's effectiveness, particularly for cold users, offering a fresh perspective for future research. The implementation can be accessed at https://github.com/WANGLin0126/CLSRec.

</details>

---

_知识库更新时间：2026-07-20T04:18:26.518851_
