---
title: "基于画像感知的LLM评判器评估播客推荐"
paper_id: "https://doi.org/10.1145/3705328.3759305"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 69.0
tags: ["paper", "recommender-systems", "Video Analysis and Summarization", "Web Data Mining and Analysis"]
---

# 基于画像感知的LLM评判器评估播客推荐

> **英文原标题**：Evaluating Podcast Recommendations with Profile-Aware LLM-as-a-Judge

[查看原文](https://dblp.org/rec/conf/recsys/FabbriPDWNDGDSL25) · [ArXiv](https://arxiv.org/abs/2508.08777)

## 一句话结论

> 本文提出一种基于用户画像的LLM评判框架，用于离线评估播客推荐质量，实验表明其与人类判断高度一致，优于使用原始收听历史的方法。

## 论文信息

- **作者**：Francesco Fabbri, Gustavo Penha, Edoardo D’Amico, Alice Wang, Marco De Nadai, Jackie Doremus, Paul Gigioli, Andreas Damianou, Oskar Stål, Mounia Lalmas
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：69.0
- **DOI**：[https://doi.org/10.1145/3705328.3759305](https://doi.org/10.1145/3705328.3759305)

<details open>
<summary><strong>中文摘要</strong></summary>

评估个性化推荐仍是一项核心挑战，尤其是在播客等长格式音频领域中，传统离线指标存在曝光偏差，而在线方法如A/B测试成本高昂且受运营条件限制。在本文中，我们提出了一种新颖的框架，利用大语言模型（LLMs）作为离线评判者，以可扩展且可解释的方式评估播客推荐质量。我们的两阶段画像感知方法首先从90天的收听历史中提炼出自然语言用户画像。这些画像既概括了主题兴趣，也总结了行为模式，作为用户偏好的紧凑且可解释的表示。我们并非用原始数据直接提示LLM，而是利用这些画像提供高层次、语义丰富的上下文，使LLM能够更有效地推理用户兴趣与推荐单集之间的匹配程度。这降低了输入复杂度并提升了可解释性。随后，LLM被提示基于画像与单集的匹配度给出细粒度的逐点判断和成对判断。在一项包含47名参与者的受控研究中，我们的画像感知评判者与人类判断高度一致，并且优于或等同于使用原始收听历史的变体。该框架为推荐系统中的迭代测试和模型选择提供了高效、画像感知的评估途径。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Evaluating personalized recommendations remains a central challenge, especially in long-form audio domains like podcasts, where traditional offline metrics suffer from exposure bias and online methods such as A/B testing are costly and operationally constrained. In this paper, we propose a novel framework that leverages Large Language Models (LLMs) as offline judges to assess the quality of podcast recommendations in a scalable and interpretable manner. Our two-stage profile-aware approach first constructs natural-language user profiles distilled from 90 days of listening history. These profiles summarize both topical interests and behavioral patterns, serving as compact, interpretable representations of user preferences. Rather than prompting the LLM with raw data, we use these profiles to provide high-level, semantically rich context-enabling the LLM to reason more effectively about alignment between a user's interests and recommended episodes. This reduces input complexity and improves interpretability. The LLM is then prompted to deliver fine-grained pointwise and pairwise judgments based on the profile-episode match. In a controlled study with 47 participants, our profile-aware judge matched human judgments with high fidelity and outperformed or matched a variant using raw listening histories. The framework enables efficient, profile-aware evaluation for iterative testing and model selection in recommender systems.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出了一种利用大型语言模型作为离线评判器来评估个性化播客推荐质量的新框架。该框架首先从用户90天的收听历史中自动构建自然语言用户画像，概括其主题兴趣和行为模式，作为用户偏好的紧凑、可解释表示。然后，LLM基于该画像和候选节目元数据进行推理，提供细粒度的点式和成对判断。在47名参与者的受控实验中，该画像感知评判器与人类判断高度一致，并优于或匹配使用原始收听历史的变体。该框架支持高效、可解释的离线评估，用于推荐系统的迭代测试和模型选择。

### 主要创新

- 提出了一种新颖的画像感知LLM评判器框架，用于离线评估个性化播客推荐。
- 自动从收听历史中构建自然语言用户画像，作为显式的内容假设，提供高层次的语义上下文。
- 支持点式和成对两种评估模式，分别用于评估单个节目和比较两个推荐模型。
- 实验表明，画像感知评判器在模型级比较中优于基于原始历史的变体，并具有较高的召回率。

### 研究方法

该框架包括两个阶段：用户画像生成和节目评估。首先，使用LLM从用户最近三个月的收听历史中生成结构化画像，包含内容偏好和收听模式等维度。然后，在零样本设置下，使用LLM作为评判器，输入画像和节目元数据，通过思维链推理生成理由和二元判断（点式评估）。对于模型级比较，评判器比较两个推荐列表，输出维度级理由和最终偏好（成对评估）。实验采用GPT-4.1，与47名用户的人类标注进行比较。

### 关键结果

实验结果显示，LaaJ-Profile在点式评估中的ROC-AUC为0.6442，模型级评估的MSA为0.6596，RSM为0.6667。与LaaJ-History相比，模型级MSA更高（0.6596 vs 0.6170）。混淆矩阵显示，点式评估中75%的案例与人类一致，但存在17%的假阳性；模型级评估中，LLM倾向于更果断，只有1次平局，而人类有8次。增加画像中使用的节目数量可提高准确率（从5个节目的0.51提升到20个节目的0.59）。

### 技术栈

- GPT-4.1
- LLM-as-a-Judge
- Chain-of-Thought
- Sentence-BERT
- ROC-AUC
- MSA
- RSM

### 方法优势

- 提出了一种可扩展、可解释的离线评估方法，填补了传统离线指标和在线实验之间的空白。
- 用户画像作为内容假设，提高了LLM推理的准确性和可解释性。
- 实验设计严谨，包括人类评估和多种基线比较。
- 揭示了LLM评判器的偏差（如正向偏差和果断性），为未来改进提供了方向。

### 主要局限

- LLM评判器存在正向偏差，倾向于将节目判断为对齐。
- LLM在模型级比较中过于果断，很少给出平局。
- 用户画像可能无法捕捉深层兴趣，受限于近期收听历史。
- 实验规模较小（47名参与者），且未考虑偏差缓解和提示鲁棒性。

### 与当前研究方向的关联

该论文与LLM与推荐系统结合、用户建模、推荐评估等关键词高度相关。它利用LLM作为评判器，通过用户画像进行个性化评估，属于生成式推荐和用户建模的交叉领域。同时，它关注离线评估方法，对推荐系统的工业落地具有参考价值。

## 代码与复现

- [atimothee/llm-as-a-judge](https://github.com/atimothee/llm-as-a-judge)：likely，置信度 69，Stars 0

---

_知识库更新时间：2026-08-06T03:55:25.390847_
