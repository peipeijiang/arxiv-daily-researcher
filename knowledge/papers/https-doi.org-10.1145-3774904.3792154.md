---
title: "Dual-Branch Multi-Granularity Network with Structured Contrastive Ranking for Cross-Modal Retrieval"
paper_id: "https://doi.org/10.1145/3774904.3792154"
source: "www"
published: "2026-01-01T00:00:00"
score: 5.0
tags: ["paper", "recommender-systems", "Multimodal Machine Learning Applications", "Advanced Image and Video Retrieval Techniques", "Image Retrieval and Classification Techniques"]
---

# Dual-Branch Multi-Granularity Network with Structured Contrastive Ranking for Cross-Modal Retrieval

[查看原文](https://dblp.org/rec/conf/www/ChenBJW26)

## 一句话结论

> 该论文提出了一种双分支多粒度网络（DBMG）结合结构化对比排序，用于跨模态检索，通过多模态大语言模型生成辅助描述和三级对比目标，在四个基准上显著提升了检索性能。

## 论文信息

- **作者**：Zihao Chen, Chenyang Bu, Shengwei Ji, Xindong Wu
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：5.0
- **DOI**：[https://doi.org/10.1145/3774904.3792154](https://doi.org/10.1145/3774904.3792154)

<details open>
<summary><strong>中文摘要</strong></summary>

跨模态检索（CMR）通过将图像和文本特征映射到共享嵌入空间已取得显著进展；然而，这些方法仍面临两个持续存在的挑战：（1）语义稀疏性，即判别性线索局限于局部区域，使得难以识别隐含的视觉证据；（2）语义模糊下的排序不确定性，即当候选样本具有相似上下文时，模型难以维持正确的检索顺序。为解决这些问题，我们提出了带有结构化对比排序的双分支多粒度网络（DBMG），该网络通过利用多模态大语言模型生成辅助描述来丰富视觉语义，通过捕获全局与局部交互的双分支架构对齐稀疏线索，并通过三阶段对比目标强制排序一致性，该目标逐步优化类别聚类、实例对齐和基于边距的排序。在四个标准CMR基准上的大量实验表明，DBMG优于12个强基线模型，平均mAP提升15.91%，确立了新的最先进水平。代码可在 https://github.com/DMiC-Lab-HFUT/DBMG 获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Cross-modal retrieval (CMR) has advanced considerably by mapping image and text features into a shared embedding space; however, these approaches still face two persistent challenges: (1) semantic sparsity, where discriminative cues are confined to localized regions, making it difficult to identify implicit visual evidence; and (2) ranking uncertainty under semantic ambiguity, where models struggle to maintain the correct retrieval order when candidates share similar contexts. To address these issues, we propose the Dual-Branch Multi-Granularity Network (DBMG) with Structured Contrastive Ranking, which enriches visual semantics by leveraging a multimodal large language model to generate auxiliary descriptions, aligns sparse cues through a dual-branch architecture capturing both global and local interactions, and enforces ranking consistency via a three-stage contrastive objective that progressively optimizes category clustering, instance alignment, and margin-based ranking. Extensive experiments on four standard CMR benchmarks demonstrate that DBMG outperforms 12 strong baselines, achieving an average 15.91% improvement in mAP, establishing a new state-of-the-art. The code is available at https://github.com/DMiC-Lab-HFUT/DBMG.

</details>

---

_知识库更新时间：2026-08-02T04:11:29.702213_
