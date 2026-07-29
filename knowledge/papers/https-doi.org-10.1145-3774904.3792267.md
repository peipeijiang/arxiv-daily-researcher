---
title: "KE-FedRS: Tackling Data Sparsity in Federated Recommendation via Knowledge Enhancement"
paper_id: "https://doi.org/10.1145/3774904.3792267"
source: "www"
published: "2026-01-01T00:00:00"
score: 28.0
tags: ["paper", "recommender-systems", "Privacy-Preserving Technologies in Data", "Recommender Systems and Techniques", "Data Quality and Management"]
---

# KE-FedRS: Tackling Data Sparsity in Federated Recommendation via Knowledge Enhancement

[查看原文](https://dblp.org/rec/conf/www/BaoSZZWL26)

## 一句话结论

> 针对联邦推荐系统中的数据稀疏性问题，提出知识增强方法KE-FedRS，通过本地辅助用户嵌入和全局混合客户端选择策略，在四个数据集上提升了推荐性能。

## 论文信息

- **作者**：Jiayu Bao, Hongjian Shi, Guanyu Zhang, Rui Zhou, Haozhao Wang, Yuan Liu
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：28.0
- **DOI**：[https://doi.org/10.1145/3774904.3792267](https://doi.org/10.1145/3774904.3792267)

<details open>
<summary><strong>中文摘要</strong></summary>

联邦推荐系统（Federated Recommendation Systems, FRSs）近年来因其无需交换原始用户数据即可训练协作推荐模型的能力而受到广泛关注。然而，现有的联邦推荐系统面临数据稀疏性的严峻挑战，这种稀疏性在用户层面和物品层面均有体现。首先，用户数据稀疏性：部分用户可能与物品的交互数量极少，难以在本地充分训练个性化的用户嵌入（user embedding）。其次，物品数据稀疏性：某些物品可能仅获得少量用户评分，导致全局模型缺乏对其的了解。针对这些问题，我们提出了一种名为KE-FedRS的知识增强联邦推荐系统（Knowledge Enhanced Federated Recommendation System），其核心思想是在本地和全局两个层面增强交互较少的用户以及评分较少的物品的知识。具体而言，在本地层面，我们引入了一个辅助用户嵌入（auxiliary user embedding），并在相似用户之间对该辅助嵌入进行平均和聚合，从而丰富本地用户嵌入的知识。在全局层面，我们提出了一种基于物品嵌入差异（item embedding discrepancies）的混合客户端选择策略，优先选择那些物品嵌入与其他客户端差异较大的客户端，从而增强全局模型中交互较少的物品的知识。我们在四个真实数据集上进行了全面实验，结果表明，所提方法在HR@10和NDCG@10指标上始终优于基线方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Federated recommendation systems (FRSs) have recently gained widespread attention due to their ability to train collaborative recommendation models without exchanging raw user data. However, existing FRSs face a severe challenge of data sparsity, which manifests at both the user and item levels. First, user data sparsity: some users may only have a small number of interactions with items, struggling to adequately train the personalized user embedding locally. Second, item data sparsity: some items may only receive a small number of user ratings, causing the global model to lack knowledge about them. Considering these, we propose the Knowledge Enhanced Federated Recommendation System named as KE-FedRS, of which the core idea is to enhance the knowledge of users with few interactions and items with few ratings at both the local and global levels. Specifically, at the local level, we introduce an auxiliary user embedding and average and aggregate this auxiliary embedding across similar users, thereby enriching the knowledge of the local user embedding. At the global level, we propose a hybrid client selection strategy based on item embedding discrepancies, prioritizing clients that exhibit greater divergence in item embeddings from others, thus enhancing the knowledge of items with fewer interactions in the global model. We conduct comprehensive experiments on four real-world datasets, and the results show that the proposed method consistently outperforms baseline approaches in terms of HR@10 and NDCG@10.

</details>

---

_知识库更新时间：2026-07-29T03:56:18.947821_
