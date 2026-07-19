---
title: "基于推理的意图注入用于生成式推荐"
paper_id: "https://doi.org/10.1145/3805712.3808423"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 66.0
tags: ["paper", "recommender-systems"]
---

# 基于推理的意图注入用于生成式推荐

> **英文原标题**：Reasoning-Grounded Intent Injection for Generative Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/ChenGLZHQLWFCPL26)

## 一句话结论

> 提出RIGER框架，通过离线LLM推理蒸馏和在线意图注入，在生成式推荐中实现主动意图探索，在电商广告系统中提升点击率1.6%和广告花费1.3%。

## 论文信息

- **作者**：Xusong Chen, Peini Guo, Fang Liu, Yu Zhao, Yiyang Hu, Mengqin Que, Peng Li, Haoran Wang, Zhiwei Fang, Wenlong Chen, Changping Peng, Ching Law
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：66.0
- **DOI**：[https://doi.org/10.1145/3805712.3808423](https://doi.org/10.1145/3805712.3808423)

<details open>
<summary><strong>中文摘要</strong></summary>

在基于离散语义ID（SID）的工业生成式推荐系统中，其运作主要依赖行为驱动，因此难以在用户显式信号出现之前主动激活潜在需求，从而导致意图冷启动问题。为解决这一问题，我们提出RIGER（基于推理的意图注入生成式推荐），这是一个可部署的两阶段框架，在严格的延迟约束下将离线大语言模型（LLM）推理能力集成到在线生成式推荐器中。在离线阶段，为确保可扩展部署，我们通过自动化数据整理流程——利用基于评判器的提示校准与基于未来查询的拒绝过滤——将强LLM的潜在意图推理能力蒸馏至轻量级预测模型。在线阶段，为弥合自由形式文本意图与离散SID令牌空间之间的表征不匹配，预测的意图通过基于行为的映射转换为SID原生令牌，并注入已部署的仅解码器检索主干网络。我们进一步采用波束感知GRPO对模型进行微调，在SID空间中引入分层意图对齐探索奖励，同时通过KL正则化保留利用行为。离线评估表明，在仅略微降低事后召回率的情况下，意图对齐密度与多样性显著提升，说明RIGER在保持历史行为利用能力的同时，有效增强了主动意图探索。在一个大规模电商展示广告系统中，RIGER使点击量提升1.6%，广告主支出提升1.3%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Industrial generative recommendation systems operating over discrete Semantic IDs (SIDs) are largely behavior-driven, and thus struggle to proactively activate latent demand before explicit user signals emerge, leading to intent cold-start. To address this, we propose RIGER (Reasoning-grounded Intent injection for GE nerative Recommendation), a deployable two-stage framework that integrates offline large language model (LLM) reasoning into an online generative recommender under strict latency constraints. Offline, to ensure scalable deployment, we distill the latent-intent inference capability of a strong LLM into a lightweight forecasting model using an automated data curation pipeline---leveraging judge-guided prompt calibration and future-query-guided rejection filtering. Online, to bridge the representation mismatch between free-form textual intents and the discrete SID token space, predicted intents are converted into SID-native tokens through a behavior-grounded mapping and injected into the deployed decoder-only retrieval backbone. We further fine-tune the model with beam-aware GRPO, introducing a hierarchical intent-alignment exploration reward in SID space while preserving exploitation behavior through KL regularization. Offline evaluations demonstrate a substantial increase in intent-aligned density and diversity with only a marginal reduction in hindsight recall, indicating that RIGER effectively enhances proactive intent exploration while preserving its capability to exploit historical behaviors. In a large-scale e-commerce display advertising system, RIGER improves clicks by 1.6% and advertiser spend by 1.3%.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

工业生成式推荐系统通常基于离散语义ID（SID）的行为驱动，难以在用户显式信号出现前主动激活潜在需求，导致意图冷启动。为此，本文提出RIGER（基于推理的意图注入用于生成式推荐），一个可部署的两阶段框架，在严格延迟约束下将离线大语言模型（LLM）推理集成到在线生成式推荐器中。离线阶段，通过自动化数据整理流程（利用法官引导的提示校准和未来查询引导的拒绝过滤）将强LLM的潜在意图推理能力蒸馏到轻量级预测模型中，确保可扩展部署。在线阶段，为解决自由形式文本意图与离散SID令牌空间之间的表示不匹配，通过行为基础映射将预测意图转换为SID原生令牌，并注入到部署的解码器仅检索骨干中。进一步使用波束感知GRPO微调模型，在SID空间中引入分层意图对齐探索奖励，同时通过KL正则化保留利用行为。离线评估显示，意图对齐密度和多样性显著增加，而事后召回率仅略有下降，表明RIGER有效增强主动意图探索，同时保留利用历史行为的能力。在大型电子商务展示广告系统中，RIGER使点击率提升1.6%，广告主支出提升1.3%。

### 主要创新

- 提出RIGER两阶段框架，将离线LLM推理集成到在线生成式推荐中，解决意图冷启动问题。
- 设计自动化数据整理流程，通过法官引导的提示校准和未来查询引导的拒绝过滤，将LLM的潜在意图推理能力蒸馏到轻量级模型。
- 提出行为基础映射，将自由形式文本意图转换为SID原生令牌，解决表示不匹配。
- 引入波束感知GRPO，在SID空间中实现分层意图对齐探索奖励，并通过KL正则化保留利用行为。

### 研究方法

论文采用两阶段框架：离线阶段，使用自动化数据整理流程（包括法官引导的提示校准和未来查询引导的拒绝过滤）将强LLM的潜在意图推理能力蒸馏到轻量级预测模型；在线阶段，通过行为基础映射将预测意图转换为SID原生令牌，注入到解码器仅检索骨干，并使用波束感知GRPO微调模型，结合分层意图对齐探索奖励和KL正则化。

### 关键结果

离线评估显示意图对齐密度和多样性显著增加，事后召回率仅略有下降。；在大型电子商务展示广告系统中，点击率提升1.6%，广告主支出提升1.3%。

### 技术栈

- 大语言模型（LLM）
- 轻量级预测模型
- 离散语义ID（SID）
- 波束感知GRPO
- KL正则化
- 法官引导的提示校准
- 未来查询引导的拒绝过滤
- 行为基础映射

### 方法优势

- 提出可部署的两阶段框架，在严格延迟约束下集成LLM推理，具有实际工业应用价值。
- 自动化数据整理流程减少人工标注成本，提升可扩展性。
- 通过行为基础映射和波束感知GRPO有效解决意图与SID空间的表示不匹配。
- 离线评估和在线A/B测试均验证了方法的有效性，提升点击率和广告支出。

### 主要局限

- 论文局限：摘要未提供消融实验、不同基线对比或超参数敏感性分析。
- 当前证据局限：仅基于摘要，无法评估方法在其他场景的泛化性、计算开销或失败案例。

### 与当前研究方向的关联

该论文与生成式推荐、LLM与推荐系统结合、序列推荐、工业落地高度相关。它聚焦于生成式推荐中的意图冷启动问题，利用LLM推理增强推荐主动性，并在工业广告系统中验证，覆盖了用户建模、CTR/CVR预测等关键词。

---

_知识库更新时间：2026-07-19T04:08:52.138699_
