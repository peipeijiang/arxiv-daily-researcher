---
title: "Cumulated gain-based evaluation of IR techniques"
paper_id: "https://doi.org/10.1145/582415.582418"
source: "citation"
published: "2002-10-01T00:00:00"
score: 8.0
tags: ["paper", "recommender-systems", "Information Retrieval and Search Behavior", "Data Management and Algorithms", "Expert finding and Q&A systems"]
---

# Cumulated gain-based evaluation of IR techniques

[查看原文](https://doi.org/10.1145/582415.582418)

## 一句话结论

> 该论文提出了基于累积增益的评估指标（CG、DCG、NDCG），用于在分级相关性判断下评估信息检索系统的排序效果，实验表明这些指标能有效反映系统检索高度相关文档的能力。

## 论文信息

- **作者**：Kalervo Järvelin, Jaana Kekäläinen
- **来源**：ACM Transactions on Information Systems
- **发布时间**：2002-10-01
- **相关度评分**：8.0
- **DOI**：[https://doi.org/10.1145/582415.582418](https://doi.org/10.1145/582415.582418)

<details open>
<summary><strong>中文摘要</strong></summary>

现代大型检索环境往往因其庞大的输出量使用户感到不知所措。由于所有文档对用户的相关性并不相同，因此应识别出高度相关的文档并将其排在首位进行展示。为了朝这一方向发展信息检索（IR）技术，有必要开发能够对信息检索方法检索高度相关文档的能力予以肯定的评估途径与方法。这可以通过将基于二元相关性判断的传统评估方法（即召回率和精确率）扩展到分级相关性判断来实现。或者，也可以开发基于分级相关性判断的新型度量方法。本文提出了几种新型度量方法，用于计算用户在检查检索结果至给定排序位置时所获得的累积增益。第一种方法沿排序结果列表累积所检索文档的相关性得分。第二种方法类似，但对相关性得分应用折扣因子，以降低后期检索文档的价值。第三种方法基于信息检索技术能够产生的累积增益，计算其相对于理想性能的表现。本文对这些新型度量方法进行了定义和讨论，并通过使用TREC数据的案例研究展示了其应用：针对TREC-7中20个查询的系统运行结果样本。作为相关性基础，我们采用了四级量表的新型分级相关性判断。测试结果表明，所提出的度量方法能够肯定信息检索方法在检索高度相关文档方面的能力，并允许对有效性差异进行统计显著性检验。基于这些度量方法绘制的图表还能深入揭示信息检索技术的性能，并允许从用户角度等进行解读。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern large retrieval environments tend to overwhelm their users by their large output. Since all documents are not of equal relevance to their users, highly relevant documents should be identified and ranked first for presentation. In order to develop IR techniques in this direction, it is necessary to develop evaluation approaches and methods that credit IR methods for their ability to retrieve highly relevant documents. This can be done by extending traditional evaluation methods, that is, recall and precision based on binary relevance judgments, to graded relevance judgments. Alternatively, novel measures based on graded relevance judgments may be developed. This article proposes several novel measures that compute the cumulative gain the user obtains by examining the retrieval result up to a given ranked position. The first one accumulates the relevance scores of retrieved documents along the ranked result list. The second one is similar but applies a discount factor to the relevance scores in order to devaluate late-retrieved documents. The third one computes the relative-to-the-ideal performance of IR techniques, based on the cumulative gain they are able to yield. These novel measures are defined and discussed and their use is demonstrated in a case study using TREC data: sample system run results for 20 queries in TREC-7. As a relevance base we used novel graded relevance judgments on a four-point scale. The test results indicate that the proposed measures credit IR methods for their ability to retrieve highly relevant documents and allow testing of statistical significance of effectiveness differences. The graphs based on the measures also provide insight into the performance IR techniques and allow interpretation, for example, from the user point of view.

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

_知识库更新时间：2026-08-11T02:42:36.425547_
