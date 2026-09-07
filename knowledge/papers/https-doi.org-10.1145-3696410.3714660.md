---
title: "查询中蕴含什么：基于极性感知的分布公平排序"
paper_id: "https://doi.org/10.1145/3696410.3714660"
source: "www"
published: "2025-01-01T00:00:00"
score: 46.0
tags: ["paper", "recommender-systems", "Auction Theory and Applications", "Privacy-Preserving Technologies in Data", "Mobile Crowdsensing and Crowdsourcing"]
---

# 查询中蕴含什么：基于极性感知的分布公平排序

> **英文原标题**：What&apos;s in a Query: Polarity-Aware Distribution-Based Fair Ranking

[查看原文](https://dblp.org/rec/conf/www/BalagopalanWSBG25)

## 一句话结论

> 该论文提出基于分布散度的公平排名度量DistFaiR，在序列查询下实现个体公平，并证明个体公平有助于群体公平，同时指出忽略查询信息可能导致公平washing风险。

## 论文信息

- **作者**：Aparna Balagopalan, K.S. Wang, Olawale Salaudeen, Asia J. Biega, Marzyeh Ghassemi
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：46.0
- **DOI**：[https://doi.org/10.1145/3696410.3714660](https://doi.org/10.1145/3696410.3714660)

<details open>
<summary><strong>中文摘要</strong></summary>

机器学习驱动的排名系统根据查询对个体（或项目）进行排序，在多种安全关键场景中调节着搜索曝光度或注意力分配。因此，确保此类排名具有公平性至关重要。在机会均等的目标下，排名界面上分配给个体的注意力应与其在各类搜索查询中的相关性成正比。在本研究中，我们探讨了摊销式公平排名——即将相关性和注意力在一系列用户查询中累积起来，以使公平排名在实践中更具可行性。与先前基于每个个体期望摊销注意力的方法不同，我们定义了新的基于散度的排名注意力分布公平性度量（DistFaiR），将不公平性刻画为个体随时间变化的注意力分布与相关性分布之间的散度。这使我们能够提出新的不公平性定义，这些定义在测试阶段更为可靠。其次，我们证明在该定义下，对于一类有用的散度度量，群体公平性以个体公平性为上界，并通过实验表明，通过基于整数线性规划的优化来最大化个体公平性，通常对群体公平性也有益。最后，我们发现先前在摊销式公平排名方面的研究忽略了关于查询的关键信息，这可能导致实践中出现“公平洗白”风险，即排名看似比实际更加公平。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Machine learning-driven rankings, where individuals (or items) are ranked in response to a query, mediate search exposure or attention in a variety of safety-critical settings. Thus, it is important to ensure that such rankings are fair. Under the goal of equal opportunity, attention allocated to an individual on a ranking interface should be proportional to their relevance across search queries. In this work, we examine amortized fair ranking -- where relevance and attention are cumulated over a sequence of user queries to make fair ranking more feasible in practice. Unlike prior methods that operate on expected amortized attention for each individual, we define new divergence-based measures for attention distribution-based fairness in ranking (DistFaiR), characterizing unfairness as the divergence between the distribution of attention and relevance corresponding to an individual over time. This allows us to propose new definitions of unfairness, which are more reliable at test time. Second, we prove that group fairness is upper-bounded by individual fairness under this definition for a useful class of divergence measures, and experimentally show that maximizing individual fairness through an integer linear programming-based optimization is often beneficial to group fairness. Lastly, we find that prior research in amortized fair ranking ignores critical information about queries, potentially leading to a fairwashing risk in practice by making rankings appear more fair than they actually are.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文研究机器学习驱动的排序系统在安全关键场景中的公平性问题，提出在用户查询序列上实现摊销公平排序的新方法。现有方法基于每个个体的期望摊销注意力，而本文定义了新的基于散度的注意力分布公平性度量（DistFaiR），将不公平性刻画为个体注意力分布与相关性分布之间的散度，从而提出更可靠的测试时公平性定义。作者证明在特定散度类下，群体公平性受个体公平性上界约束，并通过整数线性规划优化个体公平性，实验表明这通常有利于群体公平性。此外，文章指出先前摊销公平排序研究忽略了查询的关键信息，可能导致公平洗涤风险，使排名看似更公平而实际并非如此。

### 主要创新

- 提出基于散度的注意力分布公平性度量（DistFaiR），将不公平性定义为个体注意力与相关性分布的散度，而非仅期望值。
- 提出新的不公平性定义，在测试时更可靠。
- 证明在特定散度类下，群体公平性受个体公平性上界约束。
- 通过整数线性规划优化个体公平性，并实验显示对群体公平性有益。
- 揭示先前摊销公平排序忽略查询信息可能导致公平洗涤风险。

### 研究方法

论文采用理论分析与实验验证相结合的方法。首先定义基于散度的分布公平性度量，然后推导群体公平性与个体公平性的理论关系，最后通过整数线性规划实现个体公平性优化，并在实验中验证其对群体公平性的影响。

### 关键结果

提出新的分布公平性度量，比期望注意力方法更可靠。；证明群体公平性受个体公平性上界约束（针对特定散度类）。；实验表明最大化个体公平性通常有利于群体公平性。；发现先前方法忽略查询信息可能导致公平洗涤风险。

### 技术栈

- 摘要未提供具体算法、工具或数学方法的细节，仅提及散度度量、整数线性规划。

### 方法优势

- 提出新颖的分布公平性视角，超越期望注意力。
- 理论证明群体公平与个体公平的关系，具有理论贡献。
- 实验验证优化个体公平对群体公平的积极影响。
- 揭示公平洗涤风险，对实践有警示意义。

### 主要局限

- 论文局限：摘要未提及具体实验设置、数据集或基线，无法评估实证强度。当前证据局限：仅基于摘要，缺乏方法细节和完整结果，无法全面评估。

### 与当前研究方向的关联

论文与推荐系统公平性高度相关，涉及排序与重排、用户查询建模、公平性度量与优化，属于推荐系统公平性研究范畴。

---

_知识库更新时间：2026-09-07T05:05:20.798884_
