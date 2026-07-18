---
title: "用于生成式电影推荐中流行度偏差缓解的大型语言模型多阶段对齐"
paper_id: "https://doi.org/10.21203/rs.3.rs-10375648/v1"
source: "openalex"
published: "2026-07-17T00:00:00"
score: 60.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Sentiment Analysis and Opinion Mining", "Machine Learning in Healthcare"]
---

# 用于生成式电影推荐中流行度偏差缓解的大型语言模型多阶段对齐

> **英文原标题**：Multi-Stage Alignment of Large Language Models for Popularity Bias Mitigation in Generative Movie Recommendation

[查看原文](https://doi.org/10.21203/rs.3.rs-10375648/v1)

## 一句话结论

> 该论文提出一种多阶段对齐方法，利用大语言模型缓解生成式电影推荐中的流行度偏差，通过逐步对齐模型以平衡流行度和个性化。

## 论文信息

- **作者**：Subham Raj, Krishnakant Chourey, Sriparna Saha, Brijraj Singh, Niranjan Pedanekar
- **来源**：Research Square
- **发布时间**：2026-07-17
- **相关度评分**：60.0
- **DOI**：[https://doi.org/10.21203/rs.3.rs-10375648/v1](https://doi.org/10.21203/rs.3.rs-10375648/v1)

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对大型语言模型（LLM）在推荐任务中存在的流行度偏差问题，提出了一种多阶段对齐流水线，包括偏好提取、监督微调（SFT）和直接偏好优化（DPO）。通过将行为基础与偏差校正显式分离，该框架实现了稳定且可控的曝光公平性改进。在MovieLens、Netflix和Flickscore三个数据集上，对LLaMA 3.1、LLaMA 2和Mistral 7B三种模型进行了实验，结果表明多阶段对齐在保持竞争性准确率的同时，显著提升了新颖性和目录覆盖率，并优于简单的曝光调整基线。

### 主要创新

- 将LLM推荐中的流行度偏差缓解分解为行为基础与偏差校正两个阶段，而非单一微调目标。
- 系统比较了零样本提示、SFT和偏好优化，证明单一阶段无法同时保证稳定推荐和有效去偏。
- 提出三阶段对齐流程（偏好提取、SFT、DPO），显式分离行为基础与偏差校正。
- 引入完全自动化的数据集驱动方法，利用项目流行度统计和元数据构建DPO对比偏好对。
- 在三种LLM家族和三个数据集上进行跨模型、跨数据集验证，并提供了内在对齐与经典后处理方法（重排序）的系统比较。

### 研究方法

论文采用三阶段对齐流水线：第一阶段将用户交互历史转换为结构化自然语言偏好描述；第二阶段通过监督微调（SFT）使模型学习生成连贯、格式一致的推荐输出；第三阶段使用直接偏好优化（DPO），以低流行度但主题相关的项目为偏好响应，高流行度项目为拒绝响应，进行偏差校正。DPO偏好对完全基于数据集统计和元数据自动构建。实验在三个LLM（LLaMA 3.1 8B、LLaMA 2 7B、Mistral 7B）和三个数据集（MovieLens 1M、Netflix Prize、Flickscore）上进行，评估指标包括Precision@5、nDCG@5、MAP@5、新颖性、覆盖率和平均流行度。

### 关键结果

多阶段对齐在三个数据集和三种模型上均显著提升了新颖性和覆盖率，同时保持了竞争性的准确率。例如，在MovieLens 1M上，LLaMA 3.1 8B的DPO模型将新颖性提升至17.5，覆盖率提升至22%，平均流行度从1217降至575。在Netflix Prize上，Mistral 7B的DPO模型新颖性从3.3提升至8.9，平均流行度从1615降至590。在Flickscore上，DPO模型达到最高新颖性26.5和覆盖率42%。

### 技术栈

- LLaMA 3.1 8B
- LLaMA 2 7B
- Mistral 7B
- Direct Preference Optimization (DPO)
- Supervised Fine-Tuning (SFT)
- Jaccard index
- AdamW optimizer
- Cosine learning rate schedule
- Negative log-likelihood loss
- SwiGLU activations
- Rotary Positional Embeddings (RoPE)
- Grouped-Query Attention (GQA)
- Sliding Window Attention (SWA)

### 方法优势

- 问题分解清晰，将流行度偏差缓解分为行为基础与偏差校正两个阶段，设计合理。
- 跨模型、跨数据集验证，实验规模大，结果具有鲁棒性和泛化性。
- DPO偏好对完全自动化构建，无需人工标注，可复现性强。
- 系统比较了内在对齐与经典后处理方法（重排序），提供了全面的基准。
- 代码和实验协议公开，支持可重复研究。

### 主要局限

- 仅关注电影推荐领域，未验证在其他推荐领域（如新闻、音乐）的有效性。
- 未考虑用户人口统计或群体层面的公平性，仅聚焦于流行度驱动的曝光公平。
- DPO偏好对的构建依赖于流行度分位数和类型相似性，可能无法覆盖所有用户偏好。
- 实验仅在英文数据集上进行，未涉及多语言或跨文化场景。
- 未与传统的协同过滤模型（如LightGCN、SASRec）进行直接定量比较，仅与重排序基线对比。

### 与当前研究方向的关联

论文直接涉及LLM与推荐系统结合、生成式推荐、流行度偏差缓解、直接偏好优化（DPO）等关键词，与序列推荐、排序与重排、公平性等主题高度相关。

## 代码与复现

- [krishnakantx/debiased-llm-recsys](https://github.com/krishnakantx/debiased-llm-recsys)：likely，置信度 50，Stars 0

---

_知识库更新时间：2026-07-18T03:48:20.891430_
