---
title: "用于快速排序的强化投机解码"
paper_id: "https://doi.org/10.1145/3770854.3780197"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 62.0
tags: ["paper", "recommender-systems"]
---

# 用于快速排序的强化投机解码

> **英文原标题**：Reinforcement Speculative Decoding for Fast Ranking

[查看原文](https://dblp.org/rec/conf/kdd/DuWSZJ26) · [ArXiv](https://arxiv.org/abs/2505.20316)

## 一句话结论

> 提出强化投机解码方法，通过强化学习优化多轮排序修改策略，在满足延迟约束下加速LLM排序推理，在信息检索和推荐系统任务上验证有效性。

## 论文信息

- **作者**：Yingpeng Du, Tianjun Wei, Zhu Sun 0001, Jie Zhang 0002, Xun Jiang
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：62.0
- **DOI**：[https://doi.org/10.1145/3770854.3780197](https://doi.org/10.1145/3770854.3780197)

<details open>
<summary><strong>中文摘要</strong></summary>

大语言模型（LLMs）已被广泛应用于信息检索（IR）系统和推荐系统（RSs）等排序系统中。为缓解自回归解码的延迟问题，部分研究探索了采用单（首）令牌解码进行排序近似，但该方法在尾部位置存在严重的性能退化。尽管推测解码（SD）方法可通过在不同位置进行验证来弥补这一缺陷，但由于其从左到右的解码范式，在排序系统中仍面临挑战。首先，排序系统对延迟有严格限制，但SD方法中的验证轮次仍具有不可知性；其次，SD方法通常会丢弃前几轮中未被接受项的相关列表级排序知识，这阻碍了后续的多令牌预测，尤其是当候选令牌为未接受项时。本文提出一种面向大语言模型快速排序推理的强化推测解码方法。为满足排序系统的延迟要求，我们提出一种自上而下的解码范式，该范式通过智能体在受限预算下迭代修改排序序列。具体而言，我们设计了面向排序的策略优化方法，通过强化学习（RL）主动探索经大语言模型验证的最优多轮排序修改策略。为在受限预算下更好地逼近目标大语言模型，我们促使智能体在强化学习中充分利用经大语言模型跨轮验证的所有项的列表级排序知识，从而增强智能体的修改策略。更重要的是，我们论证了所提范式及实现的理论鲁棒性与优势。在信息检索与推荐系统任务上的实验表明，我们提出的方法具有有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large Language Models (LLMs) have been widely adopted in ranking systems such as information retrieval (IR) systems and recommender systems (RSs). To alleviate the latency of auto-regressive decoding, some studies explore the single (first) token decoding for ranking approximation, but they suffer from severe degradation in tail positions. Although speculative decoding (SD) methods can be a remedy with verification at different positions, they face challenges in ranking systems due to their left-to-right decoding paradigm. Firstly, ranking systems require strict latency constraints, but verification rounds in SD methods remain agnostic; Secondly, SD methods usually discard listwise ranking knowledge about unaccepted items in previous rounds, hindering future multi-token prediction, especially when candidate tokens are the unaccepted items. In this paper, we propose a Reinforcement Speculative Decoding method for fast ranking inference of LLMs. To meet the ranking systems' latency requirement, we propose an up-to-down decoding paradigm that employs an agent to iteratively modify the ranking sequence under a constrained budget. Specifically, we design a ranking-tailored policy optimization, actively exploring optimal multi-round ranking modification policy verified by LLMs via reinforcement learning (RL). To better approximate the target LLM under the constrained budget, we trigger the agent fully utilizing the listwise ranking knowledge about all items verified by LLMs across different rounds in RL, enhancing the modification policy of the agent. More importantly, we demonstrate the theoretical robustness and advantages of our paradigm and implementation. Experiments on both IR and RS tasks show the effectiveness of our proposed method.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出一种强化投机解码方法（RSD），用于加速大语言模型在排序系统中的推理。现有方法如单令牌解码在尾部位置性能严重下降，而投机解码虽能缓解但存在延迟不可控和忽略列表级排序知识的问题。RSD采用自顶向下的解码范式，通过强化学习训练轻量级智能体在有限预算内迭代修改排序序列。该方法利用列表级排序知识增强智能体策略，并理论证明了其鲁棒性。在信息检索和推荐系统任务上的实验表明，RSD显著优于现有方法。

### 主要创新

- 提出自顶向下的解码范式，在有限预算内迭代修改排序，满足排序系统的延迟约束。
- 设计排序定制的策略优化（RPO），通过强化学习主动探索最优的多轮排序修改策略。
- 利用跨轮次的列表级排序知识增强智能体策略，捕获令牌级和轮次级的依赖关系。
- 理论证明了方法的单调性和与GRPO的等价性，以及参考优势函数的无偏性和低方差。

### 研究方法

首先通过监督学习初始化策略网络，然后使用强化学习中的排序定制策略优化（RPO）进行微调。RPO并行采样多个轨迹，基于最终回报优化策略。智能体使用Transformer建模历史LLM编码的序列模式，产生确定性分数。优势函数采用参考优势（基于贪婪解码的参考模型）以降低方差。

### 关键结果

在MS MARCO和Quora（IR任务）以及ML-1M和Amazon-Games（RS任务）上，RSD在KT、SR、FD、KD指标上均显著优于所有基线，平均提升IR任务19.61%，RS任务12.39%。消融实验验证了RPO、列表级排序知识和参考优势的有效性。

### 技术栈

- Bradley-Terry概率模型
- Transformer
- 强化学习（RL）
- 组相对策略优化（GRPO）
- Spearman距离
- Kendall's Tau
- Spearman's Rho
- Footrule距离
- Kemeny距离

### 方法优势

- 提出新颖的自顶向下解码范式，有效解决排序系统的延迟约束。
- 强化学习框架能够主动探索最优策略，且理论分析扎实。
- 充分利用列表级排序知识，克服了现有SD方法忽略未接受项的问题。
- 实验全面，在多个数据集和LLM骨干上验证了有效性。

### 主要局限

- 策略在不同骨干或领域间迁移时可能性能下降，跨域泛化能力有待提升。
- 当候选物品数量较大时，Transformer网络和LLM编码成本呈二次增长，可能限制在大规模语料上的应用。

### 与当前研究方向的关联

论文聚焦于排序系统中的快速推理，涉及LLM与推荐系统结合、排序与重排、推荐智能体等关键词。方法采用强化学习优化排序策略，与推荐智能体相关；实验涵盖推荐系统任务，与生成式推荐、序列推荐等方向有交叉。

## 代码与复现

- [hemingkx/SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers)：likely，置信度 69，Stars 1283

---

_知识库更新时间：2026-07-29T03:56:18.947505_
