---
title: "BERT4Rec：使用双向编码器表示进行序列推荐"
paper_id: "https://doi.org/10.1145/3357384.3357895"
source: "citation"
published: "2019-11-03T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Machine Learning in Healthcare"]
---

# BERT4Rec：使用双向编码器表示进行序列推荐

> **英文原标题**：BERT4Rec

[查看原文](https://doi.org/10.1145/3357384.3357895)

## 一句话结论

> BERT4Rec利用深度双向自注意力模型和Cloze目标，通过联合左右上下文预测随机掩码的物品，从而更有效地建模用户行为序列，在四个基准数据集上优于现有序列推荐模型。

## 论文信息

- **作者**：Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, Peng Jiang
- **来源**：Proceedings of the 28th ACM International Conference on Information and Knowledge Management
- **发布时间**：2019-11-03
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3357384.3357895](https://doi.org/10.1145/3357384.3357895)

<details open>
<summary><strong>中文摘要</strong></summary>

从用户的历史行为中建模其动态偏好，对于推荐系统而言既充满挑战又至关重要。以往的方法采用序列神经网络，从左到右将用户的历史交互编码为隐藏表示，以进行推荐。尽管这些方法有效，但我们认为这种从左到右的单向模型并非最优，原因包括：\begin enumerate* [label=series\itshape\alph*\upshape)] \item 单向架构限制了用户行为序列中隐藏表示的表达能力；\item 它们通常假设一个严格有序的序列，而这在实际中并不总是成立。\end enumerate* 为解决这些局限，我们提出了一种名为BERT4Rec的序列推荐模型，该模型采用深度双向自注意力机制来建模用户行为序列。为避免信息泄漏并高效训练双向模型，我们将Cloze目标引入序列推荐，通过同时基于序列中被随机遮蔽项目的左右上下文进行条件预测。通过这种方式，我们学习到一个双向表示模型，使得用户历史行为中的每个项目都能融合来自左右两侧的信息，从而进行推荐。在四个基准数据集上的大量实验表明，我们的模型在一致性上优于多种最先进的序列推荐方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modeling users' dynamic preferences from their historical behaviors is challenging and crucial for recommendation systems. Previous methods employ sequential neural networks to encode users' historical interactions from left to right into hidden representations for making recommendations. Despite their effectiveness, we argue that such left-to-right unidirectional models are sub-optimal due to the limitations including: \begin enumerate* [label=series\itshape\alph*\upshape)] \item unidirectional architectures restrict the power of hidden representation in users' behavior sequences; \item they often assume a rigidly ordered sequence which is not always practical. \end enumerate* To address these limitations, we proposed a sequential recommendation model called BERT4Rec, which employs the deep bidirectional self-attention to model user behavior sequences. To avoid the information leakage and efficiently train the bidirectional model, we adopt the Cloze objective to sequential recommendation, predicting the random masked items in the sequence by jointly conditioning on their left and right context. In this way, we learn a bidirectional representation model to make recommendations by allowing each item in user historical behaviors to fuse information from both left and right sides. Extensive experiments on four benchmark datasets show that our model outperforms various state-of-the-art sequential models consistently.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

论文针对序列推荐中用户动态偏好建模问题，指出现有基于从左到右单向序列神经网络的方法存在两个局限：一是单向架构限制了用户行为序列中隐藏表示的能力；二是它们通常假设严格有序的序列，这在实际中并不总是成立。为解决这些问题，论文提出BERT4Rec模型，采用深度双向自注意力机制对用户行为序列建模。为避免信息泄漏并高效训练双向模型，论文将Cloze目标（即随机掩码预测）应用于序列推荐，通过联合左右上下文预测序列中被随机掩码的物品。这样，模型学习双向表示，使得用户历史行为中的每个物品都能融合左右两侧的信息。在四个基准数据集上的大量实验表明，该模型一致优于多种最先进的序列推荐模型。

### 主要创新

- 首次将深度双向自注意力模型应用于序列推荐，克服单向模型的局限性。
- 将Cloze目标（掩码语言建模）引入序列推荐，实现双向上下文联合建模。
- 通过双向编码，使每个物品能融合左右两侧信息，增强表示能力。
- 在多个基准数据集上验证了模型相对于现有序列推荐方法的优越性。

### 研究方法

论文采用深度双向自注意力架构（类似BERT）对用户行为序列进行建模。具体地，将用户历史交互序列中的物品作为输入，通过多层双向Transformer编码器学习每个位置的表示。训练时采用Cloze目标：随机掩码序列中的部分物品，然后基于左右上下文预测被掩码的物品。推理时，通过模型输出每个物品的得分进行推荐。

### 关键结果

在四个基准数据集上的实验表明，BERT4Rec模型一致优于多种最先进的序列推荐模型。

### 技术栈

- 深度双向自注意力（Deep Bidirectional Self-Attention）
- Transformer编码器
- Cloze目标（掩码语言建模）

### 方法优势

- 创新性地将双向自注意力应用于序列推荐，解决了单向模型的限制。
- 采用Cloze目标有效训练双向模型，避免信息泄漏。
- 实验证明模型在多个数据集上表现优越，具有通用性。

### 主要局限

- 论文局限：摘要未提供具体局限性讨论。当前证据局限：仅基于摘要，无法评估模型复杂度、训练效率、对长序列的适应性等潜在问题。

### 与当前研究方向的关联

论文与序列推荐高度相关，直接针对用户行为序列建模；同时涉及用户建模（动态偏好）和生成式推荐（通过预测掩码物品生成推荐）。虽然未明确提及LLM，但双向自注意力架构与Transformer相关，与LLM技术有共通之处。

## 代码与复现

- [FeiSun/BERT4Rec](https://github.com/FeiSun/BERT4Rec)：likely，置信度 69，Stars 734
- [PaddlePaddle/PaddleRec](https://github.com/PaddlePaddle/PaddleRec)：possible，置信度 30，Stars 4084

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3626772.3657828
- **seed_title**：Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning
- **seed_score**：90.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.669248_
