---
title: "LightGCN"
paper_id: "https://doi.org/10.1145/3397271.3401063"
source: "citation"
published: "2020-07-25T00:00:00"
score: 20.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Image and Video Quality Assessment"]
---

# LightGCN

[查看原文](https://doi.org/10.1145/3397271.3401063)

## 一句话结论

> 论文提出LightGCN，通过简化图卷积网络（去除特征变换和非线性激活）在协同过滤推荐中取得更优性能，并揭示了GCN在推荐中有效性的原因。

## 论文信息

- **作者**：Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, Meng Wang
- **来源**：Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval
- **发布时间**：2020-07-25
- **相关度评分**：20.0
- **DOI**：[https://doi.org/10.1145/3397271.3401063](https://doi.org/10.1145/3397271.3401063)

<details open>
<summary><strong>中文摘要</strong></summary>

图卷积网络（GCN）已成为协同过滤领域的最新先进技术。然而，其在推荐任务中有效的原因尚未得到充分理解。现有将GCN应用于推荐系统的工作缺乏对GCN的彻底消融分析，而GCN最初是为图分类任务设计的，并配备了多种神经网络操作。然而，我们通过实验发现，GCN中两种最常见的设计——特征变换和非线性激活——对协同过滤的性能贡献甚微。更糟糕的是，加入这些操作会增加训练难度并降低推荐性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Graph Convolution Network (GCN) has become new state-of-the-art for collaborative filtering. Nevertheless, the reasons of its effectiveness for recommendation are not well understood. Existing work that adapts GCN to recommendation lacks thorough ablation analyses on GCN, which is originally designed for graph classification tasks and equipped with many neural network operations. However, we empirically find that the two most common designs in GCNs -- feature transformation and nonlinear activation -- contribute little to the performance of collaborative filtering. Even worse, including them adds to the difficulty of training and degrades recommendation performance.

</details>

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3705328.3748154
- **seed_title**：How Powerful are LLMs to Support Multimodal Recommendation? A Reproducibility Study of LLMRec
- **seed_score**：95.0

</details>

---

_知识库更新时间：2026-08-09T02:40:57.865912_
