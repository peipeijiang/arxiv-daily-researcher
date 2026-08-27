---
title: "可解释的多模态对齐用于可迁移推荐"
paper_id: "https://doi.org/10.1145/3696410.3714733"
source: "www"
published: "2025-01-01T00:00:00"
score: 48.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Machine Learning in Healthcare"]
---

# 可解释的多模态对齐用于可迁移推荐

> **英文原标题**：Explainable Multi-Modality Alignment for Transferable Recommendation

[查看原文](https://dblp.org/rec/conf/www/0004MGZWZZY25) · [Semantic Scholar](https://www.semanticscholar.org/paper/8668bef005e0325dc37237bec5058c8f5c977d06)

## 一句话结论

> 该论文提出了一种可解释的多模态对齐方法（EARec），通过并行对齐多种模态到共享锚点并组合模型，提升了序列推荐系统的可迁移性和可扩展性。

## 论文信息

- **作者**：Shenghao Yang, Weizhi Ma, Zhiqiang Guo, Min Zhang, Haiyang Wu, Junjie Zhai, Chunhui Zhang, Yuekui Yang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：48.0
- **DOI**：[https://doi.org/10.1145/3696410.3714733](https://doi.org/10.1145/3696410.3714733)

<details open>
<summary><strong>中文摘要</strong></summary>

随着多模态建模技术的发展，近期的序列推荐系统通过引入跨领域的通用多模态数据（如文本和图像）来增强可迁移性。现有方法通常采用成对对齐以缓解模态之间的差异。然而，这种对齐范式在可解释性、一致性和可扩展性方面存在局限，导致性能次优。本文提出了一种新颖的面向可迁移推荐系统的可解释多模态对齐方法，即EARec。具体而言，我们设计了一个两阶段框架，以在源领域实现可解释的模态对齐，并在目标领域基于对齐后的模态表示进行推荐。在第一阶段，我们采用生成式任务将多种模态并行对齐到一个具有可解释含义的共享锚点上。所有模态共享同一锚点以确保方向一致。此外，我们将行为视为一种独立模态，以将任务特定信息整合到对齐框架中。在第二阶段，我们将第一阶段训练得到的多个物品模态表示模型进行组合，以获得一个能够同时理解多种模态的统一模型，从而为目标领域的推荐提供高质量的物品模态表示。得益于并行模态对齐后模型组合的方法，该框架在扩展新模态方面表现出灵活性。在多个公开数据集上的实验结果表明，EARec优于基线方法，进一步的分析也验证了所提对齐方法的可解释性和可扩展性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

With the development of multi-modal modeling techniques, recent sequential recommender systems enhance transferability by incorporating cross-domain universal multi-modal data, e.g., text and image. Existing methods typically adopt pairwise alignment to alleviate the gap between modalities. However, this alignment paradigm has limitations on explainability, consistency, and expansibility, resulting in suboptimal performance. This paper proposes a novel Explainable multi-modality Alignment method for transferable Rec ommender systems, i.e., EARec. Specifically, we design a two-stage framework to achieve explainable modality alignment in the source domain and recommendation based on aligned modality representations in the target domain. In the first stage, we adopt a generative task to align various modalities in parallel to a shared anchor with explainable meaning. All modalities share the same anchor to ensure consistent direction. Additionally, we treat behavior as an independent modality to integrate task-specific information into the alignment framework. In the second stage, we compose multiple item modality representation models trained in the first stage to obtain a unified model capable of understanding various modalities simultaneously, thereby providing high-quality item modality representations for recommendations in the target domain. Benefiting from the approach of parallel modality alignment followed by model composition, the framework shows flexibility in expanding new modalities. Experimental results on multiple public datasets demonstrate the superiority of EARec over baselines, and further analyses indicate the explainability and expansibility of the proposed alignment method.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

随着多模态建模技术的发展，最近的序列推荐系统通过引入跨领域的通用多模态数据（如文本和图像）来增强可迁移性。现有方法通常采用成对对齐来缓解模态间的差距，但这种对齐范式在可解释性、一致性和可扩展性方面存在局限，导致性能次优。本文提出了一种新颖的可解释多模态对齐方法用于可迁移推荐系统，即EARec。具体来说，设计了一个两阶段框架，在源域实现可解释的模态对齐，并在目标域基于对齐的模态表示进行推荐。第一阶段，采用生成式任务将多种模态并行对齐到一个具有可解释意义的共享锚点，所有模态共享同一锚点以确保方向一致，并将行为视为独立模态以整合任务特定信息。第二阶段，组合第一阶段训练得到的多个物品模态表示模型，获得一个能同时理解多种模态的统一模型，从而为目标域推荐提供高质量的物品模态表示。得益于并行模态对齐和模型组合的方法，该框架在扩展新模态方面具有灵活性。在多个公开数据集上的实验结果表明EARec优于基线，进一步分析表明所提对齐方法的可解释性和可扩展性。

### 主要创新

- 提出可解释的多模态对齐方法，通过生成式任务将各模态并行对齐到共享锚点，增强可解释性。
- 所有模态共享同一锚点，确保对齐方向一致，提升一致性。
- 将行为视为独立模态，整合任务特定信息到对齐框架中。
- 采用两阶段框架：先并行对齐，再组合模型，实现灵活扩展新模态。

### 研究方法

论文采用两阶段框架。第一阶段，使用生成式任务将多种模态（如文本、图像）并行对齐到一个共享锚点，锚点具有可解释意义，所有模态共享同一锚点以保证方向一致，同时将行为作为独立模态纳入对齐。第二阶段，组合第一阶段训练得到的多个物品模态表示模型，形成统一模型，用于目标域推荐。

### 关键结果

实验结果表明EARec在多个公开数据集上优于基线，进一步分析表明所提对齐方法具有可解释性和可扩展性。具体数值未在摘要中提供。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 提出可解释的对齐方法，解决了现有成对对齐的可解释性不足。
- 通过共享锚点确保一致性，提升对齐效果。
- 将行为作为独立模态，增强任务特定信息融合。
- 两阶段框架支持灵活扩展新模态，具有可扩展性。
- 实验验证了方法的优越性。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法在复杂场景下的表现、计算开销、对噪声的鲁棒性等。

### 与当前研究方向的关联

该论文与多模态推荐、序列推荐、可迁移推荐、可解释性等关键词高度相关。它聚焦于多模态对齐，提升推荐系统的可迁移性，并强调可解释性，符合多模态推荐和可解释推荐的研究方向。

## 代码与复现

- [ysh-1998/EARec](https://github.com/ysh-1998/EARec)：possible，置信度 30，Stars 7

---

_知识库更新时间：2026-08-27T10:15:25.337934_
