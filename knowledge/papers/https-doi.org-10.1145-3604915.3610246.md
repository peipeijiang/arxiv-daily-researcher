---
title: "导航推荐系统中的反馈循环：来自工业实践的见解与策略"
paper_id: "https://doi.org/10.1145/3604915.3610246"
source: "citation"
published: "2023-09-14T00:00:00"
score: 39.0
tags: ["paper", "recommender-systems", "Advanced Bandit Algorithms Research", "Smart Grid Energy Management", "Recommender Systems and Techniques"]
---

# 导航推荐系统中的反馈循环：来自工业实践的见解与策略

> **英文原标题**：Navigating the Feedback Loop in Recommender Systems: Insights and Strategies from Industry Practice

[查看原文](https://doi.org/10.1145/3604915.3610246)

## 一句话结论

> 该论文从工业实践角度定义了推荐系统中的开放和封闭反馈循环，分析了其产生原因和测量挑战，并提出使用离线评估框架和模拟系统来评估长期反馈循环偏差，为优化推荐系统性能提供了见解。

## 论文信息

- **作者**：D.T.K. Tong, Qifeng Qiao, Ting-Po Lee, James McInerney, Justin Basilico
- **来源**：Proceedings of the 17th ACM Conference on Recommender Systems
- **发布时间**：2023-09-14
- **相关度评分**：39.0
- **DOI**：[https://doi.org/10.1145/3604915.3610246](https://doi.org/10.1145/3604915.3610246)

<details open>
<summary><strong>中文摘要</strong></summary>

理解和衡量工业推荐系统中反馈循环的影响颇具挑战性，这导致对其性能恶化的低估。在本研究中，我们定义了开放与封闭反馈循环，并基于以往研究中关注较少的实际案例，探讨了工业界反馈循环产生的独特原因。我们强调了使用传统在线A/B测试捕捉反馈循环全面影响时所面临的测量难题。为解决这一问题，我们提出采用离线评估框架作为长期反馈循环偏差的替代指标，并借助一个使用真实数据的实用模拟系统加以支持。我们的研究结果为优化在反馈循环条件下运行的推荐系统性能提供了有价值的见解。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Understanding and measuring the impact of feedback loops in industrial recommender systems is challenging, leading to the underestimation of their deterioration. In this study, we define open and closed feedback loops and investigate the unique reasons behind the emergence of feedback loops in the industry, drawing from real-world examples that have received limited attention in prior research. We highlight the measurement challenges associated with capturing the full impact of feedback loops using traditional online A/B tests. To address this, we propose the use of offline evaluation frameworks as surrogates for long-term feedback loop bias, supported by a practical simulation system using real data. Our findings provide valuable insights for optimizing the performance of recommender systems operating under feedback loop conditions.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对工业推荐系统中反馈循环的影响难以测量且常被低估的问题展开研究。作者定义了开放和封闭反馈循环，并基于工业实际案例探讨了反馈循环产生的独特原因，这些原因在以往研究中关注不足。文章指出传统在线A/B测试在捕捉反馈循环长期影响方面的挑战，为此提出使用离线评估框架作为长期反馈循环偏差的替代指标，并构建了基于真实数据的实用模拟系统。研究结果为优化反馈循环条件下的推荐系统性能提供了有价值的见解。

### 主要创新

- 明确区分开放与封闭反馈循环，并给出定义。
- 从工业实践角度揭示反馈循环产生的独特原因，补充了以往研究的不足。
- 指出传统在线A/B测试在测量反馈循环长期影响上的局限性。
- 提出使用离线评估框架作为长期反馈循环偏差的替代指标。
- 构建基于真实数据的模拟系统，用于评估反馈循环影响。

### 研究方法

论文采用理论分析与工业实践相结合的方法。首先通过定义和分类反馈循环，结合工业案例剖析其成因；然后分析传统A/B测试的不足，提出离线评估框架；最后构建基于真实数据的模拟系统进行验证。

### 关键结果

论文的主要结果包括：明确了反馈循环在工业中的成因和影响；证明了传统在线A/B测试难以全面评估反馈循环的长期影响；提出的离线评估框架和模拟系统能够有效替代长期反馈循环偏差的测量。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 聚焦工业实践，案例真实，具有实际参考价值。
- 对反馈循环的定义和分类清晰，有助于理论构建。
- 提出离线评估框架，为长期影响测量提供新思路。
- 模拟系统基于真实数据，增强了结果的可信度。

### 主要局限

- 论文局限：摘要未提及具体实验细节和量化结果，可能缺乏实证支撑。当前证据局限：仅基于摘要，无法评估方法的具体实现和验证强度。

### 与当前研究方向的关联

论文与推荐系统、反馈循环、工业落地、评估方法等关键词高度相关，涉及推荐系统的鲁棒性和长期性能优化，与因果性、公平性也有潜在关联。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：related_to_seed
- **seed_paper_id**：https://doi.org/10.1145/3726302.3729972
- **seed_title**：Exploring the Escalation of Source Bias in User, Data, and Recommender System Feedback Loop
- **seed_score**：83.0

</details>

---

_知识库更新时间：2026-08-08T02:39:38.053871_
