---
title: "Enhancing Sequential Recommender with Large Language Models for Joint Video and Comment Recommendation"
paper_id: "https://doi.org/10.1145/3705328.3748075"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 66.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Sentiment Analysis and Opinion Mining"]
---

# Enhancing Sequential Recommender with Large Language Models for Joint Video and Comment Recommendation

该论文提出利用大语言模型增强序列推荐系统，以联合推荐视频和评论，通过融合多模态信息提升推荐效果。

## Metadata

- Authors: Bowen Zheng, Zihan Lin, Enze Liu, Chen Yang, Enyang Bai, Cheng Ling, Han Li, Wayne Xin Zhao, Ji-Rong Wen
- DOI: https://doi.org/10.1145/3705328.3748075
- URL: https://dblp.org/rec/conf/recsys/0005L0YBLLZW25
- Venue: RecSys
- Score: 66.0

## Abstract

Nowadays, reading or writing comments on captivating videos has emerged as a critical part of the viewing experience on online video platforms. However, existing recommender systems primarily focus on users’ interaction behaviors with videos, neglecting comment content and interaction in user preference modeling. In this paper, we propose a novel recommendation approach called LSVCR that utilizes user interaction histories with both videos and comments to jointly perform personalized video and comment recommendation. Specifically, our approach comprises two key components: sequential recommendation (SR) model and supplemental large language model (LLM) recommender. The SR model functions as the primary recommendation backbone (retained in deployment) of our method for efficient user preference modeling. Concurrently, we employ a LLM as the supplemental recommender (discarded in deployment) to better capture underlying user preferences derived from heterogeneous interaction behaviors. In order to integrate the strengths of the SR model and the supplemental LLM recommender, we introduce a two-stage training paradigm. The first stage, personalized preference alignment, aims to align the preference representations from both components, thereby enhancing the semantics of the SR model. The second stage, recommendation-oriented fine-tuning, involves fine-tuning the alignment-enhanced SR model according to specific objectives. Extensive experiments in both video and comment recommendation tasks demonstrate the effectiveness of LSVCR. Moreover, online A/B testing on KuaiShou platform verifies the practical benefits of our approach. In particular, we attain a cumulative gain of 4.13% in comment watch time.

## Chinese Abstract

现有推荐系统主要关注视频交互，忽略评论内容与评论交互。LSVCR联合利用视频和评论交互历史，由部署时保留的序列推荐模型负责高效推荐，并在训练阶段使用补充LLM捕捉异构行为中的潜在偏好。两阶段训练先进行个性化偏好对齐，再面向推荐目标微调。摘要报告视频与评论推荐实验均验证有效，并在快手线上A/B测试中使评论观看时长累计提升4.13%。

## Analysis Basis

- abstract (no open PDF or arXiv version was available)

## Deep Analysis

```json
{
  "chinese_title": "利用大语言模型增强序列推荐的视频与评论联合推荐",
  "summary": "现有推荐系统主要关注视频交互，忽略评论内容与评论交互。LSVCR联合利用视频和评论交互历史，由部署时保留的序列推荐模型负责高效推荐，并在训练阶段使用补充LLM捕捉异构行为中的潜在偏好。两阶段训练先进行个性化偏好对齐，再面向推荐目标微调。摘要报告视频与评论推荐实验均验证有效，并在快手线上A/B测试中使评论观看时长累计提升4.13%。",
  "innovations": [
    "联合建模视频与评论交互，用于个性化视频和评论推荐。",
    "以序列推荐模型为部署骨干，LLM仅作为训练阶段的补充推荐器。",
    "通过个性化偏好对齐和面向推荐的微调连接两个组件。"
  ],
  "methodology": "序列推荐模型作为主要骨干并保留到部署阶段；补充LLM在训练阶段用于捕捉异构交互中的潜在偏好。第一阶段对齐两者的偏好表示，第二阶段按具体推荐目标微调增强后的序列推荐模型。摘要未披露具体网络结构、损失函数和训练参数。",
  "key_results": [
    "摘要称视频推荐和评论推荐实验均验证了LSVCR的有效性。",
    "快手在线A/B测试中，评论观看时长累计提升4.13%。",
    "摘要未提供离线数据集、基线、指标明细或消融结果。"
  ],
  "tech_stack": [
    "序列推荐模型（摘要未说明具体架构）",
    "大型语言模型补充推荐器（摘要未说明具体模型）",
    "两阶段训练：偏好对齐与推荐微调"
  ],
  "strengths": [
    "兼顾LLM语义建模能力与线上部署效率。",
    "同时覆盖视频和评论两种推荐任务。",
    "包含真实工业平台在线A/B测试证据。"
  ],
  "limitations": [
    "当前证据仅为摘要，无法核验完整实验表格、基线、消融和实现细节。",
    "摘要未说明模型规模、计算成本及不同用户群体上的表现。"
  ],
  "relevance_to_keywords": "与序列推荐、LLM推荐、异构交互用户建模及工业推荐高度相关。",
  "_analysis_basis": "abstract"
}
```
