---
title: "A Media Content Recommendation Method for Playlist Curators using LLM-Based Query Expansion"
paper_id: "https://doi.org/10.1145/3705328.3748129"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 34.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Video Analysis and Summarization", "Data Mining Algorithms and Applications"]
---

# A Media Content Recommendation Method for Playlist Curators using LLM-Based Query Expansion

[查看原文](https://dblp.org/rec/conf/recsys/HagioYOOF25) · [Semantic Scholar](https://www.semanticscholar.org/paper/785f67925a7a1ee669161a3090ef2432954a30a8)

## 一句话结论

> 本文提出一种基于LLM查询扩展的媒体内容推荐方法，通过将播放列表主题扩展为多个查询并利用向量检索，显著提升了推荐精度（P@10从0.79提升至0.98，P@50提升22个百分点）。

## 论文信息

- **作者**：Yuta Hagio, Chigusa Yamamura, Hiromu Ogawa, Hisayuki Ohmata, Arisa Fujii
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：34.0
- **DOI**：[https://doi.org/10.1145/3705328.3748129](https://doi.org/10.1145/3705328.3748129)

<details open>
<summary><strong>中文摘要</strong></summary>

播放列表策划是媒体内容发现服务中的关键因素，然而，由于手动构建查询耗时费力，策展人难以找到多样且相关的内容。我们提出了一种方法，利用大型语言模型（LLM）将播放列表主题扩展为多个多样化的查询。这些扩展查询的向量与原始主题向量一起，通过向量搜索检索候选内容。针对日本电视节目的实验表明，我们的方法在精度上显著优于仅使用主题向量的基线，将Precision@10从0.79提升至0.98，并将P@50提高了22个百分点。该方法提升了策展效率，并通过提供更准确、更多样的推荐改善了播放列表质量。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Playlist curation is a key factor in media content discovery services, yet finding diverse, relevant content is challenging for curators due to time-consuming manual query crafting. We propose a method where a large language model (LLM) expands a playlist theme into multiple diverse queries. Vectors from these expanded queries, along with the original theme vector, retrieve candidates via vector search. Experiments on Japanese TV programs show our method significantly improves precision over a theme-vector baseline, boosting Precision@10 from 0.79 to 0.98 and increasing P@50 by 22 percentage points. This approach enhances curator efficiency and improves playlist quality by delivering more accurate and diverse recommendations.

</details>

---

_知识库更新时间：2026-08-13T03:13:27.030153_
