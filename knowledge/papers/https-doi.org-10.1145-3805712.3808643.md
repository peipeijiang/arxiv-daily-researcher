---
title: "多智能体推荐系统：基础、视角及大规模电子商务部署的经验教训"
paper_id: "https://doi.org/10.1145/3805712.3808643"
source: "citation"
published: "2026-07-10T00:00:00"
score: 98.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Multi-Agent Systems and Negotiation", "Explainable Artificial Intelligence (XAI)"]
---

# 多智能体推荐系统：基础、视角及大规模电子商务部署的经验教训

> **英文原标题**：Multi-Agentic Recommender Systems: Foundations, Perspectives, and Lessons from Large Scale Deployments in eCommerce

[查看原文](https://doi.org/10.1145/3805712.3808643)

## 一句话结论

> 该教程系统介绍了基于LLM和多智能体编排的推荐系统的基础、设计模式及大规模电商部署经验，旨在为构建和部署智能体推荐系统提供实践指导。

## 论文信息

- **作者**：Reza Yousefi Maragheh, Yashar Deldjoo, Benjamin Coleman, Jason Cho, Chi Wang
- **来源**：Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval
- **发布时间**：2026-07-10
- **相关度评分**：98.0
- **DOI**：[https://doi.org/10.1145/3805712.3808643](https://doi.org/10.1145/3805712.3808643)

<details open>
<summary><strong>中文摘要</strong></summary>

本教程涵盖多智能体推荐系统的相关主题——即通过大语言模型（LLMs）与多智能体编排增强的推荐系统，以实现多步推理、工具调用和交互式决策。教程重点介绍基础概念、可复用的设计模式，以及从大规模电子商务部署中获得的实践经验。具体而言，我们首先回顾生成式推荐系统的背景与最新趋势，并探讨其与智能体方法的联系。随后，我们调研工业界的主要部署领域，并综述为支持这些领域而开发的智能体编排框架。最后，我们通过一个项目案例，完整梳理智能体推荐系统的全生命周期，从范围界定、数据定义，到建模、部署与监控，以提供可操作的部署洞见。本教程融合了信息检索（IR）、推荐系统（RecSys）和大规模工业实践的视角。配套资料可在 agenticrecsys.github.io 获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

This tutorial covers topics on multi-agentic recommender systems — recommender systems augmented with Large Language Models (LLMs) and multi-agent orchestration to enable multi-step reasoning, tool use, and interactive decision-making. The tutorial emphasizes foundational concepts, reusable design patterns, and practical lessons learned from large-scale e-commerce deployments. Specifically, we first cover background and recent trends in generative recommender systems and their connection to agentic approaches. We then survey major deployment areas in industry and review the agent orchestration frameworks developed to support them. Finally, we present a project walkthrough that traces the full lifecycle of an agentic recommender system, from scoping and data definition through modeling, deployment, and monitoring, to provide actionable deployment insights. The tutorial bridges perspectives from information retrieval (IR), recommender systems (RecSys), and large-scale industrial practice. The accompanying material can be found at agenticrecsys.github.io.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本教程涵盖了多智能体推荐系统的主题，即通过大语言模型和多智能体编排增强的推荐系统，以实现多步推理、工具使用和交互式决策。教程强调了基础概念、可复用的设计模式以及从大规模电子商务部署中获得的实践经验。具体而言，首先介绍了生成式推荐系统的背景和最新趋势及其与智能体方法的联系，然后调查了行业中的主要部署领域，并回顾了支持这些领域的智能体编排框架。最后，通过一个项目演练，追踪了智能体推荐系统的完整生命周期，从范围界定和数据定义到建模、部署和监控，以提供可操作的部署见解。教程弥合了信息检索、推荐系统和大规模工业实践之间的视角。配套材料可在agenticrecsys.github.io获取。

### 主要创新

- 提出了多智能体推荐系统的综合教程，涵盖基础、视角和部署经验。
- 强调了可复用的设计模式和实际部署中的经验教训。
- 提供了从范围界定到监控的完整生命周期项目演练。
- 弥合了信息检索、推荐系统和大规模工业实践之间的差距。

### 研究方法

教程采用综述和案例研究的方法，首先介绍生成式推荐系统的背景和趋势，然后调查工业部署领域和智能体编排框架，最后通过项目演练展示智能体推荐系统的完整生命周期。

### 关键结果

摘要未提供具体实验结果，但强调了教程内容涵盖基础概念、设计模式、部署领域、编排框架和生命周期管理。

### 技术栈

- 摘要提及大语言模型、多智能体编排、工具使用，但未提供具体算法、工具或数学方法。

### 方法优势

- 提供了多智能体推荐系统的全面概述，涵盖基础、视角和部署。
- 强调了实际部署中的经验教训，具有实践指导意义。
- 通过项目演练展示了完整生命周期，有助于理解落地过程。
- 弥合了学术研究与工业实践之间的差距。

### 主要局限

- 论文局限：摘要未提及具体实验或评估，可能缺乏实证支持。当前证据局限：仅基于摘要，无法评估方法的细节和有效性。

### 与当前研究方向的关联

该教程与推荐系统、LLM与推荐系统结合、推荐智能体、工业落地等关键词高度相关，但未涉及序列推荐、多模态推荐、因果性等具体方向。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3726302.3731696
- **seed_title**：Navigating Large Language Models for Recommendation: From Architecture to Learning Paradigms and Deployment
- **seed_score**：99.0

</details>

---

_知识库更新时间：2026-08-08T02:39:38.053146_
