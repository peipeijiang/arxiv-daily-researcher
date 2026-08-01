---
title: "Campaign-2-PT-RAG：基于LLM引导的语义产品类型归因用于可扩展的活动排名"
paper_id: "https://doi.org/10.1145/3774905.3795730"
source: "www"
published: "2026-01-01T00:00:00"
score: 40.0
tags: ["paper", "recommender-systems", "Sentiment Analysis and Opinion Mining", "Topic Modeling", "Text and Document Classification Technologies"]
---

# Campaign-2-PT-RAG：基于LLM引导的语义产品类型归因用于可扩展的活动排名

> **英文原标题**：Campaign-2-PT-RAG: LLM-Guided Semantic Product Type Attribution for Scalable Campaign Ranking

[查看原文](https://dblp.org/rec/conf/www/CheMGKDVSAKKA26) · [ArXiv](https://arxiv.org/abs/2602.10577) · [Semantic Scholar](https://www.semanticscholar.org/paper/277c4e424353da5dcd6b0539156511f55a7084a6)

## 一句话结论

> 该论文提出Campaign-2-PT-RAG框架，利用LLM和语义搜索将活动内容映射到产品类型，生成高质量训练标签，以提升电商活动排名模型的性能。

## 论文信息

- **作者**：Yiming Che, Mansi Ranjit Mane, K. Gopalakrishnan, Parisa Kaghazgaran, Murali Mohana Krishna Dandu, Archana Venkatachalapathy, Sinduja Subramaniam, Yokila Arora, Evren Korpeoglu, Sushant Kumar, Kannan Achan
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：40.0
- **DOI**：[https://doi.org/10.1145/3774905.3795730](https://doi.org/10.1145/3774905.3795730)

<details open>
<summary><strong>中文摘要</strong></summary>

电商活动排序模型需要大规模的训练标签，用以指示哪些用户是因活动影响而产生购买行为。然而，生成这些标签颇具挑战性，因为活动文案常使用富有创意和主题性的语言，难以直接映射到具体商品购买上。在缺乏清晰商品级归因的情况下，针对活动优化的监督学习始终受限。我们提出了Campaign-2-PT-RAG，一个可扩展的标签生成框架，通过推断每个活动所推广的产品类型（PTs）来构建用户—活动购买标签。该框架首先利用大语言模型（LLMs）解读活动内容，捕捉其隐含意图，随后通过平台分类体系上的语义搜索检索候选产品类型。一个基于结构化LLM的分类器评估每个产品类型的相关性，生成活动专属的商品覆盖集合。用户购买行为若与这些产品类型匹配，则为下游排序模型生成正向训练标签。该方法将模糊的归因问题重构为可处理的语义对齐任务，从而为生产级电商环境中的下游任务（如活动排序优化）提供可扩展且一致的监督信号。在内部及合成数据集上的实验，经专家标注的活动—产品类型映射验证，表明我们的LLM辅助方法能够生成高质量标签，精确率达78%–90%，同时召回率保持在99%以上。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

E-commerce campaign ranking models require large-scale training labels indicating which users purchased due to campaign influence. However, generating these labels is challenging because campaigns use creative, thematic language that does not directly map to product purchases. Without clear product-level attribution, supervised learning for campaign optimization remains limited. We present Campaign-2-PT-RAG, a scalable label generation framework that constructs user--campaign purchase labels by inferring which product types (PTs) each campaign promotes. The framework first interprets campaign content using large language models (LLMs) to capture implicit intent, then retrieves candidate PTs through semantic search over the platform taxonomy. A structured LLM-based classifier evaluates each PT's relevance, producing a campaign-specific product coverage set. User purchases matching these PTs generate positive training labels for downstream ranking models. This approach reframes the ambiguous attribution problem into a tractable semantic alignment task, enabling scalable and consistent supervision for downstream tasks such as campaign ranking optimization in production e-commerce environments. Experiments on internal and synthetic datasets, validated against expert-annotated campaign–PT mappings, show that our LLM-assisted approach generates high-quality labels with 78--90% precision while maintaining over 99% recall.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

电子商务活动排名模型需要大规模训练标签来指示哪些用户因活动影响而购买，但活动使用创意性、主题性语言，难以直接映射到产品购买，导致监督学习受限。本文提出Campaign-2-PT-RAG，一个可扩展的标签生成框架，通过推断活动推广的产品类型（PT）来构建用户-活动购买标签。该框架首先利用大语言模型（LLM）解释活动内容以捕捉隐含意图，然后通过语义搜索在平台分类中检索候选PT，最后使用基于LLM的结构化分类器评估每个PT的相关性，生成活动特定的产品覆盖集。匹配这些PT的用户购买行为为下游排序模型生成正训练标签。该方法将模糊的归因问题转化为可处理的语义对齐任务，为生产环境中的活动排序优化提供可扩展且一致的监督。在内部和合成数据集上的实验，经专家标注的活动-PT映射验证，表明该LLM辅助方法生成高质量标签，精确率达78-90%，召回率超过99%。

### 主要创新

- 提出将活动归因问题重构为语义对齐任务，利用LLM捕捉活动隐含意图。
- 构建Campaign-2-PT-RAG框架，结合LLM解释、语义搜索和结构化分类器生成产品类型覆盖集。
- 实现可扩展的标签生成流程，为下游活动排序模型提供大规模监督信号。
- 在内部和合成数据集上验证，达到78-90%精确率和超过99%召回率。

### 研究方法

论文采用LLM引导的语义归因方法。首先，使用LLM解析活动内容，提取隐含的产品意图；其次，通过语义搜索在平台产品类型分类中检索候选PT；然后，利用基于LLM的结构化分类器评估每个候选PT的相关性，生成活动-产品类型映射；最后，将用户购买行为与映射的PT匹配，生成正训练标签。实验在内部和合成数据集上进行，并与专家标注的映射对比验证。

### 关键结果

实验表明，LLM辅助方法生成的活动-产品类型映射标签具有78-90%的精确率和超过99%的召回率，验证了标签质量。

### 技术栈

- 摘要未提供具体技术栈，但提及使用大语言模型（LLM）、语义搜索、结构化分类器。

### 方法优势

- 创新性地将LLM应用于活动归因问题，解决语义鸿沟。
- 框架可扩展，适用于生产环境中的大规模标签生成。
- 实验验证了标签的高精确率和召回率，表明方法有效。
- 将模糊的归因问题转化为清晰的语义对齐任务，具有理论价值。

### 主要局限

- 论文局限：摘要未提及具体局限。当前证据局限：仅基于摘要，无法评估方法在不同场景下的泛化性、计算成本、对LLM的依赖程度等。

### 与当前研究方向的关联

论文与LLM与推荐系统结合、排序与重排、用户建模、CTR/CVR预测等关键词高度相关，涉及活动排序优化和标签生成，属于推荐系统工业落地范畴。

---

_知识库更新时间：2026-08-01T04:05:05.967462_
