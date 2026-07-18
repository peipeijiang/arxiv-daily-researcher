---
title: "BERT-Based Cross-Encoder for Large-Scale Engagement Prediction and Re-ranking in Walmart Search Engine"
paper_id: "https://doi.org/10.1145/3805712.3808499"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 29.0
tags: ["paper", "recommender-systems", "Information Retrieval and Search Behavior", "Expert finding and Q&A systems", "Recommender Systems and Techniques"]
---

# BERT-Based Cross-Encoder for Large-Scale Engagement Prediction and Re-ranking in Walmart Search Engine

[查看原文](https://dblp.org/rec/conf/sigir/ChenFPKSMYS26) · [Semantic Scholar](https://www.semanticscholar.org/paper/0a0d66cbdf087cc2eb05c5b7d7947e2232b7fa89)

## 一句话结论

> 论文提出基于BERT的交叉编码器用于大规模参与度预测和重排序，在Walmart搜索中提升了加购率。

## 论文信息

- **作者**：S. Chen, Philip Fu, Ajit Puthenputhussery, Changsung Kang, Ming Sun, Cun Mu, S. K. Yadav, Hongwei Shang
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：29.0
- **DOI**：[https://doi.org/10.1145/3805712.3808499](https://doi.org/10.1145/3805712.3808499)

<details open>
<summary><strong>中文摘要</strong></summary>

产品搜索系统不仅要返回相关商品，还必须理解用户在其显式查询之外的隐式偏好。例如，当搜索“牛排”时，大多数用户隐式偏好牛肉牛排，而非同样相关的替代品如猪肉牛排。预测此类参与偏好比传统的相关性建模更具挑战性，因为它需要捕捉反映相关性和用户意图的细微查询-商品关系。为捕捉这些细微差别，我们将语义理解扩展到参与预测，通过直接从查询-商品文本中学习，并以参与标签作为监督信号，而非依赖历史参与统计数据作为输入。我们的方法有效捕捉了用户在不同查询类型中的隐式偏好，从历史信号稀疏的长尾查询到理解潜在意图至关重要的宽泛查询。在沃尔玛生产搜索数据上的大量实验表明，与具有强相关性基础的生产模型相比，我们的模型取得了显著改进：交错测试中购物车添加率提升+1.71%，整体搜索会话中购物车添加率提升+0.33%。该模型已部署在Walmart.com的生产环境中。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Product search systems must not only return relevant items but also understand users' implicit preferences beyond their explicit queries. For instance, when searching for "steak", most users implicitly prefer beef steak over equally relevant alternatives like pork steak. Predicting such engagement preferences presents a more complex challenge than traditional relevance modeling, as it requires capturing nuanced query-item relationships that reflect both relevance and user intent. To capture these nuances, we extend semantic understanding to engagement prediction by learning directly from query-item text with engagement labels as supervision rather than relying on historical engagement statistics as input. Our approach effectively captures users' implicit preferences across diverse query types, from tail queries where historical signals are sparse to broad queries where understanding latent intent is critical. Extensive experiments on Walmart's production search data demonstrate significant improvements over production model with a strong relevance foundation: +1.71% add-to-cart lift in interleaving tests and +0.33% in overall search sessions with add-to-cart. Our model is deployed in the production environment of Walmart.com.

</details>

---

_知识库更新时间：2026-07-18T03:48:20.892684_
