---
title: "KGAT：用于推荐的知识图谱注意力网络"
paper_id: "https://doi.org/10.1145/3292500.3330989"
source: "citation"
published: "2019-07-25T00:00:00"
score: 44.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Epigenetics and DNA Methylation"]
---

# KGAT：用于推荐的知识图谱注意力网络

> **英文原标题**：KGAT

[查看原文](https://doi.org/10.1145/3292500.3330989) · [ArXiv](https://arxiv.org/abs/1905.07854)

## 一句话结论

> 本文提出知识图谱注意力网络（KGAT），通过显式建模知识图谱中的高阶连通性，利用注意力机制传播嵌入，从而提升推荐系统的准确性、多样性和可解释性。

## 论文信息

- **作者**：Xiang Wang, Xiangnan He, Yixin Cao, Meng Liu, Tat‐Seng Chua
- **来源**：Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery &amp; Data Mining
- **发布时间**：2019-07-25
- **相关度评分**：44.0
- **DOI**：[https://doi.org/10.1145/3292500.3330989](https://doi.org/10.1145/3292500.3330989)

<details open>
<summary><strong>中文摘要</strong></summary>

为了提供更准确、多样且可解释的推荐，必须超越对用户-物品交互的建模，并将辅助信息纳入考虑。传统方法如因子分解机（Factorization Machine, FM）将其视为监督学习问题，假设每次交互为独立实例，并编码辅助信息。由于忽略了实例或物品之间的关系（例如，某部电影的导演也是另一部电影的演员），这些方法不足以从用户的集体行为中提炼协作信号。在本工作中，我们研究了知识图谱（Knowledge Graph, KG）的效用，它通过将物品与其属性关联，打破了独立交互的假设。我们认为，在KG与用户-物品图的混合结构中，高阶关系——即通过一个或多个关联属性连接两个物品的关系——是成功推荐的关键因素。我们提出了一种名为知识图谱注意力网络（Knowledge Graph Attention Network, KGAT）的新方法，它以端到端的方式显式建模KG中的高阶连通性。该方法递归地从节点的邻居（可以是用户、物品或属性）传播嵌入以细化节点嵌入，并采用注意力机制来区分邻居的重要性。我们的KGAT在概念上优于现有的基于KG的推荐方法，后者要么通过提取路径来利用高阶关系，要么通过正则化隐式建模这些关系。在三个公开基准上的实验结果表明，KGAT显著优于最先进的方法，如Neural FM和RippleNet。进一步的研究验证了嵌入传播对高阶关系建模的有效性，以及注意力机制带来的可解释性优势。我们已在https://github.com/xiangwang1223/knowledge_graph_attention_network 发布代码和数据集。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

To provide more accurate, diverse, and explainable recommendation, it is compulsory to go beyond modeling user-item interactions and take side information into account. Traditional methods like factorization machine (FM) cast it as a supervised learning problem, which assumes each interaction as an independent instance with side information encoded. Due to the overlook of the relations among instances or items (e.g., the director of a movie is also an actor of another movie), these methods are insufficient to distill the collaborative signal from the collective behaviors of users. In this work, we investigate the utility of knowledge graph (KG), which breaks down the independent interaction assumption by linking items with their attributes. We argue that in such a hybrid structure of KG and user-item graph, high-order relations --- which connect two items with one or multiple linked attributes --- are an essential factor for successful recommendation. We propose a new method named Knowledge Graph Attention Network (KGAT) which explicitly models the high-order connectivities in KG in an end-to-end fashion. It recursively propagates the embeddings from a node's neighbors (which can be users, items, or attributes) to refine the node's embedding, and employs an attention mechanism to discriminate the importance of the neighbors. Our KGAT is conceptually advantageous to existing KG-based recommendation methods, which either exploit high-order relations by extracting paths or implicitly modeling them with regularization. Empirical results on three public benchmarks show that KGAT significantly outperforms state-of-the-art methods like Neural FM and RippleNet. Further studies verify the efficacy of embedding propagation for high-order relation modeling and the interpretability benefits brought by the attention mechanism. We release the codes and datasets at https://github.com/xiangwang1223/knowledge_graph_attention_network.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出了一种名为知识图谱注意力网络（KGAT）的推荐方法，旨在显式建模协同知识图谱中的高阶连通性。传统方法如因子分解机将交互视为独立实例，忽略了实例间关系，难以从用户集体行为中提取基于属性的协同信号。KGAT利用图神经网络框架，通过递归嵌入传播更新节点表示，并采用知识感知的注意力机制区分邻居重要性，从而端到端地捕获高阶关系。在三个公开数据集上的实验表明，KGAT显著优于现有方法，如NFM和RippleNet，并验证了嵌入传播和注意力机制的有效性及可解释性。

### 主要创新

- 提出显式建模协同知识图谱中高阶连通性的重要性，并设计端到端方法KGAT。
- 采用递归嵌入传播机制，以线性时间复杂度捕获高阶连通性。
- 引入知识感知的注意力机制，学习传播过程中邻居的权重，增强可解释性。
- 设计了Bi-Interaction聚合器，编码实体表示与其邻域表示之间的特征交互。
- 将知识图谱嵌入（TransR）与推荐模型联合优化，注入直接连接信息。

### 研究方法

KGAT包含三个主要组件：嵌入层使用TransR对协同知识图谱进行嵌入，保留图结构；注意力嵌入传播层递归地聚合邻居信息，通过关系感知的注意力权重（公式4-5）和聚合函数（GCN、GraphSage或Bi-Interaction）更新节点表示；预测层通过拼接各层表示并计算内积得到匹配分数。模型联合优化知识图谱嵌入损失（公式2）和BPR推荐损失（公式13），采用交替训练策略。

### 关键结果

在Amazon-Book、Last-FM和Yelp2018三个数据集上，KGAT在recall@20和ndcg@20上均优于所有基线，相对最强基线分别提升8.95%、4.93%、7.18%的recall@20。消融实验表明，增加传播层数（至3层）能提升性能，Bi-Interaction聚合器优于GCN和GraphSage，知识图谱嵌入和注意力机制均对性能有贡献。案例研究展示了注意力机制可解释性。

### 技术栈

- TransR知识图谱嵌入
- 图神经网络（GCN、GraphSage）
- 注意力机制
- Bi-Interaction聚合器
- BPR损失
- Adam优化器
- LeakyReLU激活函数
- TensorFlow

### 方法优势

- 显式建模高阶连通性，优于隐式方法。
- 端到端训练，避免路径提取或元路径定义。
- 注意力机制提供可解释性。
- 在多个数据集上验证有效性，并进行了充分的消融研究。
- 代码和数据集公开，便于复现。

### 主要局限

- 模型深度增加时性能提升有限，可能受限于数据稀疏性。
- 注意力机制可能引入噪声，对过于通用的实体（如“English”）解释性不足。
- 未考虑用户和物品的时序动态。
- 实验仅基于三个数据集，泛化性有待进一步验证。

### 与当前研究方向的关联

该论文属于推荐系统领域，核心是知识图谱增强的推荐，与关键词“知识图谱”、“图神经网络”、“注意力机制”、“高阶连通性”高度相关。同时涉及协同过滤、可解释推荐等方向，与“推荐系统”关键词直接相关。

## 代码与复现

- [xiangwang1223/knowledge_graph_attention_network](https://github.com/xiangwang1223/knowledge_graph_attention_network)：official，置信度 100，Stars 1161
- [LunaBlack/KGAT-pytorch](https://github.com/LunaBlack/KGAT-pytorch)：likely，置信度 69，Stars 363

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3626772.3657828
- **seed_title**：Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning
- **seed_score**：90.0

</details>

---

_知识库更新时间：2026-08-10T02:48:30.669717_
