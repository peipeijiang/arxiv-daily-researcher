---
title: "Joint Similarity Item Exploration and Overlapped User Guidance for Multi-Modal Cross-Domain Recommendation"
paper_id: "https://doi.org/10.1145/3696410.3714860"
source: "www"
published: "2025-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Advanced Graph Neural Networks"]
---

# Joint Similarity Item Exploration and Overlapped User Guidance for Multi-Modal Cross-Domain Recommendation

[查看原文](https://dblp.org/rec/conf/www/000500LWZFPW25) · [ArXiv](https://arxiv.org/abs/2502.16068) · [Semantic Scholar](https://www.semanticscholar.org/paper/a4b656f0c36b11b6dc05f4aac5a8588717a0d875)

## 一句话结论

> 该论文提出了一种联合相似物品探索和重叠用户引导的方法（SIEOUG），用于解决多模态跨域推荐中的数据稀疏和用户重叠少的问题，并在Amazon数据集上显著优于现有模型。

## 论文信息

- **作者**：Weiming Liu, Chaochao Chen, Jiahe Xu, Xinting Liao, Fan Wang, Xiaolin Zheng, Z. F. Fu, Ruiguang Pei, Jun Wang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3696410.3714860](https://doi.org/10.1145/3696410.3714860)

<details open>
<summary><strong>中文摘要</strong></summary>

跨域推荐（CDR）已被广泛研究，旨在通过跨域知识共享来解决长期存在的数据稀疏问题。在本文中，我们聚焦于多模态跨域推荐（MMCDR）问题，其中不同项目具有多模态信息，而跨域重叠用户较少。MMCDR的挑战主要体现在两个方面：充分利用每个域内多样化的多模态信息，以及有效利用跨域的有用知识迁移。然而，现有方法未能对具有相似特征的项目进行聚类，同时过滤掉不同模态中的固有噪声，从而阻碍了模型性能。更糟糕的是，传统CDR模型主要依赖重叠用户进行域适应，使其难以应对大多数用户为非重叠用户的情形。为弥补这一不足，我们提出了联合相似项目探索与重叠用户引导（SIEOUG）方法来解决MMCDR问题。SIEOUG首先提出相似项目探索模块，该模块不仅获取成对和成组的项目-项目图知识，还减少了多模态建模中的无关噪声。随后，SIEOUG提出用户-项目协同过滤模块，利用注意力机制聚合用户/项目嵌入以进行协同过滤。最后，SIEOUG提出重叠用户引导模块，通过最优用户匹配实现跨域知识共享。我们在Amazon数据集上针对多个不同任务的实证研究表明，在MMCDR设置下，SIEOUG显著优于现有最先进模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Cross-Domain Recommendation (CDR) has been widely investi- gated for solving long-standing data sparsity problem via knowl- edge sharing across domains. In this paper, we focus on the Multi- Modal Cross-Domain Recommendation (MMCDR) problem where different items have multi-modal information while few users are overlapped across domains. MMCDR is particularly challenging in two aspects: fully exploiting diverse multi-modal information within each domain and leveraging useful knowledge transfer across domains. However, previous methods fail to cluster items with similar characteristics while filtering out inherit noises within different modalities, hurdling the model performance. What is worse, conventional CDR models primarily rely on overlapped users for domain adaptation, making them ill-equipped to handle scenarios where the majority of users are non-overlapped. To fill this gap, we propose Joint Similarity Item Exploration and Overlapped User Guidance (SIEOUG) for solving the MMCDR problem. SIEOUG first proposes similarity item exploration module, which not only obtains pair-wise and group-wise item-item graph knowledge, but also reduces irrelevant noise for multi-modal modeling. Then SIEOUG proposes user-item collaborative filtering module to aggregate user/item embeddings with the attention mechanism for collaborative filtering. Finally SIEOUG proposes overlapped user guidance module with optimal user matching for knowledge sharing across domains. Our empirical study on Amazon dataset with several different tasks demonstrates that SIEOUG significantly outperforms the state-of-the-art models under the MMCDR setting.

</details>

---

_知识库更新时间：2026-08-27T10:15:25.338574_
