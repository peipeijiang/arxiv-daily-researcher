---
title: "生成式推荐：迈向个性化多模态内容生成"
paper_id: "https://doi.org/10.1145/3701716.3717529"
source: "www"
published: "2025-01-01T00:00:00"
score: 74.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Recommender Systems and Techniques", "Advanced Text Analysis Techniques"]
---

# 生成式推荐：迈向个性化多模态内容生成

> **英文原标题**：Generative Recommendation: Towards Personalized Multimodal Content Generation

[查看原文](https://dblp.org/rec/conf/www/00070F0C25) · [Semantic Scholar](https://www.semanticscholar.org/paper/94a8244e3436d9f52474d64eed6ef9290940f345)

## 一句话结论

> 该论文提出GeneRec生成式推荐范式，利用AI生成多模态内容并整合用户指令，以突破传统检索式推荐的局限，并在时尚领域验证了可行性。

## 论文信息

- **作者**：Wenjie Wang, Xinyu Lin, Fuli Feng, Xiangnan He, Tat‐Seng Chua
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：74.0
- **DOI**：[https://doi.org/10.1145/3701716.3717529](https://doi.org/10.1145/3701716.3717529)

<details open>
<summary><strong>中文摘要</strong></summary>

传统推荐系统主要从预定义的项目库中检索内容以进行个性化推荐。然而，这种基于检索的范式面临两大限制：1）现有由人工生成的项目库可能无法充分满足用户多样化的信息需求；2）用户通常依赖被动且带有噪声的反馈（例如点击）来优化推荐结果。为克服这些局限，人工智能生成内容（AI-Generated Content, AIGC）的快速发展展现出巨大潜力：1）生成式AI能够促进创建个性化多模态内容作为新项目，以满足用户的信息需求；2）大型语言模型降低了用户主动用自然语言表达信息需求的难度。基于此，我们提出一种名为GeneRec的新型生成式推荐范式，其目标包括：1）生成个性化多模态内容；2）整合用户主动指令以指导内容生成。为实现这些目标，GeneRec引入AI生成器来个性化生成多模态内容，并利用用户指令获取其信息需求。具体而言，GeneRec首先使用指令处理器对用户指令及传统反馈（如点击）进行预处理，以提取生成指导信息。随后，我们开发了包含AI编辑器和AI创建器的AI生成器，分别用于编辑现有项目与创建新项目。最后，我们在时尚领域验证了AI创建器的可行性，并取得了令人鼓舞的结果。此外，为确保生成内容的可信度，我们强调了多种可信度检查机制，例如公平性检查与安全性检查。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Traditional recommender systems primarily retrieve items from a pre-defined item corpus for personalized recommendations. However, this a retrieval-based paradigm faces two major constraints: 1) the existing item corpus with human-generated items may not adequately satisfy users' diverse information needs, and 2) users often rely on passive and noisy feedback (e.g., clicks) to refine the recommendations. To overcome the limitations, the rapid advancement of AI-Generated Content (AIGC) presents significant potential: 1) generative AI promotes the creation of personalized multimodal content as new items to satisfy users' information needs, and 2) large language models reduce the efforts of users to express information needs proactively in natural language. In this light, we propose a novel Generative Recommender paradigm named GeneRec with two objectives: 1) generating personalized multimodal content, and 2) integrating proactive user instructions to guide content generation. To achieve the objectives, GeneRec introduces an AI generator to personalize multimodal content generation and leverages user instructions to obtain users' information needs. Specifically, GeneRec first employs an instructor to pre-process users' instructions and traditional feedback (e.g., clicks) to extract generation guidance. Following the guidance, we develop the AI generator with an AI editor to edit existing items and an AI creator to create new items, respectively. Lastly, we study the feasibility of implementing the AI creator in the fashion domain, showing promising results. Furthermore, to ensure the trustworthiness of the generated items, we emphasize various trustworthiness checks such as fairness and safety checks.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

传统推荐系统主要从预定义物品库中检索物品，但存在两个局限：现有物品库可能无法充分满足用户多样化的信息需求，且用户依赖被动且嘈杂的反馈（如点击）来优化推荐。随着AI生成内容（AIGC）的快速发展，生成式AI能够创建个性化多模态内容作为新物品，大语言模型也降低了用户主动表达信息需求的难度。为此，本文提出名为GeneRec的新型生成式推荐范式，目标包括：生成个性化多模态内容，以及整合主动用户指令以指导内容生成。GeneRec引入AI生成器来个性化多模态内容生成，并利用用户指令获取信息需求。具体地，GeneRec首先使用指令处理器预处理用户指令和传统反馈（如点击）以提取生成指导；然后开发AI生成器，包括编辑现有物品的AI编辑器和创建新物品的AI创建器；最后在时尚领域验证了AI创建器的可行性，结果令人鼓舞。此外，为确保生成物品的可信度，强调了公平性和安全性等可信度检查。

### 主要创新

- 提出生成式推荐范式GeneRec，突破传统检索式推荐局限，直接生成个性化多模态内容。
- 整合主动用户指令（自然语言）与传统被动反馈（如点击），实现更精准的信息需求获取。
- 设计双模块AI生成器：AI编辑器（修改现有物品）和AI创建器（生成全新物品），覆盖不同生成场景。
- 在时尚领域验证AI创建器可行性，并强调生成物品的可信度检查（公平性、安全性）。

### 研究方法

论文提出GeneRec框架，包含三个核心组件：1）指令处理器：预处理用户指令和传统反馈（如点击），提取生成指导；2）AI生成器：包括AI编辑器（基于指导修改现有物品）和AI创建器（基于指导生成全新物品）；3）可信度检查：对生成物品进行公平性和安全性等检查。在时尚领域进行AI创建器的可行性实验。

### 关键结果

在时尚领域实现AI创建器的可行性研究，结果显示该方法具有前景。具体实验数字、数据集、基线等摘要未提供。

### 技术栈

- AI生成器（可能基于生成对抗网络或扩散模型等，但摘要未明确）、大语言模型（用于处理用户指令）、指令处理器（自然语言处理技术）、可信度检查方法（公平性、安全性评估）。具体算法、工具、数学方法摘要未提供。

### 方法优势

- 创新性地将生成式AI引入推荐系统，突破检索式范式，可满足用户多样化信息需求。
- 融合主动指令与被动反馈，提升用户意图理解的准确性。
- 双模块生成器设计灵活，兼顾编辑与创造。
- 关注生成物品的可信度，体现负责任的AI理念。

### 主要局限

- 论文局限：仅验证了时尚领域的AI创建器，其他领域及AI编辑器的效果未提及。
- 当前证据局限：摘要未提供具体实验数据、基线对比、消融实验等，无法评估方法实际性能。
- 当前证据局限：未讨论生成内容的质量控制、计算成本、用户隐私等潜在问题。

### 与当前研究方向的关联

高度相关：论文聚焦生成式推荐（生成式推荐）、结合大语言模型（LLM与推荐系统结合）、涉及多模态内容（多模态推荐）、用户指令交互（对话式推荐）、以及可信度（公平性、鲁棒性）。

---

_知识库更新时间：2026-07-13T06:43:12.875364_
