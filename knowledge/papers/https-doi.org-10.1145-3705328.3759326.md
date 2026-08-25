---
title: "A Dual-Key Attention Framework for Sequential Recommendation with Side Information"
paper_id: "https://doi.org/10.1145/3705328.3759326"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Advanced Graph Neural Networks"]
---

# A Dual-Key Attention Framework for Sequential Recommendation with Side Information

[查看原文](https://dblp.org/rec/conf/recsys/KimKKSLC25) · [Semantic Scholar](https://www.semanticscholar.org/paper/df650c4a2e7cba0032464c88b2e096a2d8178600)

## 一句话结论

> 该论文提出了一种双键注意力框架（DK-SR），通过同时学习基于关系和基于属性的物品表示来提升序列推荐性能，并在四个真实数据集上验证了其优于现有方法。

## 论文信息

- **作者**：Minje Kim, Wooseung Kang, Gun-Woo Kim, Chie Hoon Song, Suwon Lee, Sang-Min Choi
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3705328.3759326](https://doi.org/10.1145/3705328.3759326)

<details open>
<summary><strong>中文摘要</strong></summary>

序列推荐（Sequential Recommendation, SR）旨在基于用户的历史行为预测其未来的交互。近年来，利用辅助信息的基于深度学习的序列推荐模型受到了广泛关注。在这些系统中，物品可以从基于关系和基于属性两个视角进行观察。基于关系的视角根据用户交互中隐含的关系和上下文依赖来刻画物品；而基于属性的视角则通过物品的固有属性（如类别或类型）来定义物品。然而，这两种视角天然相互纠缠，使得分别学习变得具有挑战性。为解决这一问题，我们提出了一种用于序列推荐的双键注意力框架（Dual-Key Attention Framework for Sequential Recommendation, DK-SR），该框架能够有效学习基于关系和基于属性两种表示。DK-SR采用具有双键的注意力机制：一个用于物品级注意力，促进基于关系的表示学习；另一个用于属性级注意力，增强基于属性的表示。在四个真实世界数据集上进行的大量实验表明，我们的模型优于六种利用辅助信息的最先进的序列推荐模型。此外，消融研究验证了双键机制的贡献。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation (SR) aims to predict users’ future interactions based on their historical behavior. Recently, deep learning-based SR models leveraging side information have gained considerable attention. Within these systems, items can be viewed from relation-based and attribute-based perspectives. The relation-based perspective characterizes items based on implicit relationships and contextual dependencies derived from user interactions. The attribute-based perspective defines items using inherent properties, such as category or genre. However, these perspectives are inherently entangled, making separate learning challenging. To address this issue, we propose a dual-key attention framework for sequential recommendation (DK-SR), which effectively learns both relation-based and attribute-based representations. DK-SR employs an attention mechanism with dual keys: one for item-level attention, facilitating relation-based representation learning, and another for attribute-level attention, enhancing attribute-based representation. Extensive experiments on four real-world datasets demonstrate that our model outperforms six state-of-the-art SR models leveraging side information. Additionally, an ablation study validates the contribution of the dual-key mechanism.

</details>

---

_知识库更新时间：2026-08-25T02:16:23.899887_
