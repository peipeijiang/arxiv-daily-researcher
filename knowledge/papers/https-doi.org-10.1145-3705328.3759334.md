---
title: "基于大语言模型的推荐系统智能体"
paper_id: "https://doi.org/10.1145/3705328.3759334"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 68.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# 基于大语言模型的推荐系统智能体

> **英文原标题**：Large Language Model-based Recommendation System Agents

[查看原文](https://dblp.org/rec/conf/recsys/CarraroSP25) · [Semantic Scholar](https://www.semanticscholar.org/paper/97c6529767968e63e68e8bc39ababf1a69f0e9e5)

## 一句话结论

> 该论文首次尝试设计基于LLM的推荐系统智能体，通过工具调用和RAG技术访问预训练推荐系统、数据库和向量存储，以处理复杂的推荐和解释查询。

## 论文信息

- **作者**：Tommaso Carraro, Brijraj Singh, Niranjan Pedanekar
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：68.0
- **DOI**：[https://doi.org/10.1145/3705328.3759334](https://doi.org/10.1145/3705328.3759334)

<details open>
<summary><strong>中文摘要</strong></summary>

基于大语言模型的智能体是一种人工智能助手，它利用先进的工具调用（Tool Calling, TC）与检索增强生成（Retrieval Augmented Generation, RAG）技术来访问外部工具（例如Python代码、数据库）。这使得智能体能够查询与其预训练知识互补的额外信息来源。通过这种方式，每当新知识出现时，可以避免对大语言模型进行重新训练或微调，因为助手能够借助现有工具获取这些信息。在本演示中，我们于推荐系统（Recommendation Systems, RSs）场景下探究了这一思路。具体而言，我们设计了一款用于推荐的AI助手，它能够访问（i）一个预训练的推荐系统，（ii）一个数据库，以及（iii）一个向量存储库。该演示展示了助手如何与这些工具交互，以回应需要对工具结果进行推理的复杂推荐与解释查询。据我们所知，这是设计基于大语言模型的推荐系统智能体的首次尝试。本演示论文的代码可通过此URL1获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

A Large Language Model-based agent is an AI assistant that makes use of advanced Tool Calling (TC) and Retrieval Augmented Generation (RAG) techniques to access external tools (e.g., Python code, databases). This allows the agent to consult additional sources of information that are complementary to its pre-trained knowledge. By doing so, re-training or fine-tuning of the LLM each time new knowledge becomes available can be avoided, as the assistant can access this information thanks to the available tools. In this demo, we investigate this idea in the Recommendation Systems (RSs) scenario. In particular, we design an AI assistant for recommendation that can access (i) a pre-trained recommender system, (ii) a database, and (iii) a vector store. The demo shows how the assistant is able to interact with these tools to reply to complex recommendation and explanation queries that require reasoning on the tool’s results. To the best of our knowledge, this is the first attempt at designing LLM-based recommendation system agents. The code for this demo paper is available at this URL1.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出一种基于大语言模型（LLM）的推荐系统智能体，利用工具调用（TC）和检索增强生成（RAG）技术访问外部工具（如Python代码、数据库），从而避免每次新知识出现时重新训练或微调LLM。该智能体可访问预训练的推荐系统、数据库和向量存储，通过推理工具结果来回答复杂的推荐和解释查询。这是首次尝试设计基于LLM的推荐系统智能体，代码已公开。

### 主要创新

- 首次将LLM智能体应用于推荐系统场景
- 结合工具调用和检索增强生成技术，使LLM能动态访问外部知识源
- 设计可访问预训练推荐系统、数据库和向量存储的多工具架构
- 支持复杂推荐和解释查询的推理与回答

### 研究方法

采用LLM作为核心智能体，通过工具调用接口连接预训练推荐系统、数据库和向量存储。利用检索增强生成技术从外部工具获取补充信息，结合LLM的推理能力处理用户查询。

### 关键结果

摘要未提供具体实验数字或结果，仅说明演示展示了智能体能够与工具交互并回答复杂查询。

### 技术栈

- 大语言模型（LLM）
- 工具调用（Tool Calling, TC）
- 检索增强生成（Retrieval Augmented Generation, RAG）
- 预训练推荐系统
- 数据库
- 向量存储

### 方法优势

- 创新性地将LLM智能体引入推荐系统，避免频繁重训练
- 利用外部工具扩展LLM知识，提升推荐和解释能力
- 代码开源，便于复现和进一步研究

### 主要局限

- **论文本身局限**：摘要未提及局限性，可能包括工具调用延迟、依赖外部工具质量等。
- **当前证据局限**：当前仅基于摘要，缺乏实验细节、数据集、基线对比等，无法全面评估方法有效性。

### 与当前研究方向的关联

该论文与“LLM与推荐系统结合”和“推荐智能体”高度相关，直接提出基于LLM的推荐智能体；与“生成式推荐”和“对话式推荐”有一定关联，但摘要未明确涉及序列推荐、多模态等关键词。

---

_知识库更新时间：2026-07-13T06:43:12.874401_
