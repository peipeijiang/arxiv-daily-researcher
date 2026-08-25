---
title: "SPARK：通过智能体驱动的检索与知识共享实现搜索个性化"
paper_id: "https://doi.org/10.1145/3779211.3793173"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 62.0
tags: ["paper", "recommender-systems"]
---

# SPARK：通过智能体驱动的检索与知识共享实现搜索个性化

> **英文原标题**：SPARK: Search Personalization via Agent-Driven Retrieval and Knowledge-sharing

[查看原文](https://dblp.org/rec/conf/wsdm/ChhetriDC26) · [ArXiv](https://arxiv.org/abs/2512.24008) · [Semantic Scholar](https://www.semanticscholar.org/paper/9e003dc5a54c90d36e641013103543fc97165243)

## 一句话结论

> SPARK框架通过协调基于LLM的个性化智能体进行检索和知识共享，以建模用户动态多维信息需求，实现搜索个性化。

## 论文信息

- **作者**：Gaurab Chhetri, Subasish Das, Tausif Islam Chowdhury
- **来源**：WSDM Companion
- **发布时间**：2026-01-01
- **相关度评分**：62.0
- **DOI**：[https://doi.org/10.1145/3779211.3793173](https://doi.org/10.1145/3779211.3793173)

<details open>
<summary><strong>中文摘要</strong></summary>

个性化搜索要求系统能够建模用户不断演化的、多维度的信息需求；这对于受限于静态用户画像或单一检索流程的系统而言是一项挑战。我们提出SPARK（通过智能体驱动的检索与知识共享实现搜索个性化），该框架通过协调基于人物角色的多种大语言模型（LLM）智能体，实现任务特定的检索与涌现式个性化。SPARK形式化定义了一个由角色、专长、任务上下文和领域构成的人物角色空间，并引入了一个人物角色协调器，能够动态解读输入查询，以激活最相关的专业化智能体。每个智能体执行独立的检索增强生成流程，并配备专用的长期与短期记忆存储以及上下文感知推理模块。智能体间的协作通过结构化通信协议实现，包括共享记忆库、迭代式辩论和接力式知识传递。借鉴认知架构、多智能体协调理论与信息检索的原理，SPARK建模了涌现式个性化属性如何从由最小协调规则支配的分布式智能体行为中产生。该框架在协调效率、个性化质量和认知负荷分布方面提供了可检验的预测，同时融入了用于持续人物角色优化的自适应学习机制。通过将细粒度的智能体专业化与协作式检索相结合，SPARK为能够捕捉人类信息寻求行为的复杂性、流动性和上下文敏感性的下一代搜索系统提供了洞见。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Personalized search demands the ability to model users' evolving, multi-dimensional information needs; a challenge for systems constrained by static profiles or monolithic retrieval pipelines. We present SPARK (Search Personalization via Agent-Driven Retrieval and Knowledge-sharing), a framework in which coordinated persona-based large language model (LLM) agents deliver task-specific retrieval and emergent personalization. SPARK formalizes a persona space defined by role, expertise, task context, and domain, and introduces a Persona Coordinator that dynamically interprets incoming queries to activate the most relevant specialized agents. Each agent executes an independent retrieval-augmented generation process, supported by dedicated long- and short-term memory stores and context-aware reasoning modules. Inter-agent collaboration is facilitated through structured communication protocols, including shared memory repositories, iterative debate, and relay-style knowledge transfer. Drawing on principles from cognitive architectures, multi-agent coordination theory, and information retrieval, SPARK models how emergent personalization properties arise from distributed agent behaviors governed by minimal coordination rules. The framework yields testable predictions regarding coordination efficiency, personalization quality, and cognitive load distribution, while incorporating adaptive learning mechanisms for continuous persona refinement. By integrating fine-grained agent specialization with cooperative retrieval, SPARK provides insights for next-generation search systems capable of capturing the complexity, fluidity, and context sensitivity of human information-seeking behavior.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

个性化搜索需要建模用户不断演化的多维度信息需求，这对受限于静态画像或单一检索流程的系统构成挑战。本文提出SPARK框架，通过协调基于角色的LLM智能体实现任务特定检索和涌现式个性化。SPARK定义了由角色、专长、任务上下文和领域构成的角色空间，并引入角色协调器动态解读查询以激活最相关的专业智能体。每个智能体独立执行检索增强生成，配备专用长期和短期记忆存储及上下文感知推理模块。智能体间通过共享记忆库、迭代辩论和接力式知识传递等结构化通信协议协作。借鉴认知架构、多智能体协调理论和信息检索原理，SPARK展示了涌现式个性化如何从受最小协调规则支配的分布式智能体行为中产生。该框架对协调效率、个性化质量和认知负荷分布提供可测试预测，并纳入自适应学习机制以持续优化角色。通过结合细粒度智能体专业化与协作检索，SPARK为捕捉人类信息寻求行为的复杂性、流动性和上下文敏感性的下一代搜索系统提供了见解。

### 主要创新

- 提出SPARK框架，利用协调的基于角色的LLM智能体实现个性化搜索
- 定义形式化的角色空间，包括角色、专长、任务上下文和领域
- 引入角色协调器动态激活相关专业智能体
- 设计智能体间协作协议，包括共享记忆、迭代辩论和接力式知识传递
- 将认知架构和多智能体协调理论应用于搜索个性化

### 研究方法

SPARK采用多智能体框架，每个智能体执行独立的检索增强生成，配备专用记忆和推理模块。角色协调器根据查询动态选择相关智能体。智能体间通过结构化通信协议协作，包括共享记忆库、迭代辩论和接力式知识传递。框架基于认知架构、多智能体协调理论和信息检索原理，并包含自适应学习机制以持续优化角色。

### 关键结果

摘要未提供具体实验结果。框架提出可测试的预测，涉及协调效率、个性化质量和认知负荷分布，但未给出数值结果。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。提及的技术概念包括：基于角色的LLM智能体、检索增强生成、长期和短期记忆存储、上下文感知推理模块、共享记忆库、迭代辩论、接力式知识传递、认知架构、多智能体协调理论、信息检索原理、自适应学习机制。

### 方法优势

- 提出新颖的多智能体框架，结合角色专业化与协作检索
- 形式化定义角色空间，增强可解释性和模块化
- 借鉴多学科理论，提供理论支撑
- 强调涌现式个性化，符合复杂系统观点
- 包含自适应学习机制，支持持续优化

### 主要局限

- 论文局限：摘要未提供实验验证，缺乏实证支持
- 当前证据局限：仅基于摘要，无法评估实际性能、效率或与现有方法的比较
- 摘要未提及具体实现细节、数据集或基线

### 与当前研究方向的关联

该论文与推荐系统、LLM与推荐系统结合、推荐智能体、用户建模等关键词高度相关。它聚焦于个性化搜索，利用LLM智能体进行检索和知识共享，涉及用户建模和智能体协调，属于生成式推荐和LLM应用的前沿方向。

---

_知识库更新时间：2026-08-25T02:16:23.901922_
