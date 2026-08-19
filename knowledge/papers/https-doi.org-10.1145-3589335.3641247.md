---
title: "大型语言模型用于推荐：进展与未来方向"
paper_id: "https://doi.org/10.1145/3589335.3641247"
source: "citation"
published: "2024-05-12T00:00:00"
score: 95.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# 大型语言模型用于推荐：进展与未来方向

> **英文原标题**：Large Language Models for Recommendation: Progresses and Future Directions

[查看原文](https://doi.org/10.1145/3589335.3641247)

## 一句话结论

> 该论文综述了LLM在推荐系统中的应用进展，探讨了LLM如何推动推荐系统在架构、学习范式和能力上的发展，并指出了该领域面临的挑战和未来方向。

## 论文信息

- **作者**：Jizhi Zhang, Keqin Bao, Yang Zhang, Wenjie Wang, Fuli Feng, Xiangnan He
- **来源**：Companion Proceedings of the ACM Web Conference 2024
- **发布时间**：2024-05-12
- **相关度评分**：95.0
- **DOI**：[https://doi.org/10.1145/3589335.3641247](https://doi.org/10.1145/3589335.3641247)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型（LLMs）已对推荐系统产生了显著影响。学术界和工业界对开发用于推荐目的的大语言模型兴趣日益浓厚，这种方法通常被称为LLM4Rec。相关努力包括利用大语言模型进行生成式物品检索和排序，以及可能为各种推荐任务创建通用大语言模型，这标志着推荐系统可能迎来范式转变。本教程旨在回顾LLM4Rec的发展历程，并对当前主流研究进行深入分析。我们将讨论大语言模型如何在模型架构、学习范式以及对话、泛化、规划和内容生成等能力方面推动推荐系统的进步。此外，本教程还将重点介绍这一新兴领域中的开放问题和挑战，涉及可信度、效率、在线训练和推荐数据建模等相关关切。最后，本教程将总结以往研究的要点，并为未来研究提出建议方向。我们的目标是帮助受众掌握LLM4Rec的发展动态，并激发进一步研究的灵感。通过此举，我们期望为LLM4Rec的成长与成功做出贡献，并可能推动推荐范式的根本性变革。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large language models (LLMs) have significantly influenced recommender systems. Both academia and industry have shown growing interest in developing LLMs for recommendation purposes, an approach commonly referred to as LLM4Rec. This involves efforts such as utilizing LLMs for generative item retrieval and ranking, along with the potential for creating universal LLMs for varied recommendation tasks, signaling a possible paradigm shift in recommender systems. This tutorial is designed to review the progression of LLM4Rec and provide an in-depth analysis of the prevailing studies. We will discuss how LLMs advance recommender systems in model architecture, learning paradigms, and capabilities like conversation, generalization, planning, and content generation. Additionally, the tutorial will highlight open problems and challenges in this nascent field, addressing concerns related to trustworthiness, efficiency, online training, and recommendation data modeling. Concluding with a summary of the takeaways from previous research, the tutorial will suggest avenues for future investigations. Our aim is to help the audience grasp the developments in LLM4Rec, as well as to spark inspiration for further research. By doing so, we expect to contribute to the growth and success of LLM4Rec, possibly leading to a fundamental change in recommender paradigms.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文是一篇关于大型语言模型（LLMs）在推荐系统中应用的综述性教程。文章指出，LLMs在推荐系统领域引起了广泛关注，学术界和工业界都致力于开发基于LLM的推荐方法（LLM4Rec），包括利用LLM进行生成式物品检索和排序，以及构建通用LLM以处理多种推荐任务，这可能标志着推荐系统范式的转变。本教程旨在回顾LLM4Rec的发展历程，深入分析现有研究，讨论LLM如何在模型架构、学习范式以及对话、泛化、规划、内容生成等能力方面推动推荐系统的进步。同时，文章还指出了该新兴领域面临的开放问题和挑战，如可信度、效率、在线训练和推荐数据建模等。最后，教程总结了以往研究的要点，并为未来研究提出了方向，以帮助读者理解LLM4Rec的发展，并激发进一步研究，期望为推荐范式的根本性变革做出贡献。

### 主要创新

- 提出LLM4Rec概念，系统梳理LLM在推荐系统中的应用进展。
- 从模型架构、学习范式和能力（如对话、泛化、规划、内容生成）多维度分析LLM对推荐系统的提升。
- 指出LLM可能引发推荐系统范式转变，从传统方法转向生成式检索和排序。
- 探讨了通用LLM用于多种推荐任务的潜力。
- 识别了LLM4Rec中的开放问题和挑战，如可信度、效率、在线训练和数据建模。

### 研究方法

本文为综述性教程，采用文献回顾和定性分析的方法，对LLM4Rec领域的研究进展进行系统梳理和总结，并基于现有研究提出未来研究方向。

### 关键结果

LLM在推荐系统中展现出巨大潜力，尤其在生成式物品检索和排序方面。；LLM能够增强推荐系统的对话、泛化、规划和内容生成能力。；LLM4Rec面临可信度、效率、在线训练和数据建模等挑战。；LLM4Rec可能引发推荐系统范式的根本性变革。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 全面综述了LLM4Rec的进展，涵盖多个维度。
- 指出了LLM对推荐系统的潜在范式转变影响。
- 明确了当前面临的挑战和未来研究方向。
- 适合作为教程，帮助读者快速了解领域。

### 主要局限

- 论文局限：作为综述，未提供具体实验验证；当前证据局限：仅基于摘要，无法评估具体方法细节和实证结果。

### 与当前研究方向的关联

高度相关：论文主题直接涉及LLM与推荐系统的结合，涵盖生成式推荐、对话式推荐、用户建模等关键词，并讨论了推荐系统的可信度、效率等工业落地问题。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3705328.3748007
- **seed_title**：A Tutorial on Agentic LLM for Recommender Systems
- **seed_score**：97.0

</details>

---

_知识库更新时间：2026-08-19T02:19:07.185801_
