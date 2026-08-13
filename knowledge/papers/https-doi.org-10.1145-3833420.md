---
title: "RosePO：基于LLM的推荐中的定制化偏好对齐"
paper_id: "https://doi.org/10.1145/3833420"
source: "citation"
published: "2026-08-11T00:00:00"
score: 81.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)", "Sentiment Analysis and Opinion Mining"]
---

# RosePO：基于LLM的推荐中的定制化偏好对齐

> **英文原标题**：RosePO: Customized Preference Alignment in LLM-Based Recommendation

[查看原文](https://doi.org/10.1145/3833420)

## 一句话结论

> 该论文提出RosePO框架，通过个性化平滑的成对偏好优化来改进基于LLM的推荐，有效缓解语义幻觉和流行度偏差，提升推荐性能。

## 论文信息

- **作者**：Jiayi Liao, Xiangnan He, Ruobing Xie, Jiancan Wu, Yancheng Yuan, Xingwu Sun, Zhanhui Kang, Jingru Duan, Wenyu Zang, Xiang Wang
- **来源**：ACM Transactions on Information Systems
- **发布时间**：2026-08-11
- **相关度评分**：81.0
- **DOI**：[https://doi.org/10.1145/3833420](https://doi.org/10.1145/3833420)

<details open>
<summary><strong>中文摘要</strong></summary>

大型语言模型（LLMs）的最新进展激发了其在序列推荐系统中的应用，通常通过监督微调（SFT）实现。然而，传统的SFT方法往往难以捕捉物品之间细微的比较关系。尽管近期方法采用了直接偏好优化（DPO），但在建模定制化偏好方面仍面临挑战，包括捕捉细粒度用户偏好以及易受语义幻觉和流行度偏差的影响。为克服这些挑战，我们提出了RosePO框架，一种通过个性化平滑的成对偏好优化来精炼基于LLM的推荐的方法。我们通过三个与基于LLM的推荐相关的关键偏好示例来说明这一概念。具体而言，我们针对每种定制化偏好设计了相应的拒绝采样策略。为确保对自动构建的偏好数据中不确定标签的鲁棒性，我们将由用户预言机预测的个性化平滑因子纳入优化目标。在三个真实世界数据集上的实证评估证明了我们方法的有效性，不仅展示了有前景的推荐性能，还缓解了语义幻觉和流行度偏差。我们希望这项工作为未来构建有益且无害的基于LLM的推荐服务铺平道路。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recent advancements in Large Language Models (LLMs) have inspired their application in sequential recommendation systems, often through supervised fine-tuning (SFT). However, conventional SFT methods often struggle to capture nuanced comparative relationships between items. While recent approaches utilize Direct Preference Optimization (DPO), they remain constrained by challenges in modeling customized preferences, including capturing fine-grained user preferences and being susceptible to semantic hallucination and popularity bias. To overcome these challenges, we propose RosePO, a framework to refine LLM-based recommendation through pairwise preference optimization with personalized smoothing. We illustrate the concept with three critical preference examples pertinent to LLM-based recommendation. Specifically, we design rejected sampling strategies tailored for each customized preference. To ensure robustness against uncertain labels present in automatically constructed preference data, we incorporate a personalized smoothing factor predicted by a user oracle into the optimization objective. Empirical evaluation on three real-world datasets demonstrates the effectiveness of our method, showcasing not only promising recommendation performance but also mitigation of semantic hallucination and popularity bias. We hope this work paves a way to build helpful and harmless LLM-based recommendation service in the future.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对基于大型语言模型（LLM）的序列推荐系统，指出现有监督微调（SFT）方法难以捕捉物品间的细微比较关系，而直接偏好优化（DPO）方法在建模定制化偏好时面临挑战，如难以捕捉细粒度用户偏好、易受语义幻觉和流行度偏差影响。为此，提出RosePO框架，通过成对偏好优化与个性化平滑来改进LLM推荐。文章阐述了三个关键的定制化偏好示例，并针对每种偏好设计了拒绝采样策略。为应对自动构建偏好数据中的不确定标签，在优化目标中引入由用户预言机预测的个性化平滑因子。在三个真实数据集上的实验表明，该方法不仅提升了推荐性能，还缓解了语义幻觉和流行度偏差。

### 主要创新

- 提出RosePO框架，将成对偏好优化与个性化平滑相结合，用于LLM推荐系统的定制化偏好对齐。
- 针对LLM推荐中的三种定制化偏好，设计了专门的拒绝采样策略。
- 引入个性化平滑因子，由用户预言机预测，以增强对自动构建偏好数据中不确定标签的鲁棒性。
- 实验证明该方法能缓解语义幻觉和流行度偏差，提升推荐性能。

### 研究方法

论文采用成对偏好优化方法，结合个性化平滑因子。具体地，针对三种定制化偏好设计拒绝采样策略，构建偏好数据。在优化目标中，引入由用户预言机预测的个性化平滑因子，以调整损失权重，从而处理不确定标签。在三个真实数据集上进行实验评估。

### 关键结果

在三个真实数据集上的实验表明，RosePO方法不仅取得了有前景的推荐性能，还缓解了语义幻觉和流行度偏差。

### 技术栈

- 摘要未提供具体技术栈，但涉及大型语言模型（LLM）、监督微调（SFT）、直接偏好优化（DPO）、成对偏好优化、拒绝采样、个性化平滑因子、用户预言机等概念。

### 方法优势

- 针对LLM推荐中的定制化偏好问题，提出了创新的优化框架。
- 设计了针对不同偏好类型的拒绝采样策略，具有针对性。
- 引入个性化平滑因子，增强了对噪声标签的鲁棒性。
- 实验验证了方法在推荐性能和缓解偏差方面的有效性。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：由于仅提供摘要，无法评估方法的计算复杂度、可扩展性、对超参数的敏感性等，也无法验证实验细节和统计显著性。

### 与当前研究方向的关联

该论文与关键词高度相关。它聚焦于LLM与推荐系统的结合，属于生成式推荐和序列推荐范畴；通过偏好优化进行用户建模，涉及排序与重排；同时关注推荐系统的鲁棒性（缓解语义幻觉和流行度偏差）。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-08-13T03:13:27.030878_
