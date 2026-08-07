---
title: "Abacus：面向序列用户建模的自监督事件计数对齐分布预训练"
paper_id: "https://doi.org/10.1145/3773966.3779391"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 45.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Customer churn and segmentation"]
---

# Abacus：面向序列用户建模的自监督事件计数对齐分布预训练

> **英文原标题**：Abacus: Self-Supervised Event Counting-Aligned Distributional Pretraining for Sequential User Modeling

[查看原文](https://dblp.org/rec/conf/wsdm/CastroBMM26) · [ArXiv](https://arxiv.org/abs/2512.16581)

## 一句话结论

> The paper proposes Abacus, a self-supervised pretraining method that predicts event frequency distributions to improve sequential user modeling for display advertising, achieving up to +6.1% AUC over baselines.

## 论文信息

- **作者**：Sullivan Castro, Artem Betlei, Thomas Di Martino, Nadir El Manouzi
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：45.0
- **DOI**：[https://doi.org/10.1145/3773966.3779391](https://doi.org/10.1145/3773966.3779391)

<details open>
<summary><strong>中文摘要</strong></summary>

对用户购买行为进行建模是在线展示广告系统中的一项关键挑战，对于实时竞价而言必不可少。该难点源于正向用户事件的稀疏性以及用户行为的随机性，导致严重的类别不平衡和事件时间的不规则性。预测系统通常依赖手工构建的“计数”特征，而忽略了用户意图在细粒度时间维度上的演变。与此同时，现有的序列模型提取直接的序列信号，却遗漏了有用的事件计数统计信息。我们通过自监督预训练策略增强深度序列模型，以应用于展示广告。特别地，我们引入了Abacus，一种预测用户事件经验频率分布的新方法。我们进一步提出了一种混合目标函数，将Abacus与序列学习目标统一起来，结合了聚合统计的稳定性与序列建模的敏感性。在两个真实数据集上的实验表明，Abacus预训练在加速下游任务收敛方面优于现有方法，而混合方法相较于基线模型在AUC上最高可提升+6.1%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modeling user purchase behavior is a critical challenge in display advertising systems, necessary for real-time bidding. The difficulty arises from the sparsity of positive user events and the stochasticity of user actions, leading to severe class imbalance and irregular event timing. Predictive systems usually rely on hand-crafted "counter" features, overlooking the fine-grained temporal evolution of user intent. Meanwhile, current sequential models extract direct sequential signal, missing useful event-counting statistics. We enhance deep sequential models with self-supervised pretraining strategies for display advertising. Especially, we introduce Abacus, a novel approach of predicting the empirical frequency distribution of user events. We further propose a hybrid objective unifying Abacus with sequential learning objectives, combining stability of aggregated statistics with the sequence modeling sensitivity. Experiments on two real-world datasets show that Abacus pretraining outperforms existing methods accelerating downstream task convergence, while hybrid approach yields up to +6.1% AUC compared to the baselines.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对展示广告中用户购买行为建模的挑战，提出了一种名为Abacus的自监督预训练方法。该方法通过预测用户事件序列的经验频率分布来训练序列编码器，从而捕捉事件计数统计信息，弥补传统计数特征和序列模型各自的不足。作者进一步提出了混合目标，将Abacus与掩码序列建模和Barlow Twins对比学习相结合，以融合聚合统计的稳定性和序列建模的敏感性。在私有数据集和公开的Taobao数据集上的实验表明，Abacus预训练能加速下游任务收敛，混合方法相比基线在AUC上最高提升6.1%。

### 主要创新

- 提出Abacus预训练任务，通过预测事件经验分布来对齐计数信号，无需手工特征工程。
- 设计了三种序列增强变体（无增强、随机置换、片段掩码），增强鲁棒性。
- 提出混合多任务学习目标，结合Abacus、掩码序列建模和Barlow Twins，提升性能和稳定性。
- 在展示广告场景中验证了自监督预训练的有效性，并分析了不同预训练任务的对齐性。

### 研究方法

采用两阶段训练：预训练阶段，对用户行为序列应用任务特定的增强，通过共享编码器（GRU或BERT）得到序列嵌入，再通过任务特定头进行预测。Abacus任务使用交叉熵损失预测事件类型直方图；掩码序列建模任务重建被掩码的事件和时间戳；Barlow Twins任务通过最大化两个增强视图的相关性并减少冗余。混合模型使用多任务学习，加权求和各任务损失。下游任务为购买预测，微调阶段更新事件嵌入和编码器，从头学习预测头。

### 关键结果

在Taobao数据集上，混合方法在BERT上AUC达到0.6411，相对无预训练提升5.49%；在私有数据集上，混合方法在GRU上AUC达到0.7525，相对提升6.07%。Abacus-R在私有数据集上对GRU和BERT分别提升3.72%和2.82%。预训练模型表现出更快的收敛速度和更高的验证AUC。

### 技术栈

- GRU
- BERT
- 自监督学习
- 多任务学习
- 交叉熵损失
- 均方误差损失
- Barlow Twins
- AdamW优化器
- PyTorch

### 方法优势

- 提出新颖的计数对齐预训练目标，有效结合了传统计数特征和序列模型的优势。
- 实验设计全面，在多个数据集和编码器上验证了方法的有效性。
- 混合多任务学习策略提升了性能并降低了方差，显示了任务互补性。
- 提供了详细的消融实验和讨论，分析了各任务的影响。

### 主要局限

- Abacus损失值较高，模型无法精确计数，可能影响极端情况下的性能。
- 实验仅使用GRU和BERT两种编码器，未涵盖更多现代架构。
- 未在更长序列或更大词汇表上验证，泛化性有待进一步研究。
- 未讨论计算成本或训练时间的具体细节。

### 与当前研究方向的关联

序列推荐：本文针对序列用户建模，属于序列推荐范畴。；用户建模：核心是用户行为序列的表示学习。；自监督学习：采用自监督预训练方法。；CTR/CVR预测：下游任务是购买预测，与转化率预测相关。；工业落地：研究背景为展示广告，具有工业应用价值。

---

_知识库更新时间：2026-08-07T03:44:30.773293_
