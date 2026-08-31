---
title: "Embedding Prior Task-specific Knowledge into Language Models for Context-aware Document Ranking"
paper_id: "https://doi.org/10.1145/3690624.3709282"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 14.0
tags: ["paper", "recommender-systems", "Topic Modeling", "Semantic Web and Ontologies", "Web Data Mining and Analysis"]
---

# Embedding Prior Task-specific Knowledge into Language Models for Context-aware Document Ranking

[查看原文](https://dblp.org/rec/conf/kdd/00020D25) · [Semantic Scholar](https://www.semanticscholar.org/paper/57a2737324d34f1090e2247e1a7272290f0df5c8)

## 一句话结论

> 该论文提出LOCK模型，通过将任务特定的先验知识嵌入预训练语言模型，以改进上下文感知的文档排序性能。

## 论文信息

- **作者**：Shuting Wang, Yutao Zhu, Zhicheng Dou
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：14.0
- **DOI**：[https://doi.org/10.1145/3690624.3709282](https://doi.org/10.1145/3690624.3709282)

<details open>
<summary><strong>中文摘要</strong></summary>

利用当前会话中用户的上下文行为已被证明对文档排序任务有益。近年来，上下文感知的文档排序任务得益于预训练语言模型（PLMs）在语言建模方面的卓越能力。大多数基于PLM的上下文感知文档排序模型通过在历史搜索日志上微调PLMs来隐式学习任务特定知识。然而，由于搜索日志数据包含噪声且涵盖多种用户意图和搜索模式，这种黑盒方式可能阻碍模型充分掌握有效的上下文感知搜索知识。为解决这一问题，我们提出了LOCK，一种基于PLM的上下文感知文档排序模型，该模型将任务特定的先验知识显式嵌入PLMs中以指导模型优化。从局部到全局，我们识别了三种类型的任务特定知识，包括会话内信号、会话间信号和全局会话信号。LOCK将这些先验知识形式化为先验注意力偏置，以影响PLMs的微调过程。这一操作可以通过任务特定的先验知识引导排序模型，从而提升模型收敛速度和排序能力。此外，我们引入了一个任务特定的预训练阶段，涉及掩码语言建模和先验注意力矩阵的软重构，这有助于PLMs适应我们的任务。大量实验验证了我们方法的有效性和收敛性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Exploiting users' contextual behaviors in the current session has been proven favorable to the document ranking task. Recently, the context-aware document ranking task has benefited from pre-trained language models (PLMs) due to their superior ability in language modeling. Most PLM-based context-aware document ranking models implicitly learn task-specific knowledge by fine-tuning PLMs on historical search logs. However, since search log data is noisy and contains various user intents and search patterns, such a black-box way may prevent models from fully mastering effective context-aware search knowledge. To solve this problem, we propose LOCK, a PLM-based context-aware document ranking model that explicitly embeds task-specific prior knowledge into PLMs to guide the model optimization. From local to global, we identify three types of task-specific knowledge, including intra-turn signals, inter-turn signals, and global session signals. LOCK formulates such prior knowledge into prior attention biases for impacting the fine-tuning of PLMs. This operation can guide the ranking model by task-specific prior knowledge, thereby improving model convergence and ranking ability. Additionally, we introduce a task-specific pre-training stage that involves masked language modeling and the soft reconstruction of the prior attention matrix, which helps the PLMs adapt to our task. Extensive experiments validate the effectiveness and convergence of our method.

</details>

---

_知识库更新时间：2026-08-31T05:58:38.711004_
