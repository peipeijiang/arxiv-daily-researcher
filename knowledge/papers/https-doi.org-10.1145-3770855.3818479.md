---
title: "ScienceDB AI：面向大规模科学数据共享服务的LLM驱动智能体推荐系统"
paper_id: "https://doi.org/10.1145/3770855.3818479"
source: "citation"
published: "2026-08-06T00:00:00"
score: 88.0
tags: ["paper", "recommender-systems"]
---

# ScienceDB AI：面向大规模科学数据共享服务的LLM驱动智能体推荐系统

> **英文原标题**：ScienceDB AI: An LLM-Driven Agentic Recommender System for Large-Scale Scientific Data Sharing Services

[查看原文](https://doi.org/10.1145/3770855.3818479)

## 一句话结论

> 本文提出了ScienceDB AI，一个基于LLM的智能体推荐系统，通过对话和深度推理为大规模科学数据共享服务提供个性化推荐，离线指标提升超过30%，点击率提升超过200%。

## 论文信息

- **作者**：Qingqing Long, Haotian Chen, Chenyang Zhao, Xiaolei Du, Xuezhi Wang, Pengyao Wang, Chengzan Li, Yuanchun Zhou, Hengshu Zhu
- **来源**：Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2
- **发布时间**：2026-08-06
- **相关度评分**：88.0
- **DOI**：[https://doi.org/10.1145/3770855.3818479](https://doi.org/10.1145/3770855.3818479)

<details open>
<summary><strong>中文摘要</strong></summary>

AI for Science（AI4S）的快速发展凸显了科学数据集的重要性，促使众多国家科学数据中心和共享平台的建立。尽管取得了这些进展，如何高效促进数据集的共享与利用以服务于科学研究仍面临挑战。科学数据集蕴含复杂的领域特定知识与上下文，使得基于传统协同过滤的推荐系统难以胜任。大语言模型（LLMs）的最新进展为构建具备深度语义理解与个性化推荐能力的对话式智能体提供了前所未有的机遇。为此，我们提出了ScienceDB AI，一种新颖的由大语言模型驱动的智能体推荐系统，该系统基于全球最大的科学数据共享平台之一——科学数据银行（Science Data Bank, ScienceDB）开发。ScienceDB AI利用自然语言对话与深度推理，能够准确推荐与研究人员科学意图及不断变化的需求相匹配的数据集。该系统引入了多项创新：科学意图感知器（Scientific Intention Perceptor），用于从复杂查询中提取结构化实验要素；结构化记忆压缩器（Structured Memory Compressor），用于有效管理多轮对话；以及可信检索增强生成（Trustworthy Retrieval-Augmented Generation, Trustworthy RAG）框架。Trustworthy RAG采用两阶段检索机制，并通过可引用科学任务记录（Citable Scientific Task Record, CSTR）标识符提供可引用的数据集参考文献，从而增强推荐的可信度与可复现性。通过使用超过1000万个真实世界数据集进行的大量离线和在线实验，ScienceDB AI展现了显著的 effectiveness，在离线指标上相比先进基线方法提升了超过30%，在点击率上相比基于关键词的搜索引擎提升了超过200%。据我们所知，ScienceDB AI是首个专门针对大规模科学数据集共享服务量身定制的大语言模型驱动的对话式推荐系统，目前服务于来自90多个国家的数百万用户。该平台公开访问地址为：https://ai.scidb.cn/en。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

The rapid growth of AI for Science (AI4S) has underscored the significance of scientific datasets, leading to the establishment of numerous national scientific data centers and sharing platforms. Despite this progress, efficiently promoting dataset sharing and utilization for scientific research remains challenging. Scientific datasets contain intricate domain-specific knowledge and contexts, rendering traditional collaborative filtering-based recommenders inadequate. Recent advances in Large Language Models (LLMs) offer unprecedented opportunities to build conversational agents capable of deep semantic understanding and personalized recommendations. In response, we present ScienceDB AI, a novel LLM-driven agentic recommender system developed on Science Data Bank (ScienceDB), one of the largest global scientific data-sharing platforms. ScienceDB AI leverages natural language conversations and deep reasoning to accurately recommend datasets aligned with researchers' scientific intents and evolving requirements. The system introduces several innovations: a Scientific Intention Perceptor to extract structured experimental elements from complicated queries, a Structured Memory Compressor to manage multi-turn dialogues effectively, and a Trustworthy Retrieval-Augmented Generation (Trustworthy RAG) framework. The Trustworthy RAG employs a two-stage retrieval mechanism and provides citable dataset references via Citable Scientific Task Record (CSTR) identifiers, enhancing recommendation trustworthiness and reproducibility. Through extensive offline and online experiments using over 10 million real-world datasets, ScienceDB AI has demonstrated significant effectiveness, achieving more than 30% improvement in offline metrics compared to advanced baselines and an over 200% increase in click-through rates compared to keyword-based search engines. To our knowledge, ScienceDB AI is the first LLM-driven conversational recommender tailored explicitly for large-scale scientific dataset sharing services, which currently serves millions of users across more than 90 countries. The platform is publicly accessible at: https://ai.scidb.cn/en.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

随着AI for Science的快速发展，科学数据集的重要性日益凸显，但现有推荐系统难以处理科学数据的复杂领域知识。本文提出ScienceDB AI，一个基于大型语言模型的智能体推荐系统，部署于全球最大的科学数据共享平台之一Science Data Bank。该系统通过自然语言对话和深度推理，准确推荐符合研究者科学意图的数据集。其创新包括科学意图感知器、结构化记忆压缩器以及可信检索增强生成框架。离线与在线实验基于超过1000万真实数据集，相比先进基线离线指标提升超过30%，点击率相比关键词搜索提升超过200%。ScienceDB AI是首个面向大规模科学数据共享服务的LLM驱动对话式推荐系统，已服务90多个国家的数百万用户。

### 主要创新

- 提出科学意图感知器，从复杂查询中提取结构化实验要素。
- 设计结构化记忆压缩器，有效管理多轮对话。
- 构建可信检索增强生成框架，采用两阶段检索机制。
- 通过CSTR标识符提供可引用的数据集参考，增强推荐可信度和可复现性。
- 首个专门为大规模科学数据共享服务设计的LLM驱动对话式推荐系统。

### 研究方法

论文采用LLM驱动的智能体推荐系统方法，结合自然语言对话和深度推理。系统包含科学意图感知器用于解析用户查询，结构化记忆压缩器用于管理对话历史，以及可信检索增强生成框架，该框架采用两阶段检索机制并利用CSTR标识符提供可引用参考。通过离线实验和在线实验评估系统性能。

### 关键结果

离线指标相比先进基线提升超过30%；在线点击率相比关键词搜索提升超过200%；系统已服务90多个国家的数百万用户。

### 技术栈

- 大型语言模型（LLM）、智能体（Agent）、检索增强生成（RAG）、两阶段检索机制、CSTR标识符、自然语言处理、对话系统。

### 方法优势

- 针对科学数据共享场景，创新性地结合LLM与推荐系统。
- 提出多个新颖组件（科学意图感知器、结构化记忆压缩器、可信RAG）。
- 在真实大规模平台（ScienceDB）上部署，验证了实际效果。
- 提供可引用的数据集参考，增强推荐的可信度和可复现性。
- 实验规模大（超1000万数据集），结果显著。

### 主要局限

- 论文局限：摘要未提及具体局限性，如计算成本、可扩展性、多语言支持等。当前证据局限：仅基于摘要，无法评估方法的细节、对比基线的具体类型、用户研究或长期效果。

### 与当前研究方向的关联

论文与关键词高度相关：涉及LLM与推荐系统结合（LLM+推荐）、对话式推荐（对话式推荐）、推荐智能体（智能体）、生成式推荐（生成式推荐）、序列推荐（通过对话历史）、用户建模（科学意图感知）、CTR预测（在线点击率提升）、工业落地（部署于真实平台）。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3626772.3657828
- **seed_title**：Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning
- **seed_score**：90.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.666712_
