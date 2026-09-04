---
title: "Conf-GNNRec: Quantifying and Calibrating the Prediction Confidence for GNN-based Recommendation Methods"
paper_id: "https://doi.org/10.1145/3701716.3715475"
source: "www"
published: "2025-01-01T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Radiomics and Machine Learning in Medical Imaging", "Machine Learning in Healthcare"]
---

# Conf-GNNRec: Quantifying and Calibrating the Prediction Confidence for GNN-based Recommendation Methods

[查看原文](https://dblp.org/rec/conf/www/0013XWGZZ25) · [ArXiv](https://arxiv.org/abs/2505.16466) · [Semantic Scholar](https://www.semanticscholar.org/paper/ae42790189466fecf3dfbb8960314bc80363e6f9)

## 一句话结论

> 评分失败，无法生成摘要

## 论文信息

- **作者**：Meng Yan, Cai Xu, Xujing Wang, Ziyu Guan, Wei Zhao, Yuhang Zhou
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3701716.3715475](https://doi.org/10.1145/3701716.3715475)

<details>
<summary><strong>英文摘要</strong></summary>

Recommender systems based on graph neural networks perform well in tasks such as rating and ranking. However, in real-world recommendation scenarios, noise such as user misuse and malicious advertisement gradually accumulates through the message propagation mechanism. Even if existing studies mitigate their effects by reducing the noise propagation weights, the severe sparsity of the recommender system still leads to the low-weighted noisy neighbors being mistaken as meaningful information, and the prediction result obtained based on the polluted nodes is not entirely trustworthy. Therefore, it is crucial to measure the confidence of the prediction results in this highly noisy framework. Furthermore, our evaluation of the existing representative GNN-based recommendation shows that it suffers from overconfidence. Based on the above considerations, we propose a new method to quantify and calibrate the prediction confidence of GNN-based recommendations (Conf-GNNRec). Specifically, we propose a rating calibration method that dynamically adjusts excessive ratings to mitigate overconfidence based on user personalization. We also design a confidence loss function to reduce the overconfidence of negative samples and effectively improve recommendation performance. Experiments on public datasets demonstrate the validity of Conf-GNNRec in prediction confidence and recommendation performance.

</details>

---

_知识库更新时间：2026-09-04T05:10:12.466156_
