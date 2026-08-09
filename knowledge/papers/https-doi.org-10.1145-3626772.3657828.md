---
title: "让我为您代劳：通过工具学习实现大语言模型赋能的推荐系统"
paper_id: "https://doi.org/10.1145/3626772.3657828"
source: "citation"
published: "2024-07-10T00:00:00"
score: 90.0
tags: ["paper", "recommender-systems", "Digital Rights Management and Security", "Semantic Web and Ontologies", "Recommender Systems and Techniques"]
---

# 让我为您代劳：通过工具学习实现大语言模型赋能的推荐系统

> **英文原标题**：Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning

[查看原文](https://doi.org/10.1145/3626772.3657828) · [ArXiv](https://arxiv.org/abs/2405.15114)

## 一句话结论

> 论文提出ToolRec框架，利用LLM作为代理用户并通过工具学习生成推荐列表，以解决现有LLM推荐系统中的幻觉和语义对齐问题，从而更精准地捕捉用户细粒度偏好。

## 论文信息

- **作者**：Yuyue Zhao, Jiancan Wu, Xiang Wang, Wei Tang, Dingxian Wang, Maarten de Rijke
- **来源**：Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval
- **发布时间**：2024-07-10
- **相关度评分**：90.0
- **DOI**：[https://doi.org/10.1145/3626772.3657828](https://doi.org/10.1145/3626772.3657828)

<details open>
<summary><strong>中文摘要</strong></summary>

传统推荐系统（RSs）在精确捕捉用户细粒度偏好方面面临挑战。大语言模型（LLMs）已展现出在常识推理和利用外部工具方面的能力，这可能有助于应对这些挑战。然而，现有的基于LLM的推荐系统存在幻觉问题、物品语义空间与用户行为空间之间的错位，或控制策略过于简单（例如，仅决定是否排序或直接呈现现有结果）。为弥合这些差距，我们引入了ToolRec，一个通过工具学习实现LLM赋能推荐的框架，该框架将LLM用作替代用户，从而引导推荐过程并调用外部工具生成与用户细微偏好高度契合的推荐列表。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Conventional recommender systems (RSs) face challenges in precisely capturing users' fine-grained preferences. Large language models (LLMs) have shown capabilities in commonsense reasoning and leveraging external tools that may help address these challenges. However, existing LLM-based RSs suffer from hallucinations, misalignment between the semantic space of items and the behavior space of users, or overly simplistic control strategies (e.g., whether to rank or directly present existing results). To bridge these gap, we introduce ToolRec, a framework for LLM-empowered recommendations via tool learning that uses LLMs as surrogate users, thereby guiding the recommendation process and invoking external tools to generate a recommendation list that aligns closely with users' nuanced preferences.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对传统推荐系统难以精确捕捉用户细粒度偏好、缺乏常识知识等问题，提出ToolRec框架，利用大语言模型（LLM）作为代理用户，通过工具学习引导推荐过程。ToolRec包含用户决策模拟模块、属性导向工具（排序工具和检索工具）以及记忆策略。LLM模拟用户决策，根据用户历史交互和当前上下文，选择属性并调用工具探索物品池，迭代优化候选列表，直至满意。实验在ML-1M、Amazon-Book和Yelp2018三个数据集上进行，结果表明ToolRec在富含语义知识的场景下优于现有基线，验证了其有效性。

### 主要创新

- 提出ToolRec框架，将LLM作为代理用户，通过工具学习增强推荐系统，实现多轮交互式推荐。
- 设计属性导向工具，包括排序工具和检索工具，分别利用LLM的排序能力和冻结骨干网络加微调属性编码器的检索能力。
- 引入记忆策略，验证和存储中间结果，确保推荐列表的准确性和可追溯性。
- 通过用户决策模拟，使LLM能够主动分析偏好不匹配，并决定何时调用工具或终止推荐过程。

### 研究方法

ToolRec采用LLM（ChatGPT）作为核心控制器，通过链式思维提示（CoT）进行推理和行动。用户历史交互序列作为初始上下文，LLM在每轮中根据当前观察选择属性并调用工具（检索或排序），获取候选物品集，然后更新上下文，重复直至满意。检索工具采用两阶段训练：先预训练基础序列推荐模型（如SASRec），再冻结其参数，微调属性编码器，结合属性序列和用户表示进行推荐。排序工具则通过指令模板让LLM对候选物品排序。记忆策略用于验证物品存在性并记录工具标记。

### 关键结果

在ML-1M数据集上，ToolRec的Recall和NDCG分别达到0.215和0.1171，相比最优基线分别提升3.36%和15.10%；在Amazon-Book上，Recall和NDCG分别为0.053和0.0259，提升14.28%和5.14%；在Yelp2018上性能下降，Recall和NDCG分别为0.028和0.0159，下降29.16%和27.32%。消融实验表明，用户决策模拟和属性导向工具对性能有显著贡献。

### 技术栈

- 大语言模型：ChatGPT (gpt-3.5-turbo-16k)
- 序列推荐模型：SASRec, BERT4Rec
- 属性编码器：Transformer
- 词嵌入：GloVe
- 损失函数：BPR损失
- 评估指标：Recall@10, NDCG@10
- 数据集：ML-1M, Amazon-Book, Yelp2018

### 方法优势

- 创新性地将工具学习引入推荐系统，使LLM能够主动探索物品空间。
- 设计了属性导向工具，兼顾了排序和检索能力，提高了推荐的准确性。
- 通过用户决策模拟，使推荐过程更贴近人类决策过程。
- 实验验证了在富含语义知识的领域（如电影、书籍）中的有效性。

### 主要局限

- 在Yelp2018等本地商业数据上性能下降，可能由于LLM对本地商业知识有限。
- 依赖LLM的推理能力，不同LLM（如Vicuna、PaLM）表现不佳。
- 实验仅采样200个用户，可能影响结果的稳定性。
- 未考虑推荐系统的实时性和可扩展性。

### 与当前研究方向的关联

该论文与序列推荐、LLM与推荐系统结合、推荐智能体等关键词高度相关，通过工具学习实现LLM对推荐流程的控制，属于LLM控制推荐系统的前沿研究。

## 代码与复现

- [tsinghua-fib-lab/LLM-Agent-for-Recommendation-and-Search](https://github.com/tsinghua-fib-lab/LLM-Agent-for-Recommendation-and-Search)：likely，置信度 69，Stars 116
- [Go0day/ToolRec-Code](https://github.com/Go0day/ToolRec-Code)：possible，置信度 30，Stars 25

<details>
<summary><strong>发现与关联证据</strong></summary>

- **channel**：citation_expansion
- **relation**：referenced_by_seed
- **seed_paper_id**：https://doi.org/10.1145/3805712.3808643
- **seed_title**：Multi-Agentic Recommender Systems: Foundations, Perspectives, and Lessons from Large Scale Deployments in eCommerce
- **seed_score**：98.0

</details>

---

_知识库更新时间：2026-08-09T02:40:57.864356_
