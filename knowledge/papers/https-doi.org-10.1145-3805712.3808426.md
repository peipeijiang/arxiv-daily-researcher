---
title: "CMSL：面向推荐系统的建设性多序列学习"
paper_id: "https://doi.org/10.1145/3805712.3808426"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 64.0
tags: ["paper", "recommender-systems"]
---

# CMSL：面向推荐系统的建设性多序列学习

> **英文原标题**：CMSL: Constructive Multi-Sequence Learning for Recommendation Systems

[查看原文](https://dblp.org/rec/conf/sigir/CuiWYSWLGJWLYRY26) · [ArXiv](https://arxiv.org/abs/2606.28533) · [Semantic Scholar](https://www.semanticscholar.org/paper/5a99d9d629828100acb16389ec8a45876d03c04c)

## 一句话结论

> 论文提出Constructive Multi-Sequence Learning (CMSL)方法，通过将用户历史分解为多个连贯序列来解决单序列建模中的上下文污染问题，并在Meta的排序和检索任务中取得效果。

## 论文信息

- **作者**：Zikun Cui, Renzhi Wu, Junjie Yang, Li Sheng, Jijie Wei, Linfeng Liu, Tai Guo, Tao Jia, Xiaodong Wang, Hong Li, Li Yu, Sri Reddy, Hong Yan
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：64.0
- **DOI**：[https://doi.org/10.1145/3805712.3808426](https://doi.org/10.1145/3805712.3808426)

<details open>
<summary><strong>中文摘要</strong></summary>

序列学习已成为推荐系统中颇具前景的范式，通过捕捉用户行为的时间细微变化，超越了传统的深度学习推荐模型（DLRM）。然而，当前最先进的架构仍受限于一种类比：它们将用户历史视为单一的时间序列，类似于大语言模型（LLM）中的句子。我们观察到自然语言与推荐数据之间存在根本性差异：与文本的线性、逻辑性流动不同，用户历史本质上是多方面的。用户的旅程是多样化兴趣的碎片化反映，导致项目之间的连贯性远弱于LLM训练数据中的表现。这种结构统一性的缺失引发了上下文污染。在单序列建模中，不相关的行为会争夺相同的注意力预算。这种“噪声”信号稀释了模型的聚焦能力，实际上限制了其从背景活动中识别高意图模式的能力。为解决这一问题，我们提出了建设性多序列学习（CMSL），这是一种从被动序列输入到主动“上下文工程”的范式转变，在潜在空间中构建多个连贯序列。CMSL利用可学习的序列构建模块将用户历史分解为“纯净”的主题线索，随后通过线性注意力机制高效地对这些线索进行规模化建模。CMSL已在Meta的排序与检索任务中部署，并覆盖四个主要业务场景。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequence learning has emerged as the promising paradigm in recommendation systems, surpassing traditional Deep Learning Recommendation Models (DLRM) by capturing the temporal nuances of user behavior. However, current state-of-the-art architectures operate under a limiting analogy: they treat user history as a monolithic chronological sequence like a sentence in a Large Language Model (LLM). We observe a fundamental divergence between natural language and recommendation data: unlike the linear, logical flow of text, user history is inherently multi-faceted. A user's journey is a fragmented reflection of diverse interests, resulting in much weaker coherence between items than is found in LLM training data. This lack of structural unity leads to context pollution. In single-sequence modeling, unrelated behaviors compete for the same attention budget. This ''noisy'' signal dilutes the model's focus, effectively capping its ability to discern high-intent patterns from background activity. To address this, we propose Constructive Multi-Sequence Learning (CMSL), a paradigm shift from passive sequence ingestion to active ''context engineering'' that constructs multiple coherent sequences in latent space. CMSL leverages a learnable Sequence Construction Module to disentangle user history into ''pure'' thematic strands, followed by a linear attention mechanism to efficiently model these strands at scale. CMSL has been deployed across ranking and retrieval tasks and across four major surfaces at Meta.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出建设性多序列学习（CMSL）框架，旨在解决序列推荐中用户历史行为序列的“上下文污染”问题。传统方法将用户历史视为单一单调序列，但用户行为本质上是多方面的，不同兴趣混杂导致注意力分散。CMSL通过可学习的序列构建模块，将用户历史在潜在空间中解耦为多个主题一致的序列，并采用线性注意力机制高效建模。该方法在Meta的多个排序和检索任务中部署，实验表明CMSL在CTR/CVR预测和检索指标上均取得显著提升。

### 主要创新

- 提出“上下文污染”问题，并引入多序列构建与学习范式。
- 设计可学习的多序列构建模块，通过交叉注意力实现意图感知的上下文构建。
- 开发线性时间注意力机制，降低Transformer风格注意力的计算成本，支持高效多序列建模。
- 在工业级规模（数十亿日活用户）上验证有效性，覆盖排序和检索任务。

### 研究方法

CMSL包含特征预处理和CMSL块。特征预处理将非序列特征（稠密/稀疏）映射为d维嵌入，并将多序列通过门控求和压缩为单一序列。CMSL块由多序列构建（基于非序列特征投影出K组key/value，通过交叉注意力构建K个序列）、自注意力（采用线性近似HSTU的注意力）、序列摘要（PMA池化）和序列压缩（拼接后MLP投影）组成。最终表示用于多任务预测。

### 关键结果

在排序任务上，CMSL在表面1的Comment和Like任务上训练NE分别降低0.54%和0.31%，评估NE降低0.62%和0.33%；在表面2/3/4的两阶段架构中，CTR和CVR的NE降低0.06%-0.13%。在检索任务上，表面5的在线A/B测试中四个指标分别提升0.116%、0.158%、0.171%和0.092%。

### 技术栈

- SiLU激活函数
- 泰勒展开近似
- 多项式核函数
- 线性注意力机制
- 交叉注意力
- 多头注意力池化（PMA）
- 门控MLP
- HSTU注意力近似
- 原生稀疏注意力（Native Sparse Attention）

### 方法优势

- 创新性地提出多序列构建范式，有效缓解上下文污染。
- 线性注意力机制降低了计算复杂度，支持工业级部署。
- 在Meta多个大规模生产系统上验证，结果可靠。
- 方法通用，可应用于排序和检索任务。

### 主要局限

- 多序列构建模块引入额外参数和计算开销。
- 线性注意力近似可能损失部分精度。
- 实验仅在Meta内部数据上验证，泛化性未知。
- 未与最新LLM-based推荐方法进行直接比较。

### 与当前研究方向的关联

论文紧密围绕序列推荐、生成式推荐、CTR/CVR预测和工业落地。提出CMSL方法解决序列推荐中的上下文污染，采用生成式序列建模思路，并在Meta工业系统部署，与关键词高度相关。

---

_知识库更新时间：2026-07-24T04:05:55.201280_
