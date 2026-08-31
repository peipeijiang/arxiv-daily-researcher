---
title: "TRACE：一个可扩展且可扩展的审计YouTube推荐算法的框架"
paper_id: "https://doi.org/10.1145/3773966.3779410"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 71.0
tags: ["paper", "recommender-systems", "Persona Design and Applications", "Recommender Systems and Techniques", "AI in Service Interactions"]
---

# TRACE：一个可扩展且可扩展的审计YouTube推荐算法的框架

> **英文原标题**：TRACE: A Scalable and Extensible Framework for Auditing YouTube&apos;s Recommendation Algorithm

[查看原文](https://dblp.org/rec/conf/wsdm/DessainTK26) · [Semantic Scholar](https://www.semanticscholar.org/paper/ef9b5d058372e1b2fcba99a442a91f3dd6b5e3cc)

## 一句话结论

> TRACE是一个可扩展的框架，利用大语言模型模拟用户旅程，以可复现的方式审计YouTube推荐算法，从而研究个性化推荐和过滤气泡的形成。

## 论文信息

- **作者**：Quentin Dessain, Colin Timmers, Corentin Vande Kerckhove
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：71.0
- **DOI**：[https://doi.org/10.1145/3773966.3779410](https://doi.org/10.1145/3773966.3779410)

<details open>
<summary><strong>中文摘要</strong></summary>

审计像YouTube这样的大规模推荐系统，在方法论上仍面临挑战，原因在于行为真实性、可扩展性和可复现性之间的权衡。我们提出了TRACE，一个开源框架，它集成大语言模型（Large Language Models）来模拟情境感知、人物驱动的用户旅程。TRACE结合了容器化浏览器自动化、数据库支持的追踪性以及异步数据增强，从而能够对YouTube的推荐生态系统进行可复现的大规模审计。通过将实验情境与人物角色解耦，并支持多种行为模式，它使研究者能够建模多样化的用户身份，并探索推荐动态如何随时间演变。该框架的模块化架构、可复现设计以及基于网络的控制界面，促进了算法个性化及潜在过滤气泡形成的透明、比较性研究。TRACE为推荐系统的经验驱动、可扩展且符合伦理的审计奠定了可扩展的基础。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Auditing large-scale recommender systems like YouTube remains a methodological challenge due to the trade-off between behavioral realism, scalability, and reproducibility. We present TRACE, an open-source framework that integrates Large Language Models to simulate context-aware, persona-driven user journeys. TRACE combines containerized browser automation, database-backed traceability, and asynchronous data enrichment to enable reproducible large-scale audits of YouTube's recommendation ecosystem. By decoupling experimental contexts from personas and supporting multiple behavioral modes, it allows researchers to model diverse user identities and explore how recommendation dynamics evolve over time. The framework's modular architecture, reproducible design, and web-based control interface facilitate transparent, comparative studies of algorithmic personalization and potential filter bubble formation. TRACE establishes a scalable foundation for empirically grounded, extensible, and ethically sound auditing of recommender systems.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

审计YouTube等大规模推荐系统在方法论上仍面临挑战，主要在于行为真实性、可扩展性和可复现性之间的权衡。本文提出TRACE，一个开源框架，集成大型语言模型来模拟情境感知、角色驱动的用户旅程。TRACE结合了容器化浏览器自动化、数据库支持的追踪性和异步数据增强，以实现对YouTube推荐生态系统的可复现的大规模审计。通过将实验情境与角色分离并支持多种行为模式，它允许研究人员模拟不同的用户身份，并探索推荐动态如何随时间演变。该框架的模块化架构、可复现设计和基于Web的控制界面，促进了算法个性化和潜在过滤气泡形成的透明、比较性研究。TRACE为推荐系统的实证、可扩展和伦理审计建立了可扩展的基础。

### 主要创新

- 集成大型语言模型模拟情境感知、角色驱动的用户旅程
- 结合容器化浏览器自动化、数据库支持的追踪性和异步数据增强
- 将实验情境与角色解耦，支持多种行为模式
- 模块化架构和可复现设计，便于透明比较研究
- 基于Web的控制界面，促进可访问性和可扩展性

### 研究方法

TRACE框架采用容器化浏览器自动化模拟用户行为，利用大型语言模型生成情境感知和角色驱动的用户旅程，通过数据库支持追踪用户交互，并使用异步数据增强处理数据。框架支持多种行为模式，允许研究人员定义不同的用户角色和实验情境，从而进行大规模可复现的审计。

### 关键结果

摘要未提供具体实验结果，但框架旨在实现可扩展的大规模审计，并促进对算法个性化和过滤气泡形成的比较研究。

### 技术栈

- 大型语言模型（LLM）
- 容器化浏览器自动化
- 数据库
- 异步数据增强
- 模块化架构
- Web控制界面

### 方法优势

- 解决了行为真实性、可扩展性和可复现性之间的权衡
- 集成LLM增强用户模拟的真实性
- 模块化设计提高灵活性和可扩展性
- 开源框架促进透明和可复现研究
- 支持多种行为模式，适应不同研究需求

### 主要局限

- 论文局限：摘要未提及具体实验验证或性能评估。当前证据局限：仅基于摘要，无法评估框架的实际效果、性能指标或与现有方法的比较。

### 与当前研究方向的关联

该论文与推荐系统审计、算法个性化、过滤气泡、大型语言模型应用、用户建模等关键词高度相关。它涉及推荐系统的公平性、鲁棒性和工业落地，并提出了一个可扩展的审计框架，符合推荐系统研究的前沿方向。

---

_知识库更新时间：2026-08-31T05:58:38.710021_
