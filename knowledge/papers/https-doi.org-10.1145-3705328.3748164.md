---
title: "是时候划分了：探索序列推荐离线评估中的数据划分策略"
paper_id: "https://doi.org/10.1145/3705328.3748164"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Customer churn and segmentation"]
---

# 是时候划分了：探索序列推荐离线评估中的数据划分策略

> **英文原标题**：Time to Split: Exploring Data Splitting Strategies for Offline Evaluation of Sequential Recommenders

[查看原文](https://dblp.org/rec/conf/recsys/GusakVKVF25) · [ArXiv](https://arxiv.org/abs/2507.16289) · [Semantic Scholar](https://www.semanticscholar.org/paper/6d5c24297d7421053e665e55ea600183ff8faff4)

## 一句话结论

> 该论文系统分析了序列推荐离线评估中不同数据划分策略（如留一法和全局时间划分）对评估结果的影响，指出留一法存在时间泄漏和测试范围不现实的问题，而全局时间划分更贴近实际部署，并提出了改进的评估协议。

## 论文信息

- **作者**：Danil Gusak, Anna Volodkevich, Anton Klenitskiy, Alexey Vasilev, Evgeny Frolov
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3705328.3748164](https://doi.org/10.1145/3705328.3748164)

<details open>
<summary><strong>中文摘要</strong></summary>

现代序列推荐系统，从轻量级基于Transformer的变体到大型语言模型，因其在下一项预测任务中的卓越表现，在学术界和工业界日益受到重视。然而，序列推荐的通用评估协议仍发展不足：它们往往无法准确反映相应的推荐任务，或与现实场景不一致。尽管广泛使用的留一法划分与下一项预测相匹配，但它允许训练期与测试期重叠，导致时间泄漏和不切实际的长测试跨度，限制了其现实相关性。全局时间划分通过在不同未来时段上进行评估解决了这些问题。然而，其在序列推荐中的应用仍然

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern sequential recommender systems, ranging from lightweight transformer-based variants to large language models, have become increasingly prominent in academia and industry due to their strong performance in the next-item prediction task.Yet common evaluation protocols for sequential recommendations remain insufficiently developed: they often fail to reflect the corresponding recommendation task accurately, or are not aligned with real-world scenarios.Although the widely used leave-one-out split matches next-item prediction, it permits the overlap between training and test periods, which leads to temporal leakage and unrealistically long test horizon, limiting real-world relevance.Global temporal splitting addresses these issues by evaluating on distinct future periods.However, its applications to sequential recommendations remain

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

现代序列推荐系统在学术界和工业界日益重要，但评估协议仍不完善，常不能准确反映任务或不符合实际场景。广泛使用的留一法划分虽匹配下一项预测，但允许训练和测试期间重叠，导致时间泄漏和不切实际的长时间测试范围，限制了现实相关性。全局时间划分通过在不同未来时期评估来解决这些问题，但其在序列推荐中的应用仍待探索。本文旨在研究不同的数据划分策略对序列推荐离线评估的影响，以改进评估协议。

### 主要创新

- 系统性地比较了留一法划分与全局时间划分在序列推荐评估中的差异
- 揭示了留一法划分导致的时间泄漏和测试范围过长问题
- 提出了全局时间划分作为更符合实际场景的替代方案
- 探讨了不同划分策略对评估结果可靠性的影响

### 研究方法

本文采用理论分析和实证研究相结合的方法，对比了留一法划分和全局时间划分在序列推荐评估中的表现，分析了时间泄漏和测试范围对评估结果的影响。

### 关键结果

摘要未提供具体实验结果，但指出留一法划分存在时间泄漏和测试范围过长的问题，而全局时间划分能解决这些问题，但应用仍有限。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 指出了现有评估协议的关键缺陷，具有实际意义
- 提出了改进评估策略的方向，有助于提升评估的可靠性
- 聚焦于序列推荐评估中的时间划分问题，主题明确

### 主要局限

- 论文局限：摘要未提供具体实验验证和详细分析。当前证据局限：仅基于摘要，无法获取具体方法细节、实验结果和结论。

### 与当前研究方向的关联

该论文直接涉及序列推荐和离线评估，与序列推荐、推荐系统评估等关键词高度相关，但未涉及生成式推荐、LLM、多模态等。

## 代码与复现

- [monkey0head/time-to-split](https://github.com/monkey0head/time-to-split)：likely，置信度 69，Stars 25

---

_知识库更新时间：2026-08-13T03:13:27.030490_
