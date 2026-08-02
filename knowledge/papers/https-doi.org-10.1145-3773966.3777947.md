---
title: "利用检索增强语言模型实现对话式推荐系统中的精准物品/特征选择"
paper_id: "https://doi.org/10.1145/3773966.3777947"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 51.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Recommender Systems and Techniques", "Explainable Artificial Intelligence (XAI)"]
---

# 利用检索增强语言模型实现对话式推荐系统中的精准物品/特征选择

> **英文原标题**：Leveraging Retrieval-Augmented Language Models for Accurate Item/Feature Selection in Conversational Recommender Systems

[查看原文](https://dblp.org/rec/conf/wsdm/0003KSK26)

## 一句话结论

> 本文提出MOCHA框架，通过多阶段物品/特征选择与思维链推理增强检索增强语言模型，显著提升对话式推荐系统的推荐准确性和解释质量。

## 论文信息

- **作者**：Taeho Kim, Junpyo Kim, Won-Yong Shin, Sang-Wook Kim
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：51.0
- **DOI**：[https://doi.org/10.1145/3773966.3777947](https://doi.org/10.1145/3773966.3777947)

<details open>
<summary><strong>中文摘要</strong></summary>

对话式推荐系统（CRSs）旨在基于与用户的对话，提供个性化的物品推荐并附带解释。尽管语言模型（LMs）的进步促进了CRSs的发展，但当LMs缺乏关于物品特征的充分知识时，仍存在局限性，而这些特征对于准确的推荐和恰当的解释至关重要。为缓解这一问题，引入了检索增强语言模型（RALMs）；然而，它们带来了新的挑战：检索到的段落中可能包含相关性较低的知识。为解决这一局限，我们提出了一种新颖的CRS框架——MOCHA，该框架通过结合思维链（CoT）推理的多阶段物品/特征选择来增强RALMs。具体而言，MOCHA首先选择待推荐的物品，然后选择用于解释其推荐理由的特征，从而系统地识别相关知识；每一步选择均通过CoT推理完成。在两个公开的CRS数据集上的实验结果表明，MOCHA显著提升了推荐准确性，并为推荐物品提供了信息丰富且事实准确的解释。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Conversational recommender systems (CRSs) aim to provide personalized item recommendations along with explanations based on the conversations with users. While advancements in language models (LMs) have facilitated CRSs, limitations remain when LMs lack sufficient knowledge about item features that are essential for accurate recommendations and appropriate explanations. To alleviate this issue, retrieval-augmented language models (RALMs) have been introduced; however, they introduce a new challenge: the inclusion of less-relevant knowledge in retrieved passages. To address this limitation, we propose a novel CRS framework, MOCHA, which enhances RALMs through a multi-stage item/feature selection with Chain-of-Thought (CoT) reasoning. Specifically, MOCHA systematically identifies relevant knowledge by first selecting the item to recommend and then selecting its features to explain; each selection is performed via CoT reasoning. Experimental results on two public CRS datasets demonstrate that MOCHA significantly improves the recommendation accuracy, and provides informative and factually-correct explanations for the recommended items.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

对话式推荐系统旨在通过与用户的对话提供个性化物品推荐和解释。尽管语言模型的发展促进了对话式推荐系统，但当语言模型缺乏关于物品特征的知识时，其推荐准确性和解释适当性受限。为此，检索增强语言模型被引入，但带来了检索段落中包含不相关知识的挑战。针对此问题，本文提出了一种新颖的对话式推荐系统框架MOCHA，通过多阶段物品/特征选择结合思维链推理来增强检索增强语言模型。具体而言，MOCHA首先选择要推荐的物品，然后选择其解释特征，每次选择均通过思维链推理进行。在两个公开的对话式推荐数据集上的实验结果表明，MOCHA显著提高了推荐准确性，并为推荐物品提供了信息丰富且事实正确的解释。

### 主要创新

- 提出MOCHA框架，将多阶段物品/特征选择与思维链推理相结合，以增强检索增强语言模型在对话式推荐中的表现。
- 通过先选择物品再选择特征的两阶段选择策略，系统性地识别相关知识，减少不相关检索段落的影响。
- 利用思维链推理进行选择，提高了推荐和解释的准确性和可解释性。
- 在多个公开数据集上验证了方法的有效性，显著提升了推荐准确性和解释质量。

### 研究方法

本文提出MOCHA框架，其核心是多阶段物品/特征选择与思维链推理。具体技术路线为：首先，利用检索增强语言模型获取相关段落；然后，通过思维链推理，第一阶段选择要推荐的物品，第二阶段选择该物品的特征用于解释；最后，基于选择的物品和特征生成推荐和解释。实验在两个公开的对话式推荐数据集上进行，评估推荐准确性和解释质量。

### 关键结果

实验结果表明，MOCHA显著提高了推荐准确性，并提供了信息丰富且事实正确的解释。具体数值在摘要中未提供。

### 技术栈

- 摘要中未提供具体算法、工具或数学方法。

### 方法优势

- 提出了一种新颖的框架，有效解决了检索增强语言模型中不相关知识的问题。
- 通过多阶段选择和思维链推理，提高了推荐和解释的准确性和可解释性。
- 在多个数据集上验证了方法的有效性，具有较好的泛化能力。

### 主要局限

- 论文局限：摘要未提及。当前证据局限：仅基于摘要，无法评估方法的计算复杂度、对噪声检索的鲁棒性、以及在不同领域或语言上的表现。

### 与当前研究方向的关联

该论文与对话式推荐、检索增强语言模型、思维链推理、物品/特征选择等关键词高度相关。它聚焦于对话式推荐系统中的推荐准确性和解释生成，通过检索增强和推理技术提升性能，符合对话式推荐和LLM结合推荐系统的研究方向。

## 代码与复现

- [HAI-UESTC/LLM-for-Conversational-Recommender-Systems](https://github.com/HAI-UESTC/LLM-for-Conversational-Recommender-Systems)：possible，置信度 30，Stars 3
- [BIAOBIAO12138/LLM-for-Conversational-Recommender-Systems](https://github.com/BIAOBIAO12138/LLM-for-Conversational-Recommender-Systems)：possible，置信度 30，Stars 0

---

_知识库更新时间：2026-08-02T04:11:29.700883_
