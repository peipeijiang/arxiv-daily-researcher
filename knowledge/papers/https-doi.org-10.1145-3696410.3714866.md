---
title: "通过协调双动态索引机制释放LLM在序列推荐中的潜力"
paper_id: "https://doi.org/10.1145/3696410.3714866"
source: "www"
published: "2025-01-01T00:00:00"
score: 74.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Customer churn and segmentation", "Image Retrieval and Classification Techniques"]
---

# 通过协调双动态索引机制释放LLM在序列推荐中的潜力

> **英文原标题**：Unleash LLMs Potential for Sequential Recommendation by Coordinating Dual Dynamic Index Mechanism

[查看原文](https://dblp.org/rec/conf/www/0005ZL00HZ0SD0Z25) · [Semantic Scholar](https://www.semanticscholar.org/paper/f870e3e2ba564bbe5138d5d166797b5dd6070812)

## 一句话结论

> 提出ED2推荐器，通过双动态索引机制将索引生成与序列推荐统一到LLM管道中，并利用用户相关信息，在三个数据集上平均提升Hit-Rate 19.62%和NDCG 21.11%。

## 论文信息

- **作者**：Jun Yin, Zhengxin Zeng, Mingzheng Li, Hao Yan, Chaozhuo Li, Weihao Han, Jianjin Zhang, Ruochen Liu, Hao Sun, Weiwei Deng, Feng Sun, Qi Zhang, Shirui Pan, Senzhang Wang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：74.0
- **DOI**：[https://doi.org/10.1145/3696410.3714866](https://doi.org/10.1145/3696410.3714866)

<details open>
<summary><strong>中文摘要</strong></summary>

由于大语言模型（LLMs）在语义理解与逻辑推理方面展现出前所未有的能力，其在开发下一代序列推荐系统（RSs）中已显示出巨大潜力。然而，现有基于LLM的序列推荐系统大多将索引生成与序列推荐分离，导致语义信息与协同信息整合不足。另一方面，对用户相关信息的忽视阻碍了基于LLM的序列推荐系统利用高阶用户-物品交互模式。本文提出端到端双动态（ED2）推荐器，这是首个采用双动态索引机制的基于LLM的序列推荐系统，旨在同时解决上述局限性。双动态索引机制不仅能够将索引生成与序列推荐整合至统一的LLM主干流水线中，还能使基于LLM的序列推荐系统有效利用用户相关信息。具体而言，为增强LLM对双动态索引的理解能力，我们提出多粒度令牌调节器，该调节器基于LLM的语义知识在多个表示粒度上构建对齐监督。此外，我们专门定制了关联用户集合数据及一系列新型指令微调任务，以捕获高阶用户-物品交互模式。在三个公开数据集上的大量实验证明了ED2的优越性，其在命中率（Hit-Rate）上平均提升19.62%，在归一化折损累计增益（NDCG）上平均提升21.11%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Owing to the unprecedented capability in semantic understanding and logical reasoning, large language models (LLMs) have shown fantastic potential in developing next-generation sequential recommender systems (RSs). However, existing LLM-based sequential RSs mostly separate index generation from sequential recommendation, leading to insufficient integration between semantic information and collaborative information. On the other hand, the neglect of user-related information hinders LLM-based sequential RSs from exploiting high-order user-item interaction patterns. In this paper, we propose the End-to-End Dual Dynamic (ED2) recommender, the first LLM-based sequential RS which adopts dual dynamic index mechanism, targeting resolving the above limitations simultaneously. The dual dynamic index mechanism can not only assembly index generation and sequential recommendation into a unified LLM-backbone pipeline, but also make it practical for LLM-based sequential recommender to take advantage of user-related information. Specifically, to facilitate the LLM comprehension ability to dual dynamic index, we propose a multigrained token regulator which constructs alignment supervision based on LLMs semantic knowledge across multiple representation granularities. Moreover, the associated user collection data and a series of novel instruction tuning tasks are specially customized to capture the high-order user-item interaction patterns. Extensive experiments on three public datasets demonstrate the superiority of ED2, achieving an average improvement of 19.62% in Hit-Rate and 21.11% in NDCG.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

大型语言模型（LLMs）在语义理解和逻辑推理方面展现出卓越能力，为开发下一代序列推荐系统（RSs）提供了巨大潜力。然而，现有的基于LLM的序列推荐系统大多将索引生成与序列推荐分离，导致语义信息与协同信息整合不足；同时，忽略用户相关信息阻碍了模型利用高阶用户-物品交互模式。本文提出端到端双动态（ED2）推荐器，这是首个采用双动态索引机制的基于LLM的序列推荐系统，旨在同时解决上述限制。双动态索引机制不仅将索引生成和序列推荐整合到统一的LLM骨干流水线中，还使基于LLM的序列推荐器能够利用用户相关信息。具体地，为促进LLM对双动态索引的理解，提出多粒度令牌调节器，基于LLM的语义知识跨多个表示粒度构建对齐监督。此外，定制了关联用户收集数据和一系列新颖的指令调优任务，以捕获高阶用户-物品交互模式。在三个公开数据集上的大量实验表明ED2的优越性，平均在Hit-Rate上提升19.62%，在NDCG上提升21.11%。

### 主要创新

- 首次提出双动态索引机制，将索引生成与序列推荐整合到统一的LLM骨干流水线中。
- 双动态索引机制使基于LLM的序列推荐器能够利用用户相关信息。
- 提出多粒度令牌调节器，基于LLM语义知识跨多个表示粒度构建对齐监督。
- 定制关联用户收集数据和一系列新颖的指令调优任务，以捕获高阶用户-物品交互模式。

### 研究方法

论文采用端到端双动态（ED2）推荐器，核心是双动态索引机制，将索引生成和序列推荐统一在LLM骨干中。通过多粒度令牌调节器促进LLM对双动态索引的理解，利用关联用户收集数据和指令调优任务捕获高阶交互模式。实验在三个公开数据集上进行，评估指标为Hit-Rate和NDCG。

### 关键结果

在三个公开数据集上，ED2平均在Hit-Rate上提升19.62%，在NDCG上提升21.11%。

### 技术栈

- 大型语言模型（LLMs）
- 双动态索引机制
- 多粒度令牌调节器
- 指令调优任务

### 方法优势

- 首次将索引生成与序列推荐统一在LLM流水线中，实现端到端优化。
- 有效整合语义信息和协同信息，同时利用用户相关信息。
- 在三个公开数据集上取得显著性能提升，平均Hit-Rate提升19.62%，NDCG提升21.11%。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估模型复杂度、泛化能力或潜在缺陷。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、LLM与推荐系统结合高度相关，直接针对序列推荐中的索引生成与推荐分离问题，并利用LLM能力。与推荐智能体、多模态推荐、对话式推荐等关键词相关性较低。

## 代码与复现

- [Esperanto-mega/ED2](https://github.com/Esperanto-mega/ED2)：possible，置信度 30，Stars 11

---

_知识库更新时间：2026-07-13T06:43:12.874653_
