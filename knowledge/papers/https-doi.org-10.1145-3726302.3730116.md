---
title: "Why is Normalization Necessary for Linear Recommenders?"
paper_id: "https://doi.org/10.1145/3726302.3730116"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Advanced Bandit Algorithms Research"]
---

# Why is Normalization Necessary for Linear Recommenders?

[查看原文](https://dblp.org/rec/conf/sigir/0002YKL25) · [ArXiv](https://arxiv.org/abs/2504.05805) · [Semantic Scholar](https://www.semanticscholar.org/paper/d6c87ebd39933b16d3f741e34561650ace273086)

## 一句话结论

> 本文通过理论分析揭示了归一化对线性自编码器推荐模型中流行度偏差和邻域偏差的影响，并提出了数据自适应归一化（DAN）方法，在多个数据集上显著提升了长尾物品和公平性评估的性能。

## 论文信息

- **作者**：Seongmin Park, Mincheol Yoon, H. J. Kim, Jongwuk Lee
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3726302.3730116](https://doi.org/10.1145/3726302.3730116)

<details open>
<summary><strong>中文摘要</strong></summary>

尽管线性自编码器（LAE）模型结构简单，但在推荐任务中，其性能已可与神经推荐模型相媲美甚至更优，且推理速度更快。然而，LAE面临两个关键挑战：（i）流行度偏差，即倾向于推荐热门物品；（ii）邻域偏差，即过度关注捕捉局部物品相关性。为解决这些问题，本文首先分析了两种现有LAE归一化方法（即随机游走归一化和对称归一化）的影响。理论分析表明，归一化方式显著影响物品间流行度偏差和邻域偏差的程度。受此分析启发，我们提出了一种通用归一化方案，称为数据自适应归一化（DAN），该方案通过调整物品侧和用户侧归一化以适配数据集独特特征，从而灵活控制流行度偏差和邻域偏差。由于DAN具有模型无关特性，可轻松应用于各种基于LAE的模型。实验结果表明，配备DAN的LAE在六个基准数据集上持续优于现有基于LAE的模型，在长尾物品评估和无偏评估中分别取得了高达128.57%和12.36%的显著提升。相关代码参见https://github.com/psm1206/DAN。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Despite their simplicity, linear autoencoder (LAE)-based models have shown comparable or even better performance with faster inference speed than neural recommender models. However, LAEs face two critical challenges: (i) popularity bias, which tends to recommend popular items, and (ii) neighborhood bias, which overly focuses on capturing local item correlations. To address these issues, this paper first analyzes the effects of two existing normalization methods for LAEs, i.e., random-walk and symmetric normalization. Our theoretical analysis reveals that normalization highly affects the degree of popularity and neighborhood biases among items. Inspired by this analysis, we propose a versatile normalization solution, called Data-Adaptive Normalization (DAN), which flexibly controls the popularity and neighborhood biases by adjusting item- and user-side normalization to align with unique dataset characteristics. Owing to its model-agnostic property, DAN can be easily applied to various LAE-based models. Experimental results show that DAN-equipped LAEs consistently improve existing LAE-based models across six benchmark datasets, with significant gains of up to 128.57% and 12.36% for long-tail items and unbiased evaluations, respectively. Refer to our code in https://github.com/psm1206/DAN.

</details>

---

_知识库更新时间：2026-09-06T04:59:26.700210_
