---
title: "个性化马尔可夫链分解用于下一购物篮推荐"
paper_id: "https://doi.org/10.1145/1772690.1772773"
source: "citation"
published: "2010-04-26T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Consumer Market Behavior and Pricing"]
---

# 个性化马尔可夫链分解用于下一购物篮推荐

> **英文原标题**：Factorizing personalized Markov chains for next-basket recommendation

[查看原文](https://doi.org/10.1145/1772690.1772773)

## 一句话结论

> 该论文提出因子化个性化马尔可夫链（FPMC）模型，通过分解用户-物品转移立方体来同时建模用户长期偏好和序列模式，在下一购物篮推荐任务中优于传统矩阵分解和马尔可夫链方法。

## 论文信息

- **作者**：Steffen Rendle, Christoph Freudenthaler, Lars Schmidt-Thieme
- **来源**：Proceedings of the 19th international conference on World wide web
- **发布时间**：2010-04-26
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/1772690.1772773](https://doi.org/10.1145/1772690.1772773)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统是许多网站的重要组成部分。两种最流行的方法分别基于矩阵分解（MF）和马尔可夫链（MC）。MF方法通过对观测到的用户-项目偏好矩阵进行分解来学习用户的整体偏好。而MC方法则通过学习项目间的转移图来建模序列行为，该转移图用于根据用户近期的行为预测其下一步操作。本文提出了一种将这两种方法相结合的技术。我们的方法基于底层马尔可夫链上的个性化转移图。这意味着为每个用户学习一个独立的转移矩阵——因此该方法整体上使用了一个转移立方体。由于用于估计转移的观测数据通常非常有限，我们的方法采用成对交互模型（该模型是塔克分解的一个特例）对转移立方体进行分解。我们证明，所提出的分解个性化MC（FPMC）模型同时涵盖了通用马尔可夫链和标准矩阵分解模型。在模型参数学习方面，我们引入了针对序列购物篮数据改进的贝叶斯个性化排序（BPR）框架。实验结果表明，我们的FPMC模型在性能上优于标准矩阵分解模型以及未经分解和经分解学习的非个性化MC模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recommender systems are an important component of many websites. Two of the most popular approaches are based on matrix factorization (MF) and Markov chains (MC). MF methods learn the general taste of a user by factorizing the matrix over observed user-item preferences. On the other hand, MC methods model sequential behavior by learning a transition graph over items that is used to predict the next action based on the recent actions of a user. In this paper, we present a method bringing both approaches together. Our method is based on personalized transition graphs over underlying Markov chains. That means for each user an own transition matrix is learned - thus in total the method uses a transition cube. As the observations for estimating the transitions are usually very limited, our method factorizes the transition cube with a pairwise interaction model which is a special case of the Tucker Decomposition. We show that our factorized personalized MC (FPMC) model subsumes both a common Markov chain and the normal matrix factorization model. For learning the model parameters, we introduce an adaption of the Bayesian Personalized Ranking (BPR) framework for sequential basket data. Empirically, we show that our FPMC model outperforms both the common matrix factorization and the unpersonalized MC model both learned with and without factorization.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出了一种结合矩阵分解（MF）和马尔可夫链（MC）的推荐方法。MF通过分解用户-物品偏好矩阵学习用户的一般兴趣，而MC通过物品转移图建模序列行为。作者提出个性化转移图，为每个用户学习独立的转移矩阵，形成转移立方体。由于观测数据稀疏，他们使用成对交互模型（Tucker分解的特例）对转移立方体进行分解，得到因子化个性化MC（FPMC）模型。该模型同时包含普通MC和MF模型。为学习参数，他们引入了针对序列购物篮数据的贝叶斯个性化排序（BPR）框架的改编。实验表明，FPMC模型优于普通MF和未个性化MC模型（无论是否使用分解）。

### 主要创新

- 提出因子化个性化马尔可夫链（FPMC）模型，结合MF和MC方法。
- 为每个用户学习个性化转移矩阵，形成转移立方体。
- 使用成对交互模型（Tucker分解特例）分解转移立方体，解决数据稀疏问题。
- 改编BPR框架以适应序列购物篮数据。

### 研究方法

论文使用因子化个性化马尔可夫链（FPMC）模型，通过成对交互模型（Tucker分解特例）分解用户-物品转移立方体。学习算法采用改编的贝叶斯个性化排序（BPR）框架，针对序列购物篮数据优化。

### 关键结果

FPMC模型在性能上优于普通矩阵分解和未个性化马尔可夫链模型（无论是否使用分解）。

### 技术栈

- 矩阵分解（MF）
- 马尔可夫链（MC）
- Tucker分解
- 成对交互模型
- 贝叶斯个性化排序（BPR）

### 方法优势

- 创新性地融合MF和MC，同时捕捉用户长期偏好和短期序列模式。
- 个性化转移矩阵更贴合用户行为差异。
- 使用分解技术有效处理稀疏数据。
- 改编BPR框架适用于购物篮数据，优化排序性能。

### 主要局限

- 论文局限：摘要未提供具体实验设置、数据集、基线模型名称、损失函数或消融实验，无法评估泛化能力。当前证据局限：仅基于摘要，缺乏详细结果和实现细节。

### 与当前研究方向的关联

该论文与序列推荐高度相关，因其核心是建模用户序列行为（下一购物篮预测）。同时涉及用户建模（个性化转移矩阵）和排序优化（BPR框架）。与生成式推荐、LLM结合、推荐智能体等关键词相关性较低。

## 代码与复现

- [khesui/FPMC](https://github.com/khesui/FPMC)：likely，置信度 69，Stars 100

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3746252.3761384
- **seed_title**：Autonomous Reasoning-Retrieval for Large Language Model Based Recommendation
- **seed_score**：83.0

</details>

---

_知识库更新时间：2026-07-19T04:08:52.139873_
