---
title: "一次前向，任意顺序：基于LLM的推荐中位置不变的列表式重排序"
paper_id: "https://doi.org/10.1145/3805712.3809952"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 68.0
tags: ["paper", "recommender-systems"]
---

# 一次前向，任意顺序：基于LLM的推荐中位置不变的列表式重排序

> **英文原标题**：One Pass, Any Order: Position-Invariant Listwise Reranking for LLM-Based Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/BitoRH26) · [ArXiv](https://arxiv.org/abs/2604.27599)

## 一句话结论

> 本文提出InvariRank，一种基于架构的排列不变性listwise重排框架，通过屏蔽交叉注意力和共享位置编码，使LLM推荐重排对候选顺序不敏感，在保持竞争力的同时产生稳定排序。

## 论文信息

- **作者**：Ethan Bito, Yongli Ren, Estrid He
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：68.0
- **DOI**：[https://doi.org/10.1145/3805712.3809952](https://doi.org/10.1145/3805712.3809952)

<details open>
<summary><strong>中文摘要</strong></summary>

大型语言模型（LLMs）正越来越多地被用于推荐重排序，但其列表式预测可能依赖于候选项目的呈现顺序。这导致了基于集合的推荐本质与仅解码器LLMs基于序列的计算方式之间的不匹配——当对原本相同的候选集进行排列时，项目得分和最终排序可能发生改变。这种顺序敏感性使得基于LLM的重排序器难以依赖，因为排序结果可能反映的是提示序列化方式而非用户偏好。我们提出InvariRank，一种在架构层面解决这一依赖性的排列不变列表式重排序框架。InvariRank通过结构化注意力掩码阻断跨候选注意力，并利用旋转位置编码（RoPE）下的共享位置框架消除位置引起的评分变化。结合列表式学习排序目标，该模型可在单次前向传播中对所有候选项目进行评分，避免了需要多次排列候选集的基于排列的不变性训练目标。在推荐基准上的实验表明，InvariRank在保持具有竞争力的排序效果的同时，能在候选排列间产生稳定的排序结果。研究结果表明，架构层面的不变性是实现可靠且高效的基于LLM的推荐重排序的实用路径。源代码见https://github.com/ejbito/InvariRank。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large language models (LLMs) are increasingly used for recommendation reranking, but their listwise predictions can depend on the order in which candidates are presented. This creates a mismatch between the set-based nature of recommendation and the sequence-based computation of decoder-only LLMs, where permuting an otherwise identical candidate set can change item scores and final rankings. Such order sensitivity makes LLM-based rerankers difficult to rely on, since rankings may reflect prompt serialization rather than user preference. We propose InvariRank, a permutation-invariant listwise reranking framework that addresses this dependence at the architectural level. InvariRank blocks cross-candidate attention with a structured attention mask and negates position-induced scoring changes through shared positional framing under Rotary Positional Embeddings (RoPE). Combined with a listwise learning-to-rank objective, the model scores all candidates in a single forward pass, avoiding permutation-based invariance training objectives that require multiple permutations of a candidate set. Experiments on recommendation benchmarks show that InvariRank maintains competitive ranking effectiveness while producing stable rankings across candidate permutations. The results suggest that architectural invariance is a practical route to reliable and efficient LLM-based recommendation reranking. The source code is at https://github.com/ejbito/InvariRank.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

论文研究了大语言模型（LLM）在列表式推荐重排序中的位置偏差问题，即候选集顺序变化会导致评分和排序结果不同。作者指出这种顺序敏感性源于解码器LLM的架构特性：跨候选注意力泄漏和旋转位置编码（RoPE）导致的偏移漂移。为此，提出InvariRank框架，通过结构化注意力掩码阻止候选间交互，并利用共享位置框架消除RoPE引入的位置依赖，使模型在单次前向传播中实现排列不变性。实验在MovieLens-32M和Amazon Books数据集上使用LLaMA 3.2 3B和Mistral 7B模型，结果表明InvariRank在保持竞争性排序效果的同时，显著提升了排列鲁棒性（Kendall's τ接近1），且无需多次推理或辅助损失。

### 主要创新

- 识别出跨候选注意力泄漏和RoPE偏移漂移是LLM重排序中位置偏差的两个具体来源。
- 提出InvariRank框架，通过结构化注意力掩码和共享位置框架在架构层面强制实现排列不变性。
- 在单次前向传播中实现排列不变性，无需排列集成或辅助不变性损失。
- 结合LambdaRank列表式排序目标，在保持列表式监督的同时确保计算不变性。

### 研究方法

采用两阶段推荐流水线：第一阶段使用LightGCN检索候选集，第二阶段使用LLM（LLaMA 3.2 3B或Mistral 7B）进行列表式重排序。InvariRank通过结构化段掩码（公式4）阻止候选间注意力，并通过共享位置框架（公式6）使每个候选与用户上下文保持相同的位置偏移。训练使用LoRA微调，优化目标为LambdaRank损失（公式7），权重为ΔnDCG。评估指标包括HR@k、nDCG@k以及排列鲁棒性指标（Kendall's τ、Spearman's ρ、Top-5一致性）。

### 关键结果

InvariRank在MovieLens-32M和Amazon Books上取得了接近完美的排列鲁棒性（Kendall's τ > 0.98），同时保持了与列表式微调（LFT）相近的排序效果（nDCG@10约0.82 vs 0.85）。消融实验表明，结构化注意力掩码是主要贡献者，共享位置框架进一步提升了鲁棒性。与基线相比，InvariRank在单次前向传播中实现了比推理时方法（如Bootstrapping、SGS）更高的鲁棒性。

### 技术栈

- LLaMA 3.2 3B-Instruct
- Mistral 7B-Instruct
- LoRA（rank=16, α=32）
- Rotary Positional Embeddings (RoPE)
- LambdaRank损失
- LightGCN（第一阶段检索器）
- 结构化注意力掩码
- 共享位置框架

### 方法优势

- 从架构层面解决位置偏差，而非通过推理时聚合或训练正则化，从根本上消除了顺序依赖。
- 单次前向传播即可实现排列不变性，计算效率高。
- 在多个数据集和LLM骨干上验证了方法的有效性和鲁棒性。
- 消融实验清晰展示了各组件贡献。

### 主要局限

- 候选隔离去除了跨候选交互，可能丢失有用的比较信号，限制细粒度偏好建模。
- 实验仅针对固定大小的候选集（N=25）和两个推荐数据集，泛化性有待验证。
- 排序效果相比列表式微调（LFT）略有下降，存在效果-鲁棒性权衡。

### 与当前研究方向的关联

论文与LLM与推荐系统结合、排序与重排、用户建模高度相关，直接研究LLM重排序中的位置偏差和排列不变性，属于推荐系统鲁棒性和可靠性的重要方向。

## 代码与复现

- [ejbito/InvariRank](https://github.com/ejbito/InvariRank)：official，置信度 100，Stars 4

---

_知识库更新时间：2026-07-16T03:56:50.204347_
