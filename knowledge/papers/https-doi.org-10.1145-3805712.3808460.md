---
title: "扩展搜索相关性：利用LLM生成的判断增强应用商店排序"
paper_id: "https://doi.org/10.1145/3805712.3808460"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 41.0
tags: ["paper", "recommender-systems"]
---

# 扩展搜索相关性：利用LLM生成的判断增强应用商店排序

> **英文原标题**：Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments

[查看原文](https://dblp.org/rec/conf/sigir/Christakopoulou26) · [ArXiv](https://arxiv.org/abs/2602.23234)

## 一句话结论

> 该论文通过微调LLM生成文本相关性标签，解决了大规模搜索排序中专家标签稀缺的问题，显著提升了App Store排序的转化率。

## 论文信息

- **作者**：Evangelia Christakopoulou, Vivekkumar Patel, Hemanth Velaga, Sandip Gaikwad
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：41.0
- **DOI**：[https://doi.org/10.1145/3805712.3808460](https://doi.org/10.1145/3805712.3808460)

<details open>
<summary><strong>中文摘要</strong></summary>

大规模商业搜索系统通过优化相关性来驱动成功的会话，帮助用户找到他们想要的内容。为了最大化相关性，我们利用两个互补的目标：行为相关性（用户倾向于点击或下载的结果）和文本相关性（结果与查询在语义上的匹配程度）。一个长期存在的挑战是，相对于丰富的行为相关性标签，专家提供的文本相关性标签十分稀缺。我们首先通过系统评估大语言模型（LLM）配置来解决这一问题，发现一个经过专门微调的模型在提供高相关性标签方面显著优于一个规模更大的预训练模型。利用该模型作为人工标注的增效器，我们生成了数百万个文本相关性标签，以克服数据稀缺问题。我们证明，将这些文本相关性标签引入生产级排序器后，帕累托前沿（Pareto frontier）发生了显著外移：离线NDCG在行为相关性上得到提升，同时文本相关性也得到增强。这些离线收益通过全球范围内的App Store排序器A/B测试得到了验证，结果显示转化率统计显著提升了+0.24%，其中尾部查询（tail queries）的性能提升最为显著——在新的文本相关性标签提供了可靠信号的情况下，弥补了行为相关性标签的缺失。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Large-scale commercial search systems optimize for relevance to drive successful sessions that help users find what they are looking for. To maximize relevance, we leverage two complementary objectives: behavioral relevance (results users tend to click or download) and textual relevance (a result's semantic fit to the query). A persistent challenge is the scarcity of expert-provided textual relevance labels relative to abundant behavioral relevance labels. We first address this by systematically evaluating LLM configurations, finding that a specialized, fine-tuned model significantly outperforms a much larger pre-trained one in providing highly relevant labels. Using this model as a force multiplier for human annotation, we generate millions of textual relevance labels to overcome the data scarcity. We show that augmenting our production ranker with these textual relevance labels leads to a significant outward shift of the Pareto frontier: offline NDCG improves for behavioral relevance while simultaneously increasing for textual relevance. These offline gains were validated by a worldwide A/B test on the App Store ranker, which demonstrated a statistically significant +0.24% increase in conversion rate, with the most substantial performance gains occurring in tail queries, where the new textual relevance labels provide a robust signal in the absence of reliable behavioral relevance labels.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对大规模商业搜索系统中文本相关性标签稀缺的问题，提出利用LLM作为离线标注工具生成数百万文本相关性标签，以增强多目标排序器的训练。作者首先系统评估了多种LLM配置，发现经过微调的3B参数模型在生成高质量标签方面显著优于更大的预训练模型。随后，将生成的标签作为额外训练数据加入生产排序器，离线评估显示NDCG指标在行为相关性和文本相关性上均得到提升，实现了帕累托前沿的外移。在线A/B测试表明，该方法在全球应用商店排序器上带来了+0.24%的转化率提升，尤其在长尾查询上效果显著。

### 主要创新

- 系统评估了多种LLM配置（预训练vs微调、不同参数量、零样本vs少样本），确定微调小模型在相关性标注任务上优于大预训练模型。
- 利用微调LLM生成数百万文本相关性标签，作为人类标注的“力量倍增器”，大幅扩展训练数据。
- 将LLM生成的标签融入多目标排序器训练，实现了行为相关性和文本相关性的帕累托前沿外移。
- 通过离线评估和全球在线A/B测试验证了方法的有效性，并发现长尾查询的转化率提升最为显著。

### 研究方法

论文采用两阶段方法：首先，使用微调后的3B参数LLM对历史搜索日志中的查询-应用对生成点式文本相关性标签；然后，将这些标签与行为相关性标签（点击/下载）结合，通过数据混合（标量化）的方式训练多目标排序器。LLM标签生成使用少样本提示，标签为字符串形式的序数等级。

### 关键结果

微调3B模型（FT-3B）在预测人类标签上的F1得分为0.800，远优于预训练3B（0.287）和预训练30B（0.382）。；离线评估中，llm-augmented模型在文本相关性和行为相关性的NDCG@1、3、7上均优于prod模型。；在线A/B测试显示，llm-augmented模型带来+0.24%的转化率提升，且89%的商店fronts表现更优。；长尾查询的转化率提升幅度最大，而高频查询提升较小。

### 技术栈

- LLM：内部3B和30B参数模型（预训练和微调）
- 提示策略：零样本、少样本提示；字符串标签
- 多目标优化：标量化（数据混合）
- 评估指标：NDCG@k、精确率、召回率、F1、转化率

### 方法优势

- 在工业规模上验证了LLM-as-a-Judge范式的有效性，具有实际应用价值。
- 方法简单有效，无需修改排序器架构，仅通过扩充训练数据即可提升性能。
- 离线与在线实验相结合，结果可靠。
- 对长尾查询的改进具有实际意义，解决了数据稀疏问题。

### 主要局限

- 仅使用了点式标签，未探索成对或列表式标签生成。
- 微调仅针对3B模型，未尝试微调30B模型。
- 未详细讨论LLM生成标签的潜在偏差或错误传播问题。
- 实验仅在应用商店场景下进行，泛化性有待验证。

### 与当前研究方向的关联

论文与“LLM与推荐系统结合”、“排序与重排”、“工业落地”高度相关，直接涉及LLM生成标签用于排序模型训练，并在工业环境中验证。与“CTR/CVR预测”间接相关（转化率指标）。与“用户建模”、“多模态推荐”等关键词相关性较低。

---

_知识库更新时间：2026-07-23T04:05:05.423278_
