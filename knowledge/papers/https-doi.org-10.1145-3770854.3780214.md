---
title: "TAMEing Long Contexts in Personalization: Towards Training-Free and State-Aware MLLM Personalized Assistant"
paper_id: "https://doi.org/10.1145/3770854.3780214"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 25.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Multimodal Machine Learning Applications", "Speech and dialogue systems"]
---

# TAMEing Long Contexts in Personalization: Towards Training-Free and State-Aware MLLM Personalized Assistant

[查看原文](https://dblp.org/rec/conf/kdd/HongLZWZ26) · [ArXiv](https://arxiv.org/abs/2512.21616)

## 一句话结论

> 该论文提出了LCMP基准和TAME框架，用于评估和提升多模态大语言模型在长上下文个性化对话中的能力，通过训练无关的状态感知方法实现更好的个性化交互。

## 论文信息

- **作者**：Rongpei Hong, Jian Lang, Ting Zhong, Yong Wang, Fan Zhou
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：25.0
- **DOI**：[https://doi.org/10.1145/3770854.3780214](https://doi.org/10.1145/3770854.3780214)

<details open>
<summary><strong>中文摘要</strong></summary>

多模态大语言模型（MLLM）个性化是一个关键的研究问题，旨在促进针对特定实体（称为个性化概念）的个性化对话。然而，现有方法和基准主要关注对个性化概念的简单、上下文无关的视觉识别和文本替换（例如，“一只黄色的小狗” -> “你的小狗Mochi”），忽视了支持长上下文对话的能力。一个理想的个性化MLLM助手应当能够与人类进行长上下文对话，并通过从过去的对话历史中学习来持续提升其体验质量。为弥补这一空白，我们提出了LCMP，这是首个长上下文MLLM个性化评估基准。LCMP评估了MLLM在感知个性化概念变化以及生成反映这些变化的上下文适当个性化响应方面的能力。作为LCMP的强基线，我们引入了一种新颖的免训练且状态感知的框架TAME。TAME赋予MLLM双重记忆，以差异化方式管理每个个性化概念的时间性变化和持续性变化。此外，TAME还纳入了一种新的免训练检索-对齐增强生成（RA2G）范式。RA2G引入了一个对齐步骤，从多记忆检索到的知识中提取与当前问题上下文匹配的信息，从而实现对复杂真实世界用户查询的更好交互。在LCMP上的实验表明，TAME取得了最佳性能，展示了在长上下文场景中显著且不断演进的交互体验。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multimodal Large Language Model (MLLM) Personalization is a critical research problem that facilitates personalized dialogues with MLLMs targeting specific entities (known as personalized concepts). However, existing methods and benchmarks focus on the simple, context-agnostic visual identification and textual replacement of the personalized concept (e.g., "A yellow puppy" -> "Your puppy Mochi"), overlooking the ability to support long-context conversations. An ideal personalized MLLM assistant is capable of engaging in long-context dialogues with humans and continually improving its experience quality by learning from past dialogue histories. To bridge this gap, we propose LCMP, the first Long-Context MLLM Personalization evaluation benchmark. LCMP assesses the capability of MLLMs in perceiving variations of personalized concepts and generating contextually appropriate personalized responses that reflect these variations. As a strong baseline for LCMP, we introduce a novel training-free and state-aware framework TAME. TAME endows MLLMs with double memories to manage the temporal and persistent variations of each personalized concept in a differentiated manner. In addition, TAME incorporates a new training-free Retrieve-then-Align Augmented Generation (RA2G) paradigm. RA2G introduces an alignment step to extract the contextually fitted information from the multi-memory retrieved knowledge to the current questions, enabling better interactions for complex real-world user queries. Experiments on LCMP demonstrate that TAME achieves the best performance, showcasing remarkable and evolving interaction experiences in long-context scenarios.

</details>

---

_知识库更新时间：2026-08-02T04:11:29.701564_
