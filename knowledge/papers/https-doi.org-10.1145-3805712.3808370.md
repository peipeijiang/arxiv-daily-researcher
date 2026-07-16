---
title: "TRACE：基于智能体反事实解释的可持续旅游推荐对话框架"
paper_id: "https://doi.org/10.1145/3805712.3808370"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 68.0
tags: ["paper", "recommender-systems", "AI in Service Interactions", "Explainable Artificial Intelligence (XAI)", "Recommender Systems and Techniques"]
---

# TRACE：基于智能体反事实解释的可持续旅游推荐对话框架

> **英文原标题**：TRACE: A Conversational Framework for Sustainable Tourism Recommendation with Agentic Counterfactual Explanations

[查看原文](https://dblp.org/rec/conf/sigir/BanerjeeSWD26) · [ArXiv](https://arxiv.org/abs/2604.14223) · [Semantic Scholar](https://www.semanticscholar.org/paper/5ba397b352549d4cbacdb935f13700ae519fa854)

## 一句话结论

> TRACE是一个基于LLM的多智能体对话框架，通过反事实解释和澄清问题促进可持续旅游推荐，在保持推荐质量的同时有效支持可持续决策。

## 论文信息

- **作者**：Ashmi Banerjee, Adithi Satish, Wolfgang Wörndl, Yashar Deldjoo
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：68.0
- **DOI**：[https://doi.org/10.1145/3805712.3808370](https://doi.org/10.1145/3805712.3808370)

<details open>
<summary><strong>中文摘要</strong></summary>

传统对话式旅游推荐系统主要针对用户相关性和便利性进行优化，往往强化了热门拥挤目的地及高碳排放旅行选择。为解决这一问题，我们提出TRACE（基于智能体反事实解释的旅游推荐系统），这是一个基于大语言模型的多智能体框架，通过交互式助推促进可持续旅游。TRACE采用模块化的编排器-工作者架构，其中专门化的智能体能够挖掘潜在可持续性偏好、构建结构化用户画像，并生成兼顾相关性与环境影响的推荐。其关键创新在于运用智能体反事实解释与大语言模型驱动的澄清性问题，共同揭示更环保的替代方案并细化对用户意图的理解，从而在非强制条件下促进用户反思。用户研究与语义对齐分析表明，TRACE在保持推荐质量与交互响应性的同时，有效支持了可持续决策。TRACE基于Google Agent Development Kit实现，并提供了完整代码、Docker配置、提示词及公开可用的演示视频以确保可复现性。项目摘要（含所有资源、提示词及演示访问入口）详见https://ashmibanerjee.github.io/trace-chatbot。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Traditional conversational travel recommender systems primarily optimize for user relevance and convenience, often reinforcing popular, overcrowded destinations and carbon-intensive travel choices. To address this, we present TRACE (Tourism Recommendation with Agentic Counterfactual Explanations), a multi-agent, LLM-based framework that promotes sustainable tourism through interactive nudging. TRACE uses a modular orchestrator-worker architecture where specialized agents elicit latent sustainability preferences, construct structured user personas, and generate recommendations that balance relevance with environmental impact. A key innovation lies in its use of agentic counterfactual explanations and LLM-driven clarifying questions, which together surface greener alternatives and refine understanding of intent, fostering user reflection without coercion. User studies and semantic alignment analyses demonstrate that TRACE effectively supports sustainable decision-making while preserving recommendation quality and interactive responsiveness. TRACE is implemented on Google's Agent Development Kit, with full code, Docker setup, prompts, and a publicly available demo video to ensure reproducibility. A project summary, including all resources, prompts, and demo access, is available at https://ashmibanerjee.github.io/trace-chatbot.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

TRACE是一个基于多智能体和大语言模型的对话式推荐系统，旨在通过交互式助推促进可持续旅游。系统采用编排器-工作者架构，包含专门智能体用于挖掘潜在可持续偏好、构建结构化用户画像，并生成平衡相关性与环境影响的推荐。其核心创新在于利用智能体反事实解释和LLM驱动的澄清问题，在尊重用户偏好的同时温和地展示更绿色的替代方案。用户研究和语义对齐分析表明，TRACE能有效支持可持续决策，同时保持推荐质量和交互响应速度。系统基于Google Agent Development Kit实现，代码、Docker配置和演示视频已公开。

### 主要创新

- 提出多智能体LLM框架，通过专门智能体分别处理用户建模、澄清问题、推荐生成和解释，实现可持续旅游的数字化助推。
- 引入智能体反事实解释机制：当用户不愿妥协时，系统仍推荐基线选项，但通过反事实解释展示更可持续的替代方案，实现非强制性助推。
- 通过澄清问题间接挖掘用户潜在可持续偏好，而非硬编码可持续约束，增强系统灵活性和用户接受度。
- 开源完整代码、Docker设置和演示视频，促进可重复性和后续研究。

### 研究方法

采用编排器-工作者架构，包含三个层次：用户交互层（前端）、编排层（中间件）和智能体推理层（后端）。智能体推理层由顺序流水线组成：澄清问题智能体生成最多5个问题以挖掘偏好；意图分类智能体基于用户回答构建结构化用户画像和妥协意愿向量；推荐智能体使用少样本提示生成基线推荐和可持续推荐；解释生成智能体根据妥协意愿选择直接对齐或反事实助推策略，输出最终推荐、解释和替代选项。系统使用Google ADK、Vertex AI、gemini-2.5-flash模型、FastAPI、Firestore和Chainlit实现。

### 关键结果

用户研究中，79.1%的用户选择了主要推荐选项，其中75.5%的会话中主要推荐为可持续推荐。；当基线推荐作为主要选项时，16.7%的用户选择了可持续替代方案，表明存在适度助推效果。；55.2%的用户认为澄清问题质量“很好”或“极好”，65.4%的用户认为解释质量“很好”或“极好”。；约60%的用户报告对初始选择有一定程度的重新考虑。；语义相似度分析显示，解释与完整对话的相似度均值为0.7033，意图分类器输出与对话的相似度为0.7883，意图分类器输出与解释的相似度为0.7437。；系统平均延迟23秒，最大延迟38秒。

### 技术栈

- Google Agent Development Kit (ADK)
- Vertex AI
- gemini-2.5-flash模型
- FastAPI
- Google Firestore
- Chainlit
- Docker
- Google Cloud Run
- all-MiniLM-L6-v2模型（用于语义相似度计算）

### 方法优势

- 创新性地将反事实解释与对话式推荐结合，实现非强制性可持续助推。
- 模块化多智能体架构设计清晰，各智能体职责明确，便于扩展和维护。
- 通过用户研究和语义度量进行多维度评估，验证了系统在可持续性、用户信任和交互响应方面的平衡。
- 开源完整实现，包括代码、Docker配置和演示视频，可重复性强。

### 主要局限

- 当前仅支持单一欧洲城市旅行，不支持多城市或多日行程。
- 存在可持续性悖论：持续推荐“隐藏宝石”可能无意中创造新热点，转移而非减少过度旅游。
- 用户研究样本量较小（24人），且主要通过社交媒体和大学邮件列表招募，可能引入偏差。
- 系统平均延迟23秒，对于实时交互仍有优化空间。

### 与当前研究方向的关联

该论文直接涉及对话式推荐系统（Conversational Recommender Systems）、大语言模型（LLMs）、多智能体系统（Multi-Agent Systems）、可持续旅游（Sustainable Tourism）和反事实解释（Counterfactual Explanations）等关键词。论文提出的TRACE框架正是这些技术的综合应用，与推荐系统领域的前沿方向高度相关。

---

_知识库更新时间：2026-07-16T03:56:50.204027_
