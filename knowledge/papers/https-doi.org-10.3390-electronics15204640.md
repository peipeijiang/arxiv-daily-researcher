---
title: "模拟用户以评估推荐系统中LLM生成解释：一个统一智能体框架与初步结果的实证研究"
paper_id: "https://doi.org/10.3390/electronics15204640"
source: "citation"
published: "2026-10-11T00:00:00"
score: 73.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)", "Information Retrieval and Search Behavior"]
---

# 模拟用户以评估推荐系统中LLM生成解释：一个统一智能体框架与初步结果的实证研究

> **英文原标题**：Simulating Users to Evaluate LLM-Generated Explanations in Recommender Systems: A Unified Agentic Framework and Empirical Study with Preliminary Results

[查看原文](https://doi.org/10.3390/electronics15204640)

## 一句话结论

> 论文针对 LLM 生成的推荐解释难以忠实且难以严格评估的问题，提出一个耦合 RecoWorld 模拟环境、RecBole 策略引擎和 LLM 用户智能体的统一三层智能体框架，在 MovieLens-32M 上对 BPR、ConvNCF、NeuMF 策略生成的解释进行多样性、忠实性、反事实和可读性评估及 LLM 用户访谈模拟，发现解释高度忠实且个性化，但模拟用户对清晰度评分最高而对信任度评分最低。

## 论文信息

- **作者**：Ionuţ-Dragoş Neremzoiu, Costin Bădică
- **来源**：Electronics
- **发布时间**：2026-10-11
- **相关度评分**：73.0
- **DOI**：[https://doi.org/10.3390/electronics15204640](https://doi.org/10.3390/electronics15204640)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型（LLMs）正日益被同时用作推荐器和推荐解释的生成器，然而生成忠实的、以用户为中心的解释并对其进行严格评估仍然是未解决的难题，推荐系统研究中已有文献记录的可复现性危机更加剧了这一困境。在本工作中，我们将推荐形式化为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process），并提出了一个统一的三层智能体框架，该框架将模拟环境（RecoWorld）、可复现的策略引擎（RecBole）和认知型LLM用户智能体耦合在一起。作为该框架在MovieLens-32M数据集上的离线单轮验证，我们对传统策略（贝叶斯个性化排序（BPR）、卷积神经协同过滤和神经矩阵分解（NeuMF））的初步单轮检查点进行了基准测试，从BPR推荐结果生成基于LLM的解释，并在约一百万用户-物品对上用量化的多样性、忠实性、反事实和可读性指标对其进行评分，同时运行了一项LLM作为用户的访谈模拟，其中由Qwen2.5解释器生成的解释由Llama-3受访者通过六标准解释质量调查进行评估；在2000名用户上的受控比较表明，将BPR替换为更准确的NeuMF策略后，这些调查得分实际上保持不变。生成的解释被证明具有高度忠实性（特征精确率0.9996，充分性0.9999）和用户定制化特征（唯一句子比率0.9978），模拟用户对清晰度评分最高（3.86/5），但对信任度评分最低（2.60/5）。因此，忠实的模板解释被信任的程度低于被理解的程度，这促使我们转向可控的生成式解释和可扩展的模拟评估。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models (LLMs) are increasingly used both as recommenders and to explain recommendations, yet producing faithful, user-centric explanations and evaluating them rigorously remain open problems, compounded by a documented reproducibility crisis in recommender systems research. In this work we formalise recommendation as a Partially Observable Markov Decision Process and propose a unified, three-tier agentic framework that couples a simulation environment (RecoWorld), a reproducible policy engine (RecBole), and a cognitive LLM user agent. As an offline, single-turn validation of this framework on the MovieLens-32M dataset, we benchmark preliminary single-epoch checkpoints of traditional policies (Bayesian Personalized Ranking (BPR), Convolutional Neural Collaborative Filtering and Neural Matrix Factorisation (NeuMF)), generate LLM-based explanations from the BPR recommendations and score them with quantitative diversity, faithfulness, counterfactual and readability metrics over roughly one million user-item pairs, and run an LLM-as-user interview simulation in which explanations produced by a Qwen2.5 explainer are assessed by a Llama-3 respondent through a six-criterion explanation-quality survey; a controlled comparison on 2000 users shows that replacing BPR with the more accurate NeuMF policy leaves these survey scores practically unchanged. The generated explanations prove highly faithful (feature precision 0.9996, sufficiency 0.9999) and user-tailored explanations (unique-sentence ratio 0.9978), and simulated users rate clarity highest (3.86/5) yet trust lowest (2.60/5). Faithful template explanations are, therefore, trusted less than they are understood, motivating a shift towards controllable generative explanation and scalable simulated evaluation.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

大语言模型（LLM）日益被用于推荐与解释推荐，但生成忠实、以用户为中心的解释并严格评估仍是开放问题，且推荐系统研究存在可复现性危机。本文将推荐形式化为部分可观测马尔可夫决策过程，提出一个统一的三层智能体框架，耦合模拟环境（RecWorld）、可复现策略引擎（RecBole）和认知LLM用户智能体。在MovieLens-32M数据集上的离线单轮验证中，作者对传统策略（BPR、卷积神经协同过滤、NeuMF）的初步单轮检查点进行基准测试，从BPR推荐生成LLM解释，并在约一百万用户-物品对上用多样性、忠实性、反事实和可读性指标评分，同时运行LLM作为用户的访谈模拟：Qwen2.5解释器生成的解释由Llama-3受访者通过六标准解释质量调查评估；在2000用户上的受控比较显示，用更准确的NeuMF替换BPR后调查分数几乎不变。生成解释高度忠实（特征精度0.9996，充分性0.9999）且用户定制（唯一句子比例0.9978），模拟用户对清晰度评分最高（3.86/5）但信任最低（2.60/5）。忠实的模板解释被理解却信任不足，促使转向可控生成解释和可扩展模拟评估。

### 主要创新

- 将推荐形式化为部分可观测马尔可夫决策过程，并提出统一的三层智能体框架，耦合模拟环境RecWorld、可复现策略引擎RecBole和认知LLM用户智能体。
- 在MovieLens-32M数据集上对传统策略（BPR、卷积神经协同过滤、NeuMF）的初步单轮检查点进行基准测试，并生成LLM解释。
- 在约一百万用户-物品对上使用多样性、忠实性、反事实和可读性指标定量评估LLM生成的解释。
- 运行LLM作为用户的访谈模拟，由Qwen2.5解释器生成解释、Llama-3受访者通过六标准解释质量调查评估。
- 通过2000用户受控比较发现，用更准确的NeuMF替换BPR后调查分数几乎不变，并揭示忠实模板解释被理解却信任不足的现象。

### 研究方法

论文将推荐形式化为部分可观测马尔可夫决策过程，提出统一的三层智能体框架：模拟环境（RecWorld）、可复现策略引擎（RecBole）和认知LLM用户智能体。在MovieLens-32M数据集上进行离线单轮验证，基准测试传统策略（BPR、卷积神经协同过滤、NeuMF）的初步单轮检查点；从BPR推荐生成LLM解释，并在约一百万用户-物品对上用多样性、忠实性、反事实和可读性指标评分；运行LLM作为用户的访谈模拟，其中Qwen2.5解释器生成的解释由Llama-3受访者通过六标准解释质量调查评估；在2000用户上进行受控比较，替换BPR为NeuMF。

### 关键结果

生成解释高度忠实：特征精度0.9996，充分性0.9999。；生成解释用户定制：唯一句子比例0.9978。；模拟用户对解释清晰度评分最高（3.86/5），但信任最低（2.60/5）。；在2000用户上的受控比较显示，用更准确的NeuMF替换BPR后，六标准解释质量调查分数几乎不变。；忠实的模板解释被理解却信任不足，促使转向可控生成解释和可扩展模拟评估。

### 技术栈

- 大语言模型（LLM）
- 部分可观测马尔可夫决策过程（POMDP）
- RecWorld（模拟环境）
- RecBole（可复现策略引擎）
- 认知LLM用户智能体
- 贝叶斯个性化排序（BPR）
- 卷积神经协同过滤
- 神经矩阵分解（NeuMF）
- Qwen2.5（解释器）
- Llama-3（受访者）
- 多样性、忠实性、反事实和可读性指标
- 六标准解释质量调查

### 方法优势

- 提出统一的三层智能体框架，整合模拟环境、可复现策略引擎和认知LLM用户智能体，结构清晰。
- 在MovieLens-32M数据集上进行大规模评估，覆盖约一百万用户-物品对，具有实证规模。
- 同时采用定量指标（多样性、忠实性、反事实、可读性）和LLM作为用户的访谈模拟，评估维度较全面。
- 通过2000用户受控比较检验策略替换对调查分数的影响，增强了结论的稳健性。
- 揭示忠实模板解释被理解却信任不足的现象，为可控生成解释和模拟评估提供动机。

### 主要局限

- 论文局限：摘要明确为离线、单轮验证，且使用初步单轮检查点，可能限制结论的泛化性。
- 论文局限：仅报告了初步结果，未涉及多轮交互或在线部署验证。
- 论文局限：受控比较仅涉及BPR与NeuMF两种策略，未覆盖更多策略或解释生成方法。
- 当前证据局限：仅提供摘要，未披露具体实现细节、超参数、消融实验、损失函数或完整实验设置。
- 当前证据局限：摘要未提供关于可复现性危机如何被具体解决的细节，也未提供代码或数据公开信息。

### 与当前研究方向的关联

论文与多个研究关键词高度相关：涉及LLM与推荐系统结合（LLM生成解释、LLM用户智能体）、推荐智能体（三层智能体框架）、用户建模（认知LLM用户智能体、模拟用户访谈）、排序与重排（传统策略基准测试）、以及推荐系统的可复现性（RecBole策略引擎、可复现性危机）。同时涉及生成式推荐（LLM生成解释）和评估方法（多样性、忠实性、反事实、可读性指标）。与序列推荐、多模态推荐、对话式推荐、CTR/CVR预测、因果性、公平性、鲁棒性和工业落地的直接相关性在摘要中未明确体现。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-10-14T05:16:32.946152_
