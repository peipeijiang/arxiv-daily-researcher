---
title: "Privacy-Preserving Social Recommendation: Privacy Leakage and Countermeasure"
paper_id: "https://doi.org/10.1145/3705328.3748051"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 16.0
tags: ["paper", "recommender-systems", "Privacy-Preserving Technologies in Data", "Cryptography and Data Security", "Internet Traffic Analysis and Secure E-voting"]
---

# Privacy-Preserving Social Recommendation: Privacy Leakage and Countermeasure

[查看原文](https://dblp.org/rec/conf/recsys/Chen0JWFWL25) · [Semantic Scholar](https://www.semanticscholar.org/paper/b84540ce2a555163889ba141f3684ed4806a7ac0)

## 一句话结论

> 该论文发现SeSoRec框架中的SSMM协议存在隐私泄露，提出Two-Time Pad攻击和Zero-Padding攻击，并设计了PPMM协议作为替代，以保护社交推荐中的用户隐私。

## 论文信息

- **作者**：Yuyue Chen, Peng Yang, Zoe L. Jiang, Wenhao Wu, Junbin Fang, Xuan Wang, Chuanyi Liu
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：16.0
- **DOI**：[https://doi.org/10.1145/3705328.3748051](https://doi.org/10.1145/3705328.3748051)

<details open>
<summary><strong>中文摘要</strong></summary>

社交推荐系统通常利用两类数据：来自评分平台（P0）的用户-项目交互矩阵（R）和来自社交平台（P1）的用户-用户社交图（S）。考虑到用户隐私，即R和S均不能直接共享，Chen等人引入了基于秘密共享矩阵乘法（SSMM）协议的安全社交推荐（SeSoRec）框架。然而，我们发现SSMM引入的中间信息泄露最终会导致S泄露给P0，这对SeSoRec的隐私保障构成了挑战。本研究首先通过形式化证明指出，SSMM违反了半诚实安全性，并确认SeSoRec中所谓的“无害”泄露源于SSMM在两个随机化阶段重复使用相同的One-Time Pad密钥。其次，本研究提出了双时间垫攻击（Two-Time Pad Attack），并设计了两种重构算法来评估泄露的严重程度。该攻击能够提取矩阵\(\mathbf {A}_{c_{-}\!even}\)和\(\mathbf {A}_{c_{-}\!odd}\)的列和，以及矩阵\(\mathbf {B}_{r_{-}\!even}\)和\(\mathbf {B}_{r_{-}\!odd}\)的行差，而这些矩阵与R或S密切相关。稀疏矩阵重构（SMR）算法在FilmTrust、Epinions和Douban数据集上对S中非零条目的重构率分别达到99.35%、83.83%和77.14%。灰度图像重构（GIR）算法能够成功恢复MNIST图像轮廓。第三，当SSMM中输入矩阵A/B的列数/行数为奇数（需通过零填充扩展为偶数维度）时，本研究提出了零填充攻击（Zero-Padding Attack），该攻击可直接暴露A/B的最后一列/行。最后，本研究提出了隐私保护矩阵乘法（PPMM）协议，并通过实验证明其可作为SSMM的替代方案，在保持效率的同时消除了此类泄露。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Social recommendation systems generally utilize two types of data, user-item interaction matrices (R) from rating platform (P0), and user-user social graphs (S) from social platform (P1). Considering user privacy that neither R nor S can be directly shared, Chen et al. introduced the Secure Social Recommendation (SeSoRec) framework with the Secret Sharing-based Matrix Multiplication (SSMM) protocol. However, we find that the leakage of intermeidate information introduced by SSMM will eventually lead to the leakage of S to P0, which challenges the privacy guarantees of SeSoRec. This work firstly identifies that the claimed "innocuous" leakage in SeSoRec originates from reusing the same One-Time Pad key during two randomization phases in SSMM, with formal proof that SSMM violates semi-honest security. Secondly, this work proposes the Two-Time Pad Attack with two reconstruction algorithms to evaluate the severity of the leakage. The Two-Time Pad Attack can extract the column-wise sum of matrices \(\mathbf {A}_{c_{-}\!even}\) and \(\mathbf {A}_{c_{-}\!odd}\), and the row-wise difference of matrices \(\mathbf {B}_{r_{-}\!even}\) and \(\mathbf {B}_{r_{-}\!odd}\), where such matrices are closely related to R or S. The Sparse Matrix Reconstruction (SMR) algorithm can achieve 99.35%, 83.83%, and 77.14% reconstruction rates for non-zero entries in S on FilmTrust, Epinions, and Douban datasets, respectively. The Grayscale Image Reconstruction (GIR) algorithm can successfully recover MNIST image contours. Thirdly, when the number of columns/rows of the input matrix A/B in SSMM is odd (requiring zero-padding to an even dimension), this work proposes the Zero-Padding Attack which can directly expose the last column/row of A/B. Finally, this work proposes the Privacy-Preserving Matrix Multiplication (PPMM) protocol with experimental demonstration as a replacement for SSMM, which eliminates such leakage while maintaining efficiency.

</details>

---

_知识库更新时间：2026-07-28T03:53:18.339473_
