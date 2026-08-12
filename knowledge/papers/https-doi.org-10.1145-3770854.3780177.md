---
title: "FCN: Fusing Exponential and Linear Cross Network for Click-Through Rate Prediction"
paper_id: "https://doi.org/10.1145/3770854.3780177"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 31.0
tags: ["paper", "recommender-systems"]
---

# FCN: Fusing Exponential and Linear Cross Network for Click-Through Rate Prediction

[查看原文](https://dblp.org/rec/conf/kdd/LiZZLSZ26) · [ArXiv](https://arxiv.org/abs/2407.13349) · [Semantic Scholar](https://www.semanticscholar.org/paper/93d0d6d8a362c2c7fca0099c568047b6579f446a)

## 一句话结论

> 该论文提出了一种融合指数和线性交叉网络的FCN模型，用于显式建模高阶特征交互，在多个数据集上提升了CTR预测的准确性和效率。

## 论文信息

- **作者**：Honghao Li, Yiwen Zhang, Yi Zhang, Hanwei Li, Lei Sang, Jieming Zhu
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：31.0
- **DOI**：[https://doi.org/10.1145/3770854.3780177](https://doi.org/10.1145/3770854.3780177)

<details open>
<summary><strong>中文摘要</strong></summary>

作为点击率（CTR）预测中一种重要的建模范式，Deep & Cross Network及其衍生模型因其在计算成本与性能之间取得良好平衡而获得广泛认可。然而，该范式通常依赖深度神经网络（DNN）隐式学习高阶特征交互，出于对模型复杂度的顾虑，并未显式建模极高阶交互。为解决这一局限，我们提出了一种新颖的CTR预测模型，称为融合交叉网络（FCN），其由两个子网络组成：指数交叉网络（ECN）和线性交叉网络（LCN）。具体而言，ECN显式捕获极高阶特征交互，其交互阶数随网络深度呈指数增长，而LCN则以线性增长的阶数捕获低阶特征交互。通过整合这两个子网络，FCN能够显式建模广泛范围的特征交互，从而无需依赖DNN的隐式建模。此外，我们引入了一种低成本聚合方法，将参数数量减少50%，推理延迟降低23%。同时，我们提出了一种简单而有效的损失函数Tri-BCE，为每个子网络提供定制化的监督信号。我们在六个公开基准数据集和16个基线上评估了FCN的有效性和效率。此外，我们还在一个覆盖七天的真实业务数据集上验证了FCN的有效性。代码、运行日志及详细的超参数配置已公开于https://github.com/salmon1802/FCN。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

As an important modeling paradigm in click-through rate (CTR) prediction, the Deep & Cross Network and its derivative models have gained widespread recognition, primarily due to their success in trade-off computational cost and performance. However, this paradigm typically depends on deep neural network (DNN) to implicitly learn high-order feature interactions, without explicitly modeling extremely high-order interactions due to concerns about model complexity. To address this limitation, we propose a novel model for CTR prediction, called the Fusing Cross Network (FCN), which consists of two sub-networks: the Exponential Cross Network (ECN) and the Linear Cross Network (LCN). Specifically, ECN explicitly captures extremely high-order feature interactions whose order increases exponentially with network depth, while LCN captures low-order feature interactions with linearly increasing order. By integrating these two sub-networks, FCN is able to explicitly model a broad spectrum of feature interactions, thereby eliminating the need to rely on implicit modeling by DNN. Moreover, we introduce a low-cost aggregation method that reduces the number of parameters by 50% and inference latency by 23%. Meanwhile, we propose a simple yet effective loss function, Tri-BCE, which provides tailored supervision signals for each sub-network. We evaluate the effectiveness and efficiency of FCN on six public benchmark datasets and 16 baselines. Furthermore, we verify the effectiveness of the FCN on a real-world business dataset spanning seven days. The code, running logs, and detailed hyperparameter configurations are publicly available at https://github.com/salmon1802/FCN.

</details>

---

_知识库更新时间：2026-08-12T03:12:07.694863_
