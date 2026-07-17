---
title: "USD：面向大规模首页推荐的用户意图驱动采样与双重去偏框架"
paper_id: "https://doi.org/10.1145/3705328.3748096"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Spam and Phishing Detection", "Image and Video Quality Assessment"]
---

# USD：面向大规模首页推荐的用户意图驱动采样与双重去偏框架

> **英文原标题**：USD: A User-Intent-Driven Sampling and Dual-Debiasing Framework for Large-Scale Homepage Recommendations

[查看原文](https://dblp.org/rec/conf/recsys/0015GCHLZ25) · [ArXiv](https://arxiv.org/abs/2507.06503) · [Semantic Scholar](https://www.semanticscholar.org/paper/68e58fc45e843af65b497c6e7e5cbf095963eeb7)

## 一句话结论

> 针对大规模首页推荐中曝光偏差导致的伪负样本和伪正样本问题，提出用户意图驱动的采样和双去偏框架，在淘宝首页线上实验中显著提升用户点击率。

## 论文信息

- **作者**：Jiaqi Zheng, Cheng Guo, Yi Cao, Chaoqun Hou, Tong Liu, Bo Zheng
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3705328.3748096](https://doi.org/10.1145/3705328.3748096)

<details open>
<summary><strong>中文摘要</strong></summary>

大规模首页推荐面临由曝光偏差导致的伪负样本这一关键挑战，其中非点击行为可能反映用户注意力缺失而非缺乏兴趣。现有研究缺乏对无效曝光的深入分析，通常仅针对孤立问题（如采样策略），忽视了伪正样本的关键影响——例如首页点击仅为访问营销入口的行为。我们提出一个面向大规模首页推荐的统一采样与去偏框架。该框架包含两个核心组件：（1）用户意图感知的负采样模块，用于过滤无效曝光样本；（2）意图驱动的双去偏模块，可联合校正曝光偏差与点击偏差。在淘宝平台上的大规模在线实验验证了本框架的有效性，在淘宝首页的两个营销板块——百亿补贴与淘宝秒杀中，用户点击率（UCTR）分别显著提升35.4%和14.5%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large-scale homepage recommendations face critical challenges from pseudo-negative samples caused by exposure bias, where non-clicks may indicate inattention rather than disinterest. Existing work lacks thorough analysis of invalid exposures and typically addresses isolated aspects (e.g., sampling strategies), overlooking the critical impact of pseudo-positive samples - such as homepage clicks merely to visit marketing portals. We propose a unified framework for large-scale homepage recommendation sampling and debiasing. Our framework consists of two key components: (1) a user intent-aware negative sampling module to filter invalid exposure samples, and (2) an intent-driven dual-debiasing module that jointly corrects exposure bias and click bias. Extensive online experiments on Taobao demonstrate the efficacy of our framework, achieving significant improvements in user click-through rates (UCTR) by 35.4% and 14.5% in two variants of the marketing block on the Taobao homepage, Baiyibutie and Taobaomiaosha.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

论文针对大规模首页推荐中因曝光偏差导致的伪负样本问题，以及点击偏差导致的伪正样本问题，提出统一框架USD。该框架包含两个核心模块：用户意图感知负采样模块，用于过滤无效曝光样本；意图驱动的双重去偏模块，联合纠正曝光偏差和点击偏差。在淘宝首页的两个营销板块（百亿补贴和淘宝秒杀）上进行在线实验，用户点击率分别提升35.4%和14.5%。

### 主要创新

- 首次联合解决大规模首页推荐中的无效曝光和样本选择偏差问题，提出意图驱动的采样与去偏框架。
- 提出用户意图感知采样器，利用用户当天是否访问营销门户来筛选置信负样本，优于基于点击的采样。
- 提出因果双重去偏模块，基于用户对营销门户和营销板块的意图概率，分别对曝光偏差和点击偏差进行差异化校正。
- 设计用户意图提取模块（UIEM），利用用户历史行为序列建模细粒度意图，辅助去偏。

### 研究方法

论文首先定义CTR预测任务，提出用户意图驱动负采样，选择当天访问营销门户的用户作为置信样本。然后构建用户意图提取模块（UIEM），使用Transformer解码器处理用户过去一个月的行为序列，预测用户对营销门户和营销板块的意图概率。最后，基于因果推断，对采样后的样本进行双重去偏：对仅访问门户的用户使用1/(1-门户意图概率)加权，对点击板块的用户使用1/板块意图概率加权，并联合优化CTR损失和两个辅助意图预测损失。

### 关键结果

离线实验：USD在GAUCavg、GAUCshow、GAUCclick和AUC上均优于BASE、ESMM、NISE、ESCM²-IPW、ESCM²-DR、DCMT等基线。；消融实验：移除意图采样（仅点击采样）导致性能下降；移除双重去偏模块、门户去偏或板块去偏均导致GAUCavg下降，分别下降2.55%、0.65%、0.82%。；在线A/B测试：在淘宝首页百亿补贴板块UCTR提升35.4%，在淘宝秒杀板块UCTR提升14.5%。

### 技术栈

- Transformer架构（Decoder + 因果掩码 + 位置编码）
- 多层感知机（MLP）
- 逆倾向得分（IPS）
- 交叉熵损失函数
- AdagradDecayV2优化器
- GAUC评估指标

### 方法优势

- 针对首页推荐场景的独特问题（无效曝光和伪正样本）提出统一解决方案，具有实际工业价值。
- 方法创新性强，将用户意图显式建模并用于采样和去偏，而非仅用于表示学习。
- 离线实验和在线A/B测试均验证了有效性，且已在淘宝全量部署。
- 消融实验充分，验证了各模块的必要性。

### 主要局限

- 方法依赖用户当天是否访问营销门户作为采样信号，可能不适用于无此类行为的场景。
- 用户意图提取模块需要用户历史行为序列，对冷启动用户可能效果有限。
- 论文未讨论超参数α和β的敏感性分析。
- 仅针对淘宝首页营销板块，泛化性未在其他平台验证。

### 与当前研究方向的关联

CTR/CVR预测：论文核心任务是CTR预测，并针对点击偏差进行去偏。；用户建模：通过用户意图提取模块建模用户对营销门户和板块的意图。；推荐系统的因果性：使用逆倾向得分进行因果去偏。；工业落地：论文方法已在淘宝首页全量部署，在线实验提升显著。；排序与重排：论文聚焦于排序阶段的采样和去偏。

---

_知识库更新时间：2026-07-17T03:54:55.380080_
