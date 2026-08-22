---
title: "探索大语言模型在推荐系统中意外发现评估的潜力"
paper_id: "https://doi.org/10.1145/3705328.3748167"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 41.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Intelligent Tutoring Systems and Adaptive Learning"]
---

# 探索大语言模型在推荐系统中意外发现评估的潜力

> **英文原标题**：Exploring the Potential of LLMs for Serendipity Evaluation in Recommender Systems

[查看原文](https://dblp.org/rec/conf/recsys/KangZC25) · [Semantic Scholar](https://www.semanticscholar.org/paper/a78b1f6262d280a19bf04f733086c3a08ae0900c)

## 一句话结论

> 本文探索了LLM在推荐系统惊喜度评估中的潜力，发现即使最简单的零样本LLM也能达到或超越传统代理指标，且多LLM技术和辅助数据能进一步提升与人类感知的一致性。

## 论文信息

- **作者**：Li Kang, Yuhan Zhao, Li Chen
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：41.0
- **DOI**：[https://doi.org/10.1145/3705328.3748167](https://doi.org/10.1145/3705328.3748167)

<details open>
<summary><strong>中文摘要</strong></summary>

偶然性在推荐系统中对提升用户满意度起着关键作用，然而由于其固有的主观性和概念模糊性，对其评估面临重大挑战。当前的算法方法主要依赖代理指标进行间接评估，往往无法与真实用户感知对齐，从而形成差距。随着大语言模型（LLMs）日益革新各种人工标注任务的评估方法，我们受到启发，探索一个核心研究命题：LLMs能否有效模拟人类用户进行偶然性评估？为回答此问题，我们在源自电子商务和电影领域真实用户研究的两个数据集上开展元评估，聚焦三个关键方面：LLMs相较于传统代理指标的准确性、辅助数据对LLM理解的影响，以及近期流行的多LLM技术的有效性。我们的研究结果表明，即便最简单的零样本LLMs也能达到或超越传统指标的性能。此外，多LLM技术和辅助数据的引入进一步增强了与人类视角的一致性。基于我们的发现，LLMs的最优评估与用户研究结果相比，皮尔逊相关系数达到21.5%。本研究暗示LLMs可能作为潜在准确且成本效益高的评估器，为推荐系统中的偶然性评估引入新范式。我们的代码公开于 https://github.com/Leah-HKBU/SerenEva。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Serendipity plays a pivotal role in enhancing user satisfaction within recommender systems, yet its evaluation poses significant challenges due to its inherently subjective nature and conceptual ambiguity. Current algorithmic approaches predominantly rely on proxy metrics for indirect assessment, often failing to align with real user perceptions, thus creating a gap. With large language models (LLMs) increasingly revolutionizing evaluation methodologies across various human annotation tasks, we are inspired to explore a core research proposition: Can LLMs effectively simulate human users for serendipity evaluation? To address this question, we conduct a meta-evaluation on two datasets derived from real user studies in the e-commerce and movie domains, focusing on three key aspects: the accuracy of LLMs compared to conventional proxy metrics, the influence of auxiliary data on LLM comprehension, and the efficacy of recently popular multi-LLM techniques. Our findings indicate that even the simplest zero-shot LLMs achieve parity with, or surpass, the performance of conventional metrics. Furthermore, multi-LLM techniques and the incorporation of auxiliary data further enhance alignment with human perspectives. Based on our findings, the optimal evaluation by LLMs yields a Pearson correlation coefficient of 21.5% when compared to the results of the user study. This research implies that LLMs may serve as potentially accurate and cost-effective evaluators, introducing a new paradigm for serendipity evaluation in recommender systems. Our code is publicly available at https://github.com/Leah-HKBU/SerenEva.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

意外发现（Serendipity）在推荐系统中对提升用户满意度至关重要，但其评估因主观性和概念模糊性而具有挑战性。现有算法方法主要依赖代理指标进行间接评估，往往与真实用户感知不一致。随着大语言模型（LLMs）在人类标注任务中的评估方法上带来革命，本文探讨核心问题：LLMs能否有效模拟人类用户进行意外发现评估？为此，我们在电商和电影领域的两个真实用户研究数据集上进行元评估，关注三个方面：LLMs与传统代理指标的准确性对比、辅助数据对LLM理解的影响、以及近期流行的多LLM技术的有效性。研究发现，即使最简单的零样本LLM也能达到或超越传统指标的性能。此外，多LLM技术和辅助数据的加入进一步提升了与人类视角的一致性。基于研究结果，LLM评估与用户研究结果的皮尔逊相关系数最高达21.5%。这表明LLMs可能成为准确且成本效益高的评估器，为推荐系统中的意外发现评估引入新范式。代码已公开。

### 主要创新

- 首次系统性地探索LLMs在意外发现评估中的潜力，提出核心研究命题：LLMs能否模拟人类用户进行意外发现评估。
- 在两个真实用户研究数据集（电商和电影领域）上进行元评估，比较LLMs与传统代理指标的准确性。
- 分析辅助数据对LLM理解意外发现的影响，以及多LLM技术（如集成方法）在提升评估一致性方面的有效性。
- 发现零样本LLM即可达到或超越传统指标，且多LLM技术和辅助数据能进一步提升与人类感知的一致性。
- 提出LLMs作为准确且成本效益高的评估器的新范式，并公开代码以促进可复现性。

### 研究方法

论文采用元评估方法，在两个真实用户研究数据集（电商和电影领域）上，比较LLMs与传统代理指标在意外发现评估中的准确性。研究关注三个关键方面：LLMs的准确性、辅助数据的影响、以及多LLM技术的有效性。实验设计包括零样本LLM、引入辅助数据的LLM、以及多LLM集成技术，并与用户研究结果进行对比，使用皮尔逊相关系数衡量一致性。

### 关键结果

最简单的零样本LLM在意外发现评估中达到或超越传统代理指标的性能。多LLM技术和辅助数据的加入进一步提升了与人类视角的一致性。最优的LLM评估与用户研究结果的皮尔逊相关系数为21.5%。

### 技术栈

- 摘要未提供具体算法、工具或数学方法的细节。仅提及使用大语言模型（LLMs）、零样本（zero-shot）设置、多LLM技术（multi-LLM techniques）、皮尔逊相关系数（Pearson correlation coefficient）作为评估指标。

### 方法优势

- 研究问题具有创新性，探索LLMs在意外发现评估中的潜力，填补了现有代理指标与用户感知之间的差距。
- 在两个不同领域（电商和电影）的真实用户研究数据集上进行元评估，增强了结论的泛化性。
- 系统性地分析了辅助数据和多LLM技术的影响，提供了全面的评估视角。
- 发现零样本LLM即可达到或超越传统指标，表明LLMs具有成本效益和实用性。
- 公开代码，促进可复现性和后续研究。

### 主要局限

- 论文局限：摘要未提及具体局限性，但可能包括LLM评估的固有偏差、数据集规模有限、以及皮尔逊相关系数21.5%表明仍有较大提升空间。当前证据局限：由于仅提供摘要，无法获取具体实验细节、数据集规模、基线模型、消融实验等，因此无法全面评估方法的稳健性和局限性。

### 与当前研究方向的关联

该论文与推荐系统、LLM与推荐系统结合、用户建模、评估方法等关键词高度相关。具体而言，它聚焦于推荐系统中的意外发现评估，利用LLMs模拟用户感知，属于LLM在推荐系统评估中的应用，同时涉及用户建模（用户感知）和推荐系统评估（元评估）。

## 代码与复现

- [Leah-HKBU/SerenEva](https://github.com/Leah-HKBU/SerenEva)：official，置信度 100，Stars 2

---

_知识库更新时间：2026-08-22T02:17:50.832977_
