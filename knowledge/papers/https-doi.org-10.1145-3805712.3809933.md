---
title: "From Continuous Pretraining to Domain-Adaptive Reranking via Task Vector Adaptation"
paper_id: "https://doi.org/10.1145/3805712.3809933"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 8.0
tags: ["paper", "recommender-systems"]
---

# From Continuous Pretraining to Domain-Adaptive Reranking via Task Vector Adaptation

[查看原文](https://dblp.org/rec/conf/sigir/ChoLSHLL26)

## 一句话结论

> 该论文提出一种基于任务向量的细粒度适应方法，通过学习参数级缩放系数，将连续预训练中的领域知识迁移到LLM reranker中，在多个领域实现稳定性能提升。

## 论文信息

- **作者**：Sanghyun Cho, Myeongjin Lee, Jong-hun Shin, Jeong Heo, Kiyoung Lee, Soojong Lim
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：8.0
- **DOI**：[https://doi.org/10.1145/3805712.3809933](https://doi.org/10.1145/3805712.3809933)

<details open>
<summary><strong>中文摘要</strong></summary>

基于大语言模型（LLM）的排序器在信息检索任务中展现出强大性能，但由于构建高质量领域特定训练数据集需要大量成本与精力，将其适配至专业领域仍具挑战。为解决这一局限，我们利用从持续预训练中获取的任务向量作为领域知识迁移的机制。然而，现有任务向量整合方法对缩放因子高度敏感，可能导致跨领域与跨模型规模的性能不稳定。本研究提出一种细粒度任务向量适配方法，该方法为任务向量学习参数级缩放系数。这些系数通过语言建模目标进行优化，同时保持所有模型参数固定，从而在不降低排序能力的前提下实现领域特定知识的有效整合。在通用领域基准及两个模型规模下的五个专业领域上的实验表明，我们的方法在大多数领域均能提供稳定的性能提升，并避免了固定任务向量缩放所导致的性能退化问题。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large language model (LLM)-based rerankers have demonstrated strong performance in information retrieval tasks, but adapting them to specialized domains remains challenging due to the substantial cost and effort required to construct high-quality domain-specific training datasets. To address this limitation, we leverage task vectors derived from continuous pretraining as a mechanism for transferring domain knowledge. However, existing task vector integration methods are highly sensitive to scaling factors and can lead to unstable performance across domains and model scales. In this work, we propose a fine-grained task vector adaptation method that learns parameter-wise scaling coefficients for the task vector. These coefficients are optimized using a language modeling objective while keeping all model parameters fixed, enabling effective integration of domain-specific knowledge without degrading reranking capabilities. Experiments on a general-domain benchmark and five specialized domains across two model scales demonstrate that our method provides stable improvements across most domains and avoids the degradation observed with fixed task vector scaling.

</details>

---

_知识库更新时间：2026-07-22T04:05:16.240944_
