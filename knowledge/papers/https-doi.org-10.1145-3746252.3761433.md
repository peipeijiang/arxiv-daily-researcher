---
title: "TransAct V2：Pinterest推荐中的终身用户行为序列建模"
paper_id: "https://doi.org/10.1145/3746252.3761433"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 58.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Mobile Crowdsensing and Crowdsourcing", "Personal Information Management and User Behavior"]
---

# TransAct V2：Pinterest推荐中的终身用户行为序列建模

> **英文原标题**：TransAct V2: Lifelong User Action Sequence Modeling on Pinterest Recommendation

[查看原文](https://dblp.org/rec/conf/cikm/0007JRLLPB0E25) · [ArXiv](https://arxiv.org/abs/2506.02267)

## 一句话结论

> 该论文提出TransAct V2，通过长用户序列、低延迟部署和下一动作损失函数，显著提升Pinterest Homefeed的CTR预测和推荐多样性。

## 论文信息

- **作者**：X.-G. Xia, Saurabh Vishwas Joshi, Kousik Rajesh, Kangnan Li, Yangyi Lu, Nikil Pancha, Dhruvil Badani, Jiajing Xu, Pong Eksombatchai
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：58.0
- **DOI**：[https://doi.org/10.1145/3746252.3761433](https://doi.org/10.1145/3746252.3761433)

<details open>
<summary><strong>中文摘要</strong></summary>

对用户行为序列进行建模已成为工业推荐系统研究的热点，尤其是在点击率（Click-Through Rate, CTR）预测任务中。然而，工业级CTR模型通常依赖短用户序列，限制了其捕捉长期行为的能力。这些模型也极少涉及高效服务大规模序列模型所需的基础设施挑战。此外，在逐点排序框架下，这类模型通常缺乏集成的行为预测任务，从而削弱了其预测能力。我们提出了TransAct V2——一个用于Pinterest首页推荐排序系统的生产模型，其包含三项关键创新：（1）利用超长用户序列提升CTR预测效果；（2）采用可扩展、低延迟的部署方案，以应对长用户行为序列带来的计算需求；（3）集成下一行为损失函数（Next Action Loss），增强用户行为预测能力。为克服延迟与存储限制，我们采用了高效的数据处理策略与模型服务优化，实现了无缝的工业级部署。消融实验进一步验证了我们方法的有效性。此外，广泛的离线与在线A/B实验证实，该方法在关键指标上取得了显著提升，包括用户参与度与推荐多样性，充分展示了TransAct V2的实际应用价值。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modeling user action sequences has become a popular focus in industrial recommendation system research, particularly for Click-Through Rate (CTR) prediction tasks. However, industry-scale CTR models often rely on short user sequences, limiting their ability to capture long-term behavior. They also rarely address the infrastructure challenges involved in efficiently serving large-scale sequential models. Additionally, these models typically lack an integrated action-prediction task within a point-wise ranking framework, reducing their predictive power. We introduce TransAct V2, a production model for Pinterest's Homefeed ranking system, featuring three key innovations: (1) leveraging very long user sequences to improve CTR predictions, (2) employing scalable, low-latency deployment solutions tailored to handle the computational demands of extended user action sequences, and (3) integrating a Next Action Loss function for enhanced user action forecasting. To overcome latency and storage constraints, we leverage efficient data-processing strategies and model-serving optimizations, enabling seamless industrial-scale deployment. Our approach's effectiveness is further demonstrated through ablation studies. Furthermore, extensive offline and online A/B experiments confirm major gains in key metrics, including engagement volume and recommendation diversity, showcasing TransAct V2's real-world impact.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出TransAct V2，一种用于Pinterest首页推荐排序的CTR预测模型。该模型通过三个关键创新提升推荐效果：利用极长用户序列（终身序列）改进CTR预测、集成下一动作损失函数增强用户行为预测能力、以及采用可扩展的低延迟部署方案处理长序列的计算需求。模型结合实时序列和终身序列，通过最近邻搜索提取相关子序列，并使用Transformer编码器处理。在离线实验中，TransAct V2在HIT@3/repin上提升13.31%，HIT@3/hide降低11.25%；在线A/B测试中，首页Repin量提升6.35%，Hide量降低12.80%，同时提升了推荐多样性和应用使用时长。此外，论文详细介绍了服务优化技术，包括请求级去重、融合反量化、单核统一Transformer等，显著降低了延迟和存储成本。

### 主要创新

- 结合实时序列和终身用户序列进行CTR预测，提升用户参与度和推荐多样性。
- 引入下一动作损失函数，采用基于印象的负采样，增强模型对用户行为的预测能力。
- 设计可扩展的低延迟服务系统，包括请求级去重、融合反量化、单核统一Transformer等优化，有效处理O(10^4)长度的序列。
- 提出最近邻特征日志策略，将存储复杂度从O(N)降至O(1)，实现训练与服务的一致性。

### 研究方法

采用点式多任务学习架构，输入包括上下文、创作者、物品和用户特征。用户序列处理：先对终身序列、实时序列和印象序列进行最近邻搜索（基于候选PinSage嵌入的点积相似度），并保留实时序列的最新r个动作，拼接后输入Transformer编码器（2层，单头注意力，维度64）。编码器输出用于多头预测和下一动作预测（采用采样softmax损失）。训练时使用加权交叉熵损失和下一动作损失联合优化。服务时通过自定义Triton内核实现融合操作，减少数据传输和内核启动开销。

### 关键结果

离线实验：TransAct V2在HIT@3/repin上提升13.31%，HIT@3/hide降低11.25%。；在线A/B测试：首页Repin量提升6.35%，Hide量降低12.80%，印象多样性提升0.45%，应用使用时长提升1.41%。；服务优化：单核统一Transformer相比PyTorch实现延迟降低85.09%，内存减少13.24%；端到端推理延迟在p99上提升250倍。

### 技术栈

- Transformer编码器（2层，单头注意力，维度64，前馈网络维度32）
- 最近邻搜索（基于点积相似度）
- 采样softmax损失
- 加权交叉熵损失
- PinSage嵌入（32维，经仿射量化至int8）
- CUDAGraph
- Triton自定义内核（融合反量化、最近邻搜索、单核统一Transformer）
- Pinned Memory Arena
- 请求级去重（稀疏张量格式）

### 方法优势

- 创新性地结合终身序列和实时序列，有效平衡短期和长期用户兴趣。
- 下一动作损失采用印象负采样，提供更具挑战性的负样本，提升模型区分能力。
- 服务优化全面，从数据管道到推理内核均进行了针对性设计，实现了工业级部署。
- 离线与在线实验均验证了显著效果，且指标提升幅度大。

### 主要局限

- 终身序列长度基于90百分位用户行为历史，可能对长尾用户覆盖不足。
- 最近邻搜索依赖PinSage嵌入，嵌入质量直接影响检索效果。
- 模型训练和推理依赖Pinterest内部基础设施，通用性可能受限。
- 未与生成式推荐模型（如HSTU）进行直接对比。

### 与当前研究方向的关联

序列推荐：核心研究内容，建模用户行为序列。；CTR/CVR预测：模型用于CTR预测任务。；用户建模：通过终身序列和实时序列建模用户兴趣。；工业落地：论文详细描述了在Pinterest的部署和服务优化。；排序与重排：模型应用于Homefeed排序阶段。

---

_知识库更新时间：2026-07-19T04:08:52.139311_
