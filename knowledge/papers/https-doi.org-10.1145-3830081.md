---
title: "协同大语言模型与知识图谱用于冷启动推荐"
paper_id: "https://doi.org/10.1145/3830081"
source: "citation"
published: "2026-07-15T00:00:00"
score: 66.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Sentiment Analysis and Opinion Mining"]
---

# 协同大语言模型与知识图谱用于冷启动推荐

> **英文原标题**：Synergizing Large Language Model and Knowledge Graph for Cold-Start Recommendation

[查看原文](https://doi.org/10.1145/3830081)

## 一句话结论

> 本文提出SCSRec框架，通过协同大语言模型和知识图谱生成高质量的模拟交互数据，以解决冷启动推荐问题，并在多个数据集上取得最优性能。

## 论文信息

- **作者**：Haobo Zhang, Qiannan Zhu, Zhicheng Dou
- **来源**：ACM Transactions on Information Systems
- **发布时间**：2026-07-15
- **相关度评分**：66.0
- **DOI**：[https://doi.org/10.1145/3830081](https://doi.org/10.1145/3830081)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统中的冷启动项目问题长期以来一直具有挑战性且被广泛研究，因为冷启动项目没有交互数据。这使得难以获得这些项目的有效表示，并导致推荐性能下降。冷启动推荐中最先进的方法主要利用大语言模型（LLM）从冷项目的内容中提取相关语义信息，以丰富其表示。然而，基于LLM的方法由于缺乏足够的事实知识和依据，常常生成错误信息。相反，知识图谱（KG）包含关于用户和项目的事实知识，可以为LLM提供更全面的依据。因此，我们提出了一种新颖的框架，即SCSRec，它协同利用LLM和KG为冷项目生成高质量的交互模拟数据，并进一步提升冷启动推荐的性能。该框架主要通过LLM与KG的协同作用生成高质量的冷项目表示，用于交互模拟，并利用这些交互来训练推荐模型。具体而言，首先，为了获得高质量的表示，我们采用双增强方法协同LLM和KG。我们使用LLM丰富实体的描述并完善冷项目的结构信息，以获得信息丰富的知识图谱。然后，我们提取实体的子图作为事实知识和依据，用于LLM表示生成。接下来，我们引入自适应专家协同模块，深度融合和协同基于LLM的表示与基于KG的用户和项目表示。基于集成的高质量嵌入，我们利用项目与用户之间的相似性为冷项目生成模拟交互。最后，我们将模拟数据与数据集中热项目的交互数据相结合，共同训练推荐器，以增强冷启动推荐的性能。在三个公开数据集上的实验结果表明，我们的模型在热项目、冷项目及整体推荐场景中均优于现有最先进的方法。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

The cold-start item problem in recommendation systems has long been challenging and widely studied because there is no interaction data for cold-start items. This makes it difficult to obtain effective representations of these items and leads to a decline in the recommendation performance. The state-of-the-art methods in cold-start recommendation mainly leverage LLMs to extract relevant semantic information from the content of cold items to enrich their representation. However, LLM-based methods often generate incorrect information due to the lack of sufficient factual knowledge and groundings. Instead, KG contains factual knowledge about users and items and can provide LLMs with more comprehensive groundings. Therefore, we propose a novel framework, namely SCSRec, which synergizes both LLM and KG to generate high-quality interaction simulation data for cold items and further enhances the performance of cold-start recommendations. It mainly generates high-quality cold item representations with the synergy of LLM and KG for interaction simulation and uses the interactions to train the recommendation model. Specifically, first, to obtain high-quality representations, we synergize the LLM and KG using a dual-enhanced method. We use the LLM to enrich the descriptions of entities and complete the structural information of cold items to obtain a KG with rich information. Then we extract entities’ sub-graphs as factual knowledge and groundings for LLM representation generation. Next, we introduce an Adaptive Expert Synergy Module to deeply integrate and synergize the LLM-based representations and the KG-based representations of users and items. Based on the integrated high-quality embedding, we use the similarity between items and users to generate simulated interactions for cold items. Finally, we combine the simulation data with the interaction data of warm items from the dataset to jointly train the recommender and enhance the performance of cold-start recommendations. Experimental results on three public datasets show that our model outperforms existing state-of-the-art methods in the scenarios of warm, cold, and overall recommendations.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

冷启动项目问题在推荐系统中长期存在且被广泛研究，因为冷启动项目没有交互数据，难以获得有效表示，导致推荐性能下降。现有最先进方法主要利用大语言模型（LLM）从冷项目内容中提取语义信息以丰富表示，但LLM方法常因缺乏足够事实知识和依据而产生错误信息。知识图谱（KG）包含用户和项目的事实知识，可为LLM提供更全面的依据。为此，本文提出新框架SCSRec，协同LLM和KG生成高质量交互模拟数据，提升冷启动推荐性能。首先，通过双增强方法协同LLM和KG获得高质量表示：用LLM丰富实体描述并补全冷项目结构信息，得到信息丰富的KG；然后提取实体子图作为LLM表示生成的事实知识和依据。接着引入自适应专家协同模块，深度融合LLM和KG表示。基于集成的高质量嵌入，利用项目与用户相似度生成冷项目模拟交互。最后将模拟数据与数据集中热项目交互数据结合，联合训练推荐器，提升冷启动推荐性能。在三个公开数据集上的实验表明，模型在热、冷和整体推荐场景中均优于现有最先进方法。

### 主要创新

- 提出协同LLM和KG的框架SCSRec，用于冷启动推荐，利用KG为LLM提供事实依据，减少错误信息。
- 采用双增强方法：LLM丰富KG实体描述并补全冷项目结构信息，获得信息丰富的KG。
- 引入自适应专家协同模块，深度融合LLM和KG表示，获得高质量嵌入。
- 基于高质量嵌入，利用用户-项目相似度生成冷项目模拟交互，并联合热项目交互数据训练推荐器。

### 研究方法

论文提出SCSRec框架，包含以下步骤：1) 双增强：使用LLM丰富KG实体描述并补全冷项目结构信息，得到信息丰富的KG；2) 提取实体子图作为事实知识和依据，用于LLM表示生成；3) 引入自适应专家协同模块，深度融合LLM和KG表示；4) 基于集成嵌入，利用用户-项目相似度生成冷项目模拟交互；5) 将模拟数据与热项目交互数据结合，联合训练推荐模型。

### 关键结果

在三个公开数据集上的实验表明，所提模型在热、冷和整体推荐场景中均优于现有最先进方法。

### 技术栈

- 大语言模型（LLM）
- 知识图谱（KG）
- 自适应专家协同模块
- 相似度计算
- 联合训练

### 方法优势

- 创新性地协同LLM和KG，利用KG提供事实依据，缓解LLM幻觉问题。
- 双增强方法同时丰富KG和LLM表示，提高表示质量。
- 自适应专家协同模块灵活融合不同表示，增强模型适应性。
- 在多个数据集上验证了有效性，覆盖热、冷和整体推荐场景。

### 主要局限

- 摘要未提供具体局限性。当前证据仅基于摘要，无法评估模型复杂度、计算成本、可扩展性等。

### 与当前研究方向的关联

论文与LLM与推荐系统结合、知识图谱、冷启动推荐、推荐系统等关键词高度相关。

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3589334.3645537
- **seed_title**：AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems
- **seed_score**：100.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.667964_
