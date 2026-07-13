---
title: "可解释的多模态对齐方法用于可迁移推荐系统"
paper_id: "https://doi.org/10.1145/3696410.3714733"
source: "www"
published: "2025-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Machine Learning in Healthcare"]
---

# 可解释的多模态对齐方法用于可迁移推荐系统

> **英文原标题**：Explainable Multi-Modality Alignment for Transferable Recommendation

[查看原文](https://dblp.org/rec/conf/www/0004MGZWZZY25) · [Semantic Scholar](https://www.semanticscholar.org/paper/8668bef005e0325dc37237bec5058c8f5c977d06)

## 一句话结论

> 该论文提出了一种可解释的多模态对齐方法（EARec），通过生成式任务将多种模态并行对齐到共享锚点，并组合模型以提升推荐系统的可迁移性和可解释性，实验表明其优于基线方法。

## 论文信息

- **作者**：Shenghao Yang, Weizhi Ma, Zhiqiang Guo, Min Zhang, Haiyang Wu, Junjie Zhai, Chunhui Zhang, Yuekui Yang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3696410.3714733](https://doi.org/10.1145/3696410.3714733)

<details open>
<summary><strong>中文摘要</strong></summary>

随着多模态建模技术的发展，近期序列推荐系统通过引入跨领域的通用多模态数据（例如文本和图像）来增强可迁移性。现有方法通常采用成对对齐来缓解模态间的差异。然而，这种对齐范式在可解释性、一致性和可扩展性方面存在局限性，导致性能次优。本文提出了一种面向可迁移推荐系统的可解释多模态对齐方法，即EARec。具体而言，我们设计了一个两阶段框架，在源域中实现可解释的模态对齐，并在目标域中基于对齐后的模态表示进行推荐。在第一阶段，我们采用生成式任务将多种模态并行地对齐到一个具有可解释含义的共享锚点（anchor）上。所有模态共享同一锚点以确保方向一致性。此外，我们将行为视为一种独立模态，将任务特定信息整合到对齐框架中。在第二阶段，我们组合第一阶段训练得到的多个物品模态表示模型，以获得一个能够同时理解多种模态的统一模型，从而为目标域中的推荐提供高质量的物品模态表示。得益于并行模态对齐后接模型组合的方法，该框架在扩展新模态方面展现出灵活性。在多个公开数据集上的实验结果表明，EARec优于基线方法，进一步的分析也证明了所提对齐方法的可解释性和可扩展性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

With the development of multi-modal modeling techniques, recent sequential recommender systems enhance transferability by incorporating cross-domain universal multi-modal data, e.g., text and image. Existing methods typically adopt pairwise alignment to alleviate the gap between modalities. However, this alignment paradigm has limitations on explainability, consistency, and expansibility, resulting in suboptimal performance. This paper proposes a novel Explainable multi-modality Alignment method for transferable Rec ommender systems, i.e., EARec. Specifically, we design a two-stage framework to achieve explainable modality alignment in the source domain and recommendation based on aligned modality representations in the target domain. In the first stage, we adopt a generative task to align various modalities in parallel to a shared anchor with explainable meaning. All modalities share the same anchor to ensure consistent direction. Additionally, we treat behavior as an independent modality to integrate task-specific information into the alignment framework. In the second stage, we compose multiple item modality representation models trained in the first stage to obtain a unified model capable of understanding various modalities simultaneously, thereby providing high-quality item modality representations for recommendations in the target domain. Benefiting from the approach of parallel modality alignment followed by model composition, the framework shows flexibility in expanding new modalities. Experimental results on multiple public datasets demonstrate the superiority of EARec over baselines, and further analyses indicate the explainability and expansibility of the proposed alignment method.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对现有序列推荐系统在多模态对齐中存在的可解释性、一致性和可扩展性不足的问题，提出了一种可解释的多模态对齐方法EARec。该方法采用两阶段框架：第一阶段通过生成式任务将多种模态并行对齐到一个共享的、具有可解释意义的锚点，并将行为视为独立模态以整合任务特定信息；第二阶段组合第一阶段训练好的多个模态表示模型，获得统一模型以理解多种模态，为目标域推荐提供高质量表示。实验表明EARec优于基线方法，并验证了其可解释性和可扩展性。

### 主要创新

- 提出两阶段框架实现可解释的模态对齐，第一阶段生成式对齐，第二阶段模型组合。
- 将多种模态并行对齐到共享的、具有可解释意义的锚点，确保一致性方向。
- 将行为视为独立模态，整合任务特定信息到对齐框架中。
- 通过并行对齐后模型组合的方式，实现新模态的灵活扩展。

### 研究方法

论文采用两阶段框架：第一阶段使用生成式任务将文本、图像等模态并行对齐到共享的锚点，行为作为独立模态参与对齐；第二阶段组合第一阶段训练好的多个模态表示模型，形成统一模型用于目标域推荐。

### 关键结果

在多个公开数据集上的实验表明EARec优于基线方法，进一步分析验证了所提对齐方法的可解释性和可扩展性。

### 技术栈

- 生成式任务、多模态对齐、模型组合

### 方法优势

- 提出可解释的模态对齐方法，解决了现有方法可解释性不足的问题。
- 两阶段框架具有灵活性和可扩展性，易于引入新模态。
- 将行为作为独立模态，增强了任务特定信息的整合。

### 主要局限

- **论文本身局限**：摘要未提供具体局限性。
- **当前证据局限**：当前仅基于摘要分析，缺乏实验细节、数据集名称、基线模型等具体信息，无法全面评估局限性。

### 与当前研究方向的关联

论文涉及多模态推荐、序列推荐、可解释性、迁移学习等关键词，与推荐系统领域高度相关。

## 代码与复现

- [ysh-1998/EARec](https://github.com/ysh-1998/EARec)：possible，置信度 30，Stars 7

---

_知识库更新时间：2026-07-13T01:23:50.736528_
