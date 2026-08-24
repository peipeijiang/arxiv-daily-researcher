---
title: "基于数据Shapley值的邻域推荐可扩展数据调试"
paper_id: "https://doi.org/10.1145/3705328.3748049"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 37.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Data Management and Algorithms", "Image Retrieval and Classification Techniques"]
---

# 基于数据Shapley值的邻域推荐可扩展数据调试

> **英文原标题**：Scalable Data Debugging for Neighborhood-based Recommendation with Data Shapley Values

[查看原文](https://dblp.org/rec/conf/recsys/KersbergenSKRS25) · [Semantic Scholar](https://www.semanticscholar.org/paper/6dc15586d82fcab0ffdca6835ae3e3a12ee8afbe)

## 一句话结论

> This paper introduces KMC-Shapley, a scalable algorithm for estimating Data Shapley values in neighborhood-based recommendation systems, enabling efficient identification of harmful data points to improve recommendation quality and safety.

## 论文信息

- **作者**：Barrie Kersbergen, Olivier Sprangers, Bojan Karlaš, Maarten de Rijke, Sebastian Schelter
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：37.0
- **DOI**：[https://doi.org/10.1145/3705328.3748049](https://doi.org/10.1145/3705328.3748049)

<details open>
<summary><strong>中文摘要</strong></summary>

基于机器学习的推荐系统帮助用户发现他们可能感兴趣的物品。然而，这些系统所处理的交互数据中存在的问题常常导致各种故障，例如意外推荐低质量产品或危险物品。这类数据问题难以提前预见，通常是在部署之后、已经对用户体验造成影响时才被发现。我们认为，需要一种有原则的数据调试流程，在该流程中，人类专家能够识别潜在有害的数据问题并提前加以缓解。近年来提出的“数据重要性”概念，如数据Shapley值（DSV），为识别可能导致问题的训练数据点提供了一个有前景的方向。然而，现实世界交互数据集的规模使得在推荐场景中应用现有技术计算DSV变得不可行。为解决这一问题，我们引入了KMC-Shapley算法，用于在稀疏交互数据上基于邻域的推荐中可扩展地估计数据Shapley值。我们在包含数百万交互的公开数据集和专有数据集上，对该算法的效率和可扩展性进行了实验评估，并展示了DSV在电子商务的两项推荐任务中能够识别出具有影响力的数据点。此外，我们还讨论了DSV在电子商务真实点击和购买数据上的应用，例如识别危险产品或提升产品推荐的生态可持续性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Machine learning-powered recommendation systems help users find items they like. Issues in the interaction data processed by these systems frequently lead to problems, e.g., to the accidental recommendation of low-quality products or dangerous items. Such data issues are hard to anticipate upfront, and are typically detected post-deployment after they have already impacted the user experience. We argue that a principled data debugging process is required during which human experts identify potentially hurtful data issues and preemptively mitigate them. Recent notions of “data importance,” such as the Data Shapley value (DSV), represent a promising direction to identify training data points likely to cause issues. However, the scale of real-world interaction datasets makes it infeasible to apply existing techniques to compute the DSV in recommendation scenarios. We tackle this problem by introducing the KMC-Shapley algorithm for the scalable estimation of Data Shapley values in neighbor-hood-based recommendation on sparse interaction data. We conduct an experimental evaluation of the efficiency and scalability of our algorithm on both public and proprietary datasets with millions of interactions, and showcase that the DSV identifies impactful data points for two recommendation tasks in e-commerce. Furthermore, we discuss applications of the DSV on real-world click and purchase data in e-commerce, such as identifying dangerous products or improving the ecological sustainability of product recommendations.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

推荐系统常因交互数据中的问题导致推荐低质量或危险物品，这些问题难以提前预见，通常在部署后影响用户体验。本文提出一种原则性的数据调试流程，由专家识别潜在有害数据问题并预先缓解。数据重要性概念（如数据Shapley值，DSV）为识别可能引发问题的训练数据点提供了有前景的方向，但真实交互数据集的规模使得现有DSV计算方法在推荐场景中不可行。为此，本文提出KMC-Shapley算法，用于在稀疏交互数据上基于邻域的推荐中可扩展地估计数据Shapley值。实验在包含数百万交互的公开和专有数据集上评估了算法的效率和可扩展性，并展示了DSV在电子商务中两个推荐任务中识别有影响力数据点的能力。此外，讨论了DSV在真实点击和购买数据上的应用，如识别危险产品或提高产品推荐的生态可持续性。

### 主要创新

- 提出KMC-Shapley算法，实现邻域推荐中数据Shapley值的可扩展估计，解决现有方法在真实规模数据上的不可行问题。
- 针对稀疏交互数据设计算法，提高计算效率，适用于大规模推荐场景。
- 在公开和专有数据集上（数百万交互）验证了算法的效率和可扩展性。
- 展示了DSV在电子商务推荐任务中识别有影响力数据点的实际应用，包括识别危险产品和提升生态可持续性。

### 研究方法

论文提出KMC-Shapley算法，用于在邻域推荐中可扩展地估计数据Shapley值。算法针对稀疏交互数据设计，可能结合了KMC（Kernel Mean Clustering？）和Shapley值估计技术。具体技术路线包括：利用邻域方法（如基于物品的协同过滤）作为推荐模型，通过采样或近似方法高效计算Shapley值，并在大规模数据集上验证。

### 关键结果

实验表明，KMC-Shapley算法在包含数百万交互的公开和专有数据集上具有高效性和可扩展性。DSV能够识别电子商务推荐任务中有影响力的数据点，并应用于识别危险产品或改善生态可持续性。

### 技术栈

- 数据Shapley值（Data Shapley value）
- KMC-Shapley算法
- 邻域推荐方法（neighborhood-based recommendation）
- 稀疏交互数据（sparse interaction data）

### 方法优势

- 针对推荐系统中数据调试问题，提出可扩展的DSV计算方法，具有实际应用价值。
- 算法在真实大规模数据集上验证，展示了效率和可扩展性。
- 应用场景明确，包括识别危险产品和生态可持续性，具有社会意义。

### 主要局限

- 论文局限：摘要未提及具体实验细节，如基线比较、消融研究等。当前证据局限：仅基于摘要，无法评估算法在更多场景下的表现，也无法确认其与现有方法的优劣。

### 与当前研究方向的关联

论文涉及推荐系统、数据调试、数据重要性、可扩展算法，与关键词中的推荐系统、鲁棒性、工业落地高度相关。

## 代码与复现

- [bkersbergen/illoominate](https://github.com/bkersbergen/illoominate)：official，置信度 100，Stars 4

---

_知识库更新时间：2026-08-24T02:13:54.085781_
