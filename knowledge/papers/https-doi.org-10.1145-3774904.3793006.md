---
title: "从洞察到干预：可解释的神经元引导用于控制推荐系统中的流行度偏差"
paper_id: "https://doi.org/10.1145/3774904.3793006"
source: "www"
published: "2026-01-01T00:00:00"
score: 45.0
tags: ["paper", "recommender-systems"]
---

# 从洞察到干预：可解释的神经元引导用于控制推荐系统中的流行度偏差

> **英文原标题**：From Insight to Intervention: Interpretable Neuron Steering for Controlling Popularity Bias in Recommender Systems

[查看原文](https://dblp.org/rec/conf/www/AhmadovM26) · [ArXiv](https://arxiv.org/abs/2601.15122) · [Semantic Scholar](https://www.semanticscholar.org/paper/e50553035c96a8ef06ceeaa5781ee0965254b17e)

## 一句话结论

> 本文提出PopSteer方法，利用稀疏自编码器解释并缓解推荐系统中的流行度偏差，在提升公平性的同时最小化对准确性的影响。

## 论文信息

- **作者**：Parviz Ahmadov, Masoud Mansoury
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：45.0
- **DOI**：[https://doi.org/10.1145/3774904.3793006](https://doi.org/10.1145/3774904.3793006)

<details open>
<summary><strong>中文摘要</strong></summary>

流行度偏差是推荐系统中普遍存在的挑战，即少数热门物品占据主导关注，而大多数非热门物品则曝光不足。这种不平衡会降低推荐质量，并导致物品曝光的不公平。尽管现有的缓解方法在一定程度上解决了这一问题，但其运作方式往往缺乏透明度。本文提出了一种事后处理方法PopSteer，利用稀疏自编码器（Sparse Autoencoder, SAE）来解读并缓解推荐模型中的流行度偏差。该SAE经过训练，能够复现已训练模型的行为，同时实现神经元层面的可解释性。通过引入对热门或非热门物品具有强烈偏好的合成用户，我们根据神经元的激活模式识别出编码流行度信号的神经元。随后，通过调整最具偏差神经元的激活值来引导推荐。在三个公开数据集上使用序列推荐模型进行的实验表明，PopSteer在显著提升公平性的同时，对准确性的影响极小，并能提供可解释的洞察以及对公平性-准确性权衡的细粒度控制。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Popularity bias is a pervasive challenge in recommender systems, where a few popular items dominate attention while the majority of less popular items remain underexposed. This imbalance can reduce recommendation quality and lead to unfair item exposure. Although existing mitigation methods address this issue to some extent, they often lack transparency in how they operate. In this paper, we propose a post-hoc approach, PopSteer, that leverages a Sparse Autoencoder (SAE) to both interpret and mitigate popularity bias in recommendation models. The SAE is trained to replicate a trained model's behavior while enabling neuron-level interpretability. By introducing synthetic users with strong preferences for either popular or unpopular items, we identify neurons encoding popularity signals through their activation patterns. We then steer recommendations by adjusting the activations of the most biased neurons. Experiments on three public datasets with a sequential recommendation model demonstrate that PopSteer significantly enhances fairness with minimal impact on accuracy, while providing interpretable insights and fine-grained control over the fairness–accuracy trade-off.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出PopSteer方法，利用稀疏自编码器（SAE）解释和缓解推荐系统中的流行度偏差。通过生成极端偏好流行或非流行物品的合成用户，识别编码流行度信号的神经元，并调整其激活值以引导推荐。实验表明，PopSteer在三个数据集上显著提升公平性，同时保持推荐准确性，并提供可解释性和细粒度控制。

### 主要创新

- 首次提出基于SAE的可解释方法解决推荐系统流行度偏差。
- 利用合成用户剖面隔离流行度信号，通过Cohen's d量化神经元偏差。
- 基于神经元激活标准差和Cohen's d进行加权引导，避免硬干预的副作用。
- 后处理方法，无需重新训练模型，易于部署。

### 研究方法

训练SAE复制预训练推荐模型（SASRec）的行为；生成仅含流行或非流行物品的合成用户剖面；通过SAE激活计算每个神经元的Cohen's d；根据阈值和权重调整神经元激活值，得到修正后的用户嵌入用于推荐。

### 关键结果

PopSteer在ML-1M、BeerAdvocate和Yelp上优于所有基线，在相近nDCG下显著提高物品覆盖率和降低基尼系数；SAE重建余弦相似度>0.98；神经元激活分析验证了偏差编码；消融实验表明Cohen's d引导的神经元选择和定向引导均不可或缺。

### 技术栈

- Sparse Autoencoder (SAE)
- TopAct激活函数
- Cohen's d效应量
- SASRec序列推荐模型
- UMAP降维
- Wasserstein距离
- nDCG、物品覆盖率、基尼指数

### 方法优势

- 提供神经元级别的可解释性，揭示偏差内部机制。
- 后处理方式，无需修改原模型或重新训练。
- 细粒度控制公平性-准确性权衡，曲线平滑稳定。
- 在多个数据集上验证有效性，消融实验充分。

### 主要局限

- 合成用户剖面极端，可能不完全反映真实用户行为。
- 依赖SAE的重建质量，若重建误差大则影响效果。
- 超参数较多（αPop, αUnpop, β），需要调优。
- 仅以SASRec为基模型，对其他架构的泛化性未充分验证。

### 与当前研究方向的关联

论文直接针对推荐系统中的流行度偏差（公平性），提出可解释的神经元引导方法，与公平性、可解释性、推荐系统高度相关。

## 代码与复现

- [parepic/PopSteer2.0](https://github.com/parepic/PopSteer2.0)：possible，置信度 30，Stars 2
- [parepic/PopSteer](https://github.com/parepic/PopSteer)：possible，置信度 30，Stars 2

---

_知识库更新时间：2026-07-24T04:05:55.202101_
