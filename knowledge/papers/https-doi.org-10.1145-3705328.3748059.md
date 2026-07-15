---
title: "NLGCL: Naturally Existing Neighbor Layers Graph Contrastive Learning for Recommendation"
paper_id: "https://doi.org/10.1145/3705328.3748059"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 25.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Topic Modeling"]
---

# NLGCL: Naturally Existing Neighbor Layers Graph Contrastive Learning for Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/000300000HN25) · [ArXiv](https://arxiv.org/abs/2507.07522) · [Semantic Scholar](https://www.semanticscholar.org/paper/3220304f179720f1ecdd67223f9fa457efc83874)

## 一句话结论

> 该论文提出NLGCL框架，利用图神经网络中相邻层的自然对比视图进行对比学习，避免了传统数据增强带来的噪声和计算开销，在多个数据集上提升了推荐效果和效率。

## 论文信息

- **作者**：Jinfeng Xu, Zheyu Chen, Shuo Yang, Jinze Li, Hewei Wang, Wei Wang, Xiping Hu, Edith C.‐H. Ngai
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：25.0
- **DOI**：[https://doi.org/10.1145/3705328.3748059](https://doi.org/10.1145/3705328.3748059)

<details open>
<summary><strong>中文摘要</strong></summary>

图神经网络（Graph Neural Networks, GNNs）被广泛用于协同过滤中以捕获高阶用户-物品关系。为解决推荐系统中的数据稀疏问题，图对比学习（Graph Contrastive Learning, GCL）作为一种有前景的范式应运而生，其通过最大化对比视图间的互信息来提升性能。然而，现有GCL方法依赖的数据增强技术会引入语义无关的噪声，并产生显著的计算与存储开销，从而限制了其有效性与效率。为克服这些挑战，我们提出NLGCL——一种新颖的对比学习框架，该框架利用GNN中相邻层之间的自然对比视图。通过将每个节点及其下一层邻居视为正样本对，而将其他节点视为负样本，NLGCL避免了基于增强的噪声，同时保留了语义相关性。该范式消除了昂贵的视图构建与存储需求，使其在真实场景中兼具计算高效性与实用性。在四个公开数据集上的大量实验表明，NLGCL在有效性与效率方面均优于当前最先进的基线方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Graph Neural Networks (GNNs) are widely used in collaborative filtering to capture high-order user-item relationships. To address the data sparsity problem in recommendation systems, Graph Contrastive Learning (GCL) has emerged as a promising paradigm that maximizes mutual information between contrastive views. However, existing GCL methods rely on augmentation techniques that introduce semantically irrelevant noise and incur significant computational and storage costs, limiting effectiveness and efficiency. To overcome these challenges, we propose NLGCL, a novel contrastive learning framework that leverages naturally contrastive views between neighbor layers within GNNs. By treating each node and its neighbors in the next layer as positive pairs, and other nodes as negatives, NLGCL avoids augmentation-based noise while preserving semantic relevance. This paradigm eliminates costly view construction and storage, making it computationally efficient and practical for real-world scenarios. Extensive experiments on four public datasets demonstrate that NLGCL outperforms state-of-the-art baselines in effectiveness and efficiency.

</details>

---

_知识库更新时间：2026-07-15T03:52:18.776863_
