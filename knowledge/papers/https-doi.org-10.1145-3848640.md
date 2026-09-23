---
title: "一致的解释者还是不可靠的叙述者：大型语言模型在群体推荐中一致性与敏感性的系统性差异"
paper_id: "https://doi.org/10.1145/3848640"
source: "openalex"
published: "2026-09-22T00:00:00"
score: 53.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)", "Topic Modeling"]
---

# 一致的解释者还是不可靠的叙述者：大型语言模型在群体推荐中一致性与敏感性的系统性差异

> **英文原标题**：Consistent Explainers or Unreliable Narrators: Systematic Differences in Consistency and Sensitivity Across Large Language Models for Group Recommendations

[查看原文](https://doi.org/10.1145/3848640)

## 一句话结论

> 本文分析了大语言模型在群组推荐中作为决策者和解释生成器的表现，发现模型家族是推荐质量和解释一致性的主要差异来源，GPT-OSS提供一致排序而Mistral对领域和群组配置更敏感。

## 论文信息

- **作者**：Cedric Waterschoot, Nava Tintarev, Francesco Barile
- **来源**：ACM Transactions on Recommender Systems
- **发布时间**：2026-09-22
- **相关度评分**：53.0
- **DOI**：[https://doi.org/10.1145/3848640](https://doi.org/10.1145/3848640)

<details open>
<summary><strong>中文摘要</strong></summary>

群体推荐系统（Group Recommender Systems, GRS）面临的核心挑战在于如何整合相互冲突的个体偏好。尽管大语言模型（Large Language Models, LLMs）正日益被整合到群体推荐系统中，但它们可能引入输出不一致或对群体特征敏感等风险。本文分析了LLMs在群体推荐中同时充当决策者和解释生成者的角色。我们贡献了一个新颖的数据集，包含虚构的群体偏好、前10项推荐以及自然语言解释。解释由多个LLMs生成，用以检验模型家族（GPT-OSS与Mistral）和模型规模之间的差异。我们的方法在不同领域（抽象、低风险、高风险）和群体配置（一致型、分歧型、联盟型或少数型）下，将推荐结果和解释与传统的基于社会选择的聚合策略进行评估比较。研究发现，LLM主干模型的选择是推荐质量及解释中所述推荐程序差异的主要驱动因素。我们发现模型家族之间存在明显分歧。GPT-OSS提供了较为一致的排序，而Mistral则对领域和群体配置表现出更高的敏感性。虽然未发现领域和群体配置的主效应，但显著的高阶交互作用表明，性能效应在配置、领域和聚合策略的特定组合中持续存在。我们进一步讨论了LLMs在缓解冷启动问题和群体调解中的作用，以及透明度和隐私等局限性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Group Recommender Systems (GRS) face the challenge of combining conflicting individual preferences. While Large Language Models (LLMs) are increasingly integrated into GRS, they may introduce risks regarding output inconsistency or sensitivity to group characteristics. In this paper, we analyze LLMs acting as both decision-makers and explanation generators for group recommendations. We contribute a novel dataset featuring fictitious group preferences, top-10 recommendations, and natural language explanations. Explanations are generated across multiple LLMs, testing differences between model families ( GPT-OSS vs. Mistral ) and model sizes. Our methodology evaluates recommendations and explanations against traditional social choice-based aggregation strategies across domains (abstract, low-stakes, high-stakes) and group configurations (uniform, divergent, coalitional, or minority). Findings reveal that the choice of LLM backbone is the primary driver of variance in recommendation quality and recommendation procedures detailed in the explanations. We found a clear divergence across model families. GPT-OSS provided consistent rankings, while Mistral exhibited more sensitivity to domain and group configurations. While main effects for domain and group configuration were not found, significant higher-order interactions suggest performance effects persist in specific combinations of configuration, domain, and aggregation strategy. We further discuss LLM roles in mitigating cold-start issues and group moderation, alongside drawbacks like transparency and privacy.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

群体推荐系统（GRS）面临整合冲突个体偏好的挑战。随着大型语言模型（LLM）被越来越多地集成到GRS中，它们可能引入输出不一致或对群体特征敏感的风险。本文分析了LLM在群体推荐中同时作为决策者和解释生成者的角色。作者贡献了一个新数据集，包含虚构的群体偏好、前10推荐和自然语言解释。解释由多个LLM生成，测试模型家族（GPT-OSS vs. Mistral）和模型大小之间的差异。方法评估推荐和解释，对照传统基于社会选择的聚合策略，跨领域（抽象、低风险、高风险）和群体配置（均匀、分歧、联盟或少数）。研究发现，LLM骨干的选择是推荐质量和解释中推荐程序方差的主要驱动因素。模型家族之间存在明显分歧：GPT-OSS提供一致的排名，而Mistral对领域和群体配置表现出更高的敏感性。虽然领域和群体配置的主效应未发现，但显著的高阶交互表明性能效应在配置、领域和聚合策略的特定组合中持续存在。作者进一步讨论了LLM在缓解冷启动问题和群体调节中的作用，以及透明度和隐私等缺点。

### 主要创新

- 贡献了一个新的数据集，包含虚构的群体偏好、前10推荐和自然语言解释，用于分析LLM在群体推荐中的表现。
- 同时分析LLM作为决策者和解释生成者的角色，评估推荐质量和解释的一致性。
- 系统比较了不同模型家族（GPT-OSS vs. Mistral）和模型大小在群体推荐中的差异。
- 评估了跨领域（抽象、低风险、高风险）和群体配置（均匀、分歧、联盟、少数）的推荐和解释，并与传统社会选择聚合策略对比。
- 揭示了LLM骨干选择是推荐质量和解释中推荐程序方差的主要驱动因素，并发现模型家族间的明显分歧。

### 研究方法

论文使用了一个新构建的数据集，包含虚构的群体偏好、前10推荐和自然语言解释。解释由多个LLM生成，测试模型家族（GPT-OSS vs. Mistral）和模型大小之间的差异。评估方法将推荐和解释与传统的基于社会选择的聚合策略进行对比，覆盖不同领域（抽象、低风险、高风险）和群体配置（均匀、分歧、联盟或少数）。通过分析主效应和高阶交互来评估推荐质量和解释的一致性及敏感性。

### 关键结果

LLM骨干的选择是推荐质量和解释中推荐程序方差的主要驱动因素。；模型家族之间存在明显分歧：GPT-OSS提供一致的排名，而Mistral对领域和群体配置表现出更高的敏感性。；领域和群体配置的主效应未发现，但显著的高阶交互表明性能效应在配置、领域和聚合策略的特定组合中持续存在。；讨论了LLM在缓解冷启动问题和群体调节中的作用，以及透明度和隐私等缺点。

### 技术栈

- 大型语言模型（LLM）
- GPT-OSS
- Mistral
- 传统社会选择-based聚合策略

### 方法优势

- 提出了一个新颖的数据集，支持对LLM在群体推荐中决策和解释生成的系统分析。
- 系统比较了不同模型家族和模型大小，揭示了模型选择对推荐质量和解释一致性的重要影响。
- 跨领域和群体配置的评估设计全面，考虑了多种实际场景。
- 发现了模型家族间的明显分歧，为实际应用中选择LLM提供了依据。
- 讨论了LLM在群体推荐中的潜在优势和缺点，如冷启动缓解与透明度、隐私问题。

### 主要局限

- 论文局限：摘要未提供具体实验数字、数据集规模、基线模型、损失函数或消融实验等细节。
- 论文局限：仅基于虚构的群体偏好，可能无法完全反映真实世界群体推荐的复杂性。
- 论文局限：未深入探讨LLM解释的透明度和隐私问题的具体解决方案。
- 当前证据局限：仅提供摘要，无法确认具体模型名称、数据集、基线、损失函数、参数或实现细节。
- 当前证据局限：摘要未披露实验的统计显著性水平、效应大小或具体评估指标。

### 与当前研究方向的关联

论文与推荐系统领域的最新学术研究高度相关，特别是LLM与推荐系统结合、群体推荐、推荐解释生成、公平性和鲁棒性。它关注LLM在群体推荐中的一致性和敏感性，涉及模型家族差异和群体配置影响，与关键词中的‘LLM与推荐系统结合’、‘推荐系统的因果性、公平性、鲁棒性’直接相关。同时，论文讨论的冷启动问题和群体调节也与‘用户建模’和‘工业落地’有一定关联。但论文未涉及序列推荐、生成式推荐、多模态推荐、对话式推荐、排序与重排、CTR/CVR预测等关键词。

## 代码与复现

- [Cwaterschoot/Consistent-Explainers-or-Unreliable-Narrators](https://github.com/Cwaterschoot/Consistent-Explainers-or-Unreliable-Narrators)：likely，置信度 50，Stars 0

---

_知识库更新时间：2026-09-23T05:05:07.848532_
