---
title: "打开黑箱：推荐系统中流行度偏差的可解释补救措施"
paper_id: "https://doi.org/10.1145/3705328.3759310"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 43.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Topic Modeling"]
---

# 打开黑箱：推荐系统中流行度偏差的可解释补救措施

> **英文原标题**：Opening the Black Box: Interpretable Remedies for Popularity Bias in Recommender Systems

[查看原文](https://dblp.org/rec/conf/recsys/AhmadovM25)

## 一句话结论

> 本文提出一种基于稀疏自编码器的后处理方法，用于解释和缓解深度推荐模型中的流行度偏差，在提升公平性的同时保持推荐准确性。

## 论文信息

- **作者**：Parviz Ahmadov, Masoud Mansoury
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：43.0
- **DOI**：[https://doi.org/10.1145/3705328.3759310](https://doi.org/10.1145/3705328.3759310)

<details open>
<summary><strong>中文摘要</strong></summary>

流行度偏差是推荐系统中一个公认的挑战，即少数热门物品获得不成比例的关注，而大多数冷门物品则被严重忽视。这种不平衡往往导致推荐质量下降以及物品曝光的不公平。尽管现有的缓解技术在一定程度上解决了这一偏差，但它们通常缺乏操作过程的透明度。在本文中，我们提出了一种基于稀疏自编码器（Sparse Autoencoder, SAE）的事后方法，用于解释和缓解深度推荐模型中的流行度偏差。该SAE经过训练，能够复制预训练模型的行为，同时实现神经元级别的可解释性。通过引入对热门或冷门物品具有明确偏好的合成用户，我们根据神经元的激活模式识别出编码流行度信号的神经元。随后，我们调整最具偏差的神经元的激活值，以引导推荐走向更公平的曝光。在基于序列推荐模型的两个公开数据集上的实验表明，我们的方法在最小化对准确率影响的同时显著提升了公平性。此外，该方法还提供了可解释性，并能够对公平性与准确率之间的权衡进行细粒度控制。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Popularity bias is a well-known challenge in recommender systems, where a small number of popular items receive disproportionate attention, while the majority of less popular items are largely overlooked.This imbalance often results in reduced recommendation quality and unfair exposure of items.Although existing mitigation techniques address this bias to some extent, they typically lack transparency in how they operate.In this paper, we propose a post-hoc method using a Sparse Autoencoder (SAE) to interpret and mitigate popularity bias in deep recommendation models.The SAE is trained to replicate a pre-trained model's behavior while enabling neuron-level interpretability.By introducing synthetic users with clear preferences for either popular or unpopular items, we identify neurons encoding popularity signals based on their activation patterns.We then adjust the activations of the most biased neurons to steer recommendations toward fairer exposure.Experiments on two public datasets using a sequential recommendation model show that our method significantly improves fairness with minimal impact on accuracy.Moreover, it offers interpretability and fine-grained control over the fairness-accuracy trade-off.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对推荐系统中的流行度偏差问题，提出了一种基于稀疏自编码器（SAE）的后处理方法，旨在解释并缓解深度推荐模型中的流行度偏差。该方法通过训练SAE复制预训练模型的行为，实现神经元级别的可解释性。通过引入对流行或非流行物品有明确偏好的合成用户，根据激活模式识别编码流行度信号的神经元，并调整这些神经元的激活值以引导推荐向更公平的曝光方向。在两个公开数据集上使用序列推荐模型进行实验，结果表明该方法在显著提升公平性的同时，对准确率影响极小，并提供了可解释性和对公平-准确权衡的细粒度控制。

### 主要创新

- 提出使用稀疏自编码器（SAE）实现神经元级别的可解释性，揭示流行度偏差的内部机制。
- 通过合成用户识别编码流行度信号的神经元，提供了一种新颖的偏差定位方法。
- 通过调整特定神经元的激活值来缓解偏差，实现了对公平-准确权衡的细粒度控制。
- 方法为后处理方式，无需重新训练模型，具有实用性和灵活性。

### 研究方法

论文采用后处理方法，首先训练一个稀疏自编码器（SAE）来复制预训练深度推荐模型的行为，从而获得可解释的神经元表示。然后，通过构造对流行或非流行物品有明确偏好的合成用户，分析SAE中神经元的激活模式，识别出编码流行度信号的神经元。最后，调整这些最偏斜神经元的激活值，以引导推荐结果向更公平的曝光分布偏移。实验使用序列推荐模型在两个公开数据集上进行评估。

### 关键结果

实验表明，该方法显著提升了推荐公平性，同时对推荐准确率的影响极小。此外，该方法提供了可解释性，并允许对公平性与准确性之间的权衡进行细粒度控制。

### 技术栈

- 稀疏自编码器（SAE）
- 序列推荐模型
- 合成用户生成
- 神经元激活模式分析
- 激活值调整

### 方法优势

- 方法具有可解释性，能够揭示模型内部流行度偏差的编码机制。
- 后处理方式无需重新训练模型，易于集成到现有系统中。
- 提供了对公平-准确权衡的细粒度控制，灵活性高。
- 在两个公开数据集上验证了有效性，且对准确率影响小。

### 主要局限

- 论文局限：方法依赖于合成用户的设计，可能无法完全覆盖真实用户偏好多样性。
- 当前证据局限：摘要未提供具体数据集名称、基线模型、实验数值（如准确率、公平性指标的具体数值）以及与其他方法的对比结果。
- 当前证据局限：未讨论该方法在不同推荐模型架构上的泛化能力。

### 与当前研究方向的关联

论文直接涉及推荐系统的公平性（流行度偏差缓解）和可解释性（黑箱打开），与关键词“公平性”、“可解释性”高度相关。同时，方法基于序列推荐模型，与“序列推荐”相关。论文未涉及生成式推荐、LLM、多模态、对话式推荐等关键词。

---

_知识库更新时间：2026-07-18T03:48:20.891958_
