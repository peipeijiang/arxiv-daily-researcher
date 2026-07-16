---
title: "利用大语言模型增强序列推荐器以实现视频与评论联合推荐"
paper_id: "https://doi.org/10.1145/3705328.3748075"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 57.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Sentiment Analysis and Opinion Mining"]
---

# 利用大语言模型增强序列推荐器以实现视频与评论联合推荐

> **英文原标题**：Enhancing Sequential Recommender with Large Language Models for Joint Video and Comment Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/0005L0YBLLZW25) · [ArXiv](https://arxiv.org/abs/2403.13574) · [Semantic Scholar](https://www.semanticscholar.org/paper/db27dd3ac801d641059ba335a4d7ff70b1bab478)

## 一句话结论

> 论文提出LSVCR方法，利用用户与视频和评论的交互历史，结合序列推荐模型和大语言模型，通过两阶段训练实现个性化视频和评论联合推荐，在快手平台取得评论观看时长累计增长4.13%。

## 论文信息

- **作者**：Bowen Zheng, Zihan Lin, Enze Liu, Chen Yang, Enyang Bai, Cheng Ling, Han Li, Wayne Xin Zhao, Ji-Rong Wen
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：57.0
- **DOI**：[https://doi.org/10.1145/3705328.3748075](https://doi.org/10.1145/3705328.3748075)

<details open>
<summary><strong>中文摘要</strong></summary>

如今，在引人入胜的视频下阅读或撰写评论已成为在线视频平台观看体验的关键组成部分。然而，现有推荐系统主要关注用户与视频的交互行为，在用户偏好建模中忽视了评论内容及其交互。本文提出一种名为LSVCR的新型推荐方法，该方法利用用户与视频及评论的交互历史，联合执行个性化视频与评论推荐。具体而言，我们的方法包含两个核心组件：序列推荐（SR）模型与补充性大语言模型（LLM）推荐器。SR模型作为方法的主要推荐主干（部署阶段保留），用于高效建模用户偏好；同时，我们采用LLM作为补充推荐器（部署阶段舍弃），以更好地捕捉源自异构交互行为的潜在用户偏好。为整合SR模型与补充性LLM推荐器的优势，我们引入两阶段训练范式：第一阶段为个性化偏好对齐，旨在对齐两个组件的偏好表征，从而增强SR模型的语义能力；第二阶段为面向推荐的微调，即根据特定目标对经对齐增强的SR模型进行微调。在视频与评论推荐任务上的大量实验证明了LSVCR的有效性。此外，在快手平台上的在线A/B测试验证了该方法在实际应用中的优势，其中评论观看时长累计提升4.13%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Nowadays, reading or writing comments on captivating videos has emerged as a critical part of the viewing experience on online video platforms. However, existing recommender systems primarily focus on users’ interaction behaviors with videos, neglecting comment content and interaction in user preference modeling. In this paper, we propose a novel recommendation approach called LSVCR that utilizes user interaction histories with both videos and comments to jointly perform personalized video and comment recommendation. Specifically, our approach comprises two key components: sequential recommendation (SR) model and supplemental large language model (LLM) recommender. The SR model functions as the primary recommendation backbone (retained in deployment) of our method for efficient user preference modeling. Concurrently, we employ a LLM as the supplemental recommender (discarded in deployment) to better capture underlying user preferences derived from heterogeneous interaction behaviors. In order to integrate the strengths of the SR model and the supplemental LLM recommender, we introduce a two-stage training paradigm. The first stage, personalized preference alignment, aims to align the preference representations from both components, thereby enhancing the semantics of the SR model. The second stage, recommendation-oriented fine-tuning, involves fine-tuning the alignment-enhanced SR model according to specific objectives. Extensive experiments in both video and comment recommendation tasks demonstrate the effectiveness of LSVCR. Moreover, online A/B testing on KuaiShou platform verifies the practical benefits of our approach. In particular, we attain a cumulative gain of 4.13% in comment watch time.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出LSVCR框架，用于在短视频平台上联合进行视频和评论推荐。该方法包含两个核心组件：序列推荐（SR）模型作为主推荐骨干（部署时保留），以及大语言模型（LLM）作为补充推荐器（部署时丢弃）。通过两阶段训练范式整合两者优势：第一阶段进行个性化偏好对齐，利用对比学习对齐SR模型与LLM推荐器的偏好表示；第二阶段进行面向推荐的微调，增强SR模型。实验在快手工业数据集和Amazon基准上验证了有效性，在线A/B测试中评论观看时长累计提升4.13%。

### 主要创新

- 提出联合视频与评论推荐的统一框架，同时建模视频和评论交互行为。
- 设计两阶段训练范式：个性化偏好对齐和面向推荐的微调，有效整合LLM的语义理解能力与SR模型的效率。
- 引入序列-补充偏好对比和视频-评论偏好对比两种对比学习损失，对齐SR模型与LLM推荐器的偏好表示。
- 提出评论多样化数据增强和随机位置编码技术，提升对齐阶段的数据利用和长度泛化能力。

### 研究方法

使用Transformer作为SR模型骨干，LLM（ChatGLM3）作为补充推荐器。第一阶段通过对比学习（InfoNCE）对齐SR模型和LLM的偏好表示，联合优化语言模型损失、SR损失和对比损失。第二阶段丢弃LLM，加入视频ID嵌入，使用ID-文本正则化损失和任务特定损失（视频推荐用全候选集InfoNCE，评论推荐用当前视频下评论候选集InfoNCE）进行微调。

### 关键结果

在快手工业数据集上，视频推荐任务Recall@10达0.3322，NDCG@10达0.2233；评论推荐任务Recall@10达0.3901，NDCG@10达0.2541。在线A/B测试中，评论观看时长提升4.13%，交互数提升1.36%。在Amazon数据集上，LSVCR w/o Comment变体Recall@10达0.7088，NDCG@10达0.5166。

### 技术栈

- Transformer
- ChatGLM3
- LoRA
- InfoNCE损失
- 对比学习
- 多注意力机制
- AdamW优化器
- 随机位置编码

### 方法优势

- 创新性地将LLM作为补充推荐器，通过对齐提升SR模型语义，同时保持部署效率。
- 两阶段训练范式设计合理，对齐阶段充分利用LLM能力，微调阶段适配具体任务。
- 在工业数据集和公共数据集上均取得显著提升，在线A/B测试验证实际效果。
- 方法具有通用性，可推广到一般物品推荐场景。

### 主要局限

- 依赖LLM进行离线训练，计算资源消耗较大。
- 评论多样化增强可能引入噪声，影响对齐质量。
- 仅在一个工业数据集和一个Amazon子集上验证，泛化性需更多数据集支持。
- 未讨论冷启动用户或视频的处理策略。

### 与当前研究方向的关联

论文聚焦于序列推荐与LLM结合，属于生成式推荐和LLM与推荐系统结合方向；涉及用户建模（视频和评论交互）、工业落地（在线A/B测试），与关键词高度相关。

---

_知识库更新时间：2026-07-16T03:56:50.203722_
