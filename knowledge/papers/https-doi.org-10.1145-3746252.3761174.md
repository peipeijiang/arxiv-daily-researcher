---
title: "Hypercomplex Prompt-aware Multimodal Recommendation"
paper_id: "https://doi.org/10.1145/3746252.3761174"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Machine Learning in Healthcare"]
---

# Hypercomplex Prompt-aware Multimodal Recommendation

[查看原文](https://dblp.org/rec/conf/cikm/0003000WH25) · [ArXiv](https://arxiv.org/abs/2508.10753) · [Semantic Scholar](https://www.semanticscholar.org/paper/13b9fc3f792c98033854f74b738780348d12c0cc)

## 一句话结论

> 提出HPMRec框架，利用超复数嵌入和提示感知补偿机制增强多模态推荐性能，在四个数据集上达到最优。

## 论文信息

- **作者**：Zheyu Chen, Jinfeng Xu, Hewei Wang, Shuo Yang, Zitong Wan, Haibo Hu
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3746252.3761174](https://doi.org/10.1145/3746252.3761174)

<details open>
<summary><strong>中文摘要</strong></summary>

现代推荐系统在应对信息过载问题以及处理多模态表示学习的固有局限性方面面临关键挑战。现有方法存在三个根本性缺陷：（1）通过单一表示来表征丰富多模态特征的能力受限；（2）现有的线性模态融合策略忽略了模态之间的深层非线性关联；（3）静态优化方法无法动态缓解图卷积网络（GCN）中的过平滑问题。为克服这些局限，我们提出HPMRec——一种新型超复数提示感知多模态推荐框架，该框架利用多分量形式的超复数嵌入来增强多模态特征的表示多样性。HPMRec采用超复数乘法自然建立非线性跨模态交互以弥合语义鸿沟，这有助于探索跨模态特征。HPMRec还引入提示感知补偿机制，以修正分量与模态特定特征丢失之间的错位问题，该机制从根本上缓解了过平滑现象。此外，框架进一步设计了自监督学习任务，以增强表示多样性并对齐不同模态。在四个公开数据集上的大量实验表明，HPMRec实现了最先进的推荐性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern recommender systems face critical challenges in handling information overload while addressing the inherent limitations of multimodal representation learning. Existing methods suffer from three fundamental limitations: (1) restricted ability to represent rich multimodal features through a single representation, (2) existing linear modality fusion strategies ignore the deep nonlinear correlations between modalities, and (3) static optimization methods failing to dynamically mitigate the over-smoothing problem in graph convolutional network (GCN). To overcome these limitations, we propose HPMRec, a novel Hypercomplex Prompt-aware Multimodal Recommendation framework, which utilizes hypercomplex embeddings in the form of multi-components to enhance the representation diversity of multimodal features. HPMRec adopts the hypercomplex multiplication to naturally establish nonlinear cross-modality interactions to bridge semantic gaps, which is beneficial to explore the cross-modality features. HPMRec also introduces the prompt-aware compensation mechanism to aid the misalignment between components and modality-specific features loss, and this mechanism fundamentally alleviates the over-smoothing problem. It further designs self-supervised learning tasks that enhance representation diversity and align different modalities. Extensive experiments on four public datasets show that HPMRec achieves state-of-the-art recommendation performance.

</details>

---

_知识库更新时间：2026-07-17T03:54:55.380878_
