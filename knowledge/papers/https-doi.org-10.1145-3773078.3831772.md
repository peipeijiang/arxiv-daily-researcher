---
title: "BiLPR：面向情境感知学习路径推荐的双向师生智能体交互"
paper_id: "https://doi.org/10.1145/3773078.3831772"
source: "citation"
published: "2026-09-25T00:00:00"
score: 41.0
tags: ["paper", "recommender-systems"]
---

# BiLPR：面向情境感知学习路径推荐的双向师生智能体交互

> **英文原标题**：BiLPR: Bidirectional Teacher-Student Agent Interaction for Context-Aware Learning Path Recommendation

[查看原文](https://doi.org/10.1145/3773078.3831772)

## 一句话结论

> 针对现有学习路径推荐缺乏双向交互和动态上下文感知的问题，本文提出双向教师-学生智能体交互框架BiLPR，在Junyi和ASSIST2009数据集上显著提升了推荐效果。

## 论文信息

- **作者**：Zejun Chen, Weiwei Chen, Suojuan Zhang, Zhi Zheng, Dawei Jin, Ziwei Zhao, Tong Xu, Cui Jing, Jiaqi Long, Enhong Chen
- **来源**：Proceedings of the 20th ACM Conference on Recommender Systems
- **发布时间**：2026-09-25
- **相关度评分**：41.0
- **DOI**：[https://doi.org/10.1145/3773078.3831772](https://doi.org/10.1145/3773078.3831772)

<details open>
<summary><strong>中文摘要</strong></summary>

学习路径推荐是智能教育系统的关键组成部分，旨在根据每个学生的认知状态为其规划个性化的学习资源序列。现有方法主要依赖单向建模进行推荐，未能充分捕捉教师与学生之间的双向交互。这导致缺乏反馈驱动的自适应机制，难以形成有效的教学闭环。此外，当前的学习路径推荐通常局限于静态的学生-习题匹配，无法感知和响应动态的学习情境，从而导致适应性不足。这一局限源于对关键情境因素考虑不充分，包括实时认知状态、交互历史、习题语义和知识结构。为解决这些问题，本文提出了一种面向情境感知学习路径推荐的双向师生智能体交互方法（Bidirectional Teacher-Student Agent Interaction for Context-Aware Learning Path Recommendation，BiLPR），实现了双向、动态且协同的过程。具体而言，教师智能体（Teacher Agent）融合领域知识图谱与语义推理，深入挖掘学习情境特征，从而在知识迁移的支撑下实现动态习题适配与推荐策略。学生智能体（Student Agent）模拟真实学习过程中动态认知状态和行为的演化，并对其表现提供反馈。这种交互建立了一种新颖的推荐、反馈与反思的迭代闭环。在Junyi和ASSIST2009两个真实教育数据集上的评估表明，所提方法在推荐效果上显著优于基线模型。代码可在https://github.com/czj9843/BiLPR.git获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Learning path recommendation is a critical component of intelligent education systems, aiming to plan a personalized sequence of learning resources for each student based on their cognitive state. Existing methods predominantly rely on unidirectional modeling for recommendations, failing to adequately capture the bidirectional interaction between teachers and students. This leads to a lack of feedback-driven adaptation and difficulty in forming an effective instructional closed loop. Furthermore, current learning path recommendations are often limited to static student-exercise matching. They cannot perceive and respond to dynamic learning contexts, which results in insufficient adaptability. This limitation stems from an inadequate consideration of key contextual factors, including real-time cognitive states, interaction history, exercise semantics, and knowledge structures. To address these issues, this paper proposes a Bidirectional Teacher-Student Agent Interaction for Context-Aware Learning Path Recommendation (BiLPR), which implements a bidirectional, dynamic, and synergistic process. Specifically, the Teacher Agent integrates domain knowledge graphs with semantic reasoning to thoroughly mine features of the learning context. This enables dynamic exercise adaptation and recommendation strategies underpinned by knowledge transfer. The Student Agent simulates the evolution of dynamic cognitive states and behaviors during authentic learning processes, providing feedback on its performance. This interaction establishes a novel iterative closed loop of recommendation, feedback, and reflection. Evaluated on two real-world educational datasets, Junyi and ASSIST2009, the proposed method significantly outperforms baseline models in recommendation effectiveness. The code is available at https://github.com/czj9843/BiLPR.git.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

学习路径推荐是智能教育系统的关键组成部分，旨在根据学生的认知状态为其规划个性化的学习资源序列。现有方法主要依赖单向建模进行推荐，未能充分捕捉师生之间的双向交互，导致缺乏反馈驱动的适应性，难以形成有效的教学闭环。此外，当前的学习路径推荐往往局限于静态的学生-习题匹配，无法感知和响应动态学习情境，适应性不足。这一局限源于对关键情境因素（包括实时认知状态、交互历史、习题语义和知识结构）的考虑不充分。为解决这些问题，本文提出了面向情境感知学习路径推荐的双向师生智能体交互框架（BiLPR），实现了双向、动态、协同的过程。具体而言，教师智能体融合领域知识图谱与语义推理，深入挖掘学习情境特征，实现基于知识迁移的动态习题适配与推荐策略。学生智能体模拟真实学习过程中动态认知状态与行为的演化，并对其表现提供反馈。这种交互建立了推荐、反馈与反思的新型迭代闭环。在Junyi和ASSIST2009两个真实教育数据集上的评估表明，所提方法在推荐效果上显著优于基线模型。代码已开源。

### 主要创新

- 提出双向师生智能体交互框架BiLPR，实现推荐、反馈与反思的迭代闭环，突破传统单向建模的局限。
- 教师智能体融合领域知识图谱与语义推理，深入挖掘学习情境特征，支持基于知识迁移的动态习题适配与推荐策略。
- 学生智能体模拟动态认知状态与行为演化，提供表现反馈，增强推荐系统的适应性和情境感知能力。
- 在Junyi和ASSIST2009两个真实教育数据集上验证了方法的有效性，推荐效果显著优于基线模型。

### 研究方法

论文提出BiLPR框架，采用双向师生智能体交互机制。教师智能体整合领域知识图谱与语义推理，挖掘学习情境特征，进行动态习题适配和推荐策略生成；学生智能体模拟动态认知状态和行为演化，并对学习表现提供反馈。两者交互形成推荐、反馈、反思的迭代闭环。在Junyi和ASSIST2009两个真实教育数据集上进行评估，与基线模型对比推荐效果。

### 关键结果

在Junyi和ASSIST2009两个真实教育数据集上，所提方法在推荐效果上显著优于基线模型。；建立了推荐、反馈与反思的新型迭代闭环，实现了双向、动态、协同的学习路径推荐过程。

### 技术栈

- 领域知识图谱
- 语义推理
- 双向师生智能体交互
- 动态认知状态模拟
- 迭代闭环机制

### 方法优势

- 针对现有学习路径推荐中单向建模和静态匹配的不足，提出了双向动态交互框架，具有明确的问题导向。
- 教师智能体融合知识图谱与语义推理，增强了情境感知和知识迁移能力。
- 学生智能体模拟认知状态演化并提供反馈，形成了推荐-反馈-反思的闭环，提升了适应性。
- 在两个真实教育数据集上验证了方法的有效性，且代码开源，便于复现。

### 主要局限

- 论文局限：摘要未提及具体模型架构细节、损失函数、训练策略等实现信息。
- 论文局限：摘要未说明在Junyi和ASSIST2009上使用的具体评价指标和数值结果。
- 论文局限：摘要未讨论方法的计算复杂度、可扩展性或实际部署中的潜在挑战。
- 当前证据局限：仅提供摘要，无法确认基线模型的具体名称、消融实验设计及参数设置。
- 当前证据局限：无法验证方法在不同教育场景或数据分布下的泛化能力。

### 与当前研究方向的关联

该论文与推荐系统领域多个关键词高度相关：属于序列推荐（学习路径推荐本质是序列规划）；涉及推荐智能体（师生智能体交互）；与用户建模相关（学生认知状态建模）；涉及情境感知推荐（动态学习情境）；与知识图谱结合（教师智能体使用领域知识图谱）；属于教育推荐应用场景。与生成式推荐、LLM结合、多模态推荐、对话式推荐、CTR/CVR预测、因果性、公平性、鲁棒性等关键词的直接相关性在摘要中未明确体现。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-09-27T05:37:07.636490_
