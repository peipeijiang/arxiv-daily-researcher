---
title: "STAR-Rec：在序列推荐中实现长度变化与模式多样性的和谐统一"
paper_id: "https://doi.org/10.1145/3726302.3730087"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 38.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Customer churn and segmentation"]
---

# STAR-Rec：在序列推荐中实现长度变化与模式多样性的和谐统一

> **英文原标题**：STAR-Rec: Making Peace with Length Variance and Pattern Diversity in Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/00010GWW0Y0025)

## 一句话结论

> STAR-Rec通过结合偏好感知注意力、状态空间建模和混合专家，有效处理序列推荐中的长度变化和模式多样性，在多个数据集上超越现有方法。

## 论文信息

- **作者**：Maolin Wang, Sheng Zhang, Ruocheng Guo, Wanyu Wang, Xuetao Wei, Zitao Liu, Hongzhi Yin, Yi Chang, Xiangyu Zhao
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：38.0
- **DOI**：[https://doi.org/10.1145/3726302.3730087](https://doi.org/10.1145/3726302.3730087)

<details open>
<summary><strong>中文摘要</strong></summary>

近期提出的深度序列推荐模型往往难以有效建模用户行为的关键特征，尤其是在处理序列长度变化和捕捉多样化交互模式方面。我们提出了STAR-Rec，一种新颖的架构，通过序列级混合专家框架，将偏好感知注意力与状态空间建模协同结合。STAR-Rec通过以下方式解决上述挑战：（1）采用偏好感知注意力来捕捉本质上相似的项目关系以及多样化偏好；（2）利用状态空间建模以线性复杂度高效处理可变长度序列；（3）引入混合专家组件，将不同的行为模式自适应地路由至专门的专家，从而同时处理聚焦于特定类别的浏览行为和多样化的类别探索模式。我们从理论上证明了在推荐场景中，状态空间模型与注意力机制可以自然统一，其中状态空间模型通过状态压缩捕捉时间动态，而注意力机制则同时建模相似与多样的项目关系。在四个真实世界数据集上的大量实验表明，STAR-Rec在多种评估指标上持续优于最先进的序列推荐方法，尤其是在涉及多样化用户行为和不同序列长度的场景中表现突出。实现代码已匿名公开，便于复现实验结果。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recent deep sequential recommendation models often struggle to effectively model key characteristics of user behaviors, particularly in handling sequence length variations and capturing diverse interaction patterns. We propose STAR-Rec, a novel architecture that synergistically combines preference-aware attention and state-space modeling through a sequence-level mixture-of-experts framework. STAR-Rec addresses these challenges by: (1) employing preference-aware attention to capture both inherently similar item relationships and diverse preferences (2) utilizing state-space modeling to efficiently process variable-length sequences with linear complexity, and (3) incorporating a mixture-of-experts component that adaptively routes different behavioral patterns to specialized experts, handling both focused category-specific browsing and diverse category exploration patterns. We theoretically demonstrate how the state space model and attention mechanisms can be naturally unified in recommendation scenarios, where SSM captures temporal dynamics through state compression while attention models both similar and diverse item relationships. Extensive experiments on four real-world datasets demonstrate that STAR-Rec consistently outperforms state-of-the-art sequential recommendation methods, particularly in scenarios involving diverse user behaviors and varying sequence lengths. The implementation code is available anonymously online for easy reproducibility.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

近期深度序列推荐模型在处理用户行为的关键特征时，尤其是在处理序列长度变化和捕捉多样化交互模式方面，常常面临挑战。为此，本文提出STAR-Rec，一种新颖的架构，通过序列级混合专家框架，协同结合偏好感知注意力与状态空间建模。STAR-Rec通过以下方式解决上述挑战：(1) 采用偏好感知注意力，捕捉内在相似的项目关系及多样化偏好；(2) 利用状态空间建模，以线性复杂度高效处理变长序列；(3) 引入混合专家组件，自适应地将不同行为模式路由至专门专家，同时处理聚焦类目浏览和多样化类目探索模式。理论上，本文论证了状态空间模型与注意力机制在推荐场景中的自然统一，其中SSM通过状态压缩捕捉时间动态，而注意力则建模相似与多样项目关系。在四个真实数据集上的大量实验表明，STAR-Rec在多种场景下均优于最先进的序列推荐方法，尤其在用户行为多样和序列长度变化的情况下。实现代码已匿名公开，便于复现。

### 主要创新

- 提出STAR-Rec架构，将偏好感知注意力与状态空间建模通过序列级混合专家框架协同结合。
- 偏好感知注意力机制，同时捕捉相似项目关系与多样化用户偏好。
- 利用状态空间模型高效处理变长序列，实现线性复杂度。
- 混合专家组件自适应路由不同行为模式至专门专家，处理聚焦与多样化探索模式。
- 理论上论证SSM与注意力机制在推荐场景中的自然统一。

### 研究方法

论文提出STAR-Rec架构，包含三个关键组件：偏好感知注意力、状态空间模型和混合专家。偏好感知注意力用于捕捉项目间相似性和用户偏好多样性；状态空间模型以线性复杂度处理变长序列，通过状态压缩捕捉时间动态；混合专家框架自适应路由不同行为模式至专门专家。整体通过序列级混合专家框架整合，并进行了理论分析。实验在四个真实数据集上评估，与最先进方法对比。

### 关键结果

在四个真实数据集上的实验表明，STAR-Rec在多种场景下均优于最先进的序列推荐方法，尤其在用户行为多样和序列长度变化的情况下。

### 技术栈

- 偏好感知注意力、状态空间模型（SSM）、混合专家（MoE）、序列级混合专家框架。

### 方法优势

- 创新性地结合注意力与状态空间模型，解决序列长度变化和模式多样性问题。
- 理论分析提供了SSM与注意力统一的基础。
- 实验在多个真实数据集上验证，显示优越性能。
- 代码公开，便于复现。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估方法细节、实验设置、消融研究等，可能存在的局限性包括计算复杂度、对超参数的敏感性、专家数量选择等，但摘要未提供。

### 与当前研究方向的关联

论文与序列推荐高度相关，直接针对序列推荐中的长度变化和模式多样性问题；同时涉及用户建模（偏好感知）、生成式推荐（状态空间建模）等方向，与推荐系统前沿研究紧密相关。

---

_知识库更新时间：2026-08-02T04:11:29.699868_
