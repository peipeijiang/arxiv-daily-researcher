---
title: "建模内生逻辑：用于可解释多行为推荐的因果神经符号推理模型"
paper_id: "https://doi.org/10.1145/3774904.3792419"
source: "www"
published: "2026-01-01T00:00:00"
score: 43.0
tags: ["paper", "recommender-systems", "Explainable Artificial Intelligence (XAI)", "Recommender Systems and Techniques", "Topic Modeling"]
---

# 建模内生逻辑：用于可解释多行为推荐的因果神经符号推理模型

> **英文原标题**：Modeling Endogenous Logic: Causal Neuro-Symbolic Reasoning Model for Explainable Multi-Behavior Recommendation

[查看原文](https://dblp.org/rec/conf/www/ChenCWTVW26) · [ArXiv](https://arxiv.org/abs/2601.21335)

## 一句话结论

> 该论文提出一种因果神经符号推理模型（CNRE），通过模拟用户行为链的内生逻辑并引入因果推断，在提升多行为推荐性能的同时提供多层级可解释性。

## 论文信息

- **作者**：Yuzhe Chen, Jie Cao, Youquan Wang, Haicheng Tao, Darko Vuković, Jia Wu
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：43.0
- **DOI**：[https://doi.org/10.1145/3774904.3792419](https://doi.org/10.1145/3774904.3792419)

<details open>
<summary><strong>中文摘要</strong></summary>

现有的大多数多行为推荐方法倾向于以牺牲可解释性为代价来追求性能，而当前的可解释方法由于依赖外部信息，其泛化能力受限。神经符号融合通过将神经网络与符号逻辑规则推理相结合，为可解释性提供了一条有前景的路径。同时，我们认为用户行为链（例如，浏览→加入购物车→购买）内在地蕴含了一种适合显式推理的内生逻辑。然而，这些可观测的多行为数据受到混杂因素的干扰，导致模型学习到虚假的相关性。通过将因果推断引入这一神经符号框架，我们提出了一种新颖的因果神经符号推理模型，用于可解释的多行为推荐（CNRE）。CNRE通过模拟类人的决策过程来实现内生逻辑的操作化。具体而言，CNRE首先采用层次化偏好传播来捕捉异构跨行为依赖关系。随后，它基于偏好强度对用户行为链中隐含的内生逻辑规则进行建模，并自适应地将推理任务分配到相应的神经逻辑推理路径（例如，合取、析取）。这一过程生成一个可解释的因果中介变量，该变量逼近一个隔离了混杂效应的理想状态。在三个大规模数据集上的大量实验表明，CNRE显著优于最先进的基线方法，并从模型设计、决策过程到推荐结果等多个层面提供了可解释性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Existing multi-behavior recommendations tend to prioritize performance at the expense of explainability, while current explainable methods suffer from limited generalizability due to their reliance on external information. Neuro-Symbolic integration offers a promising avenue for explainability by combining neural networks with symbolic logic rule reasoning. Concurrently, we posit that user behavior chains (e.g., view->cart->buy) inherently embody an endogenous logic suitable for explicit reasoning. However, these observational multiple behaviors are plagued by confounders, causing models to learn spurious correlations. By incorporating causal inference into this Neuro-Symbolic framework, we propose a novel Causal Neuro-Symbolic Reasoning model for Explainable Multi-Behavior Recommendation (CNRE). CNRE operationalizes the endogenous logic by simulating a human-like decision-making process. Specifically, CNRE first employs hierarchical preference propagation to capture heterogeneous cross-behavior dependencies. Subsequently, it models the endogenous logic rule implicit in the user's behavior chain based on preference strength, and adaptively dispatches to the corresponding neural-logic reasoning path (e.g., conjunction, disjunction). This process generates an explainable causal mediator that approximates an ideal state isolated from confounding effects. Extensive experiments on three large-scale datasets demonstrate CNRE's significant superiority over state-of-the-art baselines, offering multi-level explainability from model design and decision process to recommendation results.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对多行为推荐系统在追求性能时忽视可解释性，以及现有可解释方法依赖外部信息导致泛化性受限的问题，提出了一种新颖的因果神经符号推理模型（CNRE）。该模型将用户行为链视为内生逻辑，通过层次偏好传播模块捕获跨行为依赖并抑制混杂因素，然后基于偏好强度自适应地选择神经逻辑推理路径（合取、析取等），生成可解释的因果中介变量，以近似隔离混杂效应的理想状态。在三个真实数据集上的实验表明，CNRE在推荐性能上显著优于现有基线，并从模型设计、决策过程和推荐结果三个层面提供了可解释性。

### 主要创新

- 首次系统探索多行为推荐中的可解释性问题，提出不依赖外部信息的自包含范式。
- 将因果推断（前门调整）与神经符号推理结合，构建可解释的因果中介变量。
- 基于行为链的偏好强度自适应选择神经逻辑推理路径（合取、析取），模拟人类决策过程。
- 层次偏好传播模块结合并行编码与级联结构，有效处理行为异质性和跨行为依赖。

### 研究方法

CNRE包含三个核心模块：层次偏好传播（Hierarchical Preference Propagation）通过内在偏好学习、行为感知并行编码（图卷积与超图卷积）和级联自适应投影来生成高质量嵌入；因果神经符号推理（Causal Neuro-Symbolic Reasoning）根据行为链的完整性将用户分为强、中、弱偏好，分别采用直接处理、合取推理和析取推理，生成因果中介变量；预测模块基于中介变量进行最终预测，并使用BPR损失进行多任务学习。

### 关键结果

在Beibei、Taobao和Tmall三个数据集上，CNRE在HR@10、NDCG@10等指标上均优于所有基线，例如在Beibei上HR@10达到0.1074，NDCG@10为0.0523。消融实验验证了各模块的有效性，案例分析展示了决策过程的可解释性，鲁棒性实验表明CNRE在冷启动场景下性能下降最小。

### 技术栈

- LightGCN
- 超图卷积
- 近似最近邻搜索（ANNS）
- 多层感知机（MLP）
- 前门调整（Front-door Adjustment）
- 贝叶斯个性化排序（BPR）损失
- 多任务学习

### 方法优势

- 创新性地将因果推断与神经符号推理结合，提供了多层面的可解释性。
- 不依赖外部信息，泛化性强，适用于多种数据集。
- 自适应推理路径设计符合人类决策逻辑，增强了模型的透明度和可信度。
- 在多个数据集上取得了显著的性能提升。

### 主要局限

- 缺乏公认的可解释性量化指标，未进行大规模用户研究。
- 模型复杂度较高，可能影响实际部署效率。
- 对行为链的依赖可能限制其在行为类型较少场景下的适用性。

### 与当前研究方向的关联

该论文与推荐系统、可解释推荐、因果推理、神经符号推理、多行为推荐等关键词高度相关。它聚焦于多行为推荐的可解释性，通过因果推断和神经符号方法提升模型透明度和性能，符合推荐系统领域的前沿研究方向。

---

_知识库更新时间：2026-08-16T02:20:30.031721_
