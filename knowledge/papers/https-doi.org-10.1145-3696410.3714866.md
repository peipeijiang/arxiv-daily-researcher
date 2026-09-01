---
title: "通过协调双动态索引机制释放LLMs在序列推荐中的潜力"
paper_id: "https://doi.org/10.1145/3696410.3714866"
source: "www"
published: "2025-01-01T00:00:00"
score: 86.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Customer churn and segmentation", "Image Retrieval and Classification Techniques"]
---

# 通过协调双动态索引机制释放LLMs在序列推荐中的潜力

> **英文原标题**：Unleash LLMs Potential for Sequential Recommendation by Coordinating Dual Dynamic Index Mechanism

[查看原文](https://dblp.org/rec/conf/www/0005ZL00HZ0SD0Z25) · [Semantic Scholar](https://www.semanticscholar.org/paper/f870e3e2ba564bbe5138d5d166797b5dd6070812)

## 一句话结论

> 该论文提出了一种基于LLM的双动态索引机制（ED2），将索引生成与序列推荐统一，并利用用户相关信息，显著提升了序列推荐的性能。

## 论文信息

- **作者**：Jun Yin, Zhengxin Zeng, Mingzheng Li, Hao Yan, Chaozhuo Li, Weihao Han, Jianjin Zhang, Ruochen Liu, Hao Sun, Weiwei Deng, Feng Sun, Qi Zhang, Shirui Pan, Senzhang Wang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：86.0
- **DOI**：[https://doi.org/10.1145/3696410.3714866](https://doi.org/10.1145/3696410.3714866)

<details open>
<summary><strong>中文摘要</strong></summary>

得益于在语义理解和逻辑推理方面前所未有的能力，大型语言模型（LLMs）在开发下一代序列推荐系统（RSs）方面展现出了巨大的潜力。然而，现有的基于LLM的序列推荐系统大多将索引生成与序列推荐分离，导致语义信息与协同信息之间整合不足。另一方面，对用户相关信息的忽视阻碍了基于LLM的序列推荐系统利用高阶用户-物品交互模式。在本文中，我们提出了端到端双动态（ED2）推荐器，这是首个采用双动态索引机制的基于LLM的序列推荐系统，旨在同时解决上述局限性。双动态索引机制不仅能够将索引生成与序列推荐整合到统一的LLM骨干流水线中，还能使基于LLM的序列推荐器切实利用用户相关信息。具体而言，为了增强LLM对双动态索引的理解能力，我们提出了一种多粒度令牌调节器，该调节器基于LLM的语义知识在多个表示粒度上构建对齐监督。此外，我们还专门定制了关联用户集合数据以及一系列新颖的指令微调任务，以捕捉高阶用户-物品交互模式。在三个公开数据集上的大量实验证明了ED2的优越性，其在命中率（Hit-Rate）上平均提升了19.62%，在归一化折损累计增益（NDCG）上平均提升了21.11%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Owing to the unprecedented capability in semantic understanding and logical reasoning, large language models (LLMs) have shown fantastic potential in developing next-generation sequential recommender systems (RSs). However, existing LLM-based sequential RSs mostly separate index generation from sequential recommendation, leading to insufficient integration between semantic information and collaborative information. On the other hand, the neglect of user-related information hinders LLM-based sequential RSs from exploiting high-order user-item interaction patterns. In this paper, we propose the End-to-End Dual Dynamic (ED2) recommender, the first LLM-based sequential RS which adopts dual dynamic index mechanism, targeting resolving the above limitations simultaneously. The dual dynamic index mechanism can not only assembly index generation and sequential recommendation into a unified LLM-backbone pipeline, but also make it practical for LLM-based sequential recommender to take advantage of user-related information. Specifically, to facilitate the LLM comprehension ability to dual dynamic index, we propose a multigrained token regulator which constructs alignment supervision based on LLMs semantic knowledge across multiple representation granularities. Moreover, the associated user collection data and a series of novel instruction tuning tasks are specially customized to capture the high-order user-item interaction patterns. Extensive experiments on three public datasets demonstrate the superiority of ED2, achieving an average improvement of 19.62% in Hit-Rate and 21.11% in NDCG.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出了一种名为ED2的端到端双动态推荐系统，这是首个采用双动态索引机制的基于LLM的序列推荐系统。该方法将索引生成与序列推荐整合到统一的LLM主干流程中，并利用用户相关信息捕捉高阶用户-物品交互模式。通过多粒度令牌调节器和对齐监督，以及定制的指令调整任务，ED2在三个公共数据集上平均提升了19.62%的命中率和21.11%的NDCG。

### 主要创新

- 提出双动态索引机制，将索引生成与序列推荐整合到统一LLM流程中
- 利用用户相关信息，增强对高阶用户-物品交互模式的捕捉
- 设计多粒度令牌调节器，基于LLM语义知识构建多粒度对齐监督
- 定制用户集合数据和指令调整任务，以捕捉高阶交互模式

### 研究方法

论文采用基于LLM的序列推荐方法，通过双动态索引机制实现端到端训练。具体包括：构建统一LLM主干流程，整合索引生成和推荐任务；设计多粒度令牌调节器，利用LLM语义知识进行对齐监督；定制用户集合数据和指令调整任务，以利用用户相关信息。

### 关键结果

在三个公共数据集上，ED2平均提升了19.62%的命中率（Hit-Rate）和21.11%的NDCG。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 创新性地提出双动态索引机制，解决了索引生成与推荐分离的问题
- 有效整合语义信息和协同信息，提升推荐性能
- 在多个数据集上取得了显著性能提升

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法的泛化性、计算成本等。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、LLM与推荐系统结合等关键词高度相关，属于推荐系统前沿研究。

## 代码与复现

- [Esperanto-mega/ED2](https://github.com/Esperanto-mega/ED2)：possible，置信度 30，Stars 12

---

_知识库更新时间：2026-09-01T05:31:13.527715_
