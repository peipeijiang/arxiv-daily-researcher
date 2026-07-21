---
title: "我们真的需要专门化吗？评估通用文本嵌入在零样本推荐和搜索中的表现"
paper_id: "https://doi.org/10.1145/3705328.3748040"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 51.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Recommender Systems and Techniques", "Machine Learning in Healthcare"]
---

# 我们真的需要专门化吗？评估通用文本嵌入在零样本推荐和搜索中的表现

> **英文原标题**：Do We Really Need Specialization? Evaluating Generalist Text Embeddings for Zero-Shot Recommendation and Search

[查看原文](https://dblp.org/rec/conf/recsys/AttimonelliBPJS25) · [ArXiv](https://arxiv.org/abs/2507.05006) · [Semantic Scholar](https://www.semanticscholar.org/paper/5247338575ce40db1bbbadaa6f68887debd4d4b2)

## 一句话结论

> 论文证明通用文本嵌入模型（GTEs）在零样本序列推荐和产品搜索中优于专门微调的模型，无需领域特定适配。

## 论文信息

- **作者**：Matteo Attimonelli, Alessandro Bellis, Claudio Pomo, Dietmar Jannach, Eugenio Di Sciascio, Tommaso Di Noia
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：51.0
- **DOI**：[https://doi.org/10.1145/3705328.3748040](https://doi.org/10.1145/3705328.3748040)

<details open>
<summary><strong>中文摘要</strong></summary>

预训练语言模型（Pre-trained Language Models, PLMs）被广泛用于从推荐系统和搜索中的项目元数据中提取语义表示。在序列推荐中，PLMs通过文本元数据增强基于ID的嵌入表示；而在产品搜索中，它们则将项目特征与用户意图对齐。近期研究表明，需要针对任务和领域进行微调以提升表示能力。本文针对电子商务应用对这一假设提出质疑，证明在大规模语料上预训练的通用文本嵌入模型（Generalist Text Embedding Models, GTEs）无需专门适配即可保证强大的零样本性能。我们在主流电子商务基准上的实验表明，GTEs在序列推荐和产品搜索中均优于传统模型及微调模型。我们将此归因于其更优的表示能力——这些模型能在嵌入空间中更均匀地分布特征。最后，我们证明通过聚焦最具信息量的方向（例如通过主成分分析，PCA）压缩嵌入维度，能有效降低噪声并提升专用模型的性能。为确保可复现性，我们提供代码仓库：https://github.com/sisinflab/GTE-Zero-Shot-Recsys。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Pre-trained language models (PLMs) are widely used to derive semantic representations from item metadata in recommendation and search.In sequential recommendation, PLMs enhance ID-based embeddings through textual metadata, while in product search, they align item characteristics with user intent.Recent studies suggest task and domain-specific fine-tuning are needed to improve representational power.This paper challenges this assumption for e-commerce applications, showing that Generalist Text Embedding Models (GTEs), pre-trained on large-scale corpora, can guarantee strong zero-shot performance without specialized adaptation.Our experiments on popular e-commerce benchmarks demonstrate that GTEs outperform traditional and fine-tuned models in both sequential recommendation and product search.We attribute this to a superior representational power, as they distribute features more evenly across the embedding space.Finally, we show that compressing embedding dimensions by focusing on the most informative directions (e.g., via PCA) effectively reduces noise and improves the performance of specialized models.To ensure reproducibility, we provide our repository at https://github.com/sisinflab/GTE-Zero-Shot-Recsys.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

该论文挑战了在电子商务应用中需要对文本嵌入模型进行任务和领域特定微调以提升表示能力的假设。作者提出通用文本嵌入模型（GTEs），这些模型在大规模语料库上预训练，无需专门适配即可在零样本场景下表现出色。实验表明，在序列推荐和产品搜索任务中，GTEs优于传统模型和微调模型，这归因于其更均匀的特征分布和更强的表示能力。此外，通过PCA压缩嵌入维度，聚焦于信息量最大的方向，可以有效减少噪声并提升专门化模型的性能。论文提供了开源代码以确保可复现性。

### 主要创新

- 挑战了任务和领域特定微调是提升文本嵌入表示能力必要条件的普遍假设。
- 提出通用文本嵌入模型（GTEs）在零样本电子商务推荐和搜索中表现优异。
- 发现GTEs的优越性能源于其在嵌入空间中更均匀地分布特征。
- 证明通过PCA压缩嵌入维度可减少噪声并提升专门化模型性能。

### 研究方法

论文采用实验研究方法，在流行的电子商务基准数据集上比较通用文本嵌入模型（GTEs）与传统模型及微调模型在序列推荐和产品搜索任务中的零样本性能。通过分析嵌入空间的特征分布来解释性能差异，并利用主成分分析（PCA）进行维度压缩以验证噪声减少效果。

### 关键结果

通用文本嵌入模型（GTEs）在零样本序列推荐和产品搜索中优于传统模型和微调模型。；GTEs的优越性能归因于其在嵌入空间中更均匀地分布特征。；通过PCA压缩嵌入维度，聚焦于信息量最大的方向，可有效减少噪声并提升专门化模型性能。

### 技术栈

- 预训练语言模型（PLMs）
- 通用文本嵌入模型（GTEs）
- 主成分分析（PCA）

### 方法优势

- 挑战了领域内普遍假设，具有创新性。
- 实验覆盖序列推荐和产品搜索两个重要任务，验证了GTEs的通用性。
- 提供了开源代码，确保可复现性。
- 对性能差异提供了直观的解释（特征分布均匀性）。

### 主要局限

- 论文局限：摘要未提供具体数据集、基线模型、微调方法或消融实验细节，无法评估实验的全面性。当前证据局限：仅基于摘要，无法确认实验规模、统计显著性、计算成本或实际部署可行性。

### 与当前研究方向的关联

论文与序列推荐、LLM与推荐系统结合、生成式推荐等关键词高度相关，因为它研究了预训练语言模型在推荐和搜索中的零样本能力，并挑战了微调的必要性。

## 代码与复现

- [sisinflab/GTE-Zero-Shot-Recsys](https://github.com/sisinflab/GTE-Zero-Shot-Recsys)：official，置信度 100，Stars 1

---

_知识库更新时间：2026-07-21T04:03:10.445269_
