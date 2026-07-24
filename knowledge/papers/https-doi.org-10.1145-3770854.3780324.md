---
title: "利用大语言模型将语义画像丰富到知识图谱中以用于推荐系统"
paper_id: "https://doi.org/10.1145/3770854.3780324"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 46.0
tags: ["paper", "recommender-systems"]
---

# 利用大语言模型将语义画像丰富到知识图谱中以用于推荐系统

> **英文原标题**：Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models

[查看原文](https://dblp.org/rec/conf/kdd/AhnSS26) · [ArXiv](https://arxiv.org/abs/2601.08148) · [Semantic Scholar](https://www.semanticscholar.org/paper/557ccc4e6ae350d46d37282f551a5836b22763b3)

## 一句话结论

> 该论文提出SPiKE模型，利用大语言模型生成知识图谱实体的语义画像，并通过画像感知的图聚合和成对偏好匹配提升推荐性能，在真实场景中优于现有方法。

## 论文信息

- **作者**：Seokho Ahn, Sungbok Shin, Young-Duk Seo
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：46.0
- **DOI**：[https://doi.org/10.1145/3770854.3780324](https://doi.org/10.1145/3770854.3780324)

<details open>
<summary><strong>中文摘要</strong></summary>

丰富且信息量大的用户偏好画像对于提升推荐质量至关重要。然而，关于如何最佳构建和利用此类画像，目前尚未达成共识。为解决这一问题，我们从四个维度重新审视了推荐系统中近期基于画像的方法：1）知识库，2）偏好指标，3）影响范围，以及4）主体。我们认为，大型语言模型（LLMs）能够有效从多种知识源中提取压缩后的推理依据，而知识图谱（KGs）则更适合传播这些画像以扩展其覆盖范围。基于这一见解，我们提出了一种名为SPiKE的新推荐模型。SPiKE包含三个核心组件：i）实体画像生成，利用LLMs为所有KG实体生成语义画像；ii）画像感知的KG聚合，将这些画像整合到KG中；以及iii）成对画像偏好匹配，在训练过程中对齐基于LLM和基于KG的表示。在实验中，我们证明了SPiKE在实际场景中始终优于基于KG和LLM的最先进推荐系统。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Rich and informative profiling to capture user preferences is essential for improving recommendation quality. However, there is still no consensus on how best to construct and utilize such profiles. To address this, we revisit recent profiling-based approaches in recommender systems along four dimensions: 1) knowledge base, 2) preference indicator, 3) impact range, and 4) subject. We argue that large language models (LLMs) are effective at extracting compressed rationales from diverse knowledge sources, while knowledge graphs (KGs) are better suited for propagating these profiles to extend their reach. Building on this insight, we propose a new recommendation model, called SPiKE. SPiKE consists of three core components: i) Entity profile generation, which uses LLMs to generate semantic profiles for all KG entities; ii) Profile-aware KG aggregation, which integrates these profiles into the KG; and iii) Pairwise profile preference matching, which aligns LLM- and KG-based representations during training. In experiments, we demonstrate that SPiKE consistently outperforms state-of-the-art KG- and LLM-based recommenders in real-world settings.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对推荐系统中用户画像构建和传播方法不明确的问题，提出了一种名为SPiKE的推荐模型。该模型通过四个维度（知识库、偏好指示器、影响范围、主体）分析现有方法，并利用大语言模型（LLM）为知识图谱（KG）中的所有实体生成语义画像，然后将这些画像集成到KG中通过消息传递进行传播，最后通过成对画像偏好匹配对齐LLM和KG的表示。实验结果表明，SPiKE在三个真实世界数据集上一致优于现有的基于KG和LLM的推荐方法。

### 主要创新

- 提出四个维度（知识库、偏好指示器、影响范围、主体）来系统分析推荐系统中的画像方法，并据此设计模型。
- 利用LLM为KG中所有实体（包括用户、物品和辅助实体）生成语义画像，而不仅限于用户或物品。
- 设计画像感知的KG聚合机制，通过注入-移除（ResNet风格）方式将语义画像融入KG传播，既利用画像信息又保持原始KG空间。
- 提出成对画像偏好匹配损失，对齐画像嵌入和KG嵌入的相似性结构，增强表示学习。

### 研究方法

SPiKE包含三个核心组件：1) 实体画像生成：使用LLM按顺序为物品、辅助实体和用户生成文本画像，并利用预训练文本编码器嵌入；2) 画像感知的KG聚合：将画像嵌入通过加法注入到实体初始表示中，在注意力加权的邻居聚合后移除画像，实现语义与结构的联合传播；3) 成对画像偏好匹配：通过随机采样和Frobenius范数损失，对齐KG嵌入和画像嵌入的成对余弦相似性矩阵。训练采用BPR损失与匹配损失的联合优化。

### 关键结果

SPiKE在Books、Movies & TV、Yelp三个数据集上，Recall@10/20/40和NDCG@10/20/40指标均优于所有基线（包括BPR-MF、LightGCN、SGL、LightGCL、KGRec、DiffKG、RLMRec、CoLaKG）。；消融实验表明，移除用户画像、物品画像、辅助实体画像、注入-移除机制或匹配损失均导致性能下降，其中移除注入-移除机制下降最大。；画像生成方法比较显示，使用GPT-4o生成的画像效果最好，但即使使用模板也能带来提升。；画像质量自动评估（说服力、相关性、忠实度）显示SPiKE生成的画像质量优于RLMRec和CoLaKG。

### 技术栈

- 大语言模型（LLM）：GPT-4o、Qwen3-4B
- 知识图谱（KG）
- 预训练文本编码器（F_Text）
- 多层感知机（MLP）
- 注意力机制（缩放点积注意力）
- 贝叶斯个性化排序（BPR）损失
- Frobenius范数
- 余弦相似度
- ResNet风格的注入-移除机制

### 方法优势

- 系统性地从四个维度分析现有画像方法，为模型设计提供清晰的理论依据。
- 创新性地将LLM生成的语义画像与KG的结构传播相结合，发挥两者互补优势。
- 画像覆盖所有KG实体，扩展了偏好表达的粒度。
- 注入-移除机制简单有效，避免了画像对KG空间的干扰。
- 在多个真实数据集上取得一致最优结果，且消融实验充分验证各组件贡献。

### 主要局限

- 依赖LLM生成画像，计算成本较高，且需要设计复杂的提示模板。
- 画像生成顺序（先物品后辅助实体再用户）可能引入误差累积。
- 实验仅在三个数据集上进行，泛化性有待更多领域验证。
- 未讨论LLM生成画像的偏见或错误对推荐的影响。
- 超参数（如缩放因子λ_p、采样比例γ）需要调优，可能影响实际部署。

### 与当前研究方向的关联

LLM与推荐系统结合：核心方法利用LLM生成语义画像，属于LLM增强推荐。；知识图谱：模型基于KG进行结构传播和画像集成。；用户建模：通过用户画像和偏好匹配进行用户兴趣建模。；推荐系统：整体研究属于推荐系统领域，提出新模型SPiKE。

## 代码与复现

- [circleAhn/SPiKE-pytorch](https://github.com/circleAhn/SPiKE-pytorch)：possible，置信度 30，Stars 11

---

_知识库更新时间：2026-07-24T04:05:55.201761_
