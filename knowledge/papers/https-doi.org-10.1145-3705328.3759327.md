---
title: "端到端时间间隔分段序列推荐"
paper_id: "https://doi.org/10.1145/3705328.3759327"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Image Retrieval and Classification Techniques"]
---

# 端到端时间间隔分段序列推荐

> **英文原标题**：End-to-End Time Interval-wise Segmentation for Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/KimKKSLC25a) · [Semantic Scholar](https://www.semanticscholar.org/paper/ae0b09397370e5ea6deb7357ff77dcd04e6b017f)

## 一句话结论

> This paper proposes TiSRec, a time interval-wise segmentation framework for sequential recommendation that dynamically divides user sequences into Local Preference Blocks to capture evolving preferences, outperforming state-of-the-art methods on four datasets.

## 论文信息

- **作者**：Misong Kim, Wooseung Kang, Gun-Woo Kim, Chie Hoon Song, Suwon Lee, Sang-Min Choi
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3705328.3759327](https://doi.org/10.1145/3705328.3759327)

<details open>
<summary><strong>中文摘要</strong></summary>

顺序推荐旨在基于用户的历史行为预测其下一次交互。尽管近期模型取得了显著成功，但它们往往忽略了交互之间的时间间隔，或依赖固定阈值进行会话分割，这可能导致次优结果。为解决这些局限，若干方法通过相对位置嵌入引入时间间隔，或基于固定阈值进行会话分割。然而，这些方法对阈值选择高度敏感，且容易产生不准确的分割。受上述挑战启发，我们提出了TiSRec，一种时间间隔感知的分割框架，通过选择显著的时间间隔将用户序列动态划分为局部偏好块（LPBs）。TiSRec通过块内与块间编码器捕捉用户偏好的演变。在四个真实世界数据集上的实验表明，TiSRec持续优于现有最先进方法，且消融研究证实了基于LPB建模的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation aims to predict a user's next interaction based on their historical behavior.While recent models have achieved remarkable success, they often overlook time intervals between interactions or rely on fixed thresholds for session segmentation, which can lead to suboptimal results.To address these limitations, several approaches incorporate time intervals via relative positional embeddings or session segmentation based on fixed thresholds.However, these methods are highly sensitive to threshold selection and are prone to inaccurate segmentation.Inspired by these challenges, we propose TiSRec, a Time Interval-wise Segmentation framework that dynamically divides user sequences into Local Preference Blocks (LPBs) by selecting significant time intervals.TiSRec captures evolving user preferences through intra-block and inter-block encoders.Experiments on four real-world datasets demonstrate that TiSRec consistently outperforms state-of-the-art methods, and ablation studies confirm the effectiveness of LPBbased modeling.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

序列推荐旨在根据用户历史行为预测下一次交互。现有模型虽取得显著成功，但常忽略交互间的时间间隔，或依赖固定阈值进行会话分段，导致次优结果。为解决这些问题，一些方法通过相对位置嵌入或基于固定阈值的会话分段来纳入时间间隔，但这些方法对阈值选择高度敏感且易产生不准确分段。受此启发，我们提出TiSRec，一种时间间隔分段框架，通过选择显著时间间隔将用户序列动态划分为局部偏好块（LPBs）。TiSRec通过块内和块间编码器捕捉用户偏好的演化。在四个真实数据集上的实验表明，TiSRec持续优于最先进方法，消融研究证实了基于LPB建模的有效性。

### 主要创新

- 提出时间间隔分段框架TiSRec，动态划分用户序列为局部偏好块（LPBs），避免固定阈值。
- 通过选择显著时间间隔实现自适应分段，提高分段准确性。
- 设计块内和块间编码器，分别捕捉局部偏好和偏好演化。
- 在多个真实数据集上验证了方法的有效性，优于现有方法。

### 研究方法

TiSRec框架首先根据时间间隔的显著性动态将用户序列划分为多个局部偏好块（LPBs），然后通过块内编码器捕捉每个块内的局部偏好，再通过块间编码器建模块之间的演化关系，最终生成用户表示用于预测下一次交互。

### 关键结果

在四个真实数据集上的实验表明，TiSRec持续优于最先进方法；消融研究证实了基于LPB建模的有效性。

### 技术栈

- 摘要未提供具体算法、工具或数学方法的细节。

### 方法优势

- 提出动态分段方法，避免固定阈值带来的不准确问题。
- 通过块内和块间编码器全面捕捉用户偏好及其演化。
- 在多个数据集上验证了方法的优越性。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法在极端时间间隔分布、计算复杂度或可扩展性方面的表现。

### 与当前研究方向的关联

该论文与序列推荐、用户建模、时间间隔建模等关键词高度相关，属于推荐系统领域的前沿研究。

---

_知识库更新时间：2026-08-25T02:16:23.899362_
