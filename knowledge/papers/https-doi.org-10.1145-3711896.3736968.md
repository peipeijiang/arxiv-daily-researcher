---
title: "FindRec：基于Stein引导的熵流多模态序列推荐"
paper_id: "https://doi.org/10.1145/3711896.3736968"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 56.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Image Retrieval and Classification Techniques"]
---

# FindRec：基于Stein引导的熵流多模态序列推荐

> **英文原标题**：FindRec: Stein-Guided Entropic Flow for Multi-Modal Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/kdd/0001XW0YWYGX25)

## 一句话结论

> The paper proposes FindRec, a framework for multi-modal sequential recommendation that uses Stein-guided entropic flow to coordinate multimodal features and ID streams, achieving superior performance on real-world datasets.

## 论文信息

- **作者**：Maolin Wang, Yutian Xiao, B. L. Wang, Sheng Zhang, Shanshan Ye, Wanyu Wang, Hongzhi Yin, Ruocheng Guo, Zenglin Xu
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：56.0
- **DOI**：[https://doi.org/10.1145/3711896.3736968](https://doi.org/10.1145/3711896.3736968)

<details open>
<summary><strong>中文摘要</strong></summary>

现代推荐系统在处理多模态序列数据时面临重大挑战，尤其是在时间动态建模和信息流协调方面。传统方法难以应对异构特征之间的分布差异以及多模态信号中的噪声干扰。我们提出了FindRec（灵活统一的多模态序列推荐信息解耦框架），引入了一种新颖的“信息流-控制-输出”范式。该框架包含两项关键创新：（1）基于Stein核的集成信息协调模块（IICM），从理论上保证了多模态特征与ID流之间的分布一致性；（2）一种跨模态专家路由机制，可根据上下文相关性自适应地过滤和组合多模态特征。我们的方法利用多头子空间分解实现路由稳定性，并采用RBF-Stein梯度进行无偏分布对齐，同时通过线性复杂度的Mamba层增强时间建模效率。在三个真实世界数据集上的大量实验表明，FindRec在性能上优于最先进的基线方法，尤其在处理长序列和含噪多模态输入方面表现突出。我们的框架通过模块化设计，既提升了推荐准确性，也增强了模型的可解释性。实现代码已匿名公开，便于复现：https://github.com/Applied-Machine-Learning-Lab/FindRec。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern recommendation systems face significant challenges in processing multimodal sequential data, particularly in temporal dynamics modeling and information flow coordination. Traditional approaches struggle with distribution discrepancies between heterogeneous features and noise interference in multimodal signals. We propose FindRec (Flexible unified information disentanglement for multi-modal sequential Rec ommendation), introducing a novel ''information flow-control-output'' paradigm. The framework features two key innovations: (1) A Stein kernel-based Integrated Information Coordination Module (IICM) that theoretically guarantees distribution consistency between multimodal features and ID streams, and (2) A cross-modal expert routing mechanism that adaptively filters and combines multimodal features based on their contextual relevance. Our approach leverages multi-head subspace decomposition for routing stability and RBF-Stein gradient for unbiased distribution alignment, enhanced by linear-complexity Mamba layers for efficient temporal modeling. Extensive experiments on three real-world datasets demonstrate FindRec's superior performance over state-of-the-art baselines, particularly in handling long sequences and noisy multimodal inputs. Our framework achieves both improved recommendation accuracy and enhanced model interpretability through its modular design. The implementation code is available anonymously online for easy reproducibility https://github.com/Applied-Machine-Learning-Lab/FindRec.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

现代推荐系统在处理多模态序列数据时面临时间动态建模和信息流协调的挑战，传统方法难以应对异构特征分布差异和噪声干扰。为此，本文提出FindRec框架，引入“信息流-控制-输出”新范式，包含两个关键创新：基于Stein核的集成信息协调模块（IICM）从理论上保证多模态特征与ID流之间的分布一致性，以及跨模态专家路由机制根据上下文相关性自适应过滤和组合多模态特征。方法利用多头子空间分解提高路由稳定性，采用RBF-Stein梯度实现无偏分布对齐，并集成线性复杂度的Mamba层进行高效时间建模。在三个真实数据集上的大量实验表明，FindRec在长序列和噪声多模态输入场景下优于现有基线，同时通过模块化设计提升了推荐准确性和模型可解释性。代码已公开。

### 主要创新

- 提出“信息流-控制-输出”新范式，统一多模态序列推荐流程。
- 设计基于Stein核的集成信息协调模块（IICM），理论保证多模态特征与ID流分布一致性。
- 引入跨模态专家路由机制，根据上下文相关性自适应过滤和组合多模态特征。
- 采用多头子空间分解增强路由稳定性，并利用RBF-Stein梯度实现无偏分布对齐。
- 集成线性复杂度的Mamba层，高效处理长序列时间建模。

### 研究方法

论文采用理论分析与实证验证相结合的方法。首先，提出Stein核函数用于多模态特征与ID流的分布对齐，并证明其理论性质。其次，设计跨模态专家路由机制，通过多头子空间分解实现稳定路由，并利用RBF-Stein梯度进行无偏分布对齐。最后，采用Mamba层进行序列建模，以线性复杂度处理长序列。实验在三个真实数据集上进行，与多个基线比较，验证模型性能。

### 关键结果

在三个真实世界数据集上的实验表明，FindRec在长序列和噪声多模态输入场景下优于现有最先进基线，同时通过模块化设计提升了推荐准确性和模型可解释性。

### 技术栈

- Stein核函数
- RBF-Stein梯度
- 多头子空间分解
- 跨模态专家路由
- Mamba层
- 线性复杂度序列建模

### 方法优势

- 理论保证：IICM模块提供分布一致性的理论保证。
- 创新范式：提出“信息流-控制-输出”新范式，具有通用性。
- 高效性：Mamba层实现线性复杂度，适合长序列。
- 可解释性：模块化设计增强模型可解释性。
- 实验充分：在多个数据集上验证，代码公开。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估模型在极端场景下的表现、计算开销、超参数敏感性等细节。

### 与当前研究方向的关联

论文与多模态推荐、序列推荐、推荐系统、用户建模、时间动态建模等关键词高度相关。其提出的多模态特征融合、序列建模方法直接针对多模态序列推荐问题，同时涉及信息流协调和噪声处理，与推荐系统的鲁棒性相关。

## 代码与复现

- [Applied-Machine-Learning-Lab/FindRec](https://github.com/Applied-Machine-Learning-Lab/FindRec)：official，置信度 70，Stars 11

---

_知识库更新时间：2026-08-16T02:20:30.031009_
