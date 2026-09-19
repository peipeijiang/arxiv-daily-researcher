---
title: "A Hybrid Recommendation Framework Leveraging User Community Detection and Latent Feature Extraction for Improved Personalized Recommendations"
paper_id: "https://doi.org/10.1007/s44196-026-01579-3"
source: "openalex"
published: "2026-09-18T00:00:00"
score: 26.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Complex Network Analysis Techniques", "Expert finding and Q&A systems"]
---

# A Hybrid Recommendation Framework Leveraging User Community Detection and Latent Feature Extraction for Improved Personalized Recommendations

[查看原文](https://doi.org/10.1007/s44196-026-01579-3)

## 一句话结论

> 针对大规模数据集中小社区检测困难的问题，本文提出基于Leiden社区检测和矩阵分解的混合推荐框架CHRS_c与CHRS_p，在MovieLens和Anime数据集上相比Louvain方法将MAE降低了约7%，提升了推荐准确性。

## 论文信息

- **作者**：Sarada Korrapati, Murali Krishna Enduri, V Ramanjaneyulu Yannam, Srilatha Tokala
- **来源**：International Journal of Computational Intelligence Systems
- **发布时间**：2026-09-18
- **相关度评分**：26.0
- **DOI**：[https://doi.org/10.1007/s44196-026-01579-3](https://doi.org/10.1007/s44196-026-01579-3)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统通过传递与用户偏好相匹配的信息来增强个性化，从而改善不同应用中的整体用户体验。在推荐系统中，用户-物品评分矩阵表示用户对一组物品的偏好。在本研究中，我们构建了使用余弦相似度的社区混合推荐系统（\(\text {CHRS}_{c}\)）和使用皮尔逊相似度的社区混合推荐系统（\(\text {CHRS}_{p}\)）。所提出的框架通过根据节点之间的相似性将节点分组为社区来纳入社区检测。然而，在大规模数据集中识别小型社区仍然是一个重大挑战。现有的Louvain社区检测方法存在一定局限性，因为它可能无法正确检测大型网络中的非连通社区。为解决这一局限性，我们提出了\(\text {CHRS}_{c}\)和\(\text {CHRS}_{p}\)方法。所提出的策略包括以下步骤：（1）从用户-物品评分矩阵构建二部图，（2）应用Leiden社区检测算法从二部图生成社区，并为每个社区创建单独的评分矩阵，（3）对每个社区评分矩阵结合物品属性，执行矩阵分解与余弦相似度或矩阵分解与皮尔逊相似度的凸组合，以及（4）通过比较预测评分矩阵和实际评分矩阵，使用均方根误差（RMSE）、平均绝对误差（MAE）、精确率、召回率和F1分数评估性能。所提出的CHRS方法在标准基准数据集上进行评估，包括MovieLens 100K、MovieLens 1M和Anime Recommendations。在Anime Recommendation数据集上的实验分析表明，与基于Louvain的方法相比，MAE改善了近7%。结果表明，所提出的CHRS方法即使在社会规模较小时也能有效识别具有高内部相似性的社区，从而实现更准确的推荐。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

A recommender system enhances personalization by delivering information that matches user preferences, thereby improving the overall user experience across different applications. In recommender systems, the user-item rating matrix represents user preferences for a collection of items. In this work, we build a community hybrid recommender system using cosine similarity ( \(\text {CHRS}_{c}\) ) and a community hybrid recommender system using Pearson similarity ( \(\text {CHRS}_{p}\) ). The proposed framework incorporates community detection by grouping nodes into communities according to their similarities. However, identifying small communities within large-scale datasets remains a significant challenge. The existing Louvain community detection method has certain limitations, as it may fail to correctly detect disconnected communities in large networks. To address this limitation, we propose the \(\text {CHRS}_{c}\) and \(\text {CHRS}_{p}\) approaches. The proposed strategy consists of the following steps: (1) developing a bipartite graph from the user-item rating matrix, (2) applying the Leiden community detection algorithm to generate communities from the bipartite graph and creating separate rating matrices for each community, (3) performing a convex combination of Matrix Factorization with cosine similarity or Matrix Factorization with Pearson similarity for each community rating matrix along with item properties, and (4) evaluating the performance using root mean square error (RMSE), mean absolute error (MAE), precision, recall, and F1-score by comparing predicted and actual rating matrices. The proposed CHRS method is evaluated on standard benchmark datasets, including MovieLens 100K, MovieLens 1M, and Anime Recommendations. Experimental analysis on the Anime Recommendation dataset shows nearly a 7% improvement in MAE compared with the Louvain based method. The results demonstrate that the suggested CHRS method effectively identifies communities with high internal similarity, even when community sizes are small, leading to more accurate recommendations.

</details>

---

_知识库更新时间：2026-09-19T04:55:42.052089_
