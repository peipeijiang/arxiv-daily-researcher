---
title: "跨越领域：大语言模型增强的跨域序列推荐"
paper_id: "https://doi.org/10.1145/3726302.3729911"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 58.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# 跨越领域：大语言模型增强的跨域序列推荐

> **英文原标题**：Bridge the Domains: Large Language Models Enhanced Cross-domain Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/00020W0Z0LH025) · [ArXiv](https://arxiv.org/abs/2504.18383) · [Semantic Scholar](https://www.semanticscholar.org/paper/8d3fff1bf6eb995d96659b8a0367717e27570de0)

## 一句话结论

> 该论文提出LLM4CDSR模型，利用大语言模型统一表示物品和总结用户跨域偏好，以解决跨域序列推荐中的重叠困境和转换复杂性问题，并在三个公开数据集上验证了有效性。

## 论文信息

- **作者**：Qidong Liu, Xiangyu Zhao, Yejing Wang, Zijian Zhang, Hao Zhong, Chong Chen, Xiang Li, Wei Huang, Feng Tian
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：58.0
- **DOI**：[https://doi.org/10.1145/3726302.3729911](https://doi.org/10.1145/3726302.3729911)

<details open>
<summary><strong>中文摘要</strong></summary>

跨域序列推荐（CDSR）旨在从用户在不同领域的历史交互中提取偏好。尽管CDSR已取得一定进展，但两个问题阻碍了其进一步发展，即重叠困境与转换复杂性。前者指现有CDSR方法严重依赖在所有领域均有交互的用户来学习跨域物品关系，从而损害了其实用性；后者指从混合行为序列中学习复杂转换模式的困难。凭借强大的表示与推理能力，大语言模型（LLMs）有望通过从语义视角桥接物品并捕捉用户偏好来解决这两个问题。为此，我们提出了一种大语言模型增强的跨域序列推荐模型（LLM4CDSR）。为获取语义层面的物品关系，我们首先提出一种基于LLM的统一表示模块来表示物品；随后设计了一个带有对比正则化的可训练适配器，以适配CDSR任务。此外，我们还设计了一个层次化LLM画像模块，用于总结用户的跨域偏好。最后，这两个模块被整合到所提出的三线程框架中以生成推荐结果。我们在三个公开的跨域数据集上进行了大量实验，验证了LLM4CDSR的有效性。我们已在线上公开了代码。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Cross-domain Sequential Recommendation (CDSR) aims to extract the preference from the user's historical interactions across various domains. Despite some progress in CDSR, two problems set the barrier for further advancements, i.e., overlap dilemma and transition complexity. The former means existing CDSR methods severely rely on users who own interactions on all domains to learn cross-domain item relationships, compromising the practicability. The latter refers to the difficulties in learning the complex transition patterns from the mixed behavior sequences. With powerful representation and reasoning abilities, Large Language Models (LLMs) are promising to address these two problems by bridging the items and capturing the user's preferences from a semantic view. Therefore, we propose an LLMs Enhanced Cross-domain Sequential Recommendation model (LLM4CDSR). To obtain the semantic item relationships, we first propose an LLM-based unified representation module to represent items. Then, a trainable adapter with contrastive regularization is designed to adapt the CDSR task. Besides, a hierarchical LLMs profiling module is designed to summarize user cross-domain preferences. Finally, these two modules are integrated into the proposed tri-thread framework to derive recommendations. We have conducted extensive experiments on three public cross-domain datasets, validating the effectiveness of LLM4CDSR. We have released the code online.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

跨域序列推荐旨在从用户在不同领域的历史交互中提取偏好。现有方法存在重叠困境和转换复杂性两个问题：前者指严重依赖在所有领域都有交互的用户来学习跨域项目关系，实用性受限；后者指从混合行为序列中学习复杂转换模式的困难。大语言模型凭借强大的表示和推理能力，有望从语义角度弥合项目并捕捉用户偏好。为此，本文提出LLM4CDSR模型。首先设计基于LLM的统一表示模块来表示项目，然后设计带对比正则化的可训练适配器以适应CDSR任务，并设计层次化LLM画像模块总结用户跨域偏好，最后将这两个模块集成到三线程框架中生成推荐。在三个公开跨域数据集上的实验验证了LLM4CDSR的有效性，代码已开源。

### 主要创新

- 提出基于LLM的统一项目表示模块，从语义角度弥合跨域项目关系，缓解重叠困境。
- 设计带对比正则化的可训练适配器，将LLM表示适应CDSR任务。
- 设计层次化LLM画像模块，总结用户跨域偏好，捕捉复杂转换模式。
- 提出三线程框架整合上述模块，实现跨域序列推荐。

### 研究方法

论文采用LLM增强的跨域序列推荐方法。首先，利用LLM构建统一项目表示，将不同领域的项目映射到语义空间。然后，通过可训练适配器（带对比正则化）将表示适配到推荐任务。同时，层次化LLM画像模块从用户历史中总结跨域偏好。最后，三线程框架整合表示和画像信息，生成推荐。实验在三个公开跨域数据集上进行，验证有效性。

### 关键结果

在三个公开跨域数据集上的实验验证了LLM4CDSR的有效性。具体指标数值摘要未提供。

### 技术栈

- 大语言模型（LLM）、可训练适配器、对比正则化、层次化画像模块、三线程框架。具体模型名称、损失函数等摘要未提供。

### 方法优势

- 创新性地利用LLM语义能力解决跨域推荐中的重叠和转换复杂性问题。
- 提出统一表示和层次化画像，增强跨域知识迁移。
- 三线程框架设计合理，模块可插拔。
- 在多个数据集上验证有效性，并开源代码。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法在极端稀疏场景下的表现、计算开销、与现有方法的详细对比等。

### 与当前研究方向的关联

高度相关：论文聚焦序列推荐、跨域推荐、LLM与推荐系统结合，属于生成式推荐和用户建模范畴，与关键词中的序列推荐、LLM推荐、用户建模等直接相关。

## 代码与复现

- [CHIANGEL/Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys)：official，置信度 100，Stars 1550

---

_知识库更新时间：2026-08-25T02:16:23.900884_
