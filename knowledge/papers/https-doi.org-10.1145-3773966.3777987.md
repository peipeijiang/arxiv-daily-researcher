---
title: "面向推荐的连续时间离散空间扩散模型"
paper_id: "https://doi.org/10.1145/3773966.3777987"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 46.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Complex Network Analysis Techniques", "Advanced Graph Neural Networks"]
---

# 面向推荐的连续时间离散空间扩散模型

> **英文原标题**：Continuous-time Discrete-space Diffusion Model for Recommendation

[查看原文](https://dblp.org/rec/conf/wsdm/000100F026) · [ArXiv](https://arxiv.org/abs/2511.12114)

## 一句话结论

> 该论文提出CDRec，一种连续时间离散空间扩散推荐模型，通过离散扩散和连续时间建模提升推荐准确性和计算效率。

## 论文信息

- **作者**：Chengyi Liu, Xiao Chen, Shijie Wang, Wenqi Fan, Qing Li
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：46.0
- **DOI**：[https://doi.org/10.1145/3773966.3777987](https://doi.org/10.1145/3773966.3777987)

<details open>
<summary><strong>中文摘要</strong></summary>

在信息爆炸的时代，推荐系统（RS）对于缓解信息过载和提供个性化用户体验至关重要。基于扩散的生成式推荐器的最新进展在捕捉用户偏好的动态特性方面展现出潜力。这些方法通过逐步扰动用户-物品交互的分布并从噪声中恢复潜在偏好，探索更广泛的用户兴趣，从而实现对用户行为的细致理解。然而，现有的基于扩散的方法主要通过编码后的基于图的历史交互在连续空间中运行，这可能导致潜在信息损失并存在计算效率低下的问题。为此，我们提出CDRec，一种新颖的连续时间离散空间扩散推荐框架，该框架通过对连续时间上的历史交互进行离散扩散来建模用户行为模式。离散扩散算法通过离散元素操作（例如掩码）运行，同时通过转移矩阵融入领域知识，从而生成更有意义的扩散轨迹。此外，连续时间公式实现了灵活的适应性采样。为了更好地将离散扩散模型适配到推荐任务中，CDRec引入了：（1）一种新颖的流行度感知噪声调度，可生成语义上有意义的扩散轨迹；（2）一个高效的训练框架，该框架结合了用于快速采样的一致性参数化以及由多跳协同信号引导的对比学习目标，以实现个性化推荐。在真实世界数据集上进行的大量实验表明，CDRec在推荐准确性和计算效率方面均表现出优越性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In the era of information explosion, Recommender Systems (RS) are essential for alleviating information overload and providing personalized user experiences. Recent advances in diffusion-based generative recommenders have shown promise in capturing the dynamic nature of user preferences. These approaches explore a broader range of user interests by progressively perturbing the distribution of user-item interactions and recovering potential preferences from noise, enabling nuanced behavioral understanding. However, existing diffusion-based approaches predominantly operate in continuous space through encoded graph-based historical interactions, which may compromise potential information loss and suffer from computational inefficiency. As such, we propose CDRec, a novel Continuous-time Discrete-space Diffusion Recommendation framework, which models user behavior patterns through discrete diffusion on historical interactions over continuous time. The discrete diffusion algorithm operates via discrete element operations (e.g., masking) while incorporating domain knowledge through transition matrices, producing more meaningful diffusion trajectories. Furthermore, the continuous-time formulation enables flexible adaptive sampling. To better adapt discrete diffusion models to recommendations, CDRec introduces: (1) a novel popularity-aware noise schedule that generates semantically meaningful diffusion trajectories, and (2) an efficient training framework combining consistency parameterization for fast sampling and a contrastive learning objective guided by multi-hop collaborative signals for personalized recommendation. Extensive experiments on real-world datasets demonstrate CDRec's superior performance in both recommendation accuracy and computational efficiency.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出CDRec，一种连续时间离散空间扩散推荐框架，通过离散扩散算法（如掩码操作）在连续时间上对历史交互进行扰动，并利用转移矩阵融入领域知识，生成更有意义的扩散轨迹。CDRec引入流行度感知噪声调度，模拟真实交互动态；采用一致性函数参数化反向扩散过程，支持高效单步生成和迭代采样；结合对比学习目标，利用多跳协同信号指导个性化推荐。在三个真实数据集上的实验表明，CDRec在推荐准确性和计算效率上均优于现有方法。

### 主要创新

- 提出连续时间离散空间扩散推荐框架，直接对离散交互序列进行扩散，避免连续空间的信息损失。
- 设计流行度感知噪声调度，根据物品流行度动态调整吸收概率，生成语义丰富的扩散轨迹。
- 采用一致性函数参数化反向扩散过程，实现高效单步生成与多步采样的灵活平衡。
- 引入对比学习目标，利用多跳协同信号引导扩散过程，增强个性化推荐。

### 研究方法

CDRec采用连续时间马尔可夫链（CTMC）进行前向扩散，通过流行度感知噪声调度控制掩码速率；反向扩散使用一致性函数（Transformer编码器）直接预测原始交互，训练时结合一致性损失和扩散损失；同时利用对比学习（InfoNCE损失）将生成表示与预训练用户嵌入对齐，联合优化。

### 关键结果

在Ciao、MovieLens-1M、Dianping三个数据集上，CDRec在Recall@10、Recall@5、NDCG@10、NDCG@5上均优于所有基线，相对提升最高达6.88%（MovieLens-1M Recall@5）。消融实验验证了各组件有效性；参数敏感性分析表明30步采样、λ1=0.4时性能最优；伪欧拉方法优于单步恢复。

### 技术栈

- 连续时间马尔可夫链（CTMC）
- 随机微分方程（SDE）
- 一致性函数（Consistency Function）
- Transformer编码器
- 对比学习（InfoNCE损失）
- LightGCN（预训练嵌入）
- Adam优化器

### 方法优势

- 创新性地将离散空间扩散引入推荐，避免了连续空间的信息损失。
- 流行度感知噪声调度模拟真实交互模式，提升扩散轨迹的语义性。
- 一致性函数支持单步生成，兼顾效率与质量。
- 对比学习有效融合多跳协同信号，增强个性化。
- 实验充分，在多个数据集上取得一致最优结果。

### 主要局限

- 输入内容未提供对超参数（如ω、σ）的详细敏感性分析。
- 输入内容未讨论模型在冷启动场景下的表现。
- 输入内容未提供与最新LLM-based推荐方法的对比。
- 输入内容未分析模型的可解释性。

### 与当前研究方向的关联

生成式推荐：核心方法为扩散生成模型，直接生成用户-物品交互。；序列推荐：模型处理用户历史交互序列，并生成推荐序列。；用户建模：通过扩散过程学习用户偏好分布。；推荐系统：整体框架面向推荐任务，实验在推荐数据集上进行。

## 代码与复现

- [ChengyiLIU-cs/CDRec](https://github.com/ChengyiLIU-cs/CDRec)：official，置信度 100，Stars 7
- [AAAAA-Academia-Attractions/Discrete-Diffusion](https://github.com/AAAAA-Academia-Attractions/Discrete-Diffusion)：likely，置信度 69，Stars 10

---

_知识库更新时间：2026-07-24T04:05:55.201592_
