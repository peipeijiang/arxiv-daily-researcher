---
title: "Modeling User Activity Preference by Leveraging User Spatial Temporal Characteristics in LBSNs"
paper_id: "https://doi.org/10.1109/tsmc.2014.2327053"
source: "citation"
published: "2014-06-26T00:00:00"
score: 29.0
tags: ["paper", "recommender-systems", "Human Mobility and Location-Based Analysis", "Recommender Systems and Techniques", "Context-Aware Activity Recognition Systems"]
---

# Modeling User Activity Preference by Leveraging User Spatial Temporal Characteristics in LBSNs

[查看原文](https://doi.org/10.1109/tsmc.2014.2327053)

## 一句话结论

> 该论文提出了一种STAP模型，通过分别建模空间和时间活动偏好并融合，以解决LBSN中用户活动偏好建模的数据稀疏问题，并在纽约和东京数据集上验证了其有效性。

## 论文信息

- **作者**：Dingqi Yang, Daqing Zhang, Vincent W. Zheng, Zhiyong Yu
- **来源**：IEEE Transactions on Systems Man and Cybernetics Systems
- **发布时间**：2014-06-26
- **相关度评分**：29.0
- **DOI**：[https://doi.org/10.1109/tsmc.2014.2327053](https://doi.org/10.1109/tsmc.2014.2327053)

<details open>
<summary><strong>中文摘要</strong></summary>

随着基于位置的社交网络（LBSNs）的迅猛发展，数百万用户的日常活动数据已变得易于获取。这些数据不仅包含用户活动的时空标记，还蕴含了其语义信息。LBSNs有助于理解移动用户的时空活动偏好（STAP），进而支持一系列泛在应用，如个性化情境感知的位置推荐和面向群体的广告投放。然而，建模这种用户特定的STAP需要处理高维数据，即用户-位置-时间-活动四元组，这既复杂又常常面临数据稀疏性问题。为解决此问题，我们提出了一种STAP模型。该模型首先分别对空间活动偏好和时间活动偏好进行建模，然后采用一种原则性的方法将两者结合以进行偏好推断。为了刻画空间特征对用户活动偏好的影响，我们提出了个人功能区域的概念及相关参数，用以建模和推断用户的空间活动偏好。为了在LBSNs中利用稀疏的用户活动数据建模用户的时间活动偏好，我们提出利用不同用户间的时间活动相似性，并应用非负张量分解来协同推断时间活动偏好。最后，我们提出一个情境感知的融合框架，将空间与时间活动偏好模型结合以进行偏好推断。我们在从纽约和东京收集的三个真实世界数据集上评估了所提出的方法，结果表明我们的STAP模型在各种设置下均优于基线方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

With the recent surge of location based social networks (LBSNs), activity data of millions of users has become attainable. This data contains not only spatial and temporal stamps of user activity, but also its semantic information. LBSNs can help to understand mobile users' spatial temporal activity preference (STAP), which can enable a wide range of ubiquitous applications, such as personalized context-aware location recommendation and group-oriented advertisement. However, modeling such user-specific STAP needs to tackle high-dimensional data, i.e., user-location-time-activity quadruples, which is complicated and usually suffers from a data sparsity problem. In order to address this problem, we propose a STAP model. It first models the spatial and temporal activity preference separately, and then uses a principle way to combine them for preference inference. In order to characterize the impact of spatial features on user activity preference, we propose the notion of personal functional region and related parameters to model and infer user spatial activity preference. In order to model the user temporal activity preference with sparse user activity data in LBSNs, we propose to exploit the temporal activity similarity among different users and apply nonnegative tensor factorization to collaboratively infer temporal activity preference. Finally, we put forward a context-aware fusion framework to combine the spatial and temporal activity preference models for preference inference. We evaluate our proposed approach on three real-world datasets collected from New York and Tokyo, and show that our STAP model consistently outperforms the baseline approaches in various settings.

</details>

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3770855.3818010
- **seed_title**：G²PRO: Gradient-guided Graph Prompt Optimization for LLM-based POI Recommendation
- **seed_score**：98.0

</details>

---

_知识库更新时间：2026-08-11T02:42:36.425112_
