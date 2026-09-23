---
title: "多任务深度推荐系统：综述"
paper_id: "https://doi.org/10.1145/3846376"
source: "openalex"
published: "2026-09-22T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Multimodal Machine Learning Applications", "Topic Modeling"]
---

# 多任务深度推荐系统：综述

> **英文原标题**：Multi-Task Deep Recommender Systems: A Survey

[查看原文](https://doi.org/10.1145/3846376) · [ArXiv](https://arxiv.org/abs/2302.03525)

## 一句话结论

> 该综述系统回顾了多任务深度推荐系统（MTDRS），从任务关系和方法论角度提出了分类体系，总结了应用和公开数据集，并指出了未来挑战。

## 论文信息

- **作者**：Yuhao Wang, Ha Tsz Lam, Yi Lin Wong, Ziru Liu, Wanyu Wang, Yichao Wang, Yichao Wang, Bo Chen, Huifeng Guo, Ruiming Tang, Xiangyu Zhao
- **来源**：ACM Computing Surveys
- **发布时间**：2026-09-22
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3846376](https://doi.org/10.1145/3846376)

<details open>
<summary><strong>中文摘要</strong></summary>

多任务学习（Multi-task Learning, MTL）旨在通过统一模型学习相关任务，考虑任务间的共享知识以实现相互提升。由于在多任务预测中需要兼顾性能与效率，多任务学习在推荐系统中成为一个重要课题。尽管多任务学习已得到充分研究和发展，但推荐领域仍缺乏系统性的综述。为填补这一空白，本综述对现有多任务深度推荐系统（Multi-Task Deep Recommender Systems, MTDRS）进行了全面回顾。具体而言，首先给出MTDRS的问题定义，并将其与其他相关领域进行比较。接着，描述了MTDRS的发展历程，并从任务关系和方法论两个维度介绍了分类体系。其中，任务关系被划分为并行、级联以及主辅（auxiliary with main）三类，方法论则分为参数共享、优化和训练机制三类。本综述最后总结了MTDRS的应用和公开数据集，并强调了该领域面临的挑战和未来方向。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multi-task learning (MTL) aims at learning related tasks in a unified model to achieve mutual improvement among tasks considering their shared knowledge. It is an important topic in recommendation due to the demand for multi-task prediction considering performance and efficiency. Although MTL has been well studied and developed, there is still a lack of systematic review in the recommendation community. To fill the gap, we provide a comprehensive review of existing multi-task deep recommender systems (MTDRS) in this survey. To be specific, the problem definition of MTDRS is first given, and it is compared with other related areas. Next, the development of MTDRS is depicted and the taxonomy is introduced from the task relation and methodology aspects. Specifically, the task relation is categorized into parallel, cascaded, and auxiliary with main, while the methodology is grouped into parameter sharing, optimization, and training mechanism. The survey concludes by summarizing the application and public datasets of MTDRS and highlighting the challenges and future directions of the field.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对多任务学习在推荐领域缺乏系统性综述的现状，对现有多任务深度推荐系统（MTDRS）进行了全面回顾。论文首先给出MTDRS的问题定义，并与多目标推荐、多场景推荐、多行为推荐以及CV/NLP中的多任务学习进行比较。随后从任务关系和方法论两个维度构建分类体系：任务关系分为并行、级联和主辅任务，方法论分为参数共享、优化和训练机制。论文还总结了MTDRS的应用场景与公开数据集，并指出负迁移、多任务多场景建模、大语言模型、AutoML、可解释性、任务特定偏差和工业部署等挑战与未来方向。

### 主要创新

- 首次对多任务深度推荐系统（MTDRS）进行系统性综述，填补了推荐社区在该方向上的综述空白。
- 提出基于任务关系和方法论两个互补维度的面式分类体系，而非互斥树状分类，允许同一模型出现在多个类别中。
- 将任务关系细分为并行、级联和主辅任务三类，并给出各类的典型设置、代表模型和主要挑战。
- 将方法论细分为参数共享（硬共享、稀疏共享、软共享、专家共享）、优化（负迁移、多目标权衡）和训练机制（联合训练、强化学习、辅助任务学习）。
- 系统梳理了MTDRS在广告、社交媒体等领域的应用以及公开数据集，并展望了大语言模型、AutoML等未来方向。

### 研究方法

本文采用文献综述方法。首先给出MTDRS的形式化定义，包括多任务损失加权和优化目标、可更新损失权重和BCE损失等。然后通过对比分析，将MTR与多目标推荐、多场景推荐、多行为推荐以及CV/NLP中的MTL进行区分。接着从任务关系和方法论两个维度构建分类体系，对代表性模型进行归类和比较。最后总结应用领域、公开数据集以及挑战和未来方向。

### 关键结果

MTDRS相比单独处理多个推荐任务具有两个主要优势：利用跨任务数据和知识实现任务间相互增强，以及获得更高的计算和存储效率。；MTDRS面临三个主要挑战：有效且高效地捕获任务间有用信息和相关性、转化信号等数据稀疏问题、以及推荐中跨任务用户行为的独特序列依赖。；任务关系可分为并行、级联和主辅任务三类；并行任务主要挑战是选择有用共享特征并避免弱相关任务间的负迁移；级联任务主要挑战是在样本选择偏差、数据稀疏、延迟反馈和因果混杂下建模序列依赖；主辅任务主要挑战是设计辅助任务以帮助主任务而不引入任务主导或噪声迁移。；方法论可分为参数共享、优化和训练机制三类；参数共享包括硬共享、稀疏共享、软共享和专家共享；优化关注负迁移和多目标权衡；训练机制包括联合训练、强化学习和辅助任务学习。；公开数据集包括Ali-CCP、Criteo、AliExpress、MovieLens、Yelp、Amazon、Kuairand和Tenrec，涵盖排序和召回排序阶段以及CTR、CVR、评分、解释、点击、点赞、分享、关注等任务。

### 技术栈

- 多任务学习（MTL）
- 深度神经网络（DNN）
- 硬参数共享
- 稀疏共享
- 软参数共享
- 专家共享（Mixture of Experts, MoE）
- MMoE
- PLE及其Customized Gate Control（CGC）
- DSelect-k
- AdaTT
- SNR
- MetaHeac
- PFE
- MVKE
- FDN
- STEM
- DTN
- MoME
- MoSE
- AdaTask
- MetaBalance
- GradCraft
- CSRec
- PEPNet
- TIDM
- ORCA
- ESMM
- AITM
- APEM
- DCMT
- AECM
- DDPO
- 强化学习（RL）
- 马尔可夫决策过程（MDP）
- 批量强化学习
- Actor-Critic
- 离线策略强化学习
- 贝叶斯优化
- 网格搜索
- 进化算法
- 大语言模型（LLM）
- P5
- M6-Rec
- UniMIND
- URM
- CKF
- IDGenRec
- COBRA
- UniGRF
- BCE损失
- 回归损失
- pairwise或listwise排序损失
- 重构损失
- 序列生成损失

### 方法优势

- 系统性强，首次对MTDRS进行全面综述，覆盖问题定义、相关领域对比、分类体系、应用、数据集和未来方向。
- 分类体系设计合理，采用任务关系和方法论两个互补维度，避免互斥树状分类的局限，能更灵活地归类现有模型。
- 对级联任务关系进行了详细总结，给出了代表性模型、问题和行为序列的对比表格。
- 对参数共享模式进行了清晰分类和图示说明，包括硬共享、稀疏共享、软共享和专家共享。
- 对负迁移问题从梯度主导和参数冲突两个角度进行了深入分析，并总结了多种解决方案。
- 关注工业落地，讨论了多任务融合、强化学习融合以及在线部署中的延迟、安全和奖励设计等问题。
- 指出了大语言模型、AutoML、可解释性等未来方向，具有较好的前瞻性。

### 主要局限

- 作为综述，本文未提出新的具体模型或算法，也未进行新的实验验证。
- 论文未提供定量的实验对比结果或性能指标，无法直接评估各类方法的实际效果差异。
- 分类体系为面式分类，同一模型可能出现在多个类别中，可能导致读者对模型归属产生混淆。
- 对非深度多任务推荐方法仅作为背景讨论，未进行系统梳理。
- 对多任务与多场景联合建模的讨论指出任务序列依赖未被考虑，但未给出具体解决方案。
- 对LLM在MTDRS中的应用主要停留在方向性讨论，未深入探讨具体技术路线和评估方法。
- 公开数据集列表以代表性资源为主，未穷举所有可适配的数据集，可能遗漏部分领域数据集。

### 与当前研究方向的关联

本文与推荐系统领域多个关键词高度相关。首先，论文主题为多任务深度推荐系统，直接关联CTR/CVR预测、排序与重排以及工业落地。其次，论文讨论了级联任务中的样本选择偏差、数据稀疏和因果去偏，涉及推荐系统的因果性。再次，论文展望了大语言模型在推荐中的应用，关联LLM与推荐系统结合。此外，论文涉及用户建模、多行为推荐、多场景推荐、多目标推荐、可解释性推荐和强化学习融合，与序列推荐、生成式推荐、推荐智能体、多模态推荐、对话式推荐等方向也有间接关联。论文还讨论了公平性、鲁棒性和工业部署挑战，与推荐系统的公平性、鲁棒性和工业落地关键词相关。

---

_知识库更新时间：2026-09-23T05:05:07.847914_
