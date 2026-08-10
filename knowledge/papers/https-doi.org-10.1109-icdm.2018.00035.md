---
title: "自注意力序列推荐"
paper_id: "https://doi.org/10.1109/icdm.2018.00035"
source: "citation"
published: "2018-11-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Machine Learning in Healthcare", "Generative Adversarial Networks and Image Synthesis"]
---

# 自注意力序列推荐

> **英文原标题**：Self-Attentive Sequential Recommendation

[查看原文](https://doi.org/10.1109/icdm.2018.00035)

## 一句话结论

> 该论文提出了一种基于自注意力机制的序列推荐模型（SASRec），在稀疏和密集数据集上均优于现有方法，且效率更高。

## 论文信息

- **作者**：Wang-Cheng Kang, Julian McAuley
- **来源**：2018 IEEE International Conference on Data Mining (ICDM)
- **发布时间**：2018-11-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1109/icdm.2018.00035](https://doi.org/10.1109/icdm.2018.00035)

<details open>
<summary><strong>中文摘要</strong></summary>

序列动态是现代许多推荐系统的一个关键特征，旨在基于用户最近执行的操作来捕捉其活动的“上下文”。为了捕捉此类模式，两种方法得到了广泛应用：马尔可夫链（MCs）和循环神经网络（RNNs）。马尔可夫链假设用户的下一个操作可以仅根据其最后（或最近几个）操作进行预测，而循环神经网络原则上能够揭示更长远的语义。总体而言，基于MC的方法在极其稀疏的数据集上表现最佳，此时模型简洁性至关重要；而RNN在数据密度较高、模型复杂度可承受的情况下表现更优。我们的工作目标是平衡这两者，通过提出一种基于自注意力的序列模型（SASRec），使其既能像RNN一样捕捉长期语义，又能利用注意力机制，基于相对较少的操作进行预测（类似于MC）。在每个时间步，SASRec试图从用户的操作历史中识别出“相关”的项目，并利用它们来预测下一个项目。大量实证研究表明，我们的方法在稀疏和密集数据集上均优于多种最先进的序列模型（包括基于MC/CNN/RNN的方法）。此外，该模型的效率比同类基于CNN/RNN的模型高出一个数量级。注意力权重的可视化也展示了我们的模型如何自适应地处理不同密度的数据集，并揭示活动序列中的有意义模式。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential dynamics are a key feature of many modern recommender systems, which seek to capture the 'context' of users' activities on the basis of actions they have performed recently. To capture such patterns, two approaches have proliferated: Markov Chains (MCs) and Recurrent Neural Networks (RNNs). Markov Chains assume that a user's next action can be predicted on the basis of just their last (or last few) actions, while RNNs in principle allow for longer-term semantics to be uncovered. Generally speaking, MC-based methods perform best in extremely sparse datasets, where model parsimony is critical, while RNNs perform better in denser datasets where higher model complexity is affordable. The goal of our work is to balance these two goals, by proposing a self-attention based sequential model (SASRec) that allows us to capture long-term semantics (like an RNN), but, using an attention mechanism, makes its predictions based on relatively few actions (like an MC). At each time step, SASRec seeks to identify which items are 'relevant' from a user's action history, and use them to predict the next item. Extensive empirical studies show that our method outperforms various state-of-the-art sequential models (including MC/CNN/RNN-based approaches) on both sparse and dense datasets. Moreover, the model is an order of magnitude more efficient than comparable CNN/RNN-based models. Visualizations on attention weights also show how our model adaptively handles datasets with various density, and uncovers meaningful patterns in activity sequences.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

序列动态是现代推荐系统的重要特征，旨在基于用户近期行为捕捉其活动上下文。现有方法主要有马尔可夫链（MC）和循环神经网络（RNN）：MC假设下一动作仅依赖最近动作，适合稀疏数据；RNN能捕捉长期语义，但需要密集数据。本文提出基于自注意力的序列模型（SASRec），结合两者优点：既能像RNN一样捕捉长期依赖，又通过注意力机制仅依赖少量动作进行预测。在每个时间步，SASRec从用户历史中识别相关物品并预测下一项。大量实验表明，该方法在稀疏和密集数据集上均优于多种最先进的序列模型（包括MC、CNN、RNN），且效率比CNN/RNN高一个数量级。注意力权重可视化显示模型能自适应处理不同密度的数据，并发现活动序列中的有意义模式。

### 主要创新

- 提出自注意力序列模型（SASRec），平衡MC和RNN的优势，在稀疏和密集数据上均表现优异。
- 利用自注意力机制捕捉长期语义，同时基于少量动作进行预测，兼具RNN和MC的特点。
- 模型效率比CNN/RNN高一个数量级，适合实际应用。
- 通过注意力权重可视化，展示模型自适应处理不同数据密度并发现序列模式。

### 研究方法

论文采用自注意力机制构建序列模型。具体地，模型在每个时间步对用户历史行为序列应用自注意力，计算各历史物品的权重，然后加权求和得到当前上下文表示，用于预测下一物品。训练过程使用标准监督学习，优化交叉熵损失。

### 关键结果

在稀疏和密集数据集上，SASRec均优于多种最先进的序列模型（包括MC、CNN/RNN方法）。模型效率比CNN/RNN高一个数量级。注意力权重可视化显示模型能自适应处理不同密度数据，并发现有意义的活动序列模式。

### 技术栈

- 自注意力机制
- 序列建模
- 马尔可夫链（对比）
- 循环神经网络（对比）
- 卷积神经网络（对比）

### 方法优势

- 方法创新，结合MC和RNN优点，适应不同数据密度。
- 实验全面，在稀疏和密集数据集上均验证有效性。
- 效率高，比CNN/RNN快一个数量级。
- 可视化分析提供模型可解释性。

### 主要局限

- 论文局限：摘要未提供具体数据集、基线、损失函数等细节，无法评估泛化性。当前证据局限：仅基于摘要，无法确认具体实验设置、消融研究、参数敏感性等。

### 与当前研究方向的关联

论文属于序列推荐领域，与关键词“序列推荐”高度相关；同时涉及用户建模（基于历史行为）、注意力机制（自注意力）、深度学习（RNN/CNN对比），与“用户建模”、“深度学习”相关。但未涉及生成式推荐、LLM、推荐智能体、多模态、对话式推荐、排序重排、CTR/CVR预测、因果性、公平性、鲁棒性等。

## 代码与复现

- [recommenders-team/recommenders](https://github.com/recommenders-team/recommenders)：possible，置信度 30，Stars 21849
- [tangxyw/RecSysPapers](https://github.com/tangxyw/RecSysPapers)：possible，置信度 30，Stars 2180
- [meta-recsys/generative-recommenders](https://github.com/meta-recsys/generative-recommenders)：possible，置信度 30，Stars 1958

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.666260_
