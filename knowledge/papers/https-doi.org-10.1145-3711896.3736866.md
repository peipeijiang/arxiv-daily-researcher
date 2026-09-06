---
title: "突破Top-K障碍：推进推荐系统中的Top-K排序指标优化"
paper_id: "https://doi.org/10.1145/3711896.3736866"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 45.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Data Management and Algorithms"]
---

# 突破Top-K障碍：推进推荐系统中的Top-K排序指标优化

> **英文原标题**：Breaking the Top-K Barrier: Advancing Top-K Ranking Metrics Optimization in Recommender Systems

[查看原文](https://dblp.org/rec/conf/kdd/00020Z0SF0025) · [ArXiv](https://arxiv.org/abs/2508.05673) · [Semantic Scholar](https://www.semanticscholar.org/paper/517d762cba3222663acecc68dccc4a01a6184c8e)

## 一句话结论

> 本文提出SoftmaxLoss@K损失函数，通过分位数技术处理Top-K截断并推导平滑上界，有效优化推荐系统中的NDCG@K指标，在多个数据集和骨干模型上平均提升6.03%。

## 论文信息

- **作者**：Weiqin Yang, Jiawei Chen, Shengjia Zhang, Peng Wu, Yuegang Sun, Yan Feng, Chun Chen, Can Wang
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：45.0
- **DOI**：[https://doi.org/10.1145/3711896.3736866](https://doi.org/10.1145/3711896.3736866)

<details open>
<summary><strong>中文摘要</strong></summary>

在推荐系统（RS）领域，诸如NDCG@K之类的Top-K排序指标是评估推荐性能的黄金标准。然而，在推荐模型的训练过程中，优化NDCG@K因其固有的不连续性以及复杂的Top-K截断而面临显著挑战。近期针对NDCG@K优化的尝试要么忽略了Top-K截断，要么遭受高计算成本和训练不稳定性的困扰。为克服这些局限，我们提出了SoftmaxLoss@K（SL@K），一种专为NDCG@K优化设计的新型推荐损失函数。具体而言，我们整合分位数技术以处理Top-K截断，并推导出一个平滑上界来优化NDCG@K，从而解决其不连续性问题。由此产生的SL@K损失具备多项理想特性，包括理论保证、易于实现、计算高效、梯度稳定以及噪声鲁棒性。在四个真实世界数据集和三个推荐骨干模型上的广泛实验表明，SL@K优于现有损失函数，平均提升幅度达6.03%。代码可在https://github.com/Tiny-Snow/IR-Benchmark获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In the realm of recommender systems (RS), Top-K ranking metrics such as NDCG@K are the gold standard for evaluating recommendation performance. However, during the training of recommendation models, optimizing NDCG@K poses significant challenges due to its inherent discontinuous nature and the intricate Top-K truncation. Recent efforts to optimize NDCG@K have either overlooked the Top-K truncation or suffered from high computational costs and training instability. To overcome these limitations, we propose SoftmaxLoss@K (SL@K), a novel recommendation loss tailored for NDCG@K optimization. Specifically, we integrate the quantile technique to handle Top-K truncation and derive a smooth upper bound for optimizing NDCG@K to address discontinuity. The resulting SL@K loss has several desirable properties, including theoretical guarantees, ease of implementation, computational efficiency, gradient stability, and noise robustness. Extensive experiments on four real-world datasets and three recommendation backbones demonstrate that SL@K outperforms existing losses with a notable average improvement of 6.03%. The code is available at https://github.com/Tiny-Snow/IR-Benchmark.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

在推荐系统中，Top-K排序指标如NDCG@K是评估推荐性能的金标准。然而，在训练推荐模型时，优化NDCG@K因其固有的不连续性和复杂的Top-K截断而面临重大挑战。近期优化NDCG@K的尝试要么忽略了Top-K截断，要么遭受高计算成本和训练不稳定的问题。为克服这些限制，本文提出SoftmaxLoss@K（SL@K），一种专为NDCG@K优化设计的新型推荐损失。具体而言，作者整合分位数技术处理Top-K截断，并推导出平滑上界以解决不连续性问题。所提出的SL@K损失具有多个理想特性，包括理论保证、易于实现、计算效率高、梯度稳定和噪声鲁棒性。在四个真实世界数据集和三个推荐骨干上的广泛实验表明，SL@K优于现有损失，平均提升6.03%。代码已公开。

### 主要创新

- 提出SL@K损失，专门针对NDCG@K优化，同时处理Top-K截断和不连续性问题。
- 引入分位数技术来有效处理Top-K截断。
- 推导出NDCG@K的平滑上界，解决其不连续性。
- SL@K损失具有理论保证、易于实现、计算高效、梯度稳定和噪声鲁棒等优点。

### 研究方法

本文采用理论分析与实验验证相结合的方法。首先，针对NDCG@K的优化难点，提出SL@K损失，其核心思想是整合分位数技术处理Top-K截断，并推导平滑上界。然后，在四个真实世界数据集和三个推荐骨干模型上进行实验，与现有损失函数对比，验证SL@K的有效性。

### 关键结果

在四个真实世界数据集和三个推荐骨干上的实验表明，SL@K优于现有损失，平均提升6.03%。

### 技术栈

- SoftmaxLoss@K (SL@K)
- NDCG@K
- 分位数技术
- 平滑上界
- 推荐系统

### 方法优势

- 针对NDCG@K优化的难点，提出了创新性的SL@K损失，同时解决Top-K截断和不连续性问题。
- SL@K损失具有理论保证、易于实现、计算高效、梯度稳定和噪声鲁棒等优点。
- 在多个真实数据集和推荐骨干上验证了有效性，平均提升6.03%。
- 代码公开，便于复现和进一步研究。

### 主要局限

- 论文局限：摘要未提供具体局限性讨论。当前证据局限：仅基于摘要，无法获取关于方法细节、实验设置、潜在缺点等更多信息。

### 与当前研究方向的关联

该论文与关键词高度相关。它聚焦于推荐系统中的排序与重排，特别是Top-K排序指标优化，属于推荐系统核心研究领域。同时，论文提出的方法具有明确的方法创新，并在多个数据集上验证，符合关键词中“有明确方法创新、可靠实验”的要求。

## 代码与复现

- [Tiny-Snow/IR-Benchmark](https://github.com/Tiny-Snow/IR-Benchmark)：official，置信度 100，Stars 30
- [WandRui/SLatK_imple](https://github.com/WandRui/SLatK_imple)：possible，置信度 30，Stars 1

---

_知识库更新时间：2026-09-06T04:59:26.702349_
