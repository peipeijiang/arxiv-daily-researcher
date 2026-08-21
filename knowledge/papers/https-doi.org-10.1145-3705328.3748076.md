---
title: "超越即时点击：面向序列电影推荐的参与感知与MoE增强Transformer"
paper_id: "https://doi.org/10.1145/3705328.3748076"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 57.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Expert finding and Q&A systems"]
---

# 超越即时点击：面向序列电影推荐的参与感知与MoE增强Transformer

> **英文原标题**：Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers for Sequential Movie Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/JiangPZC25) · [Semantic Scholar](https://www.semanticscholar.org/paper/5f8b494b9560ffe19ac41f10825428587cb09447)

## 一句话结论

> 该论文提出了一种参与度感知和MoE增强的Transformer序列推荐框架，通过改进负采样、多任务学习和多步预测，在流媒体数据上显著提升了排序性能。

## 论文信息

- **作者**：Haotian Jiang, Sibendu Paul, Haiyang Zhang, C Y Chen
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：57.0
- **DOI**：[https://doi.org/10.1145/3705328.3748076](https://doi.org/10.1145/3705328.3748076)

<details open>
<summary><strong>中文摘要</strong></summary>

现代视频流媒体服务高度依赖推荐系统。尽管已有多种内容个性化和推荐方法，但序列推荐模型因其能够随时间汇总用户行为而脱颖而出。我们提出了一种新颖的序列推荐框架，以解决以下关键问题：次优的负采样策略、固定的用户历史上下文长度、单一任务优化目标、对参与度感知学习的不足以及短视的预测范围，最终提升视频流媒体服务在即时和多步下一标题预测方面的表现。在本工作中，我们提出了一种新颖的方法来捕捉不同时间尺度上的交互模式。我们还通过使用具有参与度感知个性化损失的多任务学习，将长期用户满意度与即时意图信号对齐。最后，我们将传统的下一项预测扩展为下一K项预测任务，并采用带有软正标签的训练策略。在大规模流媒体数据上的广泛实验验证了我们方法的有效性。在现实排名场景下，我们的最佳模型在NDCG@1上比基线高出最多3.52%，展示了我们参与度感知和MoE增强设计的有效性。结果还表明，软标签多K训练是一种实用且可扩展的扩展方式，而均衡的个性化负采样策略具有良好的泛化能力。我们的框架在所有排名指标上均优于基线，为生产级流媒体推荐提供了稳健的解决方案。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern video streaming services heavily rely on recommender systems. Although there are many methods for content personalization and recommendation, sequential recommendation models stand out due to their ability to summarize user behavior over time. We propose a novel sequential recommendation framework to address the following key issues: suboptimal negative sampling strategies, fixed user-history context lengths, and single-task optimization objectives, insufficient engagement-aware learning, and short-sighted prediction horizons, ultimately improving both immediate and multi-step next-title prediction for video streaming services. In this work, we propose a novel approach to capture patterns of interaction at different time scales. We also align long-term user happiness with instantaneous intent signals using multi-task learning with engagement-aware personalized loss. Finally, we extend traditional next-item prediction into a next-K forecasting task using a training strategy with soft positive label. Extensive experiments on large-scale streaming data validate the effectiveness of our approach. Our best model outperforms the baseline in NDCG@1 by up to 3.52% under realistic ranking scenarios showing the effectiveness of our engagement-aware and MoE-enhanced designs. Results also show that soft-label Multi-K training is a practical and scalable extension, and that a balanced personalized negative sampling strategy generalizes well. Our framework outperforms baselines across all ranking metrics, providing a robust solution for production-scale streaming recommendations.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

现代视频流服务高度依赖推荐系统，序列推荐模型因其能总结用户随时间的行为而备受关注。本文提出一种新颖的序列推荐框架，旨在解决负采样策略欠佳、用户历史上下文长度固定、单任务优化目标、参与感知学习不足以及预测视野短浅等问题，从而提升视频流服务的即时和多步下一标题预测。方法上，作者提出捕获不同时间尺度交互模式的方法，利用多任务学习与参与感知个性化损失对齐长期用户满意度与即时意图信号，并将传统下一项预测扩展为下一K项预测，采用软正标签训练策略。在大型流数据上的广泛实验验证了方法的有效性，最佳模型在现实排序场景下NDCG@1相对基线提升高达3.52%，表明参与感知和MoE增强设计的有效性。结果还显示软标签多K训练是实用且可扩展的扩展，平衡的个性化负采样策略泛化良好。该框架在所有排序指标上优于基线，为生产级流推荐提供了稳健解决方案。

### 主要创新

- 提出参与感知的个性化损失函数，用于多任务学习，对齐长期用户满意度与即时意图信号。
- 采用MoE（专家混合）增强的Transformer架构，捕获不同时间尺度的交互模式。
- 将传统下一项预测扩展为下一K项预测，并引入软正标签训练策略。
- 设计平衡的个性化负采样策略，以改进训练效果。
- 在大型流数据上验证了框架的有效性，显著提升NDCG@1等排序指标。

### 研究方法

论文提出一个序列推荐框架，包含以下技术路线：1) 使用MoE增强的Transformer模型，通过多个专家网络捕获不同时间尺度的交互模式；2) 采用多任务学习，结合参与感知的个性化损失，同时优化即时点击和长期参与度；3) 将预测目标从下一项扩展为下一K项，使用软正标签分配策略进行训练；4) 设计平衡的个性化负采样策略，以改善负样本质量。实验在大型流数据上进行，评估了NDCG@1等排序指标。

### 关键结果

最佳模型在现实排序场景下NDCG@1相对基线提升高达3.52%；软标签多K训练被证明是实用且可扩展的扩展；平衡的个性化负采样策略泛化良好；框架在所有排序指标上优于基线。

### 技术栈

- Transformer架构、MoE（专家混合）、多任务学习、个性化损失函数、软标签训练、负采样策略、NDCG评估指标。

### 方法优势

- 针对序列推荐中的多个关键问题提出了综合解决方案，包括负采样、上下文长度、多任务优化和预测视野。
- 创新性地结合参与感知和MoE增强，有效提升推荐效果。
- 在大型流数据上验证，结果具有说服力。
- 提出的软标签多K训练策略具有实用性和可扩展性。

### 主要局限

- 论文局限：摘要未提供具体消融实验、模型细节或失败案例。当前证据局限：仅基于摘要，无法评估方法的复杂性和计算成本，也无法确认泛化性。

### 与当前研究方向的关联

该论文与序列推荐、用户建模、CTR/CVR预测、工业落地等关键词高度相关。它聚焦于序列推荐中的用户行为建模，通过多任务学习优化即时和长期目标，并考虑了生产级应用的可行性。

---

_知识库更新时间：2026-08-21T02:21:31.085834_
