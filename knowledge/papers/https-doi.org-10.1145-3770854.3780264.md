---
title: "MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation"
paper_id: "https://doi.org/10.1145/3770854.3780264"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Explainable Artificial Intelligence (XAI)"]
---

# MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/kdd/KimMPL26) · [ArXiv](https://arxiv.org/abs/2601.01753)

## 一句话结论

> 本文提出MergeRec框架，通过模型合并实现数据隔离下的跨域序列推荐，显著提升模型在未见领域的泛化性能。

## 论文信息

- **作者**：Hyunsoo Kim, Jaewan Moon, Seongmin Park, Jongwuk Lee
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3770854.3780264](https://doi.org/10.1145/3770854.3780264)

<details open>
<summary><strong>中文摘要</strong></summary>

在特定领域数据上训练的现代推荐系统往往难以跨多个领域进行泛化。跨领域序列推荐已成为应对这一挑战的一个有前景的研究方向；然而，现有方法存在根本性局限，例如依赖跨领域的重叠用户或物品，或者忽略隐私约束的不切实际假设。在本工作中，我们提出了一种新框架——MergeRec，其基于一种新的且现实的问题设定，即数据隔离的跨领域序列推荐，在该设定下，原始用户交互数据无法在领域间共享。MergeRec包含三个关键组成部分：（1）合并初始化，（2）伪用户数据构建，以及（3）协作式合并优化。首先，我们使用无需训练的合并技术初始化一个合并模型。接下来，我们通过将每个物品视为每个领域中的虚拟序列来构建伪用户数据，从而在不依赖真实用户交互的情况下合成有意义的训练样本。最后，我们通过一个联合目标来优化领域特定的合并权重，该目标结合了推荐损失（鼓励合并模型识别相关物品）和蒸馏损失（从微调后的源模型中迁移协同过滤信号）。大量实验表明，MergeRec不仅保留了原始模型的优势，还显著增强了对未见领域的泛化能力。与传统的模型合并方法相比，MergeRec始终取得更优性能，在Recall@10上平均提升高达17.21%，凸显了模型合并作为构建通用推荐系统的一种可扩展且有效方法的潜力。源代码可在github.com/DIALLab-SKKU/MergeRec获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern recommender systems trained on domain-specific data often struggle to generalize across multiple domains. Cross-domain sequential recommendation has emerged as a promising research direction to address this challenge; however, existing approaches face fundamental limitations, such as reliance on overlapping users or items across domains, or unrealistic assumptions that ignore privacy constraints. In this work, we propose a new framework, MergeRec, based on model merging under a new and realistic problem setting termed data-isolated cross-domain sequential recommendation, where raw user interaction data cannot be shared across domains. MergeRec consists of three key components: (1) merging initialization, (2) pseudo-user data construction, and (3) collaborative merging optimization. First, we initialize a merged model using training-free merging techniques. Next, we construct pseudo-user data by treating each item as a virtual sequence in each domain, enabling the synthesis of meaningful training samples without relying on real user interactions. Finally, we optimize domain-specific merging weights through a joint objective that combines a recommendation loss, which encourages the merged model to identify relevant items, and a distillation loss, which transfers collaborative filtering signals from the fine-tuned source models. Extensive experiments demonstrate that MergeRec not only preserves the strengths of the original models but also significantly enhances generalizability to unseen domains. Compared to conventional model merging methods, MergeRec consistently achieves superior performance, with average improvements of up to 17.21% in Recall@10, highlighting the potential of model merging as a scalable and effective approach for building universal recommender systems. The source code is available at github.com/DIALLab-SKKU/MergeRec.

</details>

---

_知识库更新时间：2026-08-07T03:44:30.774047_
