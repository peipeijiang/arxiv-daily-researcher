---
title: "面向高效对话式推荐：信息期望价值与赌博机学习的融合"
paper_id: "https://doi.org/10.1145/3696410.3714773"
source: "www"
published: "2025-01-01T00:00:00"
score: 48.0
tags: ["paper", "recommender-systems", "Advanced Bandit Algorithms Research", "Data Stream Mining Techniques", "Recommender Systems and Techniques"]
---

# 面向高效对话式推荐：信息期望价值与赌博机学习的融合

> **英文原标题**：Towards Efficient Conversational Recommendations: Expected Value of Information Meets Bandit Learning

[查看原文](https://dblp.org/rec/conf/www/0001LDL25) · [Semantic Scholar](https://www.semanticscholar.org/paper/7e00fa6b8a7d97fd9ae6e5ece31201f8c6af16a2)

## 一句话结论

> 该论文将期望信息价值（EVOI）集成到对话式bandit框架中，提出梯度EVOI和平滑关键术语上下文两种技术，显著降低了计算复杂度并实现了更紧的遗憾界。

## 论文信息

- **作者**：Zhuohua Li, Maoli Liu, Xiangxiang Dai, John C. S. Lui
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：48.0
- **DOI**：[https://doi.org/10.1145/3696410.3714773](https://doi.org/10.1145/3696410.3714773)

<details open>
<summary><strong>中文摘要</strong></summary>

在对话式推荐系统中，交互式地呈现查询并利用用户反馈对于高效估计用户偏好及提升推荐质量至关重要。在这些系统中选择最优查询是一项重大挑战，已被广泛研究为一种序贯决策问题。信息期望值（EVOI）通过计算期望奖励提升，为查询选择提供了理论依据。然而，该方法计算成本高昂且缺乏理论性能保证。相反，对话式强盗算法虽具有可证明的遗憾上界，但其查询选择策略相较于非对话式方法仅能带来边际性的遗憾改善。为解决这些局限，我们将EVOI整合到对话式强盗框架中，提出了一种新的对话机制，其包含两项关键技术：（1）基于梯度的EVOI，该方法用高效的随机梯度下降替代传统EVOI中复杂的贝叶斯更新，显著降低了计算复杂度并便于理论分析；（2）平滑化关键术语上下文，通过添加随机扰动来增强探索，以揭示更具体的用户偏好。我们的方法适用于对话式强盗算法的贝叶斯（汤普森采样）和频率学派（UCB）变体。我们提出了两种新算法——ConTS-EVOI与ConUCB-EVOI，并严格证明了它们能实现显著更紧的遗憾界，两种算法在时间范围T上的依赖度均实现了√d的改进，其中d为特征空间的维度。在合成数据集与真实世界数据集上的广泛评估验证了我们方法的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In conversational recommender systems, interactively presenting queries and leveraging user feedback are crucial for efficiently estimating user preferences and improving recommendation quality. Selecting optimal queries in these systems is a significant challenge that has been extensively studied as a sequential decision problem. The expected value of information (EVOI), which computes the expected reward improvement, provides a principled criterion for query selection. However, it is computationally expensive and lacks theoretical performance guarantees. Conversely, conversational bandits offer provable regret upper bounds, but their query selection strategies yield only marginal regret improvements over non-conversational approaches. To address these limitations, we integrate EVOI within the conversational bandit framework by proposing a new conversational mechanism featuring two key techniques: (1) gradient-based EVOI, which replaces the complex Bayesian updates in conventional EVOI with efficient stochastic gradient descent, significantly reducing computational complexity and facilitating theoretical analysis; and (2) smoothed key term contexts, which enhance exploration by adding random perturbations to uncover more specific user preferences. Our approach applies to both Bayesian (Thompson Sampling) and frequentist (UCB) variants of conversational bandits. We introduce two new algorithms, ConTS-EVOI and ConUCB-EVOI, and rigorously prove that they achieve substantially tighter regret bounds, with both algorithms offering a √d improvement in their dependence on the time horizon T, where d is the dimension of the feature space. Extensive evaluations on synthetic and real-world datasets validate the effectiveness of our methods.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

对话式推荐系统中，交互式查询和用户反馈对高效估计用户偏好、提升推荐质量至关重要。最优查询选择被广泛研究为序贯决策问题。信息期望价值（EVOI）通过计算期望奖励改进提供原则性准则，但计算昂贵且缺乏理论保证；对话式赌博机虽有可证明的遗憾上界，但查询选择策略相比非对话方法仅带来边际改进。为克服这些局限，本文将EVOI融入对话式赌博机框架，提出新对话机制：梯度化EVOI用随机梯度下降替代复杂贝叶斯更新，降低计算复杂度并便于理论分析；平滑关键术语上下文通过添加随机扰动增强探索，揭示更具体用户偏好。该方法适用于贝叶斯（汤普森采样）和频率派（UCB）变体，提出ConTS-EVOI和ConUCB-EVOI算法，并严格证明两者实现更紧的遗憾界，在时间T依赖上均获得√d改进（d为特征空间维度）。合成与真实数据集上的广泛评估验证了有效性。

### 主要创新

- 提出梯度化EVOI，用随机梯度下降替代传统贝叶斯更新，大幅降低计算复杂度并便于理论分析。
- 引入平滑关键术语上下文，通过随机扰动增强探索，揭示更具体的用户偏好。
- 将EVOI无缝集成到对话式赌博机框架，同时适用于汤普森采样和UCB变体。
- 提出ConTS-EVOI和ConUCB-EVOI算法，并证明其遗憾界在时间T依赖上实现√d改进。

### 研究方法

本文采用理论分析与实验验证相结合的方法。首先，将EVOI与对话式赌博机框架融合，设计梯度化EVOI以高效近似信息价值，并通过平滑关键术语上下文增强探索。然后，基于汤普森采样和UCB分别构建ConTS-EVOI和ConUCB-EVOI算法。最后，在合成和真实数据集上进行实验评估，验证算法有效性。

### 关键结果

ConTS-EVOI和ConUCB-EVOI算法均实现了更紧的遗憾界，在时间T依赖上获得√d改进。；合成和真实数据集上的广泛评估验证了方法的有效性。

### 技术栈

- 信息期望价值（EVOI）
- 随机梯度下降（SGD）
- 汤普森采样（Thompson Sampling）
- UCB（Upper Confidence Bound）
- 对话式赌博机（Conversational Bandit）

### 方法优势

- 创新性地将EVOI与对话式赌博机结合，兼顾了原则性与计算效率。
- 梯度化EVOI显著降低了计算复杂度，并提供了理论分析的可能性。
- 平滑关键术语上下文增强了探索能力，有助于发现更细粒度的用户偏好。
- 同时适用于贝叶斯和频率派方法，具有通用性。
- 提供了严格的遗憾界证明，且改进显著（√d）。

### 主要局限

- **论文局限**：摘要未提及具体实验设置、数据集名称、基线方法、消融实验或参数敏感性分析，因此无法评估方法的实际性能边界和泛化能力。
- **当前证据局限**：仅基于摘要，缺乏对方法局限性（如对噪声的鲁棒性、计算开销的实际测量、与更多基线对比等）的讨论。

### 与当前研究方向的关联

对话式推荐：核心研究内容，直接针对对话式推荐系统中的查询选择问题。；推荐系统：属于推荐系统领域，聚焦于交互式推荐场景。；序列推荐：相关，因为对话式推荐涉及序贯决策。；用户建模：通过查询和反馈估计用户偏好，属于用户建模范畴。；强化学习：对话式赌博机是强化学习的一种形式，且EVOI与决策理论相关。

---

_知识库更新时间：2026-07-30T03:48:55.615533_
