---
title: "LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation Models"
paper_id: "https://doi.org/10.1145/3705328.3748078"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 26.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Caching and Content Delivery", "Image and Video Quality Assessment"]
---

# LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation Models

[查看原文](https://dblp.org/rec/conf/recsys/JiangAA25) · [Semantic Scholar](https://www.semanticscholar.org/paper/208763d7361fceac40901b2a2b820c15661d41c6)

## 一句话结论

> 本文提出LEAF，一种基于实时访问频率分布的多级哈希框架，用于压缩大规模推荐模型中的嵌入表，在多个数据集上显著提升了AUC。

## 论文信息

- **作者**：Chaoyi Jiang, Abdulla Alshabanah, Murali Annavaram
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：26.0
- **DOI**：[https://doi.org/10.1145/3705328.3748078](https://doi.org/10.1145/3705328.3748078)

<details open>
<summary><strong>中文摘要</strong></summary>

深度学习推荐模型（Deep Learning Recommendation Models, DLRMs）在提升互联网及电子商务公司的用户参与度和体验方面发挥着核心作用。DLRMs通过建模用户行为来提供内容和商业建议。DLRMs依赖嵌入表（embedding tables）来捕捉用户行为，其中兴趣相似的用户在嵌入空间中可能被表示得更为接近。随着用户数量和特征的增长，嵌入表可扩展至数十TB规模，给训练和存储带来了挑战。这些模型通常需要大量的GPU内存，因为嵌入操作并非计算密集型，却占据大量存储空间。尽管已有一些解决方案尝试将嵌入表卸载至CPU，但这种方法仍需要TB级内存，并对CPU-GPU互连造成显著负担。我们提出了LEAF，一种基于实时访问频率分布的多级哈希框架，用于压缩大型嵌入表。具体而言，LEAF利用流式算法在线估计访问分布，无需依赖模型梯度，也无需预先知道访问分布。通过使用多个哈希函数，LEAF最小化了特征实例的碰撞率。实验表明，LEAF在Criteo Kaggle、Avazu、KDD12和Criteo Terabyte数据集上均优于最先进的压缩方法，测试AUC分别提升了1.411%、1.885%、2.761%和1.243%。LEAF的源代码可在github.com/chaoyij/LEAF获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Deep Learning Recommendation Models (DLRMs) are central to enhancing user engagement and experience with internet and ecommerce companies.DLRMs provide content and commercial suggestions by modeling user behavior.DLRMs rely on embedding tables to capture the user behavior, where users with similar interests may be represented closer in the embedding space.Embedding tables scale to tens of terabytes as the number of users and features grows, presenting challenges in training and storage.These models typically require substantial GPU memory, as embedding operations are not compute-intensive but occupy significant storage.While some solutions have explored offloading embedding tables to CPU, this approach still demands terabytes of memory and places a significant burden on CPU-GPU interconnect.We introduce LEAF, a multi-level hashing framework that compresses the large embedding tables based on real-time access frequency distribution.In particular, LEAF leverages a streaming algorithm to estimate access distributions on the fly without relying on model gradients or requiring a priori knowledge of access distribution.By using multiple hash functions, LEAF minimizes the collision rates of feature instances.Experiments show that LEAF outperforms stateof-the-art compression methods on Criteo Kaggle, Avazu, KDD12, and Criteo Terabyte datasets, with testing AUC improvements of 1.411%, 1.885%, 2.761%, and 1.243%, respectively.The source code of LEAF is available at github.com/chaoyij/LEAF.

</details>

---

_知识库更新时间：2026-08-21T02:21:31.085400_
