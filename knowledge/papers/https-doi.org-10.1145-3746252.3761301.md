---
title: "PKGRec: Personal Knowledge Graph Construction and Mining for Federated Recommendation Enhancement"
paper_id: "https://doi.org/10.1145/3746252.3761301"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 28.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Privacy-Preserving Technologies in Data", "Advanced Graph Neural Networks"]
---

# PKGRec: Personal Knowledge Graph Construction and Mining for Federated Recommendation Enhancement

[查看原文](https://dblp.org/rec/conf/cikm/00010S0Z0025) · [Semantic Scholar](https://www.semanticscholar.org/paper/c6bd861580d4c4f83b742c38f4932bdfb4e5e171)

## 一句话结论

> 提出PKGRec，一种联邦图推荐方法，通过个人知识图谱构建和分阶段图卷积，在保护隐私的同时提升推荐性能。

## 论文信息

- **作者**：Hong‐ying Yuan, Yang Zhang, Quan Z. Sheng, Lina Yao, Yipeng Zhou, Xiang He, Zhongjie Wang
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：28.0
- **DOI**：[https://doi.org/10.1145/3746252.3761301](https://doi.org/10.1145/3746252.3761301)

<details open>
<summary><strong>中文摘要</strong></summary>

个人知识图谱（Personal Knowledge Graphs, PKGs）将用户个人信息组织为由实体、属性和关系构成的结构化格式。通过利用这种结构化且语义丰富的数据，PKGs已成为保障个人数据管理和提供个性化服务的关键。为释放其在个性化推荐中的潜力，已有研究探索了PKGs的构建及其之上的推荐方法。然而，这些研究往往忽视了与跨用户分布式PKGs相关的挑战，例如联合训练与隐私保护。为应对这些挑战，我们提出PKGRec——一种专为PKGs设计的联邦图推荐方法，该方法利用联邦学习框架在联合学习过程中确保用户隐私与数据安全。此外，为适应PKGs以用户为中心的图结构，我们的方法将实体分为三类：用户、物品及其他实体，并在本地训练阶段采用一种新颖的分阶段图卷积方法，基于这些实体类别对各类实体进行建模。为实现分布式PKGs间高效的图信息共享，且无需额外数据传输或聚合，PKGRec通过联邦聚合对训练梯度进行图扩展。在四个公开数据集上进行的大量实验表明，我们的方法始终优于现有的联邦推荐方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Personal Knowledge Graphs (PKGs) organize an individual user's information into a structured format comprising entities, attributes, and relationships. By leveraging this structured and semantically rich data, PKGs have become essential for securing personal data management and delivering personalized services. To unlock their potential in personalized recommendations, prior research has explored the construction of PKGs and recommendation methods built upon them. However, these studies often overlook challenges associated with distributed PKGs across different users, such as joint training and privacy protection. To address these challenges, we propose PKGRec, a federated graph recommendation method specifically designed for PKGs, which utilizes a federated learning framework to ensure user privacy and data security during joint learning. Furthermore, to accommodate the user-centric graph structure of PKGs, our approach categorizes entities into three types: users, items, and other entities. It then applies a novel staged graph convolution method to model various entities based on these entity categories during local training. To enable efficient graph information sharing among distributed PKGs without requiring additional data transfer or aggregation, PKGRec performs graph expansion on the trained gradients by federated aggregation. Extensive experiments conducted on four publicly available datasets demonstrate that our method consistently outperforms the existing federated recommendation approaches.

</details>

---

_知识库更新时间：2026-07-15T03:52:18.777526_
