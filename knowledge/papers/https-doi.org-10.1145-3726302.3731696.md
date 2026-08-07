---
title: "导航大型语言模型用于推荐：从架构到学习范式与部署"
paper_id: "https://doi.org/10.1145/3726302.3731696"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 99.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Recommender Systems and Techniques", "Natural Language Processing Techniques"]
---

# 导航大型语言模型用于推荐：从架构到学习范式与部署

> **英文原标题**：Navigating Large Language Models for Recommendation: From Architecture to Learning Paradigms and Deployment

[查看原文](https://dblp.org/rec/conf/sigir/0001BZ00F25)

## 一句话结论

> 该论文系统综述了LLM4Rec的技术栈，涵盖架构设计、预训练/后训练、推理和部署，并讨论了用户建模、可信度和评估等挑战，旨在为LLM在推荐系统中的应用提供全面指导。

## 论文信息

- **作者**：Xinyu Lin, Keqin Bao, Jizhi Zhang, Yang Zhang, Wenjie Wang, Fuli Feng
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：99.0
- **DOI**：[https://doi.org/10.1145/3726302.3731696](https://doi.org/10.1145/3726302.3731696)

<details open>
<summary><strong>中文摘要</strong></summary>

大型语言模型（LLMs）正在重塑推荐系统的格局，催生了吸引学术界和工业界关注的新兴领域LLM4Rec。与早期仅从语言模型中借用模型架构或学习范式的方法不同，近期进展已催生了一套专门且不断演进的LLM4Rec技术栈，涵盖架构设计、预训练与后训练策略、推理技术以及实际部署。本教程通过该技术栈的视角，对LLM4Rec进行了系统而深入的概述。我们将探讨LLMs如何在各个阶段被适配到推荐任务中，赋予其推理、规划及上下文学习等能力。此外，我们还将强调实际挑战，包括复杂用户建模、可信赖性及评估。通过提炼近期研究的见解并识别开放问题，本教程旨在帮助参与者全面理解LLM4Rec，并激发这一快速演进领域中的持续创新。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models (LLMs) are reshaping the landscape of recommender systems, giving rise to the emerging field of LLM4Rec that attracts both academia and industry. Unlike earlier approaches that simply borrowed model architectures or learning paradigms from language models, recent advances have led to a dedicated and evolving technical stack for LLM4Rec, spanning architecture design, pre-training and post-training strategies, inference techniques, and real-world deployment. This tutorial offers a systematic and in-depth overview of LLM4Rec through the lens of this technical stack. We will examine how LLMs are being adapted to recommendation tasks across different stages, empowering them with capabilities such reasoning, planning, and in-context learning. Moreover, we will highlight practical challenges including complex user modeling, trustworthiness, and evaluation. Distilling insights from recent research and identifying open problems, this tutorial aims to equip participants with a comprehensive understanding of LLM4Rec and inspire continued innovation in this rapidly evolving field.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文是一篇关于大型语言模型（LLM）在推荐系统中应用的教程性综述，提出了LLM4Rec这一新兴领域。文章指出，与早期简单借用语言模型架构或学习范式的方法不同，近期进展催生了一套专门且不断演进的技术栈，涵盖架构设计、预训练与后训练策略、推理技术以及实际部署。该教程通过技术栈的视角，系统深入地概述了LLM4Rec，探讨了LLM如何在不同阶段被适配到推荐任务，赋予其推理、规划、上下文学习等能力。同时，文章强调了实际挑战，包括复杂用户建模、可信赖性和评估。通过提炼近期研究的见解并指出开放问题，本教程旨在帮助参与者全面理解LLM4Rec，并激发该快速演进领域的持续创新。

### 主要创新

- 提出从技术栈视角系统梳理LLM4Rec，涵盖架构、预训练/后训练、推理和部署。
- 强调LLM在推荐中的推理、规划和上下文学习能力，区别于早期简单借用。
- 指出实际挑战如复杂用户建模、可信赖性和评估，并识别开放问题。

### 研究方法

本文为教程性综述，采用技术栈框架，从架构设计、预训练与后训练策略、推理技术和部署四个层面分析LLM4Rec，并讨论其在不同推荐阶段的应用及面临的挑战。

### 关键结果

摘要未提供具体实验数据或结果，但指出LLM4Rec已形成专门技术栈，并面临复杂用户建模、可信赖性和评估等挑战。

### 技术栈

- 摘要未提供具体算法、工具或数学方法，但提及技术栈包括架构设计、预训练与后训练策略、推理技术和部署。

### 方法优势

- 系统性强，从技术栈角度全面覆盖LLM4Rec的多个层面。
- 关注实际部署和挑战，具有实践指导意义。
- 强调LLM的推理、规划和上下文学习能力，突出新范式。

### 主要局限

- 论文局限：作为教程，可能缺乏深度实验验证；当前证据局限：仅基于摘要，无法评估具体方法细节和实证结果。

### 与当前研究方向的关联

高度相关：论文聚焦LLM与推荐系统结合（LLM4Rec），涉及序列推荐、生成式推荐、推荐智能体、对话式推荐、用户建模、排序与重排、CTR/CVR预测等关键词，并讨论因果性、公平性、鲁棒性和工业落地。

---

_知识库更新时间：2026-08-07T03:44:30.772542_
