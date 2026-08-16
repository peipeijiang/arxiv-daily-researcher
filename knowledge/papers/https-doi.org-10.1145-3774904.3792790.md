---
title: "超越扁平序列：层次化与偏好感知的生成式推荐"
paper_id: "https://doi.org/10.1145/3774904.3792790"
source: "www"
published: "2026-01-01T00:00:00"
score: 48.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Mobile Crowdsensing and Crowdsourcing", "Explainable Artificial Intelligence (XAI)"]
---

# 超越扁平序列：层次化与偏好感知的生成式推荐

> **英文原标题**：Beyond the Flat Sequence: Hierarchical and Preference-Aware Generative Recommendations

[查看原文](https://dblp.org/rec/conf/www/ChenCLZCDLQ26) · [ArXiv](https://arxiv.org/abs/2603.00980)

## 一句话结论

> 本文提出了一种层次化和偏好感知的生成式推荐框架HPGR，通过结构感知预训练和偏好引导的稀疏注意力机制，在工业数据集和在线A/B测试中超越了现有基线，解决了生成式推荐中忽略用户行为层次结构和计算效率低的问题。

## 论文信息

- **作者**：Zerui Chen, Heng Chang, Tianying Liu, Chuantian Zhou, Yi Cao, Jiandong Ding, Ming Liu, Bing Qin
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：48.0
- **DOI**：[https://doi.org/10.1145/3774904.3792790](https://doi.org/10.1145/3774904.3792790)

<details open>
<summary><strong>中文摘要</strong></summary>

生成式推荐系统（Generative Recommenders, GRs），以层次序列转导单元（Hierarchical Sequential Transduction Unit, HSTU）为代表，已成为对长用户交互序列进行建模的强大范式。然而，我们观察到其“扁平序列”假设忽略了用户行为中丰富的内在结构，这导致两个关键局限：一是无法捕捉基于会话参与的时间层次结构；二是计算效率低下，因为密集注意力机制引入了显著噪声，在语义稀疏的历史记录中掩盖了真实偏好信号，从而降低了所学表示的质量。为此，我们提出了一种名为HPGR（Hierarchical and Preference-aware Generative Recommender，层次化与偏好感知生成式推荐系统）的新框架，该框架基于两阶段范式，将这些关键的结构先验注入模型中，以解决上述缺陷。具体而言，HPGR包含两个协同阶段：首先，结构感知预训练阶段采用基于会话的掩码物品建模（Masked Item Modeling, MIM）目标，学习一个具有层次信息且语义丰富的物品表示空间；其次，偏好感知微调阶段利用这些强大的表示，实现偏好引导的稀疏注意力机制（Preference-Guided Sparse Attention），该机制将计算动态限制在最相关的历史物品上，从而提升效率与信噪比。在来自APPGallery的大规模专有工业数据集上的实证实验以及在线A/B测试验证了HPGR在多个强基线方法（包括HSTU和MTGR）上取得了最先进的性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Generative Recommenders (GRs), exemplified by the Hierarchical Sequential Transduction Unit (HSTU), have emerged as a powerful paradigm for modeling long user interaction sequences. However, we observe that their ''flat-sequence'' assumption overlooks the rich, intrinsic structure of user behavior. This leads to two key limitations: a failure to capture the temporal hierarchy of session-based engagement, and computational inefficiency, as dense attention introduces significant noise that obscures true preference signals within semantically sparse histories, which deteriorates the quality of the learned representations. To this end, we propose a novel framework named HPGR (Hierarchical and Preference-aware Generative Recommender), built upon a two-stage paradigm that injects these crucial structural priors into the model to handle the drawback. Specifically, HPGR comprises two synergistic stages. First, a structure-aware pre-training stage employs a session-based Masked Item Modeling (MIM) objective to learn a hierarchically-informed and semantically rich item representation space. Second, a preference-aware fine-tuning stage leverages these powerful representations to implement a Preference-Guided Sparse Attention mechanism, which dynamically constrains computation to only the most relevant historical items, enhancing both efficiency and signal-to-noise ratio. Empirical experiments on a large-scale proprietary industrial dataset from APPGallery and an online A/B test verify that HPGR achieves state-of-the-art performance over multiple strong baselines, including HSTU and MTGR.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对生成式推荐模型（如HSTU）将用户历史视为扁平序列而忽略其内在层次结构和偏好稀疏性的问题，提出了HPGR框架。HPGR采用两阶段训练：首先通过结构感知预训练阶段，利用会话增强模块（SEM）和掩码物品建模（MIM）目标学习层次化的物品表示；然后在偏好感知微调阶段，引入偏好引导稀疏注意力（PGSA）机制，动态聚焦于与候选物品最相关的历史子集，提升效率和准确性。在APPGallery工业数据集上的离线实验和在线A/B测试表明，HPGR显著优于HSTU、MTGR等基线，并在在线eCPM上获得+1.99%的提升。

### 主要创新

- 提出会话增强模块（SEM），显式建模用户行为的会话层次结构，克服扁平序列假设。
- 设计偏好引导稀疏注意力（PGSA），基于预训练嵌入动态选择最相关的历史子集，提高注意力效率和信噪比。
- 采用两阶段训练范式：结构感知预训练（MIM目标）和偏好感知微调，实现通用表示与任务适配的平衡。
- 在工业级数据集和在线A/B测试中验证了方法的有效性，实现了显著的eCPM提升。

### 研究方法

HPGR包含两个阶段：1）结构感知预训练：将用户历史划分为会话，通过会话内Transformer和会话间Transformer（SEM）建模层次结构，使用掩码物品建模（MIM）目标学习物品嵌入和SEM参数。2）偏好感知微调：继承预训练权重，引入时间感知位置编码和PGSA机制，PGSA通过计算候选物品与历史物品的嵌入点积选择Top-K偏好信号，并构造高斯注意力掩码，最后通过HSTU编码器进行pCTR预测，使用二元交叉熵损失训练。

### 关键结果

在APPGallery数据集上，HPGR（Full）的AUC达到0.8377，相比最强基线MTGR（0.8253）提升+1.50%；在完整测试集上AUC为0.89288，比MTGR高+0.01139；在线A/B测试中eCPM提升+1.99%。消融实验显示，预训练、PGSA和SEM均带来性能提升。

### 技术栈

- Transformer架构
- 会话增强模块（SEM）
- 掩码物品建模（MIM）
- 偏好引导稀疏注意力（PGSA）
- 高斯注意力掩码
- 时间感知位置编码
- HSTU编码器
- 二元交叉熵损失
- UMAP可视化
- A/B测试

### 方法优势

- 创新性地将层次结构和偏好稀疏性引入生成式推荐，弥补了现有模型的不足。
- 两阶段训练策略有效结合了自监督预训练和任务微调，提升了表示质量。
- PGSA机制在提升效率的同时增强了注意力聚焦能力。
- 在工业级数据集和在线环境中验证了有效性，具有实际应用价值。

### 主要局限

- 依赖会话划分，会话边界定义可能影响性能。
- PGSA的Top-K和σ超参数需要调优。
- 预训练阶段计算开销较大。
- 实验仅在单一数据集（APPGallery）上进行，泛化性有待验证。

### 与当前研究方向的关联

论文与序列推荐、生成式推荐、用户建模、CTR预测、工业落地等关键词高度相关，提出了新的层次化建模和稀疏注意力方法，推动了生成式推荐的发展。

---

_知识库更新时间：2026-08-16T02:20:30.032073_
