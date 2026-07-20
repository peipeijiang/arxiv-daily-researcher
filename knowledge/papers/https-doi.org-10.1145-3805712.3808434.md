---
title: "MMRM：一种用于电商搜索产品排序的多重多模态表示模型"
paper_id: "https://doi.org/10.1145/3805712.3808434"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 65.0
tags: ["paper", "recommender-systems"]
---

# MMRM：一种用于电商搜索产品排序的多重多模态表示模型

> **英文原标题**：MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce Search

[查看原文](https://dblp.org/rec/conf/sigir/ChenSLCXWZ26) · [ArXiv](https://arxiv.org/abs/2607.11030) · [Semantic Scholar](https://www.semanticscholar.org/paper/d9b480006cdd6f19543a346dfcd50765742c6c7e)

## 一句话结论

> 提出MMRM模型，通过多任务对齐MLLM与多种协同信号生成多模态物品表示，并利用该表示在排序模型中进行用户行为建模，显著提升电商搜索排序效果。

## 论文信息

- **作者**：Zhen-Lin Chen, Maosen Sheng, Peng Lin, Jianmin Chen, Zhuojian Xiao, Dongyue Wang, Xiwei Zhao
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：65.0
- **DOI**：[https://doi.org/10.1145/3805712.3808434](https://doi.org/10.1145/3805712.3808434)

<details open>
<summary><strong>中文摘要</strong></summary>

多模态信息对于电子商务搜索排序至关重要。现有工作通常通过协同信号微调通用多模态大语言模型（MLLMs）来利用多模态数据，随后将所得表示作为商品特征集成到排序模型中。尽管这些方法有效，但仍面临两个主要局限：（1）它们依赖单一协同信号进行MLLM微调，未能利用多任务排序所需的多源异构信号；（2）它们将多模态表示视为排序模型中的常规商品特征，未能充分利用其在用户行为建模中的潜在能力。为解决上述问题，我们提出多路多模态表示模型（MMRM），这是一个将MLLMs与多样化协同信号对齐的统一框架。通过采用共享主干网络并配备任务特定令牌与投影层，MMRM能够同时从多个信号中学习，并在单次推理过程中生成全面的多路商品表示。此外，我们在排序模型中引入多路用户表示策略，该策略利用多路商品表示，通过基于搜索的行为序列建模推导出任务特定的用户表示。大量实验证明了MMRM卓越的效率与效果。值得注意的是，MMRM已成功部署于京东电子商务搜索引擎，为每日数百万用户带来了显著的性能提升。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multimodal information is pivotal for e-commerce search ranking. Existing works leverage multimodal data typically by fine-tuning general Multimodal Large Language Models (MLLMs) via collaborative signals, subsequently integrating the derived representations into ranking models as item features. Despite their efficacy, these methods face two primary limitations: (1) they rely on a single collaborative signal for MLLM fine-tuning, failing to exploit the heterogeneous signals essential for multitask ranking; and (2) they treat multimodal representations as regular item features in ranking models, underutilizing their latent potential for user behavior modeling. To address these challenges, we propose the Multiplex Multimodal Representation Model (MMRM), a unified framework that aligns MLLMs with diverse collaborative signals. By employing a shared backbone with task-specific tokens and projection layers, MMRM simultaneously learns from multiple signals and generates comprehensive multiplex item representations in a single inference pass. Furthermore, we introduce a multiplex user representation strategy in ranking models, which derives task-specific user representations via search-based behavior sequence modeling leveraging multiplex item representations. Extensive experiments demonstrate MMRM's superior efficiency and effectiveness. Notably, MMRM has been successfully deployed in the JD e-commerce search engine, yielding significant performance gains for millions of daily users.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出MMRM框架，旨在解决现有电商搜索排序中多模态表示学习的两大局限：一是仅依赖单一协同信号微调多模态大语言模型，未能利用多任务排序所需的异质信号；二是将多模态表示作为常规特征，未充分挖掘其在用户行为建模中的潜力。MMRM通过共享骨干网络与任务特定token及投影层，同时对齐四种协同信号（查询-点击、点击-点击、加购-加购、下单-下单），在一次推理中生成多重解耦的物品表示。此外，在排序模型中引入多重用户表示策略，利用多重物品表示通过搜索行为序列建模得到任务特定用户表示。离线实验表明MMRM在检索和排序指标上优于单任务和朴素多任务基线；在线A/B测试中，基于MMRM的排序模型在京东搜索上使UCTR、UACR、UCVR分别提升0.42%、0.37%、0.35%。

### 主要创新

- 提出MMRM统一框架，通过共享骨干网络与任务特定token及投影层，同时对齐四种异质协同信号，高效生成多重解耦物品表示。
- 在排序模型中引入多重用户表示策略，利用多重物品表示通过搜索行为序列建模得到任务特定用户表示，提升多任务排序性能。
- 采用图构建方法从用户行为序列中提取细粒度物品-物品关系，并设计硬负采样策略增强对比学习。
- 利用GradCache技术实现大batch size训练，使4B参数模型在单机H800上达到4096 batch size。

### 研究方法

首先，从用户行为日志中构建四种三元组数据集：q2i_click（查询-点击）、i2i_click（点击-点击）、i2i_cart（加购-加购）、i2i_order（下单-下单），其中i2i数据集通过图构建方法生成，并采用硬负采样。然后，MMRM使用Qwen3-VL-4B-Instruct作为骨干，输入物品图像、标题和属性，并附加四个任务特定token（[SEARCH]、[CLICK]、[CART]、[ORDER]），通过任务特定MLP投影得到任务特定表示。训练时混合四个数据集，采用对比学习损失，每个任务仅使用其正样本对，其他任务样本作为批内负样本。在排序模型中，对每个任务，使用对应任务的多模态嵌入表通过软搜索从用户行为序列中提取top-K相关子序列，再通过多头目标注意力得到任务特定用户表示，最后通过MMoE和任务塔进行多任务预测。

### 关键结果

表示模型评估：MMRM在四个测试集上的F1@5和NDCG@5均优于单任务模型和Vanilla-Multi基线，例如在q2i_click任务上F1@5为0.2055（单任务最佳0.1985），i2i_order任务上F1@5为0.0934（单任务最佳0.0908）。排序模型评估：基于MMRM所有任务嵌入的SIM_soft(item_MMRM[ALL])在CTR、ACR、CVR的GAUC上分别达到0.7037、0.7190、0.6875，优于使用单一嵌入的变体。在线A/B测试：相比基线，UCTR提升0.42%，UACR提升0.37%，UCVR提升0.35%。

### 技术栈

- Qwen3-VL-4B-Instruct（多模态大语言模型）
- 对比学习（Contrastive Learning）
- GradCache（梯度缓存技术）
- FlashAttention-2
- Adam优化器
- AdamW优化器
- MMoE（Multi-gate Mixture-of-Experts）
- 多头目标注意力（Multi-Head Target Attention，类似DIN）
- 软搜索（Soft-Search）
- 图构建方法（基于时间窗口的邻接图）
- 硬负采样（Hard Negative Sampling）

### 方法优势

- 创新性地将多任务学习与多模态表示结合，通过任务特定token实现多重解耦表示，有效利用异质协同信号。
- 在排序模型中引入多重用户表示，显著提升多任务排序性能，且在线部署验证了实际效果。
- 采用GradCache技术解决大模型训练中的batch size瓶颈，实现高效训练。
- 实验设计全面，包括离线表示评估、排序评估和在线A/B测试，结果充分。

### 主要局限

- 论文未讨论不同任务token之间的交互或共享信息，可能仍有信息冗余。
- MMRM依赖预训练MLLM，计算资源需求较高，可能不适用于资源受限场景。
- 在线实验仅报告了相对提升百分比，未提供绝对数值或统计显著性检验。
- 未与更多最新多模态推荐方法（如QARM等）进行对比。

### 与当前研究方向的关联

论文高度相关于多模态推荐、排序与重排、用户建模、CTR/CVR预测以及工业落地。MMRM聚焦于多模态表示学习与多任务排序，直接应用于电商搜索排序场景，并已在京东部署。

---

_知识库更新时间：2026-07-20T04:18:26.517954_
