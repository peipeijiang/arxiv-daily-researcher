---
title: "COHESION: Composite Graph Convolutional Network with Dual-Stage Fusion for Multimodal Recommendation"
paper_id: "https://doi.org/10.1145/3726302.3729927"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Image Retrieval and Classification Techniques"]
---

# COHESION: Composite Graph Convolutional Network with Dual-Stage Fusion for Multimodal Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/0003000KN25) · [ArXiv](https://arxiv.org/abs/2504.04452) · [Semantic Scholar](https://www.semanticscholar.org/paper/a7bec80af2f9f2e5f67c334e1ad8d0132cd5536a)

## 一句话结论

> 该论文提出了一种名为COHESION的复合图卷积网络，通过双阶段融合策略和复合图结构来改进多模态推荐中的模态融合与表示学习，实验证明其在多个数据集上优于现有基线。

## 论文信息

- **作者**：Jinfeng Xu, Zheyu Chen, Wei Wang, Xiping Hu, Sang‐Wook Kim, Edith C.‐H. Ngai
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3726302.3729927](https://doi.org/10.1145/3726302.3729927)

<details open>
<summary><strong>中文摘要</strong></summary>

近期，多模态推荐领域的研究工作引起了广泛关注，这类方法利用多样化的模态信息来应对数据稀疏性问题并提升推荐准确性。在多模态推荐中，两个关键过程是模态融合与表示学习。以往的模态融合方法通常采用简单的注意力机制或预定义策略，在早期或晚期阶段进行融合，未能有效处理模态间的无关信息。在表示学习方面，先前的研究构建了包含用户-物品、用户-用户及物品-物品关系的异质与同质图结构，以更好地捕捉用户兴趣与物品特征。然而，在以往的工作中，模态融合与表示学习被视为两个独立的过程。本文揭示了这两个过程具有互补性，能够相互促进。具体而言，强大的表示学习能够增强模态融合效果，而有效的融合则能提升表示质量。基于这两个过程，我们提出了一种用于多模态推荐的复合图卷积网络，并采用双阶段融合策略，命名为COHESION。具体来说，该方法引入双阶段融合策略以降低无关信息的影响，在早期阶段利用行为模态对所有模态进行精炼，并在晚期阶段融合其表示。同时，它提出了一种复合图卷积网络，利用用户-物品、用户-用户及物品-物品图来提取用户与物品内部的异质和同质潜在关系。此外，该方法还引入了一种新颖的自适应优化机制，以确保各模态间表示的均衡与合理。在三个公开数据集上进行的大量实验表明，COHESION相较于多种竞争性基线方法具有显著优越性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recent works in multimodal recommendations, which leverage diverse modal information to address data sparsity and enhance recommendation accuracy, have garnered considerable interest. Two key processes in multimodal recommendations are modality fusion and representation learning. Previous approaches in modality fusion often employ simplistic attentive or pre-defined strategies at early or late stages, failing to effectively handle irrelevant information among modalities. In representation learning, prior research has constructed heterogeneous and homogeneous graph structures encapsulating user-item, user-user, and item-item relationships to better capture user interests and item profiles. Modality fusion and representation learning were considered as two independent processes in previous work. This paper reveals that these two processes are complementary and can support each other. Specifically, powerful representation learning enhances modality fusion, while effective fusion improves representation quality. Stemming from these two processes, we introduce a COmposite grapH convolutional nEtwork with dual-stage fuSION for the multimodal recommendation, named COHESION. Specifically, it introduces a dual-stage fusion strategy to reduce the impact of irrelevant information, refining all modalities using behavior modality in the early stage and fusing their representations at the late stage. It also proposes a composite graph convolutional network that utilizes user-item, user-user, and item-item graphs to extract heterogeneous and homogeneous latent relationships within users and items. Besides, it introduces a novel adaptive optimization to ensure balanced and reasonable representations across modalities. Extensive experiments on three public datasets demonstrate the significant superiority of COHESION over various competitive baselines.

</details>

---

_知识库更新时间：2026-09-06T04:59:26.699415_
