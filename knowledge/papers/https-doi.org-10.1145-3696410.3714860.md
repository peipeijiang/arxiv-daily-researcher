---
title: "联合相似项目探索与重叠用户引导的多模态跨域推荐"
paper_id: "https://doi.org/10.1145/3696410.3714860"
source: "www"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Advanced Graph Neural Networks"]
---

# 联合相似项目探索与重叠用户引导的多模态跨域推荐

> **英文原标题**：Joint Similarity Item Exploration and Overlapped User Guidance for Multi-Modal Cross-Domain Recommendation

[查看原文](https://dblp.org/rec/conf/www/000500LWZFPW25) · [ArXiv](https://arxiv.org/abs/2502.16068) · [Semantic Scholar](https://www.semanticscholar.org/paper/a4b656f0c36b11b6dc05f4aac5a8588717a0d875)

## 一句话结论

> 该论文提出SIEOUG方法，通过相似物品探索和重叠用户引导解决多模态跨域推荐中的数据稀疏和模态噪声问题，在Amazon数据集上显著优于现有模型。

## 论文信息

- **作者**：Weiming Liu, Chaochao Chen, Jiahe Xu, Xinting Liao, Fan Wang, Xiaolin Zheng, Z. F. Fu, Ruiguang Pei, Jun Wang
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3696410.3714860](https://doi.org/10.1145/3696410.3714860)

<details open>
<summary><strong>中文摘要</strong></summary>

跨域推荐（Cross-Domain Recommendation, CDR）通过跨领域知识共享来解决长期存在的数据稀疏问题，已得到广泛研究。本文聚焦于多模态跨域推荐（Multi-Modal Cross-Domain Recommendation, MMCDR）问题，其中不同项目具有多模态信息，而跨域重叠用户极少。MMCDR的挑战主要体现在两个方面：充分挖掘每个领域内多样化的多模态信息，以及利用跨领域的有效知识迁移。然而，现有方法未能对具有相似特征的项目进行聚类，同时难以滤除不同模态中的固有噪声，从而阻碍了模型性能。更严重的是，传统CDR模型主要依赖重叠用户进行领域适配，导致其难以应对大多数用户非重叠的场景。为弥补这一不足，我们提出联合相似项目探索与重叠用户引导（Joint Similarity Item Exploration and Overlapped User Guidance, SIEOUG）方法来解决MMCDR问题。SIEOUG首先提出相似项目探索模块，该模块不仅能获取成对和成组的项目-项目图知识，还能减少多模态建模中的无关噪声。随后，SIEOUG提出用户-项目协同过滤模块，通过注意力机制聚合用户/项目嵌入以实现协同过滤。最后，SIEOUG提出带有最优用户匹配的重叠用户引导模块，用于跨领域知识共享。我们在Amazon数据集上针对多个不同任务进行的实证研究表明，在MMCDR设定下，SIEOUG显著优于当前最先进的模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Cross-Domain Recommendation (CDR) has been widely investi- gated for solving long-standing data sparsity problem via knowl- edge sharing across domains. In this paper, we focus on the Multi- Modal Cross-Domain Recommendation (MMCDR) problem where different items have multi-modal information while few users are overlapped across domains. MMCDR is particularly challenging in two aspects: fully exploiting diverse multi-modal information within each domain and leveraging useful knowledge transfer across domains. However, previous methods fail to cluster items with similar characteristics while filtering out inherit noises within different modalities, hurdling the model performance. What is worse, conventional CDR models primarily rely on overlapped users for domain adaptation, making them ill-equipped to handle scenarios where the majority of users are non-overlapped. To fill this gap, we propose Joint Similarity Item Exploration and Overlapped User Guidance (SIEOUG) for solving the MMCDR problem. SIEOUG first proposes similarity item exploration module, which not only obtains pair-wise and group-wise item-item graph knowledge, but also reduces irrelevant noise for multi-modal modeling. Then SIEOUG proposes user-item collaborative filtering module to aggregate user/item embeddings with the attention mechanism for collaborative filtering. Finally SIEOUG proposes overlapped user guidance module with optimal user matching for knowledge sharing across domains. Our empirical study on Amazon dataset with several different tasks demonstrates that SIEOUG significantly outperforms the state-of-the-art models under the MMCDR setting.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

跨域推荐（CDR）通过跨域知识共享解决数据稀疏问题。本文聚焦多模态跨域推荐（MMCDR），其中项目具有多模态信息但跨域重叠用户较少。现有方法难以充分挖掘多模态信息并过滤噪声，且依赖重叠用户进行域适应，在非重叠用户占多数时效果不佳。为此，本文提出SIEOUG方法，包含相似项目探索模块（获取成对和分组项目图知识并减少噪声）、用户项目协同过滤模块（利用注意力机制聚合嵌入）以及重叠用户引导模块（通过最优用户匹配实现跨域知识共享）。在Amazon数据集上的实验表明，SIEOUG显著优于现有模型。

### 主要创新

- 提出相似项目探索模块，同时获取成对和分组项目图知识，并减少多模态建模中的无关噪声
- 设计用户项目协同过滤模块，利用注意力机制聚合用户和项目嵌入
- 提出重叠用户引导模块，通过最优用户匹配实现跨域知识共享，缓解非重叠用户主导场景下的域适应问题

### 研究方法

SIEOUG包含三个模块：1）相似项目探索模块，构建成对和分组项目图并降噪；2）用户项目协同过滤模块，使用注意力机制聚合嵌入；3）重叠用户引导模块，通过最优用户匹配进行跨域知识共享。整体框架联合优化。

### 关键结果

在Amazon数据集上的多个任务中，SIEOUG显著优于最先进模型。

### 技术栈

- 摘要未提供具体算法、工具或数学方法名称。

### 方法优势

- 同时利用成对和分组项目图知识，增强多模态信息利用
- 通过注意力机制实现协同过滤，提升嵌入质量
- 引入最优用户匹配，有效处理非重叠用户占多数的场景

### 主要局限

- **论文本身局限**：摘要未提及论文自身局限。
- **当前证据局限**：当前仅基于摘要，缺乏实验细节、数据集规模、基线模型名称、消融实验等具体信息。

### 与当前研究方向的关联

该论文直接涉及多模态推荐和跨域推荐，与序列推荐、生成式推荐、LLM结合等关键词相关性较低，但与多模态推荐、推荐系统鲁棒性、用户建模高度相关。

---

_知识库更新时间：2026-07-13T06:43:12.874899_
