---
title: "Enhancing Graph Collaborative Filtering with FourierKAN Feature Transformation"
paper_id: "https://doi.org/10.1145/3746252.3760909"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 25.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Mobile Crowdsensing and Crowdsourcing"]
---

# Enhancing Graph Collaborative Filtering with FourierKAN Feature Transformation

[查看原文](https://dblp.org/rec/conf/cikm/00030000HN25) · [ArXiv](https://arxiv.org/abs/2406.01034) · [Semantic Scholar](https://www.semanticscholar.org/paper/79d7ba3b0bb8e4a73901c2dac003a3f501b0035c)

## 一句话结论

> 论文提出FourierKAN-GCF，利用傅里叶KAN网络增强图协同过滤中的特征变换，在降低训练难度的同时提升推荐性能。

## 论文信息

- **作者**：Jinfeng Xu, Zheyu Chen, Jinze Li, Shuo Yang, Wei Wang, Xiping Hu, Edith C.‐H. Ngai
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：25.0
- **DOI**：[https://doi.org/10.1145/3746252.3760909](https://doi.org/10.1145/3746252.3760909)

<details open>
<summary><strong>中文摘要</strong></summary>

图协同过滤（Graph Collaborative Filtering, GCF）已成为现代推荐系统中的主导范式，擅长建模复杂的用户-物品交互并捕获高阶协同信号。现有大多数GCF模型主要依赖简化图架构（如LightGCN），该架构策略性地移除了原始图卷积网络中的特征变换与激活函数。通过系统性分析，我们揭示消息传播中的特征变换能够增强模型表示能力，但会以增加训练难度为代价。为此，我们提出FourierKAN-GCF这一新型框架，该框架采用傅里叶科尔莫戈罗夫-阿诺德网络（Fourier Kolmogorov-Arnold Networks）作为图传播层中的高效变换模块。该设计在降低训练难度的同时增强了模型表示能力。我们的FourierKAN-GCF能够实现比大多数广泛使用的GCF骨干模型更高的推荐性能，并可作为骨干网络集成到现有先进的自监督模型中，替换其原始骨干以提升性能。在三个公开数据集上的大量实验证明了FourierKAN-GCF的优越性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Graph Collaborative Filtering (GCF) has emerged as a dominant paradigm in modern recommendation systems, excelling at modeling complex user-item interactions and capturing high-order collaborative signals. Most existing GCF models predominantly rely on simplified graph architectures like LightGCN, which strategically remove feature transformation and activation functions from vanilla graph convolution networks. Through systematic analysis, we reveal that feature transformation in message propagation can enhance model representation, though at the cost of increased training difficulty. To this end, we propose FourierKAN-GCF, a novel framework that adopts Fourier Kolmogorov-Arnold Networks as efficient transformation modules within graph propagation layers. This design enhances model representation while decreasing training difficulty. Our FourierKAN-GCF can achieve higher recommendation performance than most widely used GCF backbone models and can be integrated into existing advanced self-supervised models as a backbone, replacing their original backbone to achieve enhanced performance. Extensive experiments on three public datasets demonstrate the superiority of FourierKAN-GCF.

</details>

---

_知识库更新时间：2026-07-16T03:56:50.204590_
