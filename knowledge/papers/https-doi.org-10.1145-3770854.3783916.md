---
title: "将推荐系统Transformer扩展到十亿参数"
paper_id: "https://doi.org/10.1145/3770854.3783916"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 55.0
tags: ["paper", "recommender-systems", "Advanced Text Analysis Techniques"]
---

# 将推荐系统Transformer扩展到十亿参数

> **英文原标题**：Scaling Recommender Transformers to One Billion Parameters

[查看原文](https://dblp.org/rec/conf/kdd/KhrylchenkoMMB26) · [ArXiv](https://arxiv.org/abs/2507.15994)

## 一句话结论

> 该论文提出将生成式推荐框架扩展到十亿参数规模，通过序列转导任务改进推荐系统的扩展性，并验证了其在大规模参数下的有效性。

## 论文信息

- **作者**：Kirill Khrylchenko, Artem Matveev, Sergei Makeev, Vladimir Baikalov
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：55.0
- **DOI**：[https://doi.org/10.1145/3770854.3783916](https://doi.org/10.1145/3770854.3783916)

<details open>
<summary><strong>中文摘要</strong></summary>

尽管大型Transformer模型已在自然语言处理、计算机视觉和语音处理等众多实际应用中得到成功运用，但将Transformer扩展到推荐系统仍是一个具有挑战性的问题。近期，生成式推荐框架（Generative Recommenders）被提出，旨在超越典型的深度学习推荐模型（DLRMs）。通过将推荐任务重新表述为序列转导任务，该框架在计算方面提升了扩展性能。然而，HSTU作者所报告的最大编码器配置仅有1.76亿参数——远小于当前语言模型中常见的数千亿（甚至数万亿）参数规模。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

While large transformer models have been successfully used in many real-world applications such as natural language processing, computer vision, and speech processing, scaling transformers for recommender systems remains a challenging problem. Recently, the Generative Recommenders framework was proposed as a way to scale beyond typical Deep Learning Recommendation Models (DLRMs). By reformulating recommendation as a sequential transduction task, it improves scaling properties in terms of compute. Nevertheless, the largest encoder configuration reported by the HSTU authors is only 176 million parameters --- far smaller than the hundreds of billions (or even trillions) that are now common in language models.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出了一种将推荐系统Transformer扩展到十亿参数规模的训练方法。作者将推荐问题重新定义为序列生成任务，并提出了一个预训练目标，该目标自然分解为反馈预测和下一项预测两个子任务。实验表明，该分解在广泛的模型规模上有效扩展。作者在大型音乐平台上部署了126M参数的模型，在线A/B测试显示总收听时间提升2.26%，点赞可能性提升6.37%，是该平台历史上深度学习推荐系统最大的改进。

### 主要创新

- 提出将推荐预训练任务分解为反馈预测和下一项预测两个互补目标，并证明其在不同模型规模下均能有效扩展。
- 设计了一种计算高效的微调阶段，将大型Transformer编码器转换为双塔架构，支持离线推理并为下游模型提供强大的排序特征。
- 在工业级音乐平台上部署了126M参数、上下文长度8192的Transformer模型，取得了显著的在线性能提升。
- 通过实验验证了模型规模、上下文长度和两阶段训练流程对推荐质量的影响，提供了可复现的扩展配方。

### 研究方法

本文采用Transformer作为用户历史序列的编码器，预训练阶段使用两个任务：下一项预测（使用logQ校正的采样softmax损失）和反馈预测（多任务分类损失）。微调阶段采用印象感知的两塔结构，通过因果编码器生成用户表示，并与物品嵌入点积计算排序分数。实验在自建的大规模音乐数据集上进行，评估了不同模型规模、上下文长度和训练流程的影响。

### 关键结果

模型规模从3.2M扩展到1B参数时，反馈预测熵降低3.43%至7.15%，下一项预测熵降低10.36%，排序准确率提升从+1.35%增至+2.66%。；与HSTU（176M参数）相比，126M参数的Transformer在预训练和排序任务上表现相当。；两阶段训练均不可或缺：无预训练时，一年微调仅获得+1.17%的提升；有预训练但微调一周仅获得+0.63%的提升，而微调一年可获得+2.32%的提升。；上下文长度从512增加到8192时，排序准确率提升从+1.01%增至+2.77%。；在线部署ARGUS（126M参数）后，总收听时间提升+2.26%，点赞可能性提升+6.37%。

### 技术栈

- Transformer编码器
- logQ校正的采样softmax
- 混合负采样
- 多任务学习
- 两塔架构
- 因果注意力
- Adam优化器
- 分布式数据并行（DDP）
- PyTorch 2.x

### 方法优势

- 提出了一个可扩展的推荐Transformer训练框架，并验证了其在大规模数据上的有效性。
- 实验设计严谨，包括严格的时间分割和在线A/B测试，结果具有说服力。
- 提供了详细的超参数和实现细节，便于复现。
- 在真实工业场景中取得了显著的性能提升，具有实际应用价值。

### 主要局限

- 未在公开数据集上验证，数据集为自建，可能影响结果的可比性。
- 最大模型（1B参数）未进行在线部署，仅评估了126M参数的模型。
- 未与最新的其他推荐模型（如SASRec）进行直接比较，仅与HSTU和自身变体比较。
- 微调阶段需要大量数据（一年），可能增加计算成本。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、用户建模、排序与重排、工业落地等关键词高度相关。它提出了一种新的预训练任务和微调方法，用于训练大规模Transformer推荐模型，并在工业场景中验证了其有效性。

---

_知识库更新时间：2026-08-02T04:11:29.701234_
