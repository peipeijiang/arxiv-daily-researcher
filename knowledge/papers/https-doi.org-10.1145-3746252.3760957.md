---
title: "基于协同过滤增强的LLM推荐系统中的稀疏自编码器"
paper_id: "https://doi.org/10.1145/3746252.3760957"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 40.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)", "Advanced Graph Neural Networks"]
---

# 基于协同过滤增强的LLM推荐系统中的稀疏自编码器

> **英文原标题**：Sparse Autoencoders in Collaborative Filtering Enhanced LLM-based Recommender Systems

[查看原文](https://dblp.org/rec/conf/cikm/0003S0T25) · [Semantic Scholar](https://www.semanticscholar.org/paper/c8849b0f57426548571bc60b194c9e7d19bb4e30)

## 一句话结论

> 该论文提出使用稀疏自编码器从协同过滤中提取关键特征并去噪，以增强LLM推荐系统的输入提示，在三个数据集上取得性能提升。

## 论文信息

- **作者**：Xinyu He, Jose Sepulveda, Fei Wang, Hanghang Tong
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：40.0
- **DOI**：[https://doi.org/10.1145/3746252.3760957](https://doi.org/10.1145/3746252.3760957)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型（Large Language Model, LLM）在推荐任务中展现出了卓越的能力。近年来，研究者致力于通过从传统推荐系统中获取的协同知识来进一步提升LLM的性能。一种方法是通过可训练的投影器（projector）将学习到的嵌入向量注入LLM的提示（prompt）中，但这些嵌入向量可能携带噪声或无关信息。本文提出使用稀疏自编码器（sparse autoencoder）来改进输入提示。我们证明，稀疏自编码器能够学习到高度可解释的嵌入向量，并在推荐系统场景中提取关键的协同特征。借助稀疏自编码器，我们能够提取协同特征以增强输入提示。通过捕获每个物品的TopK特征，我们减轻了物品嵌入向量中的噪声信息，因此稀疏自编码器也有助于对提示中的嵌入向量进行去噪。我们开发了两种利用稀疏自编码器来增强或去噪输入提示的方法。在三个真实数据集上对所提方法进行了评估，结果表明两种方法均取得了显著的性能提升。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large language models (LLM) have demonstrated remarkable capability in recommendation tasks. Recently, efforts have been made to further enhance LLM performance with collaborative knowledge learned from traditional recommender systems. One approach is to inject learned embeddings into LLM prompts through a trainable projector, yet these embeddings could carry noisy or irrelevant information. In this paper, we propose using sparse autoencoders to improve input prompts. We show that sparse autoencoders can learn highly interpretable embeddings and extract key collaborative features in the case of recommender systems. With the help of sparse autoencoders, we are able to extract collaborative features to augment input prompts. By capturing TopK features of each item, we mitigate noisy information from item embeddings, therefore sparse autoencoders can also help with denoising embeddings in prompts. We develop two methods that utilize sparse autoencoders to augment or denoise input prompts. We evaluate the proposed methods on three real-world datasets and both show promising performance improvements.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文提出在基于大语言模型（LLM）的推荐系统中，利用稀疏自编码器（SAE）改进输入提示。传统方法通过可训练投影器将嵌入注入LLM提示，但嵌入可能包含噪声或无关信息。SAE能够学习高度可解释的嵌入，提取关键协同特征，并通过捕获每个物品的TopK特征来减轻噪声。作者开发了两种利用SAE增强或去噪输入提示的方法，在三个真实数据集上评估，均显示出有前景的性能提升。

### 主要创新

- 首次将稀疏自编码器应用于LLM推荐系统的提示增强
- 利用SAE提取可解释的协同特征，增强输入提示
- 通过TopK特征选择实现嵌入去噪，减少噪声信息
- 提出两种具体方法：增强提示和去噪提示

### 研究方法

使用稀疏自编码器学习物品嵌入的稀疏表示，提取TopK关键特征；将稀疏特征通过投影器注入LLM提示；在三个真实数据集上评估推荐性能。

### 关键结果

在三个真实数据集上，两种方法均显示出有前景的性能改进。

### 技术栈

- 稀疏自编码器
- 大语言模型
- 可训练投影器
- TopK特征选择

### 方法优势

- 方法创新性强，将稀疏自编码器引入LLM推荐系统
- 可解释性高，提取的协同特征易于理解
- 有效去噪，提升提示质量
- 在多个数据集上验证有效性

### 主要局限

- 摘要未提供具体局限性分析；当前证据仅基于摘要，缺乏实验细节和对比基线。

### 与当前研究方向的关联

高度相关：涉及LLM与推荐系统结合、协同过滤增强、提示工程，属于生成式推荐和序列推荐的前沿方向。

---

_知识库更新时间：2026-07-17T03:54:55.380696_
