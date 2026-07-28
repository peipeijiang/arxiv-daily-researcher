---
title: "Lasso：基于大语言模型的跨域推荐用户模拟器"
paper_id: "https://doi.org/10.1145/3705328.3748048"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 48.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# Lasso：基于大语言模型的跨域推荐用户模拟器

> **英文原标题**：Lasso: Large Language Model-based User Simulator for Cross-Domain Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/ChenYZWCLL25) · [Semantic Scholar](https://www.semanticscholar.org/paper/60ae69738509059e0a621af933c116f7b316f8d0)

## 一句话结论

> 提出Lasso框架，利用大语言模型作为用户模拟器，通过跨域训练和个性化候选池、置信度引导模块，有效缓解跨域推荐中的冷启动问题，减少对重叠用户历史交互的依赖。

## 论文信息

- **作者**：Yue Chen, Susen Yang, Tong Zhang, Chao Wang, Mingyue Cheng, Chenyi Lei, Han Li
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：48.0
- **DOI**：[https://doi.org/10.1145/3705328.3748048](https://doi.org/10.1145/3705328.3748048)

<details open>
<summary><strong>中文摘要</strong></summary>

跨域推荐（Cross-Domain Recommendation, CDR）旨在通过利用源域中的用户交互来缓解目标域中的冷启动问题。然而，现有的CDR方法往往数据效率低下，因为它们需要大量重叠用户的历史交互数据进行训练，这在实际场景中并不现实。为应对这一挑战，我们提出了Lasso框架，该框架利用大型语言模型（Large Language Model, LLM）作为用户模拟器，基于LLM卓越的内部知识来捕捉跨域用户偏好。具体而言，我们引入了一种跨域训练范式来微调基于LLM的模拟器，使其能够利用源域的历史交互数据模拟用户在目标域中的行为。此外，为提升Lasso的效率和准确性，我们提出了两个有效模块：个性化候选池（Personalized Candidate Pool, PCP）和置信度引导推理（Confidence-Guided Inference, CGI）。PCP模块采用跨域协同过滤，为每个目标域中的冷启动用户构建定制的候选项目集，以模拟其交互行为，从而提高LLM的推理效率。CGI模块则利用LLM的置信度分数降低模拟数据中的噪声，确保更准确的估计。在应用阶段，模拟交互数据作为下游推荐模型的额外输入，有效缓解了用户的冷启动问题。在公开基准数据集和真实工业数据集上的大量实验表明，Lasso在实现更高准确性的同时，减少了对重叠用户历史交互数据的需求。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Cross-Domain Recommendation (CDR) aims to mitigate the cold-start problem in target domains by leveraging user interactions from source domains. However, existing CDR methods often suffer from low data efficiency, as they require a substantial number of historical interactions from overlapping users for training, which is impractical in real-world scenarios. To address this challenge, we propose Lasso, a novel framework that leverages the large language model (LLM) as a user simulator to capture cross-domain user preferences based on the remarkable internal knowledge of the LLM. Specifically, we introduce a cross-domain training paradigm to fine-tune the LLM-based simulator, enabling it to simulate user behaviors in the target domain using historical interactions from the source domain. Furthermore, to enhance the efficiency and accuracy of Lasso, we propose two effective modules: Personalized Candidate Pool (PCP) and Confidence-Guided Inference (CGI). The PCP module employs cross-domain collaborative filtering to construct a tailored set of candidate items for simulating interactions of each cold-start user in the target domain, thereby improving the inference efficiency of the LLM. The CGI module utilizes confidence scores from the LLM to reduce noise in the simulated data, ensuring more accurate estimations. During the application phase, the simulated interactions serve as additional inputs for downstream recommendation models, effectively alleviating cold-start problems for users. Extensive experiments on public benchmark datasets and real-world industrial dataset demonstrate that Lasso achieves superior accuracy while requiring fewer historical interactions from overlapping users.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

跨域推荐旨在利用源域用户交互缓解目标域冷启动问题，但现有方法依赖大量重叠用户历史交互，数据效率低。本文提出Lasso框架，利用大语言模型作为用户模拟器，基于其内部知识捕获跨域用户偏好。通过跨域训练范式微调LLM模拟器，使其能用源域历史交互模拟目标域行为。为提升效率与准确性，提出个性化候选池和置信度引导推理模块：PCP通过跨域协同过滤为冷启动用户构建候选集，提高推理效率；CGI利用LLM置信度降低模拟数据噪声。应用阶段，模拟交互作为下游推荐模型的额外输入，缓解冷启动。实验表明Lasso在减少重叠用户历史交互需求的同时取得更优精度。

### 主要创新

- 提出基于LLM的用户模拟器框架，利用其内部知识实现跨域用户偏好捕获。
- 设计跨域训练范式，使LLM模拟器能从源域历史交互学习模拟目标域行为。
- 引入个性化候选池模块，通过跨域协同过滤提高LLM推理效率。
- 提出置信度引导推理模块，利用LLM置信度减少模拟数据噪声。

### 研究方法

论文采用基于LLM的用户模拟器框架，通过跨域训练范式微调LLM，使其能够根据源域历史交互模拟目标域用户行为。同时，设计个性化候选池模块（PCP）使用跨域协同过滤为每个冷启动用户构建候选项目集，以提升LLM推理效率；置信度引导推理模块（CGI）利用LLM输出的置信度分数过滤低质量模拟数据。最终，将模拟交互作为额外输入用于下游推荐模型。

### 关键结果

在公开基准数据集和工业数据集上的实验表明，Lasso在减少重叠用户历史交互需求的同时，实现了更优的推荐精度。

### 技术栈

- 大语言模型（LLM）
- 跨域协同过滤
- 个性化候选池（PCP）
- 置信度引导推理（CGI）

### 方法优势

- 创新性地将LLM作为用户模拟器，利用其内部知识减少对大量重叠用户历史交互的依赖。
- 提出PCP和CGI模块，分别提升推理效率和模拟数据质量。
- 在多个数据集上验证了有效性，包括工业数据集。

### 主要局限

- 摘要未提供具体局限性信息。当前证据仅基于摘要，无法评估模型复杂度、计算开销或对特定领域的适用性。

### 与当前研究方向的关联

论文与LLM与推荐系统结合、跨域推荐、冷启动问题、用户模拟等关键词高度相关。

---

_知识库更新时间：2026-07-28T03:53:18.339154_
