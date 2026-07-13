---
title: "Conf-GNNRec: Quantifying and Calibrating the Prediction Confidence for GNN-based Recommendation Methods"
paper_id: "https://doi.org/10.1145/3701716.3715475"
source: "www"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Radiomics and Machine Learning in Medical Imaging", "Machine Learning in Healthcare"]
---

# Conf-GNNRec: Quantifying and Calibrating the Prediction Confidence for GNN-based Recommendation Methods

[查看原文](https://dblp.org/rec/conf/www/0013XWGZZ25) · [ArXiv](https://arxiv.org/abs/2505.16466) · [Semantic Scholar](https://www.semanticscholar.org/paper/ae42790189466fecf3dfbb8960314bc80363e6f9)

## 一句话结论

> 针对图神经网络推荐系统存在的过自信问题，提出Conf-GNNRec方法，通过评分校准和置信度损失函数量化并校准预测置信度，提升推荐性能。

## 论文信息

- **作者**：Meng Yan, Cai Xu, Xujing Wang, Ziyu Guan, Wei Zhao, Yuhang Zhou
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3701716.3715475](https://doi.org/10.1145/3701716.3715475)

<details open>
<summary><strong>中文摘要</strong></summary>

基于图神经网络的推荐系统在评分与排序等任务中表现优异。然而，在真实推荐场景中，用户误操作与恶意广告等噪声会通过消息传播机制逐渐累积。尽管现有研究通过降低噪声传播权重来减轻其影响，但推荐系统严重的稀疏性仍会导致低权重噪声邻居被误判为有效信息，且基于受污染节点获得的预测结果并非完全可信。因此，在高噪声框架下衡量预测结果的置信度至关重要。此外，我们对现有代表性基于图神经网络的推荐方法进行评估后发现，其存在过度自信问题。基于上述考量，我们提出了一种量化与校准基于图神经网络的推荐预测置信度的新方法（Conf-GNNRec）。具体而言，我们提出了一种评分校准方法，该方法基于用户个性化动态调整过度评分以缓解过度自信；同时设计了一种置信度损失函数，以降低负样本的过度自信程度，从而有效提升推荐性能。在公开数据集上的实验验证了Conf-GNNRec在预测置信度与推荐性能方面的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recommender systems based on graph neural networks perform well in tasks such as rating and ranking. However, in real-world recommendation scenarios, noise such as user misuse and malicious advertisement gradually accumulates through the message propagation mechanism. Even if existing studies mitigate their effects by reducing the noise propagation weights, the severe sparsity of the recommender system still leads to the low-weighted noisy neighbors being mistaken as meaningful information, and the prediction result obtained based on the polluted nodes is not entirely trustworthy. Therefore, it is crucial to measure the confidence of the prediction results in this highly noisy framework. Furthermore, our evaluation of the existing representative GNN-based recommendation shows that it suffers from overconfidence. Based on the above considerations, we propose a new method to quantify and calibrate the prediction confidence of GNN-based recommendations (Conf-GNNRec). Specifically, we propose a rating calibration method that dynamically adjusts excessive ratings to mitigate overconfidence based on user personalization. We also design a confidence loss function to reduce the overconfidence of negative samples and effectively improve recommendation performance. Experiments on public datasets demonstrate the validity of Conf-GNNRec in prediction confidence and recommendation performance.

</details>

---

_知识库更新时间：2026-07-13T06:43:12.875600_
