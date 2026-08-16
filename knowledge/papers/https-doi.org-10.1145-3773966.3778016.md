---
title: "解耦用户特征用于用户冷启动应用推荐：静态属性与行为序列"
paper_id: "https://doi.org/10.1145/3773966.3778016"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 37.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Advanced Graph Neural Networks"]
---

# 解耦用户特征用于用户冷启动应用推荐：静态属性与行为序列

> **英文原标题**：Decoupling User Features for User Cold-Start App Recommendation: Static Attributes versus Behavioral Sequences

[查看原文](https://dblp.org/rec/conf/wsdm/ChenK00026)

## 一句话结论

> 本文提出AFIM架构，通过解耦用户属性特征和行为序列特征并动态融合，有效缓解了用户冷启动推荐中的特征干扰问题，在多个数据集上优于现有方法。

## 论文信息

- **作者**：Bin Chen, Yu Kang, Li Ma, Yue Ding, Xiaofeng Gao
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：37.0
- **DOI**：[https://doi.org/10.1145/3773966.3778016](https://doi.org/10.1145/3773966.3778016)

<details open>
<summary><strong>中文摘要</strong></summary>

在应用推荐中，用户冷启动一直是推荐系统面临的基本挑战。现有方法主要侧重于高效利用有限数据或从活跃用户迁移知识以缓解用户冷启动问题，但往往忽视了特征交互对用户冷启动的影响。我们根据语义类型对特征进行分组，并发现了一个有趣的现象：用户属性特征与行为序列特征相互干扰，从而限制了模型有效表示冷启动用户的能力。我们将这一问题归因于两类特征在潜在空间分布和学习复杂度上的差异，这些差异阻碍了模型准确捕捉冷启动用户的兴趣。为应对这一挑战，我们提出了AFIM架构，该架构将用户属性特征与行为序列特征的学习进行解耦。AFIM利用轻量级注意力模块从行为序列中显式捕捉用户兴趣，从而减轻下游推荐网络的学习负担。此外，该架构还引入了特征解耦与动态融合模块，以缓解异质特征空间带来的学习偏差。在两个公开数据集和两个工业数据集上的大量实验表明，AFIM始终优于最先进的基线方法，凸显了其在用户冷启动场景中的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In app recommendation, user cold-start remains a fundamental challenge in recommender systems. Existing approaches primarily focus on efficiently leveraging limited data or transferring knowledge from active users to alleviate the user cold-start problem, yet they often overlook the influence of feature interactions on user cold-start. We group features according to their semantic types and identify an interesting phenomenon: user attribute features and behavioral sequence features interfere with each other, thereby constraining the model's ability to represent cold-start users effectively. We attribute this issue to differences in the latent space distributions and learning complexities of the two feature types, which hinder the model from accurately capturing cold-start users' interests. To address this challenge, we propose the AFIM architecture, which decouples the learning of user attribute and behavior sequential features. AFIM leverages a lightweight attention module to explicitly capture user interests from behavioral sequences, thereby reducing the learning burden on downstream recommendation networks. Additionally, it incorporates feature decoupling and dynamic fusion modules to mitigate learning bias arising from heterogeneous feature spaces. Extensive experiments on two public datasets and two industrial datasets demonstrate that AFIM consistently outperforms SOTA baselines, highlighting its effectiveness in user cold-start scenarios.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

在应用推荐中，用户冷启动是推荐系统的基本挑战。现有方法主要关注高效利用有限数据或从活跃用户迁移知识，但往往忽略特征交互对用户冷启动的影响。本文根据语义类型对特征进行分组，发现用户属性特征和行为序列特征相互干扰，限制了模型对冷启动用户的有效表示。作者将问题归因于两类特征在潜在空间分布和学习复杂度上的差异。为此，提出AFIM架构，解耦用户属性和行为序列特征的学习，利用轻量级注意力模块从行为序列中显式捕获用户兴趣，减少下游推荐网络的学习负担，并通过特征解耦和动态融合模块缓解异质特征空间带来的学习偏差。在两个公共数据集和两个工业数据集上的大量实验表明，AFIM持续优于最先进的基线，证明了其在用户冷启动场景中的有效性。

### 主要创新

- 识别出用户属性特征与行为序列特征之间的相互干扰现象，并归因于潜在空间分布和学习复杂度的差异。
- 提出AFIM架构，解耦用户属性和行为序列特征的学习，降低特征间的干扰。
- 利用轻量级注意力模块从行为序列中显式捕获用户兴趣，减轻下游推荐网络的学习负担。
- 引入特征解耦和动态融合模块，缓解异质特征空间导致的学习偏差。

### 研究方法

论文提出AFIM架构，包含特征解耦模块、轻量级注意力模块和动态融合模块。首先，将用户特征分为静态属性特征和行为序列特征，并分别处理。然后，通过轻量级注意力模块从行为序列中提取用户兴趣表示。接着，利用特征解耦模块减少两类特征之间的相互干扰，并通过动态融合模块自适应地融合两类特征，以缓解异质特征空间带来的学习偏差。最后，将融合后的表示输入下游推荐网络进行预测。

### 关键结果

在两个公共数据集和两个工业数据集上的大量实验表明，AFIM持续优于最先进的基线，证明了其在用户冷启动场景中的有效性。

### 技术栈

- 摘要未提供具体技术栈，但提及了轻量级注意力模块、特征解耦和动态融合模块。

### 方法优势

- 针对用户冷启动问题，创新性地从特征交互角度切入，揭示了属性特征与行为序列特征的干扰现象。
- 提出的AFIM架构通过解耦和动态融合，有效缓解了特征干扰，提升了冷启动用户表示能力。
- 在多个数据集上验证了方法的有效性，包括公共和工业数据集，具有实际应用价值。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：由于仅提供摘要，无法评估模型复杂度、可扩展性、对长尾分布的适应性等，且未提供具体实验细节和对比结果。

### 与当前研究方向的关联

该论文与用户建模、序列推荐、CTR/CVR预测等关键词高度相关。它聚焦于用户冷启动场景，通过解耦用户属性特征和行为序列特征来改进用户建模，并利用行为序列进行推荐，属于序列推荐范畴。同时，其方法可应用于点击率预测等任务，因此与CTR/CVR预测相关。

---

_知识库更新时间：2026-08-16T02:20:30.030299_
