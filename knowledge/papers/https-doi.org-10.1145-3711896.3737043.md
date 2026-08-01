---
title: "Measure Domain&apos;s Gap: A Similar Domain Selection Principle for Multi-Domain Recommendation"
paper_id: "https://doi.org/10.1145/3711896.3737043"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 20.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Topic Modeling"]
---

# Measure Domain&apos;s Gap: A Similar Domain Selection Principle for Multi-Domain Recommendation

[查看原文](https://dblp.org/rec/conf/kdd/00010XLJW0000Z025) · [ArXiv](https://arxiv.org/abs/2505.20227) · [Semantic Scholar](https://www.semanticscholar.org/paper/f3b3ff7510b743aaab8aaedfa0fc3a4be39049c0)

## 一句话结论

> 该论文提出一种基于原型距离的相似领域选择原则，用于多领域推荐中动态选择合适领域知识，以缓解负迁移问题，并在三个数据集上验证了有效性。

## 论文信息

- **作者**：Yi Wen, Yue Liu, Derong Xu, Huishi Luo, Pengyue Jia, Yiqing Wu, Siwei Wang, Ke Liang, Maolin Wang, Yiqi Wang, Fuzhen Zhuang, Xiangyu Zhao
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：20.0
- **DOI**：[https://doi.org/10.1145/3711896.3737043](https://doi.org/10.1145/3711896.3737043)

<details open>
<summary><strong>中文摘要</strong></summary>

多域推荐（Multi-Domain Recommendation, MDR）通过有效利用不同域之间的迁移信息，实现了理想的推荐性能。尽管取得了巨大成功，但现有的大多数MDR方法采用单一结构来迁移复杂的域共享知识。然而，有益的迁移信息在不同域之间应有所差异。当域之间存在知识冲突或某个域质量较差时，不加选择地利用所有域的信息将导致严重的负迁移问题（Negative Transfer Problem, NTP）。因此，如何有效建模域之间的复杂迁移关系以避免NTP，仍是一个值得探索的方向。为解决这些问题，本文提出了一种简单且动态的相似域选择原则（Similar Domain Selection Principle, SDSP），用于多域推荐。SDSP首次探索了为每个域选择合适域知识以缓解NTP的方法。具体而言，我们提出了一种新颖的基于原型的域距离度量，以有效建模域之间的复杂关系。随后，所提出的SDSP能够基于域指标的监督信号以及从学习到的域原型中获得的非监督距离度量，动态地为每个域找到相似域。我们强调，SDSP是一种轻量级方法，可以与现有MDR方法结合使用以获得更好的性能，同时不会引入过多的时间开销。据我们所知，这是MDR领域中首个能够显式度量域级差距并动态选择合适域的解决方案。在三个数据集上的大量实验证明了我们提出方法的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multi-Domain Recommendation (MDR) achieves the desirable recommendation performance by effectively utilizing the transfer information across different domains. Despite the great success, most existing MDR methods adopt a single structure to transfer complex domain-shared knowledge. However, the beneficial transferring information should vary across different domains. When there is knowledge conflict between domains or a domain is of poor quality, unselectively leveraging information from all domains will lead to a serious Negative Transfer Problem (NTP). Therefore, how to effectively model the complex transfer relationships between domains to avoid NTP is still a direction worth exploring. To address these issues, we propose a simple and dynamic Similar Domain Selection Principle (SDSP) for multi-domain recommendation in this paper. SDSP presents the initial exploration of selecting suitable domain knowledge for each domain to alleviate NTP. Specifically, we propose a novel prototype-based domain distance measure to effectively model the complexity relationship between domains. Thereafter, the proposed SDSP can dynamically find similar domains for each domain based on the supervised signals of the domain metrics and the unsupervised distance measure from the learned domain prototype. We emphasize that SDSP is a lightweight method that can be incorporated with existing MDR methods for better performance while not introducing excessive time overheads. To the best of our knowledge, it is the first solution that can explicitly measure domain-level gaps and dynamically select appropriate domains in the MDR field. Extensive experiments on three datasets demonstrate the effectiveness of our proposed method.

</details>

---

_知识库更新时间：2026-08-01T04:05:05.966268_
