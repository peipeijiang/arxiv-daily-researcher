---
title: "推荐是一道宜趁热享用的菜肴"
paper_id: "https://doi.org/10.1145/3705328.3759331"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 42.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Topic Modeling"]
---

# 推荐是一道宜趁热享用的菜肴

> **英文原标题**：Recommendation Is a Dish Better Served Warm

[查看原文](https://dblp.org/rec/conf/recsys/GusakSF25) · [ArXiv](https://arxiv.org/abs/2508.07856) · [Semantic Scholar](https://www.semanticscholar.org/paper/009d95f70fb498f4cb448ea547592c4bd987075a)

## 一句话结论

> 该论文系统研究了推荐系统中冷启动阈值的设定对评估结果的影响，发现不一致的阈值会导致数据浪费或噪声增加，影响评估可靠性。

## 论文信息

- **作者**：Danil Gusak, Nikita Sukhorukov, Evgeny Frolov
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：42.0
- **DOI**：[https://doi.org/10.1145/3705328.3759331](https://doi.org/10.1145/3705328.3759331)

<details open>
<summary><strong>中文摘要</strong></summary>

在现代推荐系统中，实验设置通常包括基于最小交互阈值过滤掉冷用户和冷物品。然而，这些阈值往往被随意选择，且在不同研究中差异较大，导致不一致性，这可能显著影响评估结果的可比性和可靠性。在本文中，我们通过考察用于判断用户或物品是否应被视为冷启动的标准，系统性地探索了冷启动边界。我们的实验在训练过程中逐步变化不同物品的交互数量，并在推理阶段逐步更新用户交互历史的长度。我们研究了多个广泛使用的数据集上的阈值，这些数据集常见于顶级会议近期论文中，并基于多个成熟的推荐基线模型进行验证。我们的研究结果表明，冷启动阈值选择的不一致可能导致有价值数据的无谓删除，或导致冷实例被错误分类为热实例，从而为系统引入更多噪声。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In modern recommender systems, experimental settings typically include filtering out cold users and items based on a minimum interaction threshold.However, these thresholds are often chosen arbitrarily and vary widely across studies, leading to inconsistencies that can significantly affect the comparability and reliability of evaluation results.In this paper, we systematically explore the cold-start boundary by examining the criteria used to determine whether a user or an item should be considered cold.Our experiments incrementally vary the number of interactions for different items during training, and gradually update the length of user interaction histories during inference.We investigate the thresholds across several widely used datasets, commonly represented in recent papers from top-tier conferences, and on multiple established recommender baselines.Our findings show that inconsistent selection of cold-start thresholds can either result in the unnecessary removal of valuable data or lead to the misclassification of cold instances as warm, introducing more noise into the system.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

现代推荐系统的实验设置通常基于最小交互阈值过滤冷用户和冷物品，但这些阈值的选择往往随意且在不同研究中差异很大，导致评估结果的可比性和可靠性受到影响。本文系统探索了冷启动边界，通过逐步改变训练中物品的交互次数和推理中用户交互历史的长度，在多个广泛使用的数据集和多个推荐基线上研究了阈值的影响。研究发现，不一致的冷启动阈值选择可能导致有价值数据的无效移除，或将冷实例误分类为热实例，从而引入更多噪声。

### 主要创新

- 系统性地探索了冷启动边界，而非仅关注单一阈值。
- 通过增量改变交互次数和交互历史长度，动态评估阈值影响。
- 在多个数据集和基线上进行实验，揭示了阈值选择不一致带来的问题。
- 指出阈值选择不当可能导致数据浪费或噪声增加，为实验设置提供指导。

### 研究方法

论文采用实验方法，通过逐步变化训练中物品的交互次数和推理中用户交互历史的长度，在多个数据集和推荐基线上评估不同冷启动阈值的影响。具体实验细节（如数据集名称、基线模型等）摘要未提供。

### 关键结果

研究发现，不一致的冷启动阈值选择会导致有价值数据的无效移除，或将冷实例误分类为热实例，从而引入更多噪声。具体数据未在摘要中提供。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 针对推荐系统评估中常见的阈值选择问题进行了系统研究，具有实际意义。
- 通过动态调整阈值，提供了更全面的冷启动边界分析。
- 在多个数据集和基线上验证，增强了结论的可靠性。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估实验细节、数据集代表性、基线选择等，可能影响结论的普适性。

### 与当前研究方向的关联

论文与关键词“推荐系统”、“冷启动”、“评估方法”高度相关，涉及用户建模和实验设置，对推荐系统的鲁棒性和可靠性有重要影响。

---

_知识库更新时间：2026-08-12T03:12:07.692332_
