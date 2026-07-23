---
title: "SpecTran：基于频谱感知Transformer适配器的大语言模型增强序列推荐"
paper_id: "https://doi.org/10.1145/3805712.3809701"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 55.0
tags: ["paper", "recommender-systems"]
---

# SpecTran：基于频谱感知Transformer适配器的大语言模型增强序列推荐

> **英文原标题**：SpecTran: Spectral-Aware Transformer-based Adapter for LLM-Enhanced Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/CuiLWZWWC26) · [ArXiv](https://arxiv.org/abs/2601.21986)

## 一句话结论

> 提出SpecTran，一种基于谱感知Transformer的适配器，用于将LLM语义嵌入注入序列推荐模型，解决维度塌陷和刚性截断问题，提升推荐性能。

## 论文信息

- **作者**：Yu Cui, Feng Liu, Zhaoxiang Wang, Changwang Zhang, Jun Wang, Can Wang, Jiawei Chen
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：55.0
- **DOI**：[https://doi.org/10.1145/3805712.3809701](https://doi.org/10.1145/3805712.3809701)

<details open>
<summary><strong>中文摘要</strong></summary>

传统的序列推荐（SR）模型从用户-物品交互中学习低维的物品ID嵌入，往往忽略了物品标题或描述等文本信息。大语言模型（LLMs）的最新进展激发了一系列研究，这些研究利用高维语义嵌入对物品文本信息进行编码，并设计转换方法将此类嵌入注入SR模型。这些嵌入转换策略可分为两类，且均存在显著缺陷：1）基于适配器的方法会出现严重的维度坍缩，将信息集中到少数主导维度上；2）基于奇异值分解（SVD）的方法则僵化且依赖人工操作，仅考虑少数主频谱成分，而丢弃了剩余频谱中的丰富信息。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Traditional sequential recommendation (SR) models learn low-dimensional item ID embeddings from user-item interactions, often overlooking textual information such as item titles or descriptions. Recent advances in Large Language Models (LLMs) have inspired a surge of research that encodes item textual information with high-dimensional semantic embeddings, and designs transformation methods to inject such embeddings into SR models. These embedding transformation strategies can be categorized into two types, both of which exhibits notable drawbacks: 1) adapter-based methods suffer from pronounced dimension collapse, concentrating information into a few dominant dimensions; 2) SVD-based methods are rigid and manual, considering only a few principal spectral components while discarding rich information in the remaining spectrum.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对序列推荐中语言嵌入与物品嵌入维度不匹配的问题，分析了现有适配器方法存在频谱维度坍塌、SVD方法信息丢失且缺乏灵活性的缺陷，提出SpecTran——一种频谱感知的Transformer适配器。该方法在频谱域操作，利用可学习的注意力机制聚合全频谱信息，并引入可学习的频谱位置编码注入奇异值先验，引导注意力关注主要频谱分量并促进输出维度多样性。在四个真实数据集和三种序列推荐骨干上，SpecTran平均提升9.17%，且参数和计算开销小。

### 主要创新

- 识别并分析了适配器方法中的频谱维度坍塌问题。
- 提出在频谱域操作的Transformer适配器，可自适应选择和聚合信息性频谱分量。
- 设计可学习的频谱位置编码，利用泰勒展开将奇异值映射为任务特定的重要性权重。
- 采用Softshrink稀疏激活函数，防止次要频谱分量淹没主要分量。

### 研究方法

首先对物品语言嵌入进行SVD分解得到频谱空间；然后设计频谱感知Transformer适配器，其中可学习的Query和Key计算注意力分数，以U作为Value，通过Softshrink激活实现稀疏聚合；同时引入频谱位置编码矩阵A，其对角线元素由泰勒展开映射奇异值得到，仅作用于前d个主成分；最终输出E_s = U[phi(QK^T)+A]^T。该适配器与ID嵌入融合后输入序列推荐骨干（BERT4Rec、SASRec、HSTU）进行端到端训练。

### 关键结果

SpecTran在四个数据集上平均提升9.17%，显著优于所有基线。；消融实验表明，移除全局注意力或位置编码均导致性能下降，Softshrink优于Softmax。；在不同嵌入维度（16-256）下，SpecTran均优于AlphaFuse和RLMRec。；SpecTran参数量仅2.21M，训练和推理时间接近骨干模型。；案例研究显示，次要频谱分量累积权重不可忽视，SpecTran有效聚合了这些信息。

### 技术栈

- SVD（奇异值分解）
- Transformer注意力机制
- Softshrink激活函数
- 泰勒展开多项式映射
- InfoNCE损失函数
- Adam优化器
- LLaMA3-8B语言模型

### 方法优势

- 方法创新性强，从频谱角度解决维度坍塌问题，理论分析深入。
- 模型轻量且与骨干无关，易于集成。
- 实验全面，涵盖多种骨干、数据集和维度，消融充分。
- 性能提升显著，平均9.17%。

### 主要局限

- 输入内容未提供在更大规模数据集或工业场景下的验证。
- 对LLM编码器的选择（仅LLaMA3-8B）可能影响泛化性。
- Softshrink阈值λ为可学习参数，但未讨论其初始化敏感性。

### 与当前研究方向的关联

论文紧密围绕序列推荐、大语言模型增强推荐、适配器方法，属于推荐系统与LLM结合的前沿方向，与关键词高度相关。

---

_知识库更新时间：2026-07-23T04:05:05.422960_
