---
title: "利用用户搜索行为的生成式意图预测的序列推荐"
paper_id: "https://doi.org/10.1145/3773966.3779363"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 40.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Information Retrieval and Search Behavior", "Advanced Bandit Algorithms Research"]
---

# 利用用户搜索行为的生成式意图预测的序列推荐

> **英文原标题**：Sequential Recommendation with Generative Intent Prediction Utilizing User Search-Behavior

[查看原文](https://dblp.org/rec/conf/wsdm/EloviciSRE26) · [Semantic Scholar](https://www.semanticscholar.org/paper/7b69333d620a106493e2d144c4f2cf30be98158b)

## 一句话结论

> 该论文提出一种结合搜索行为的生成式意图预测模型，并将其融入序列推荐框架，以提升推荐准确性，尤其在传统方法失效的场景下表现显著。

## 论文信息

- **作者**：Guy Elovici, Bracha Shapira, Haggai Roitman, Yotam Eshel
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：40.0
- **DOI**：[https://doi.org/10.1145/3773966.3779363](https://doi.org/10.1145/3773966.3779363)

<details open>
<summary><strong>中文摘要</strong></summary>

序列推荐系统在仅依赖历史浏览数据时，往往难以准确预测用户偏好。我们提出了一种将推荐系统与搜索引擎方法相结合的新颖方案，引入了一个生成式意图预测模型，该模型同时利用商品浏览历史与历史搜索查询。通过纳入来自搜索引擎结果页面（SERP）的用户交互数据，该模型得到增强，从而能够生成与实际用户行为更一致的更准确的查询预测。通过将这一意图预测模型以受查询扩展启发的方式整合进序列推荐框架中，我们证明了相较于传统方法，该方法在性能上取得了显著提升，尤其是在传统方法表现不佳的挑战性场景中。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation systems often struggle to accurately predict user preferences when limited to historical browsing data. We present a novel approach that combines recommendation systems with search engine methodologies, introducing a generative intent prediction model that leverages both item view histories and historical search queries. The model is enhanced by incorporating user interaction data from search engine result pages (SERP), leading to more accurate query predictions aligned with actual user behavior. By integrating this intent prediction model into sequential recommendation frameworks through a query expansion-inspired approach, we demonstrate significant performance improvements over traditional methods, particularly in challenging scenarios where conventional approaches fall short.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

序列推荐系统在仅依赖历史浏览数据时，往往难以准确预测用户偏好。本文提出一种结合推荐系统与搜索引擎方法的新颖方法，引入生成式意图预测模型，同时利用物品浏览历史和搜索查询历史。该模型通过整合搜索引擎结果页（SERP）上的用户交互数据得到增强，从而产生更符合实际用户行为的查询预测。通过将意图预测模型以类似查询扩展的方式集成到序列推荐框架中，本文展示了相对于传统方法的显著性能提升，尤其是在传统方法失效的挑战性场景中。

### 主要创新

- 首次将搜索行为数据（包括SERP交互）引入序列推荐中的意图预测。
- 提出生成式意图预测模型，联合建模浏览历史和搜索查询。
- 采用查询扩展启发的集成方式，将意图预测融入序列推荐框架。
- 在传统方法失效的挑战性场景中取得显著性能提升。

### 研究方法

本文提出一种生成式意图预测模型，该模型利用物品浏览历史和搜索查询历史，并整合SERP上的用户交互数据。模型通过生成预测的查询来捕捉用户意图，然后以查询扩展的方式将这些预测集成到序列推荐框架中，以增强推荐性能。

### 关键结果

实验表明，该方法在性能上显著优于传统方法，特别是在传统方法失效的挑战性场景中。

### 技术栈

- 摘要未提供具体算法、工具或数学方法。

### 方法优势

- 创新性地融合了搜索行为数据，为序列推荐提供额外信号。
- 生成式意图预测模型能够更准确地反映用户真实意图。
- 在挑战性场景中表现出显著优势，证明了方法的有效性。

### 主要局限

- 论文局限：摘要未提及具体局限。当前证据局限：仅基于摘要，无法评估模型细节、实验规模、数据集多样性等。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、用户建模等关键词高度相关，同时涉及搜索行为与推荐系统的结合，对推荐智能体、LLM与推荐结合等方向也有启发意义。

---

_知识库更新时间：2026-09-06T04:59:26.700738_
