---
title: "组合智能体，复合风险：多智能体推荐系统中的鲁棒性与对齐教程"
paper_id: "https://doi.org/10.1145/3773078.3831750"
source: "citation"
published: "2026-09-25T00:00:00"
score: 57.0
tags: ["paper", "recommender-systems"]
---

# 组合智能体，复合风险：多智能体推荐系统中的鲁棒性与对齐教程

> **英文原标题**：Composing Agents, Compounding Risks: A Tutorial on Robustness and Alignment in Multi-Agent Recommender Systems

[查看原文](https://doi.org/10.1145/3773078.3831750)

## 一句话结论

> 该教程针对多智能体推荐系统中因智能体组合而产生的系统级风险难以评估的问题，提出了一个风险分类法、从组件到组合的评估框架以及贯穿系统生命周期的缓解措施。

## 论文信息

- **作者**：Kurt Cutajar, Jas Kandola, Anjun Hu, Yashar Deldjoo
- **来源**：Proceedings of the 20th ACM Conference on Recommender Systems
- **发布时间**：2026-09-25
- **相关度评分**：57.0
- **DOI**：[https://doi.org/10.1145/3773078.3831750](https://doi.org/10.1145/3773078.3831750)

<details open>
<summary><strong>中文摘要</strong></summary>

多智能体推荐系统（Multi-agent recommender systems）正作为一种新的设计范式兴起，其中由大语言模型（LLM）驱动的智能体在上下文上进行规划、调用工具、交换中间输出，并在交互过程中维护记忆。尽管这些组合为交互式和模块化推荐创造了新的机遇，但当智能体被孤立评估时，它们也引入了容易被忽视的系统级风险。随着推荐越来越多地源于组合式多智能体系统而非单一模型，关于风险如何通过智能体交互传播以及应如何对其进行评估，仍然缺乏一套共享的术语体系。契合RecSys 2026将推荐系统视为系统（systems）的重点，本教程通过以下方式弥补这一空白：面向多智能体推荐系统的风险分类体系、一套从组件到组合跨离线和在线测试的评估框架，以及贯穿系统生命周期的缓解措施。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multi-agent recommender systems are emerging as a new design paradigm in which LLM-powered agents plan over context, invoke tools, exchange intermediate outputs, and maintain memory across interactions. While these compositions create new opportunities for interactive and modular recommendation, they also introduce system-level risks that are easy to miss when agents are evaluated in isolation. As recommendation increasingly arises from composed multi-agent systems rather than single models, a shared vocabulary is still lacking for how risks propagate through agent interaction and how they should be evaluated. In line with RecSys 2026’s emphasis on recommender systems as systems, this tutorial addresses that gap through a risk taxonomy for multi-agent recommenders, an evaluation framework that scales from component to composition across offline and online tests, and mitigations across the system lifecycle.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

该教程论文关注多智能体推荐系统这一新兴设计范式。在该范式中，由LLM驱动的智能体在上下文上进行规划、调用工具、交换中间输出，并在交互过程中维护记忆。这种组合为交互式和模块化推荐创造了新机会，但也引入了在孤立评估单个智能体时容易被忽视的系统级风险。随着推荐越来越多地由组合式多智能体系统而非单一模型产生，目前仍缺乏共享词汇来描述风险如何在智能体交互中传播以及应如何评估这些风险。为呼应RecSys 2026对推荐系统作为系统的强调，该教程通过多智能体推荐器的风险分类法、从组件到组合并覆盖离线和在线测试的评估框架，以及贯穿系统生命周期的缓解措施来填补这一空白。

### 主要创新

- 提出面向多智能体推荐系统的风险分类法，用于描述风险在智能体交互中的传播方式。
- 提出从组件到组合的评估框架，覆盖离线与在线测试。
- 强调从孤立评估单个智能体转向系统级评估，以捕捉组合带来的系统级风险。
- 提出贯穿系统生命周期的缓解措施，将鲁棒性与对齐问题纳入多智能体推荐系统设计。
- 为多智能体推荐系统提供共享词汇，以弥补风险传播与评估讨论中的术语缺失。

### 研究方法

该工作以教程形式展开，主要方法路线包括：构建多智能体推荐系统的风险分类法；设计从组件级到组合级的评估框架，并覆盖离线与在线测试；提出贯穿系统生命周期的缓解措施。摘要未提供具体实验方法、数据集、基线或实现细节。

### 关键结果

摘要未提供具体实验数字或实证结果。摘要明确指出，多智能体组合在带来交互式和模块化推荐机会的同时，会引入在孤立评估智能体时容易忽视的系统级风险；当前缺乏关于风险如何通过智能体交互传播以及如何评估的共享词汇；该教程通过风险分类法、评估框架和生命周期缓解措施来应对这一空白。

### 技术栈

- 摘要提及LLM驱动的智能体、多智能体推荐系统、智能体规划、工具调用、中间输出交换、跨交互记忆维护、风险分类法、离线与在线评估框架以及系统生命周期缓解措施。摘要未提供具体算法、工具或数学方法。

### 方法优势

- 选题契合推荐系统作为系统的研究趋势，回应RecSys 2026的关注重点。
- 聚焦多智能体推荐系统中容易被忽视的系统级风险，具有较强的问题意识。
- 同时覆盖风险分类、评估框架和缓解措施，结构较为完整。
- 强调从组件到组合的评估视角，有助于推动多智能体推荐系统的规范化评估。
- 以教程形式提供共享词汇，有利于该方向的学术交流与后续研究。

### 主要局限

- 论文局限：当前仅提供摘要，无法判断该教程是否包含具体案例、实验验证或可复现资源；摘要未提供具体模型名称、数据集、基线、损失函数、消融实验、参数或实现细节。当前证据局限：由于只有摘要，无法评估风险分类法的完备性、评估框架的可操作性以及缓解措施的实际效果；所有具体实验数字和指标值均无法从输入中确认。

### 与当前研究方向的关联

该论文与推荐系统领域的最新学术研究高度相关，尤其涉及LLM与推荐系统结合、推荐智能体、多智能体推荐系统、鲁棒性与对齐等关键词。其关注的风险传播、系统级评估和生命周期缓解也与推荐系统的鲁棒性、公平性和工业落地等方向存在关联。摘要未涉及序列推荐、生成式推荐、多模态推荐、对话式推荐、排序与重排、用户建模、CTR/CVR预测或因果性等具体内容。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-09-27T05:37:07.635664_
