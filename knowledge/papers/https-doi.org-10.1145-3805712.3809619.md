---
title: "Unified Entity Matching under Scarce Supervision via Meta-Rule Induction and Retrieval"
paper_id: "https://doi.org/10.1145/3805712.3809619"
source: "citation"
published: "2026-07-10T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems", "Data Quality and Management", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# Unified Entity Matching under Scarce Supervision via Meta-Rule Induction and Retrieval

[查看原文](https://doi.org/10.1145/3805712.3809619)

## 一句话结论

> The paper proposes a meta-rule induction and retrieval framework for unified entity matching under scarce supervision, achieving state-of-the-art performance.

## 论文信息

- **作者**：Ziheng Zhang, Weixin Zeng, Jiuyang Tang, Xiang Zhao
- **来源**：Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval
- **发布时间**：2026-07-10
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3805712.3809619](https://doi.org/10.1145/3805712.3809619)

<details open>
<summary><strong>中文摘要</strong></summary>

实体匹配是广泛的检索与知识应用中的一项基础任务，旨在识别来自异构来源的两个对象是否对应于同一真实世界实体。其典型变体包括实体解析（entity resolution, ER）、实体链接（entity linking, EL）和实体对齐（entity alignment, EA）。尽管近期的统一匹配器通过多任务训练和全面标注取得了进展，但实际流水线往往在稀缺监督条件下运行，此时标注数据不完整，无法覆盖全部匹配场景。在这种情形下，监督式统一模型性能显著下降，而可部署的紧凑型大语言模型（LLM）仍不可靠：轻量级微调和上下文学习会产生不一致的行为，甚至在场景迁移时表现出负面效果。为填补这一空白，我们提出了ours，一种面向稀缺监督下统一实体匹配的元规则归纳与检索框架。ours不依赖参数化适配，而是将有限的监督转化为显式的自然语言规则，通过层次聚类将其抽象为可复用的元规则，并为每个输入实例检索最相关的元规则以指导LLM的推理。该设计通过将决策基于显式且可复用的证据，而非仅依赖隐式适配或提示示例，从而提升了鲁棒性。大量实验表明，ours在稀缺监督下的统一实体匹配任务中达到了最先进的性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Entity matching is a fundamental task in a wide range of retrieval and knowledge applications, aiming to identify whether two objects correspond to the same real-world entity across heterogeneous sources. Typical variants include entity resolution (ER), entity linking (EL), and entity alignment (EA). While recent unified matchers have made progress through multi-task training with comprehensive annotations, real-world pipelines often operate under scarce supervision, where labeled data is incomplete and fails to cover the full spectrum of matching scenarios. In this regime, supervised unified models degrade substantially, and deployable compact LLMs remain unreliable: lightweight fine-tuning and in-context learning yield inconsistent behavior and can even exhibit negative effects under scenario shifts. To fill in this gap, we propose øurs, a meta-rule induction and retrieval framework for unified entity matching under scarce supervision. Instead of relying on parametric adaptation, øurs converts limited supervision into explicit natural-language rules, abstracts them into reusable meta-rules via hierarchical clustering, and retrieves the most relevant meta-rules to guide the LLM's inference for each input instance. This design improves robustness by grounding decisions on explicit and reusable evidence, instead of relying solely on implicit adaptation or prompt demonstrations. Extensive experiments show that øurs achieves state-of-the-art performance on unified entity matching under scarce supervision.

</details>

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：cites_seed
- **seed_paper_id**：https://doi.org/10.1145/3726302.3731696
- **seed_title**：Navigating Large Language Models for Recommendation: From Architecture to Learning Paradigms and Deployment
- **seed_score**：99.0

</details>

---

_知识库更新时间：2026-08-08T02:39:38.052788_
