---
title: "BERT4Rec：利用Transformer的双向编码器表示进行序列推荐"
paper_id: "https://doi.org/10.48550/arxiv.1904.06690"
source: "citation"
published: "2019-04-14T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Machine Learning in Healthcare", "Topic Modeling"]
---

# BERT4Rec：利用Transformer的双向编码器表示进行序列推荐

> **英文原标题**：BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer

[查看原文](http://arxiv.org/abs/1904.06690) · [ArXiv](https://arxiv.org/abs/1904.06690)

## 一句话结论

> 论文提出BERT4Rec，利用双向Transformer和Cloze任务进行序列推荐，在多个数据集上优于现有序列推荐模型。

## 论文信息

- **作者**：Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Lin, Xiao, Wenwu Ou, Peng Jiang
- **来源**：arXiv (Cornell University)
- **发布时间**：2019-04-14
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.48550/arxiv.1904.06690](https://doi.org/10.48550/arxiv.1904.06690)

<details open>
<summary><strong>中文摘要</strong></summary>

对用户历史行为中动态且不断演化的偏好进行建模，对于推荐系统而言既具挑战性又至关重要。以往的方法采用序列神经网络（如循环神经网络）将用户的历史交互从左到右编码为隐藏表示，以进行推荐。尽管这些方法取得了令人满意的效果，但它们通常假设序列具有严格有序性，而这在实际中并不总是成立。我们认为，这种从左到右的单向架构限制了历史序列表示的能力。为此，我们提出了一种用于序列推荐的基于Transformer的双向编码器表示模型（BERT4Rec）。然而，在深度双向模型中同时基于左右上下文进行条件建模会使训练变得平凡，因为每个物品可以间接“看到目标物品”。为解决这一问题，我们使用完形填空任务（Cloze task）来训练双向模型，即通过同时基于左右上下文来预测序列中被掩码的物品。与在序列中每个位置预测下一个物品相比，完形填空任务能够产生更多样本，从而训练出更强大的双向模型。在四个基准数据集上的大量实验表明，我们的模型持续优于各种最先进的序列推荐模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modeling users' dynamic and evolving preferences from their historical behaviors is challenging and crucial for recommendation systems. Previous methods employ sequential neural networks (e.g., Recurrent Neural Network) to encode users' historical interactions from left to right into hidden representations for making recommendations. Although these methods achieve satisfactory results, they often assume a rigidly ordered sequence which is not always practical. We argue that such left-to-right unidirectional architectures restrict the power of the historical sequence representations. For this purpose, we introduce a Bidirectional Encoder Representations from Transformers for sequential Recommendation (BERT4Rec). However, jointly conditioning on both left and right context in deep bidirectional model would make the training become trivial since each item can indirectly "see the target item". To address this problem, we train the bidirectional model using the Cloze task, predicting the masked items in the sequence by jointly conditioning on their left and right context. Comparing with predicting the next item at each position in a sequence, the Cloze task can produce more samples to train a more powerful bidirectional model. Extensive experiments on four benchmark datasets show that our model outperforms various state-of-the-art sequential models consistently.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对序列推荐中传统从左到右单向模型（如RNN、SASRec）的局限性，提出了一种基于深度双向自注意力的序列推荐模型BERT4Rec。该模型采用Transformer的双向编码器结构，通过Cloze任务（随机掩码预测）来训练，使每个物品的表示能够融合左右两侧的上下文信息，从而更有效地建模用户行为序列。在四个真实数据集上的实验表明，BERT4Rec在HR、NDCG、MRR等指标上均优于多种现有最先进方法。

### 主要创新

- 首次将深度双向序列模型和Cloze目标引入推荐系统领域。
- 提出使用双向自注意力网络建模用户行为序列，克服单向模型的信息限制。
- 采用Cloze任务（随机掩码预测）训练双向模型，避免信息泄漏并提高训练效率。
- 在测试阶段通过附加[mask]标记实现与序列推荐任务的一致性。

### 研究方法

模型基于Transformer层堆叠，包含多头自注意力、位置前馈网络、残差连接和层归一化。输入为物品嵌入与位置嵌入之和，输出层使用两层前馈网络和softmax预测掩码物品。训练时随机掩码一定比例的物品，通过最小化掩码物品的负对数似然进行优化。测试时在序列末尾添加[mask]标记，预测其对应物品。

### 关键结果

在Beauty、Steam、ML-1m、ML-20m四个数据集上，BERT4Rec在HR@10、NDCG@10、MRR等指标上均优于所有基线，平均提升约7.24% HR@10、11.03% NDCG@10、11.46% MRR。

### 技术栈

- Transformer
- 多头自注意力
- 位置前馈网络
- GELU激活函数
- 残差连接
- 层归一化
- Dropout
- Adam优化器
- Cloze任务

### 方法优势

- 提出双向建模思路，有效提升序列推荐性能。
- Cloze任务设计巧妙，解决了双向模型训练中的信息泄漏问题。
- 实验充分，在多个数据集上验证了有效性。
- 提供了注意力可视化分析，增强可解释性。

### 主要局限

- 模型复杂度较高，训练和推理成本可能较大。
- 对超参数（如掩码比例、最大序列长度）敏感，需要针对数据集调整。
- 未考虑用户长期和短期兴趣的显式建模。

### 与当前研究方向的关联

论文聚焦于序列推荐，提出基于Transformer的双向模型，与关键词“序列推荐”高度相关；同时涉及用户建模和深度学习应用，与“用户建模”和“生成式推荐”有一定关联。

## 代码与复现

- [PaddlePaddle/PaddleRec](https://github.com/PaddlePaddle/PaddleRec)：likely，置信度 69，Stars 4084
- [FeiSun/BERT4Rec](https://github.com/FeiSun/BERT4Rec)：possible，置信度 30，Stars 734

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3726302.3731696
- **seed_title**：Navigating Large Language Models for Recommendation: From Architecture to Learning Paradigms and Deployment
- **seed_score**：99.0

</details>

---

_知识库更新时间：2026-08-08T02:39:38.052405_
