---
title: "A Node-Aware Dynamic Quantization Approach for Graph Collaborative Filtering"
paper_id: "https://doi.org/10.1145/3746252.3761244"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Innovative Human-Technology Interaction"]
---

# A Node-Aware Dynamic Quantization Approach for Graph Collaborative Filtering

[查看原文](https://dblp.org/rec/conf/cikm/0001LYT025) · [ArXiv](https://arxiv.org/abs/2508.16516) · [Semantic Scholar](https://www.semanticscholar.org/paper/74e9341fb190d1acc9f375df2ff386f07509f5fa)

## 一句话结论

> 提出一种基于图结构的节点感知动态量化方法GNAQ，用于图协同过滤推荐系统，在保持全精度模型性能的同时将模型大小压缩8-12倍，并提升训练速度。

## 论文信息

- **作者**：Lin Li, C. Li, Yu Yin, Xiaohui Tao, Jianwei Zhang
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3746252.3761244](https://doi.org/10.1145/3746252.3761244)

<details open>
<summary><strong>中文摘要</strong></summary>

在协同过滤推荐系统领域，图神经网络（Graph Neural Networks, GNNs）已展现出卓越性能，但由于其高嵌入参数需求和计算成本，在资源受限的边缘设备部署中面临重大挑战。直接对节点嵌入采用常规量化方法可能忽略其基于图的结构特性，导致消息传递过程中误差累积，从而降低量化嵌入的质量。为解决这一问题，我们提出基于图的节点感知动态量化训练方法（Graph based Node-Aware Dynamic Quantization training for collaborative filtering, GNAQ），这是一种利用图结构信息来增强GNNs在Top-K推荐中效率与准确性平衡的新型量化方法。GNAQ引入节点感知动态量化策略，通过融入图交互关系为单个节点嵌入自适应调整量化尺度。具体而言，该方法基于节点级特征分布初始化量化区间，并通过GNN层中的消息传递动态优化这些区间。这一策略缓解了固定量化尺度造成的信息损失，并捕捉用户-物品交互图中的层次化语义特征。此外，GNAQ采用图关系感知梯度估计替代传统直通估计器，确保训练过程中更精确的梯度传播。在四个真实数据集上的大量实验表明，GNAQ在2比特量化下平均提升Recall@10达27.8%、NDCG@10达17.6%，优于包括BiGeaR和N2UQ在内的最先进量化方法。特别地，GNAQ能够在保持全精度模型性能的同时将模型体积缩小8至12倍；此外，其训练时间相比量化基线方法快两倍。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In the realm of collaborative filtering recommendation systems, Graph Neural Networks (GNNs) have demonstrated remarkable performance but face significant challenges in deployment on resource-constrained edge devices due to their high embedding parameter requirements and computational costs. Using common quantization method directly on node embeddings may overlooks their graph based structure, causing error accumulation during message passing and degrading the quality of quantized embeddings.To address this, we propose Graph based Node-Aware Dynamic Quantization training for collaborative filtering (GNAQ), a novel quantization approach that leverages graph structural information to enhance the balance between efficiency and accuracy of GNNs for Top-K recommendation. GNAQ introduces a node-aware dynamic quantization strategy that adapts quantization scales to individual node embeddings by incorporating graph interaction relationships. Specifically, it initializes quantization intervals based on node-wise feature distributions and dynamically refines them through message passing in GNN layers. This approach mitigates information loss caused by fixed quantization scales and captures hierarchical semantic features in user-item interaction graphs. Additionally, GNAQ employs graph relation-aware gradient estimation to replace traditional straight-through estimators, ensuring more accurate gradient propagation during training. Extensive experiments on four real-world datasets demonstrate that GNAQ outperforms state-of-the-art quantization methods, including BiGeaR and N2UQ, by achieving average improvement in 27.8% Recall@10 and 17.6% NDCG@10 under 2-bit quantization. In particular, GNAQ is capable of maintaining the performance of full-precision models while reducing their model sizes by 8 to 12 times; in addition, the training time is twice as fast compared to quantization baseline methods.

</details>

---

_知识库更新时间：2026-07-16T03:56:50.204791_
