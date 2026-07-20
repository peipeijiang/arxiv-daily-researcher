---
title: "Advantage-Conditioned Flow Policy for Offline Reinforcement Learning in Recommendation"
paper_id: "https://doi.org/10.1145/3805712.3809626"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 33.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Emotion and Mood Recognition", "Explainable Artificial Intelligence (XAI)"]
---

# Advantage-Conditioned Flow Policy for Offline Reinforcement Learning in Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/ChenWY26) · [Semantic Scholar](https://www.semanticscholar.org/paper/bb64df95b09313046218e1c02fa744dcc8139fa3)

## 一句话结论

> 提出PerfRec，一种基于优势条件流策略的离线强化学习推荐框架，通过流匹配和优势条件蒸馏实现高效的一步策略，在多个基准数据集和模拟平台上优于现有方法。

## 论文信息

- **作者**：Xiaocong Chen, Siyu Wang, Lina Yao
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：33.0
- **DOI**：[https://doi.org/10.1145/3805712.3809626](https://doi.org/10.1145/3805712.3809626)

<details open>
<summary><strong>中文摘要</strong></summary>

离线强化学习（Offline Reinforcement Learning, RL）是推荐系统中一种有效的方法，因为它能够从记录的交互数据中优化长期用户反馈，而无需在线探索。其中一个关键挑战在于用户偏好的多模态特性：用户可能喜欢多种不相关的物品类型，因此单模态策略（例如高斯策略）往往会跨模态取平均，生成与任何兴趣都不匹配的动作。近年来基于扩散的策略能够建模复杂的偏好分布，但通常需要大量去噪步骤。我们提出PerfRec（偏好感知流推荐，Preference-aware Flow for Recommendation），这是一种流匹配离线强化学习框架，能够学习表达力强的行为策略，并将其蒸馏为高效的单步策略。PerfRec（i）训练一个条件流模型来克隆记录的交互动作分布，（ii）利用从所学流策略中采样的下一动作训练双Q网络（twin Q-networks），以及（iii）训练一个优势条件单步策略，该策略通过Q引导（Q-guidance）进行改进，并通过蒸馏损失使其保持接近流策略。我们采用二元优势条件（binary advantage conditioning）来分离流诱导动作分布中的高优势区域和低优势区域，从而在推理时能够通过单次前向传递从高优势模式中采样。在五个基准数据集和一个在线模拟平台上的实验表明，PerfRec相较于强离线强化学习基线方法提升了推荐性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Offline reinforcement learning (RL) is a useful approach for recommender systems because it can optimize long-term user feedback from logged interaction data without online exploration. A key challenge is the multi-modal nature of user preferences: a user may like several unrelated item types, so a unimodal policy (for example, a Gaussian) tends to average across modes and generate actions that do not match any interest. Recent diffusion-based policies can model complex preference distributions, but they often require many denoising steps. We propose PerfRec (Preference-aware Flow for Recommendation), a flow-matching offline RL framework that learns an expressive behavioral policy and distills it into an efficient one-step policy. PerfRec (i) trains a conditional flow model to clone the logged action distribution, (ii) trains twin Q-networks using next actions sampled from the learned flow policy, and (iii) trains an advantage-conditioned one-step policy with Q-guidance for improvement and a distillation loss that keeps the policy close to the flow policy. We use binary advantage conditioning to separate high-advantage and low-advantage regions of the flow-induced action distribution, so that at inference we can sample from the high-advantage mode with a single forward pass. Experiments on five benchmark datasets and one online simulation platform show that PerfRec improves recommendation performance over strong offline RL baselines.

</details>

---

_知识库更新时间：2026-07-20T04:18:26.518300_
