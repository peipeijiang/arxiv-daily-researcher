---
title: "Modeling Social Behavior in Collaborative Filtering"
paper_id: "https://doi.org/10.1145/3726302.3730039"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 36.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Mobile Crowdsensing and Crowdsourcing", "Human Mobility and Location-Based Analysis"]
---

# Modeling Social Behavior in Collaborative Filtering

[查看原文](https://dblp.org/rec/conf/sigir/0001H25) · [Semantic Scholar](https://www.semanticscholar.org/paper/959ffb618cde45a5739e29874b5b2e58b4352859)

## 一句话结论

> 该论文提出了一种更全面的社会行为模型DSCP，用于从用户-物品交互中解耦用户兴趣和从众效应，并在多个数据集上提升了推荐准确性和去偏效果。

## 论文信息

- **作者**：Yihong Zhang, Takahiro Hara
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：36.0
- **DOI**：[https://doi.org/10.1145/3726302.3730039](https://doi.org/10.1145/3726302.3730039)

<details open>
<summary><strong>中文摘要</strong></summary>

如今，许多在线服务利用推荐系统向用户提供个性化的物品推荐。协同过滤是推荐系统中的主要范式。基于用户-物品交互数据，协同过滤根据其他相似用户的偏好向目标用户推荐物品。推荐中的兴趣解耦问题目前已引起众多研究者的关注。已有若干工作提出方法，通过假设从众行为与物品流行度相关，将从众因素与用户私人兴趣进行解耦。然而，这种建模方式过于简化，忽略了用户公共兴趣、私人兴趣与物品流行度之间的多种可能性。例如，用户可能私下喜欢一部热门电影，或因社会环境刺激而购买一张小众音乐专辑。在本文中，我们提出了一种更全面的社会行为模型，用以描述用户兴趣与物品流行度之间的细粒度关系。我们的模型不依赖显式的用户关系数据，而是直接从用户-物品交互数据中提取社会行为模式。我们还将该模型构建为一个推荐框架，称为解耦社会消费者偏好（Disentangled Social Consumer Preference, DSCP），该框架可集成到现有的推荐模型（如BPRMF）中。我们在来自不同服务的四个数据集上进行了大量实验，结果表明我们的模型能够超越最先进的基线模型。在常规随机测试和用于展示去偏效果的干预测试中，我们都取得了更高的推荐准确率。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Nowadays, many online services use recommendation systems to provide personalized item recommendations to users. Collaborative filtering is the major paradigm in recommendation systems. Based on user-item interaction data, collaborative filtering recommends items to a user based on other similar users. The problem of interest disentanglement in recommendation now has attracted the attention of many researchers. Several works have proposed methods to disentangle conformity from user private interest, by assuming that conformity is correlated to item popularity. However, such modeling is simplistic and overlooks many possibilities between user public and private interest, and the item popularity. For example, a user can privately like a popular movie or buy a niche music album due to the stimulation of the social environment. In this paper, we propose a more comprehensive social behavior model that describes fine-grained relationships between user interest and item popularity. Our model does not use explicit user relationship data. Instead, we extract social behavior patterns directly from user-item interaction data. We also make our model into a recommendation framework called Disentangled Social Consumer Preference (DSCP), which can be integrated into existing recommendation models such as BPRMF. Our extensive experiments with four datasets from different services show that our model can outperform state-of-the-art baseline models. We achieve better recommendation accuracy in both the usual random test and the intervened test that shows debiasing effect.

</details>

---

_知识库更新时间：2026-08-12T03:12:07.693204_
