---
title: "重新思考推荐系统中的主观特征：个人视角优于聚合值"
paper_id: "https://doi.org/10.1145/3705328.3759316"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 44.0
tags: ["paper", "recommender-systems", "Video Analysis and Summarization", "Music and Audio Processing", "Advanced Text Analysis Techniques"]
---

# 重新思考推荐系统中的主观特征：个人视角优于聚合值

> **英文原标题**：Rethinking Subjective Features in Recommender Systems: Personal Views Over Aggregated Values

[查看原文](https://dblp.org/rec/conf/recsys/GolubovikjT25) · [Semantic Scholar](https://www.semanticscholar.org/paper/2b86d9af91990bfce52fc163c6f75ce685c54c7c)

## 一句话结论

> 该论文通过对比固定聚合与用户特定表示，证明在推荐系统中建模主观特征时用户特定表示更优，从而提升推荐性能。

## 论文信息

- **作者**：Arsen Matej Golubovikj, Marko Tkalčič
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：44.0
- **DOI**：[https://doi.org/10.1145/3705328.3759316](https://doi.org/10.1145/3705328.3759316)

<details open>
<summary><strong>中文摘要</strong></summary>

内容项的主观特征，如情感共鸣和审美质量，在推荐系统（RecSys）中变得越来越重要，因为该领域正超越客观内容和行为信号。传统上，这些特征被视为固定的项目级属性，跨用户进行聚合。然而，新出现的证据表明，主观特征本质上是依赖于用户的，受个体解读和个人视角的影响。本文首次对固定（聚合）表示与用户特定（主观）表示在推荐系统中建模主观特征方面进行了直接比较。利用涵盖电影、视频和图像三个数据集，并包含诸如幸福感（eudaimonia）、享乐感（hedonia）、情感（emotion）和美学（aesthetics）等主观特征，我们评估了表示策略（即固定表示与用户特定表示）对多种算法推荐性能的影响。我们的研究结果表明，用户特定表示始终优于聚合表示，且通常具有统计显著性改进。这些结果强调了在用户层面建模主观性的重要性，为构建更个性化和更有效的推荐系统提供了具体指导。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Subjective features of content items, such as emotional resonance and aesthetic quality, have become increasingly important in recommender systems (RecSys), as the field moves beyond objective content and behavioral signals. Traditionally, such features were treated as fixed item-level properties, aggregated across users. However, emerging evidence suggests that subjective features are inherently user-dependent, shaped by individual interpretations and personal perspectives. This paper presents the first direct comparison between fixed (aggregated) and user-specific (subjective) item representations for modeling subjective features in RecSys. Using three datasets spanning movies, videos, and images, with subjective features, such as eudaimonia, hedonia, emotion, and aesthetics, we evaluate the impact of the representation strategy (i.e. fixed vs. user-specific) on recommendation performance across multiple algorithms. Our findings show that user-specific representations consistently outperform aggregate ones, often with statistically significant improvements. These results underscore the importance of modeling subjectivity at the user level, offering concrete guidance for more personalized and effective recommendation systems.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

随着推荐系统从客观内容和行为信号扩展到主观特征（如情感共鸣和审美质量），传统上这些特征被视为固定的项目级属性，跨用户聚合。然而，新兴证据表明主观特征本质上是用户依赖的，受个人解读和视角影响。本文首次直接比较了固定（聚合）和用户特定（主观）项目表示在推荐系统中建模主观特征的效果。使用三个数据集（涵盖电影、视频和图像），包含主观特征（如幸福感、享乐感、情感和美学），评估了表示策略（固定 vs. 用户特定）对多种算法推荐性能的影响。结果表明，用户特定表示始终优于聚合表示，且通常具有统计显著性。这些结果强调了在用户层面建模主观性的重要性，为更个性化和有效的推荐系统提供了具体指导。

### 主要创新

- 首次直接比较固定（聚合）和用户特定（主观）项目表示在推荐系统中建模主观特征的效果。
- 在多个数据集（电影、视频、图像）和多种算法上验证用户特定表示的优势。
- 强调主观特征的用户依赖性，挑战传统聚合方法。
- 为推荐系统设计提供新视角，建议在用户层面建模主观性。

### 研究方法

论文使用多个数据集（涵盖电影、视频和图像），包含主观特征（如幸福感、享乐感、情感和美学），并采用多种推荐算法，比较固定（聚合）和用户特定（主观）项目表示对推荐性能的影响。具体算法和实现细节摘要未提供。

### 关键结果

用户特定表示在推荐性能上始终优于聚合表示，且通常具有统计显著性改进。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 首次对主观特征的表示策略进行直接比较，具有新颖性。
- 使用多个数据集和多种算法，增强了结论的普适性。
- 结果具有统计显著性，支持用户特定表示的有效性。
- 为推荐系统个性化提供实用指导。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估实验细节、数据集规模、算法选择、基线比较等，可能影响对方法全面性的判断。

### 与当前研究方向的关联

该论文与推荐系统、用户建模、个性化推荐高度相关，聚焦于主观特征的用户特定建模，对提升推荐系统的个性化和有效性有重要意义。

---

_知识库更新时间：2026-08-10T02:48:30.664233_
