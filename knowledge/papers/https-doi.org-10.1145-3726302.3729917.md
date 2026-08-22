---
title: "LLMs能否提升推荐系统的公平性？一种数据增强方法"
paper_id: "https://doi.org/10.1145/3726302.3729917"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 58.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Privacy-Preserving Technologies in Data", "Customer churn and segmentation"]
---

# LLMs能否提升推荐系统的公平性？一种数据增强方法

> **英文原标题**：Can LLMs Enhance Fairness in Recommendation Systems? A Data Augmentation Approach

[查看原文](https://dblp.org/rec/conf/sigir/0001S00G25) · [Semantic Scholar](https://www.semanticscholar.org/paper/42bf5db247cbfef358a47a474add136ccceed1cc)

## 一句话结论

> 本文提出利用LLM通过数据增强提升推荐系统的公平性，在真实数据集上验证了方法在推荐性能、公平性和鲁棒性上的优势。

## 论文信息

- **作者**：Hanzhe Li, Dazhong Shen, Chao Wang, Yuting Liu, Jingjing Gu
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：58.0
- **DOI**：[https://doi.org/10.1145/3726302.3729917](https://doi.org/10.1145/3726302.3729917)

<details open>
<summary><strong>中文摘要</strong></summary>

尽管推荐系统（RS）在提供满足用户需求的个性化服务方面发挥着至关重要的作用，但近年来用户公平性问题日益凸显，尤其是由用户敏感属性引发的差异化对待。这不仅损害了用户体验和平台收益，还可能导致潜在的社会不公。尽管已有许多公平感知方法被开发并取得了一定成功，但其中许多方法在过滤敏感属性信息的同时，忽略了个性化信息的潜在损失，从而导致次优结果。大语言模型（LLMs）已在各种任务中展现出卓越的能力，但其在公平感知推荐中的潜力仍有待进一步探索。在本文中，我们提出了一种新的公平感知推荐系统探索方法，通过向大语言模型提示用户的个性化公平程度，以增强公平的用户-物品交互数据用于训练。具体而言，为了估计每个用户的公平程度，我们首先设计了一个个性化不公平建模模块，该模块包含一个可替换的公平感知表示学习模型。此外，为了使大语言模型能够从语义信息中感知公平性并适应各种场景，我们提出了一种提示调优机制，以优化用户共享的提示模板，其目标是最小化与用户偏好的一致性损失并最大化增强数据的多样性。最后，我们利用大语言模型使用最优提示增强公平交互数据，并将其与原始数据整合以重新训练推荐模型。在两个真实数据集上的大量实验表明，我们的方法在推荐性能、公平性和鲁棒性方面均具有优越性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Despite the vital role of recommendation systems (RS) in delivering personalized services tailored to users' needs, user fairness issues have increasingly emerged in recent years, especially differentiated treatments caused by user sensitive attributes. This not only undermines both user experience and platform revenues, but also leads to potential social unfairness. Although many fairness-aware methods have been developed and achieved some success, many of them filter out sensitive attribute information while ignoring the potential loss of personalized information, leading to suboptimal results. Large language models (LLMs) have demonstrated remarkable capabilities across various tasks, while their potential in fairness-aware recommendation remains further unexplored. In this paper, we propose a new exploration of fairness-aware RS by prompting LLMs with the user's personalized fairness degrees to augment fair user-item interaction for training. Specifically, to estimate the fairness degree of each user, we first design a personalized unfairness modelling module, consisting of a replaceable fairness-aware representation learning model. Moreover, to enable LLMs to perceive fairness from semantic information and adapt to various scenarios, we propose a prompt tuning mechanism to optimize user-shared prompt templates with the objective of maximizing the consistency with users' preferences and the diversity of augmented data. Finally, we utilize LLMs to augment fair interaction data with the optimal prompts and integrate it with the raw data to re-train the recommendation model. Extensive experiments on two real-world datasets demonstrate the superiority of our approach in terms of recommendation performance, fairness, and robustness.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

推荐系统在提供个性化服务的同时，因用户敏感属性导致的差异化对待引发了公平性问题，损害用户体验和平台收益。现有公平性方法常过滤敏感属性信息，忽略个性化信息损失，效果欠佳。大型语言模型（LLMs）在多种任务中表现优异，但在公平性推荐中的潜力尚未充分探索。本文提出一种新方法，通过提示LLMs用户个性化公平度来增强公平的用户-物品交互数据，用于训练。具体包括：设计个性化不公平建模模块，估计用户公平度；提出提示调优机制，优化用户共享提示模板，以最大化与用户偏好的一致性及增强数据的多样性；最后利用LLMs生成公平交互数据，与原始数据整合重训练推荐模型。在两个真实数据集上的实验表明，该方法在推荐性能、公平性和鲁棒性方面均优于现有方法。

### 主要创新

- 提出利用LLMs增强公平交互数据的新框架，将用户个性化公平度融入提示中。
- 设计可替换的公平感知表示学习模型，用于估计用户不公平程度。
- 提出提示调优机制，优化用户共享提示模板，以平衡用户偏好一致性和数据多样性。
- 通过数据增强方式，在保留个性化信息的同时提升公平性，避免简单过滤敏感属性。

### 研究方法

论文采用数据增强方法，分为三步：首先，设计个性化不公平建模模块，使用可替换的公平感知表示学习模型估计每个用户的公平度；其次，提出提示调优机制，优化用户共享的提示模板，目标函数最大化与用户偏好的一致性及增强数据的多样性；最后，利用LLMs根据最优提示生成公平的用户-物品交互数据，并与原始数据整合，重新训练推荐模型。实验在两个真实数据集上进行，评估推荐性能、公平性和鲁棒性。

### 关键结果

在两个真实数据集上的实验表明，该方法在推荐性能、公平性和鲁棒性方面均优于现有方法。具体数值摘要未提供。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。但涉及大型语言模型（LLMs）、提示调优（prompt tuning）、公平感知表示学习模型、数据增强技术。

### 方法优势

- 创新性地将LLMs应用于公平性推荐，通过数据增强方式解决公平性问题。
- 提出个性化不公平建模，可替换的表示学习模型增强了灵活性。
- 提示调优机制平衡了用户偏好和数据多样性，提高增强数据的质量。
- 实验验证了方法在推荐性能、公平性和鲁棒性上的优越性。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法在真实场景中的计算成本、对LLM的依赖、以及在不同领域或更大规模数据上的泛化能力。

### 与当前研究方向的关联

论文与关键词高度相关：聚焦推荐系统公平性，属于推荐系统鲁棒性/公平性研究；利用LLMs增强数据，涉及LLM与推荐系统结合；方法包括用户建模和个性化，与用户建模相关；实验验证了推荐性能，与CTR/CVR预测相关（但摘要未明确）。

---

_知识库更新时间：2026-08-22T02:17:50.833991_
