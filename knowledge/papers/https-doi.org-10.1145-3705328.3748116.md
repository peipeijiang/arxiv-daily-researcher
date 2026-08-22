---
title: "Scaling Retrieval for Web-Scale Recommenders: Lessons from Inverted Indexes to Embedding Search"
paper_id: "https://doi.org/10.1145/3705328.3748116"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 16.0
tags: ["paper", "recommender-systems", "Advanced Image and Video Retrieval Techniques", "Data Management and Algorithms", "Recommender Systems and Techniques"]
---

# Scaling Retrieval for Web-Scale Recommenders: Lessons from Inverted Indexes to Embedding Search

[查看原文](https://dblp.org/rec/conf/recsys/JuanSZSJSHZ25) · [Semantic Scholar](https://www.semanticscholar.org/paper/3bd4543e3ccdb54af437505e50bc86af9cdd3daf)

## 一句话结论

> 本文总结了LinkedIn从倒排索引到GPU嵌入检索的检索层演进过程，提供了构建可扩展、灵活检索系统的实践经验和教训。

## 论文信息

- **作者**：Yu-Chin Juan, Jiacong Shen, S. Zhang, Qianqi Shen, Caleb Johnson, Luke Simon, Liangjie Hong, Wenjing Zhang
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：16.0
- **DOI**：[https://doi.org/10.1145/3705328.3748116](https://doi.org/10.1145/3705328.3748116)

<details open>
<summary><strong>中文摘要</strong></summary>

网络规模的搜索和推荐系统依赖于高效的检索来管理海量数据集和用户流量。本文记录了我们在LinkedIn构建检索层的演进路径，从基于CPU的倒排索引系统发展到GPU加速的基于嵌入的检索系统。最初以传统的基于术语的检索为基础，我们通过生成推断属性之间的映射，利用学习检索的方法提升了相关性和生产力。随着这些早期努力在大规模推断和匹配属性方面遇到限制，我们转向基于嵌入的检索以获得更大的灵活性和性能，但发现现有基础设施无法支持大规模生产需求。这促使我们开发了一种基于GPU的检索系统，专为高性能、灵活建模和多目标业务优化而设计。我们展示了这一转变过程中的基础设施创新、优化以及关键经验教训，为构建可扩展、灵活的检索系统提供了实用见解。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Web-scale search and recommendation systems depend on efficient retrieval to manage massive datasets and user traffic.This paper chronicles our evolutionary path in building the retrieval layer at LinkedIn, progressing from a CPU-based inverted index system to a GPU-accelerated embedding-based retrieval system.Initially anchored by traditional term-based retrieval, we enhanced relevance and productivity through learning-to-retrieve approaches by generating mappings among inferred attributes.As these early efforts encountered limitations in inferring and matching attributes at scale, we transitioned to embedding-based retrieval for greater flexibility and performance, but found that existing infrastructure couldn't support large-scale production needs.This led us to develop a GPUbased retrieval system designed for high performance, flexible modeling, and multi-objective business optimization.We present the infrastructure innovations, optimizations, and key lessons learned throughout this transition, offering practical insights for building scalable, flexible retrieval systems.

</details>

---

_知识库更新时间：2026-08-22T02:17:50.832293_
