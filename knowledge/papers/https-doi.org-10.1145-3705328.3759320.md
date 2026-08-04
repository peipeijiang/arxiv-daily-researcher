---
title: "基于切片 Wasserstein 距离正则化的隐式反馈推荐系统去偏"
paper_id: "https://doi.org/10.1145/3705328.3759320"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Generative Adversarial Networks and Image Synthesis", "Recommender Systems and Techniques", "Medical Image Segmentation Techniques"]
---

# 基于切片 Wasserstein 距离正则化的隐式反馈推荐系统去偏

> **英文原标题**：Debiasing Implicit Feedback Recommenders via Sliced Wasserstein Distance-based Regularization

[查看原文](https://dblp.org/rec/conf/recsys/EscobedoPS25) · [Semantic Scholar](https://www.semanticscholar.org/paper/7f512e83fbb4141946caaa91d73f655ee3bff1f4)

## 一句话结论

> 该论文提出一种基于切片Wasserstein距离正则化的方法，在隐式反馈推荐系统中缓解用户表示中的敏感属性偏差，同时保持推荐准确性。

## 论文信息

- **作者**：G. Escobedo, David Penz, Markus Schedl
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3705328.3759320](https://doi.org/10.1145/3705328.3759320)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐模型在训练过程中，常常会在其学习到的表示中编码用户的敏感属性（如性别或年龄），从而导致有偏见的（例如刻板印象的）推荐结果及潜在的隐私风险。为解决这一问题，以往研究主要集中于采用对抗训练，使得用户表示对敏感属性保持不变。然而，对抗方法可能因额外的网络参数而出现不稳定性，并且计算成本较高。另一种替代方案是使用正则化损失，在训练过程中最小化不同人口统计群体之间的分布差异。特别是，切片 Wasserstein 距离（SWD）通过直接对齐各群体用户表示的分布，提供了一种计算高效且稳定的缓解偏差的解决方案。我们遵循这一替代策略，提出了一种处理过程中的方法，利用基于 SWD 的正则化来缓解隐式反馈推荐系统中用户表示所编码的偏差。我们针对用户性别去偏进行了大量实验，分别使用了来自电影、音乐和新闻领域的三个数据集：ML-1M、LFM2b-DB 和 EB-NeRD。结果表明，基于 SWD 的正则化是一种有效缓解用户表示中编码偏差的方法，同时能保持具有竞争力的推荐准确性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recommendation models often encode users’ sensitive attributes (e.g., gender or age) in their learned representations during training, leading to biased (e.g., stereotypical) recommendations and potential privacy risks. To address this, previous research has predominantly focused on adversarial training to make user representations invariant to sensitive attributes. However, adversarial methods can be unstable and computationally expensive due to additional network parameters. An alternative approach is the use of regularization losses that minimize distributional discrepancies between different demographic groups during training. In particular, the Sliced Wasserstein Distance (SWD) provides a computationally efficient and stable solution for mitigating bias by directly aligning the distributions of user representations across groups. We follow this alternative strategy and propose an in-processing approach to mitigate encoded biases in user representations of implicit feedback-based recommender systems by using SWD-based regularization. We perform extensive experiments targeting the debiasing of the users’ gender on three datasets ML-1M, LFM2b-DB, and EB-NeRD from the movie, music, and news domains, respectively. Our results indicate that SWD-based regularization is an effective approach for mitigating encoded biases in user representations while keeping competitive recommendation accuracy.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

推荐模型在训练过程中常会编码用户的敏感属性（如性别、年龄），导致推荐结果存在偏见并带来隐私风险。以往研究主要采用对抗训练来使用户表示对敏感属性不变，但对抗方法可能不稳定且计算成本高。本文提出一种基于切片 Wasserstein 距离（SWD）的正则化方法，通过直接对齐不同人口统计组的用户表示分布来缓解偏差。该方法属于处理过程中的方法，适用于隐式反馈推荐系统。作者在三个数据集（ML-1M、LFM2b-DB、EB-NeRD）上针对性别去偏进行了实验，结果表明 SWD 正则化能有效缓解用户表示中的编码偏差，同时保持有竞争力的推荐准确性。

### 主要创新

- 提出使用切片 Wasserstein 距离（SWD）作为正则化项来缓解推荐系统中的用户表示偏差，替代对抗训练方法。
- 将 SWD 正则化应用于隐式反馈推荐系统，实现处理过程中的去偏。
- 在多个领域（电影、音乐、新闻）的数据集上验证了方法的有效性。
- 在保持推荐准确性的同时有效降低用户表示中的敏感属性编码。

### 研究方法

本文采用基于 SWD 正则化的处理中方法。具体地，在训练推荐模型时，除了原有的推荐损失外，增加一个 SWD 正则化项，用于最小化不同敏感属性组（如男性和女性）的用户表示分布之间的差异。通过优化该联合损失，使得模型学习到的用户表示对敏感属性不敏感，从而减少偏差。

### 关键结果

实验结果表明，SWD 正则化能有效缓解用户表示中的编码偏差，同时保持有竞争力的推荐准确性。

### 技术栈

- 切片 Wasserstein 距离（SWD）
- 正则化方法
- 隐式反馈推荐系统

### 方法优势

- 方法简单有效，避免了对抗训练的不稳定性和额外计算开销。
- 在多个领域的数据集上验证了方法的泛化性。
- 在去偏的同时保持了推荐准确性，具有实际应用价值。

### 主要局限

- 摘要未提供具体的局限性分析。

### 与当前研究方向的关联

该论文与推荐系统的公平性高度相关，属于推荐系统公平性研究中的去偏方法，同时涉及用户建模和隐式反馈推荐，与关键词“推荐系统公平性”和“用户建模”紧密相关。

## 代码与复现

- [gescobedo/swd-recsys-2025](https://github.com/gescobedo/swd-recsys-2025)：likely，置信度 50，Stars 0

---

_知识库更新时间：2026-08-04T04:04:06.468769_
