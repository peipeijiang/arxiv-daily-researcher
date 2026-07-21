---
title: "RerankArena：一个通过人类和LLM反馈评估检索、重排和RAG的统一平台"
paper_id: "https://doi.org/10.1145/3746252.3761484"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Information Retrieval and Search Behavior", "Multimodal Machine Learning Applications", "Topic Modeling"]
---

# RerankArena：一个通过人类和LLM反馈评估检索、重排和RAG的统一平台

> **英文原标题**：RerankArena: A Unified Platform for Evaluating Retrieval, Reranking and RAG with Human and LLM Feedback

[查看原文](https://dblp.org/rec/conf/cikm/AbdallahAPMAJ25) · [ArXiv](https://arxiv.org/abs/2508.05512) · [Semantic Scholar](https://www.semanticscholar.org/paper/14d2d1dc16d8ab214e2daf9698c457499d8dff44)

## 一句话结论

> RerankArena是一个统一平台，通过人类和LLM反馈评估检索、重排序和RAG系统的性能，支持多种评估模式并生成结构化数据集。

## 论文信息

- **作者**：Abdelrahman Abdallah, Mahmoud Abdalla, Bhawna Piryani, Jamshid Mozafari, Mohammed M. Abdelgwad, Adam Jatowt
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3746252.3761484](https://doi.org/10.1145/3746252.3761484)

<details open>
<summary><strong>中文摘要</strong></summary>

评估检索增强生成（RAG）与文档重排序系统的质量仍具挑战性，原因在于缺乏可扩展、以用户为中心且多视角的评估工具。我们提出RankArena，这是一个统一平台，可利用结构化的人类反馈与基于大语言模型（LLM）的反馈，对检索流水线、重排序器及RAG系统的性能进行比较与分析，并支持此类反馈的收集。RankArena支持多种评估模式：直接重排序可视化、基于人类或LLM投票的盲法成对比较、有监督的人工文档标注，以及端到端的RAG答案质量评估。该平台通过成对偏好与全列表标注两种方式捕获细粒度的相关性反馈，并附带辅助元数据，例如移动指标、标注时间与质量评分。该平台还集成了LLM-as-a-judge（大语言模型作为评判者）评估功能，可对模型生成的排序结果与人工真实标注进行对比。所有交互均以结构化评估数据集的形式存储，可用于训练重排序器、奖励模型、评判智能体或检索策略选择器。我们的平台可通过https://rankarena.ngrok.io/ 公开访问，演示视频见https://youtu.be/jIYAP4PaSSI。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Evaluating the quality of retrieval-augmented generation (RAG) and document reranking systems remains challenging due to the lack of scalable, user-centric, and multi-perspective evaluation tools. We introduce RankArena, a unified platform for comparing and analysing the performance of retrieval pipelines, rerankers, and RAG systems using structured human and LLM-based feedback as well as for collecting such feedback. RankArena supports multiple evaluation modes: direct reranking visualisation, blind pairwise comparisons with human or LLM voting, supervised manual document annotation, and end-to-end RAG answer quality assessment. It captures fine-grained relevance feedback through both pairwise preferences and full-list annotations, along with auxiliary metadata such as movement metrics, annotation time, and quality ratings. The platform also integrates LLM-as-a-judge evaluation, enabling comparison between model-generated rankings and human ground truth annotations. All interactions are stored as structured evaluation datasets that can be used to train rerankers, reward models, judgment agents, or retrieval strategy selectors. Our platform is publicly available at https://rankarena.ngrok.io/, and the Demo video is provided. https://youtu.be/jIYAP4PaSSI.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

论文提出了RerankArena，一个用于评估检索管道、重排器和RAG系统的统一平台。该平台支持多种评估模式：直接重排可视化、基于人类或LLM投票的盲法成对比较、有监督的手动文档标注以及端到端RAG答案质量评估。它通过成对偏好和全列表标注捕获细粒度相关性反馈，并收集辅助元数据如移动指标、标注时间和质量评分。平台还集成了LLM-as-a-judge评估，支持模型生成排名与人类真实标注的比较。所有交互存储为结构化评估数据集，可用于训练重排器、奖励模型、判断代理或检索策略选择器。平台已公开可用。

### 主要创新

- 统一平台：首次将检索、重排和RAG系统的评估整合在一个平台中，支持多种评估模式。
- 多源反馈：同时利用人类和LLM反馈进行成对比较和全列表标注，提供细粒度相关性评估。
- 结构化数据集：所有交互存储为结构化评估数据集，可用于训练下游模型如重排器和奖励模型。
- LLM-as-a-judge集成：支持模型生成排名与人类标注的对比，实现自动化评估与人工评估的结合。

### 研究方法

论文主要采用平台设计与评估方法。平台支持多种评估模式：直接重排可视化、盲法成对比较（人类或LLM投票）、有监督手动文档标注、端到端RAG答案质量评估。通过收集成对偏好和全列表标注获取细粒度反馈，并记录移动指标、标注时间和质量评分等元数据。集成LLM-as-a-judge进行自动化评估，所有数据存储为结构化数据集。

### 关键结果

摘要未提供具体实验结果或数值。

### 技术栈

- LLM-as-a-judge
- 成对比较
- 全列表标注
- 移动指标
- 结构化评估数据集

### 方法优势

- 统一性：整合多种评估模式，覆盖检索、重排和RAG全流程。
- 灵活性：支持人类和LLM两种反馈源，适应不同评估需求。
- 实用性：生成的结构化数据集可直接用于训练下游模型，具有实际应用价值。
- 可扩展性：平台设计支持多种评估任务，易于扩展。

### 主要局限

- 论文局限：摘要未披露平台在真实场景下的性能评估、用户研究或与现有工具的对比。当前证据局限：仅基于摘要，无法评估平台的有效性、效率或用户满意度，缺乏具体实验数据。

### 与当前研究方向的关联

高度相关。论文聚焦于排序与重排（RerankArena平台）、检索增强生成（RAG）评估，并涉及LLM与推荐系统结合（LLM-as-a-judge），与关键词“排序与重排”、“LLM与推荐系统结合”、“生成式推荐”等直接相关。

---

_知识库更新时间：2026-07-21T04:03:10.446536_
