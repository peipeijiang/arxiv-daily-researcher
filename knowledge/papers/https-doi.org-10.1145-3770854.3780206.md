---
title: "MGFRec：基于多重锚定与反馈的强化推理推荐方法"
paper_id: "https://doi.org/10.1145/3770854.3780206"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 64.0
tags: ["paper", "recommender-systems"]
---

# MGFRec：基于多重锚定与反馈的强化推理推荐方法

> **英文原标题**：MGFRec: Towards Reinforced Reasoning Recommendation with Multiple Groundings and Feedback

[查看原文](https://dblp.org/rec/conf/kdd/CaiGLSSTF26) · [ArXiv](https://arxiv.org/abs/2510.22888) · [Semantic Scholar](https://www.semanticscholar.org/paper/b45d6a21810226d0c088adad73b360c979002873)

## 一句话结论

> 该论文提出MGFRec方法，通过多轮接地和用户反馈使LLM在推荐推理中与实际物品空间对齐，实验证明其有效性。

## 论文信息

- **作者**：Shihao Cai, Chongming Gao, Haoyan Liu 0001, Wentao Shi 0002, Jianshan Sun, Ruiming Tang, Fuli Feng
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：64.0
- **DOI**：[https://doi.org/10.1145/3770854.3780206](https://doi.org/10.1145/3770854.3780206)

<details open>
<summary><strong>中文摘要</strong></summary>

大型语言模型（LLMs）强大的推理与生成能力，促使研究者将其应用于基于推理的推荐任务——这类任务需要对用户兴趣进行深度推理，并生成推荐物品。然而，以往的基于推理的推荐方法通常仅在语言空间内进行推理，未能融入实际物品空间。这导致了对用户兴趣的过度解读，并偏离了真实物品。针对这一研究空白，我们提出在推理过程中执行多轮接地（grounding），以帮助LLM更好地理解实际物品空间，从而确保其推理与真实物品保持一致。此外，我们引入了一个用户智能体（user agent），在每一轮接地步骤中提供反馈，使LLM能够更好地识别并适应用户兴趣。在三个亚马逊评论数据集上进行的综合实验表明，融入多轮接地与反馈机制具有有效性。这些发现强调了在推荐任务中，于实际物品空间内进行推理（而非局限于语言空间）的关键重要性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

The powerful reasoning and generative capabilities of large language models (LLMs) have inspired researchers to apply them to reasoning-based recommendation tasks, which require in-depth reasoning about user interests and the generation of recommended items. However, previous reasoning-based recommendation methods have typically performed inference within the language space alone, without incorporating the actual item space. This has led to over-interpreting user interests and deviating from real items. Towards this research gap, we propose performing multiple rounds of grounding during inference to help the LLM better understand the actual item space, which could ensure that its reasoning remains aligned with real items. Furthermore, we introduce a user agent that provides feedback during each grounding step, enabling the LLM to better recognize and adapt to user interests. Comprehensive experiments conducted on three Amazon review datasets demonstrate the effectiveness of incorporating multiple groundings and feedback. These findings underscore the critical importance of reasoning within the actual item space, rather than being confined to the language space, for recommendation tasks.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

针对现有基于大语言模型的推理推荐方法仅在语言空间进行推理，导致过度解读用户兴趣并偏离真实物品空间的问题，本文提出MGFRec框架。该框架将单步锚定扩展为多步锚定，使LLM在推理过程中反复接入真实物品空间，并通过用户智能体提供反馈信号。具体地，推荐智能体执行“思考-锚定-回答”的多轮循环：先推理用户兴趣并生成物品标题，然后通过锚定操作检索相关物品列表，用户智能体据此提供文本反馈，直至智能体决定输出最终推荐结果。采用GRPO算法进行强化学习训练，仅使用结果奖励函数。在三个Amazon评论数据集上的实验表明，MGFRec显著优于现有方法，验证了在真实物品空间推理的重要性。

### 主要创新

- 将单步锚定扩展为多步锚定，使LLM在推理过程中持续接入真实物品空间，逐步缩小搜索空间。
- 引入用户智能体，在每次锚定后提供模拟用户反馈，帮助推荐智能体更好地理解用户偏好。
- 采用GRPO算法进行强化学习训练，无需可训练的评论家模型，降低训练成本。
- 提出在推荐任务中从语言空间推理转向真实物品空间推理的新范式。

### 研究方法

论文提出MGFRec框架，包含推荐智能体和用户智能体。推荐智能体执行多轮“思考-锚定-回答”循环：首先基于用户交互历史和初始检索列表进行推理，生成候选物品标题；然后通过计算标题嵌入与物品嵌入的L2距离，检索最相关的10个物品；用户智能体根据交互历史和检索结果生成文本反馈。循环直至智能体决定输出最终推荐物品。训练采用GRPO算法，优化策略模型，奖励函数基于NDCG，并对格式错误的响应给予负奖励。训练时对非LLM生成的token进行掩码。

### 关键结果

MGFRec在Books、Movies and TV、CDs and Vinyl三个数据集上，在H@5、N@5、H@10、N@10、H@20、N@20指标上均优于所有基线模型。；消融实验表明，移除多步锚定、用户智能体反馈或召回模型均导致性能下降，其中多步锚定影响最大。；随着锚定次数增加，样本难度（基于物品流行度倒数）增大，表明多步锚定有助于发现长尾物品。；随着锚定次数增加，真实物品的平均排名逐渐降低，说明搜索空间逐步缩小。；训练过程中奖励曲线先快速上升后振荡收敛，响应长度逐渐增加。

### 技术栈

- Qwen2.5-1.5B-Instruction作为骨干模型
- gte-Qwen2-1.5B-instruct用于物品标题嵌入
- SASRec作为初始检索器
- GRPO（Group Relative Policy Optimization）强化学习算法
- L2距离用于计算嵌入相似度
- NDCG作为奖励函数
- GPT-4.1-nano-2025-04-14作为用户智能体

### 方法优势

- 创新性地将推理从语言空间扩展到真实物品空间，通过多步锚定有效缓解了过度解读和偏离真实物品的问题。
- 引入用户智能体提供过程反馈，增强了推荐智能体对用户偏好的理解。
- 采用GRPO算法，无需训练评论家模型，降低了计算成本。
- 在多个数据集上取得了显著优于现有方法的结果，验证了方法的有效性。

### 主要局限

- 用户智能体相对简单，可能无法完全模拟真实用户行为，反馈质量有待提升。
- 当前锚定仅基于物品标题，未利用物品的其他属性（如类别、风格、作者等），限制了锚定的灵活性。
- 随着锚定次数增加，响应长度增长，推理时间增加，存在性能与计算成本的权衡。
- 实验仅在Amazon评论数据集上进行，泛化性有待进一步验证。

### 与当前研究方向的关联

推荐系统：论文聚焦于推荐任务，提出新的推荐框架。；大语言模型：核心使用LLM进行推理和生成。；强化学习：采用GRPO算法进行训练。；推荐智能体：构建了推荐智能体和用户智能体进行多轮交互。；序列推荐：输入为用户交互历史序列。；生成式推荐：LLM生成推荐物品标题。

---

_知识库更新时间：2026-07-24T04:05:55.201928_
