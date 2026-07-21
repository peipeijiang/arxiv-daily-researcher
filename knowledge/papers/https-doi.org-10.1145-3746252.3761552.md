---
title: "基于大语言模型增强图变换器的下一代价格推荐"
paper_id: "https://doi.org/10.1145/3746252.3761552"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 39.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Sharing Economy and Platforms", "Advanced Graph Neural Networks"]
---

# 基于大语言模型增强图变换器的下一代价格推荐

> **英文原标题**：Next-Generation Price Recommendation with LLM-Augmented Graph Transformers

[查看原文](https://dblp.org/rec/conf/cikm/AbachiBMAN25) · [Semantic Scholar](https://www.semanticscholar.org/paper/76e5963ab705455e042464c3ead43ce65a45f363)

## 一句话结论

> 该论文提出了一种结合LLM和Graph Transformer的框架，用于Airbnb等双边平台的动态定价，通过LLM生成元特征并利用图神经网络建模关系，提升了价格推荐的准确性和可解释性。

## 论文信息

- **作者**：Hadi Mohammadzadeh Abachi, Amin Beheshti, Milad Mosharraf, Pooyan Asgari, Majid Namazi
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：39.0
- **DOI**：[https://doi.org/10.1145/3746252.3761552](https://doi.org/10.1145/3746252.3761552)

<details open>
<summary><strong>中文摘要</strong></summary>

在Airbnb等双边平台上，由于房源异质性、用户行为差异以及情境变量的复杂性，动态定价面临诸多挑战。本文提出了一种稳健且可解释的定价框架，利用大语言模型（LLMs）与提示工程（prompt engineering），从非结构化与结构化的房源数据中自动生成高层元特征（meta-features）。这些元特征旨在捕捉传统特征工程流程常忽略的细微语义特征。我们进一步将这些表征集成到基于Transformer的图神经网络（Graph Neural Network, GNN）中，该网络以数据驱动及多种关系构建方式，对房源之间的关联与空间依赖关系进行建模。通过将提示驱动嵌入（prompt-driven embeddings）与图感知上下文学习相结合，我们的框架显著提升了价格推荐准确性，并通过同质性分析（assortativity analysis）提供了可解释性。基于真实Airbnb数据集的大量实验表明，该方法在预测性能、跨邻域未见数据的泛化能力以及输出可解释性方面均表现优异。本研究凸显了将大语言模型、结构化图学习与可解释人工智能相统一，以构建下一代动态定价系统的潜力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Dynamic pricing on two-sided platforms such as Airbnb presents complex challenges due to the heterogeneity of listings, user behaviours, and contextual variables. In this work, we propose a robust and interpretable pricing framework that leverages Large Language Models (LLMs) and prompt engineering to automate the generation of high-level meta-features from unstructured and structured listing data. These meta-features are designed to capture nuanced semantic features that are often overlooked by traditional feature engineering pipelines. We further integrate these representations into a Transformer-based Graph Neural Network (GNN), which models the relational and spatial dependencies between listings in a data-driven and several relation-construction manner. By combining prompt-driven embeddings with graph-aware contextual learning, our framework significantly enhances price recommendation accuracy while offering transparency through assortativity analysis. Extensive experiments on real-world Airbnb datasets demonstrate our approach's performance in both prediction and unseen data across neighbourhoods and output interpretability. This work highlights the potential of unifying LLMs, structured graph learning, and interpretable AI for next-generation dynamic pricing systems.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对Airbnb等双边平台动态定价的复杂性，提出了一种鲁棒且可解释的定价框架。该框架利用大语言模型（LLM）和提示工程，从非结构化与结构化房源数据中自动生成高级元特征，捕捉传统特征工程忽略的语义信息。进一步将这些表示集成到基于Transformer的图神经网络（GNN）中，以数据驱动的方式建模房源间的关联和空间依赖。通过结合提示驱动嵌入与图感知上下文学习，框架在提升价格推荐准确性的同时，通过同质性分析提供透明度。在真实Airbnb数据集上的实验表明，该方法在预测性能、跨邻域未见数据泛化及输出可解释性方面表现优异。

### 主要创新

- 利用LLM和提示工程自动生成高级元特征，捕捉传统方法忽略的语义特征。
- 将LLM生成的嵌入与Transformer-based GNN结合，建模房源间的关联和空间依赖。
- 通过同质性分析提供模型透明度，增强可解释性。
- 提出统一LLM、结构化图学习和可解释AI的下一代动态定价系统框架。

### 研究方法

首先，使用LLM和提示工程从非结构化与结构化房源数据中自动生成高级元特征。然后，将这些元特征作为输入，集成到基于Transformer的图神经网络（GNN）中，该网络以数据驱动的方式建模房源间的多种关系。最后，通过结合提示驱动嵌入与图感知上下文学习进行价格推荐，并利用同质性分析实现可解释性。

### 关键结果

在真实Airbnb数据集上，所提框架在价格推荐准确性上显著提升。；在未见过的跨邻域数据上表现良好，具有良好的泛化能力。；输出具有可解释性，通过同质性分析提供透明度。

### 技术栈

- 大语言模型（LLM）
- 提示工程（Prompt Engineering）
- Transformer
- 图神经网络（GNN）
- 同质性分析（Assortativity Analysis）

### 方法优势

- 创新性地融合LLM与图神经网络，提升特征质量和模型性能。
- 通过同质性分析增强可解释性，便于实际应用。
- 在真实数据集上验证了有效性和泛化能力。
- 框架设计鲁棒，适用于异构和动态环境。

### 主要局限

- 论文局限：摘要未提及模型的计算复杂度或实时性要求。
- 当前证据局限：仅基于摘要，缺乏具体实验细节、数据集名称、基线对比和消融研究。

### 与当前研究方向的关联

该论文高度相关于LLM与推荐系统结合、生成式推荐、可解释推荐等关键词，同时涉及用户建模和工业落地（动态定价）。但未涉及序列推荐、多模态推荐、对话式推荐、排序重排、CTR/CVR预测、因果性、公平性等关键词。

---

_知识库更新时间：2026-07-21T04:03:10.446852_
