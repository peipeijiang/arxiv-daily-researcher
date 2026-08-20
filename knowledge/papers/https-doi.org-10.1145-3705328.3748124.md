---
title: "SocRipple：一种用于冷启动视频推荐的两阶段框架"
paper_id: "https://doi.org/10.1145/3705328.3748124"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 43.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image Retrieval and Classification Techniques", "Advanced Graph Neural Networks"]
---

# SocRipple：一种用于冷启动视频推荐的两阶段框架

> **英文原标题**：SocRipple: A Two-Stage Framework for Cold-Start Video Recommendations

[查看原文](https://dblp.org/rec/conf/recsys/JaspalDR25a) · [ArXiv](https://arxiv.org/abs/2508.07241) · [Semantic Scholar](https://www.semanticscholar.org/paper/ece454a10ebfc4eebc66328029022ce77a83bcde)

## 一句话结论

> SocRipple通过两阶段检索框架利用社交连接和KNN扩展，显著提升冷启动视频推荐的分发量（+36%）同时保持用户参与度。

## 论文信息

- **作者**：Amit Jaspal, Kapil Dalwani, Ajantha Ramineni
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：43.0
- **DOI**：[https://doi.org/10.1145/3705328.3748124](https://doi.org/10.1145/3705328.3748124)

<details open>
<summary><strong>中文摘要</strong></summary>

大多数工业级推荐系统都面临严峻的冷启动挑战——新物品缺乏交互历史，难以以个性化方式进行分发。标准协同过滤模型因交互信号稀疏而表现不佳，而仅基于内容的方法又缺乏用户特定的相关性。我们提出SocRipple，一种新颖的两阶段检索框架，专为基于社交图谱的平台中的冷启动物品分发而设计。第一阶段利用创作者的社交关系进行有针对性的初始曝光。第二阶段基于早期交互信号和稳定的用户嵌入（从历史交互中学习），通过K近邻（KNN）搜索向外“涟漪式”扩散。在大型视频平台上进行的大规模实验表明，SocRipple将冷启动物品分发量提升了36%，同时保持了用户在冷启动物品上的参与率，有效平衡了新物品曝光与个性化推荐。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Most industry-scale recommender systems face critical cold-start challenges—new items lack interaction history, making it difficult to distribute them in a personalized manner. Standard collaborative filtering models underperform due to sparse engagement signals, while content-only approaches lack user-specific relevance. We propose SocRipple, a novel two-stage retrieval framework tailored for cold-start item distribution in social graph-based platforms. Stage 1 leverages the creator's social connections for targeted initial exposure. Stage 2 builds on early engagement signals and stable user embeddings—learned from historical interactions—to "ripple" outwards via K-Nearest Neighbor (KNN) search. Large scale experiments on a major video platform show that SocRipple boosts cold-start item distribution by +36% while maintaining user engagement rate on cold-start items, effectively balancing new-item exposure with personalized recommendations.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出SocRipple，一种针对社交图谱平台冷启动视频推荐的两阶段检索框架。第一阶段利用创作者的社交连接进行初始定向曝光，第二阶段基于早期参与信号和稳定的用户嵌入，通过K近邻搜索向外扩散。在大型视频平台上的实验表明，SocRipple将冷启动物品的曝光量提升了36%，同时保持了用户参与率，有效平衡了新物品曝光与个性化推荐。

### 主要创新

- 提出两阶段级联框架，结合社交播种和嵌入驱动的邻居扩展，解决冷启动问题。
- 利用创作者社交连接进行高精度初始曝光，并利用早期参与信号进行实时邻居扩展。
- 在工业规模数据集上验证了框架的有效性，并进行了在线A/B测试。

### 研究方法

SocRipple包含两个阶段：阶段1（社交提升）将新视频推荐给创作者的粉丝，收集早期参与信号；阶段2（邻居扩展）在用户请求时，通过KNN搜索找到相似用户，聚合这些用户近期参与过的冷启动视频，并排序推荐。用户嵌入通过双塔模型学习，使用采样softmax损失训练，并存储在FAISS索引中。

### 关键结果

离线实验表明，SocRipple在Recall@200上显著优于基线，对于6小时内的物品达到12.8%，而DropoutNet为5.8%。消融实验显示，嵌入扩展比社交图扩展更有效（13.2% vs 6.7%）。在线A/B测试显示，冷启动物品曝光量提升36%，整体参与度提升0.22%，冷启动物品参与率与对照组持平。

### 技术栈

- 双塔神经网络
- 采样softmax损失
- FAISS近似最近邻索引
- K近邻搜索
- A/B测试

### 方法优势

- 提出新颖的两阶段框架，有效结合社交和嵌入信号。
- 在工业规模数据上进行了全面评估，包括离线实验和在线部署。
- 对超参数敏感性进行了分析，提供了实际调参指导。

### 主要局限

- 依赖社交图谱，对于社交关系稀疏的创作者可能效果有限。
- 阶段2的实时KNN搜索和聚合可能带来计算开销，文中未详细讨论延迟优化。
- 用户嵌入基于历史数据，可能无法捕捉用户兴趣的快速变化。

### 与当前研究方向的关联

该论文与关键词“推荐系统”、“冷启动”、“社交推荐”、“嵌入学习”高度相关，属于工业推荐系统落地研究，关注新物品分发和用户参与度。

---

_知识库更新时间：2026-08-20T02:19:08.956723_
