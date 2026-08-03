---
title: "不仅是什么，而且是什么时候：将不规则间隔整合到LLM中进行序列推荐"
paper_id: "https://doi.org/10.1145/3705328.3748013"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 63.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Bandit Algorithms Research"]
---

# 不仅是什么，而且是什么时候：将不规则间隔整合到LLM中进行序列推荐

> **英文原标题**：Not Just What, But When: Integrating Irregular Intervals to LLM for Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/DuUT25)

## 一句话结论

> 该论文提出IntervalLLM框架，将购买时间间隔整合到LLM中用于序列推荐，并在多个基准上取得平均4.4%的提升，同时从用户、物品和间隔三个视角评估了冷启动场景。

## 论文信息

- **作者**：Weiwei Du, Takuma Udagawa, Kei Tateno
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：63.0
- **DOI**：[https://doi.org/10.1145/3705328.3748013](https://doi.org/10.1145/3705328.3748013)

<details open>
<summary><strong>中文摘要</strong></summary>

购买商品之间的时间间隔是序列推荐任务中的一个关键因素，而现有方法主要关注商品序列，往往通过假设商品之间的间隔是静态的来忽略这一因素。然而，动态间隔作为一个描述用户画像的维度，不仅涉及用户自身的历史，还涉及具有相同商品历史的不同用户。在本工作中，我们提出了IntervalLLM，一个新颖的框架，将间隔信息整合到LLM中，并引入了新颖的间隔注入注意力机制，以联合考虑商品和间隔的信息。此外，与以往仅从用户和商品角度处理冷启动场景的研究不同，我们引入了一个新视角：间隔视角，作为在温暖和冷场景下评估推荐方法的额外指标。在3个基准数据集上，与基于传统方法和LLM的基线进行的大量实验表明，我们的IntervalLLM不仅平均提升了4.4%，而且在所有用户、商品以及所提出的间隔视角下，均达到了最佳的温暖和冷场景表现。此外，我们观察到，在所有推荐方法中，从间隔视角来看的冷场景经历了最显著的性能下降。这一发现强调了进一步研究基于间隔的冷挑战以及我们在序列推荐任务中整合间隔信息的必要性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Time intervals between purchasing items are a crucial factor in sequential recommendation tasks, whereas existing approaches focus on item sequences and often overlook by assuming the intervals between items are static.However, dynamic intervals serve as a dimension that describes user profiling on not only the history within a user but also different users with the same item history.In this work, we propose IntervalLLM, a novel framework that integrates interval information into LLM and incorporates the novel interval-infused attention to jointly consider information of items and intervals.Furthermore, unlike prior studies that address the cold-start scenario only from the perspectives of users and items, we introduce a new viewpoint: the interval perspective to serve as an additional metric for evaluating recommendation methods on the warm and cold scenarios.Extensive experiments on 3 benchmarks with both traditional-and LLM-based baselines demonstrate that our IntervalLLM achieves not only 4.4% improvements in average but also the best-performing warm and cold scenarios across all users, items, and the proposed interval perspectives.In addition, we observe that the cold scenario from the interval perspective experiences the most significant performance drop among all recommendation methods.This finding underscores the necessity of further research on interval-based cold challenges and our integration of interval information in the realm of sequential recommendation tasks.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

论文指出，在序列推荐中，物品之间的时间间隔是重要因素，但现有方法往往忽略或假设间隔是静态的。动态间隔不仅描述了用户内部的历史，还能区分具有相同物品历史的不同用户。为此，作者提出IntervalLLM框架，将间隔信息整合到LLM中，并引入间隔注入注意力机制，联合考虑物品和间隔信息。此外，论文从间隔视角提出了新的冷启动评估维度，区别于传统的用户和物品视角。在三个基准上的大量实验表明，IntervalLLM平均提升4.4%，并在所有用户、物品和间隔视角的冷热场景中均取得最佳性能。同时，研究发现间隔视角下的冷场景在所有推荐方法中性能下降最显著，强调了间隔冷挑战的重要性。

### 主要创新

- 提出IntervalLLM框架，首次将不规则时间间隔整合到LLM中用于序列推荐。
- 设计间隔注入注意力机制，联合建模物品和间隔信息。
- 从间隔视角提出新的冷启动评估维度，补充了传统的用户和物品视角。
- 实验证明IntervalLLM在多个基准上取得平均4.4%的提升，并在冷热场景中表现最佳。

### 研究方法

论文提出IntervalLLM框架，将物品序列和对应的时间间隔编码为输入，通过间隔注入注意力机制（interval-infused attention）在Transformer层中融合间隔信息，使模型能够感知动态间隔。同时，论文定义了基于间隔的冷启动场景，用于评估推荐方法在间隔分布变化时的表现。实验采用三个基准数据集，与传统的和基于LLM的基线进行比较。

### 关键结果

IntervalLLM在三个基准上平均提升4.4%；在所有用户、物品和间隔视角的冷热场景中均取得最佳性能；间隔视角下的冷场景在所有推荐方法中性能下降最显著。

### 技术栈

- 摘要未提供具体技术栈，但可推断涉及LLM（大型语言模型）、注意力机制、序列推荐模型。

### 方法优势

- 创新性地将时间间隔信息整合到LLM中，弥补了现有序列推荐忽略动态间隔的不足。
- 提出新的评估视角（间隔视角），为冷启动问题提供了更全面的评估维度。
- 实验证明方法在多个基准上有效，且在不同冷热场景下均表现优异。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：由于仅提供摘要，无法评估模型细节、实验设置、消融研究等，也无法验证所有声称的统计显著性。

### 与当前研究方向的关联

论文与序列推荐、LLM与推荐系统结合、用户建模、冷启动等关键词高度相关。它聚焦于序列推荐中的时间间隔建模，并利用LLM提升推荐性能，同时从新视角探讨冷启动问题。

---

_知识库更新时间：2026-08-03T04:09:55.940134_
