---
title: "Towards A Tri-View Diffusion Framework for Recommendation"
paper_id: "https://doi.org/10.1145/3770854.3780157"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 33.0
tags: ["paper", "recommender-systems"]
---

# Towards A Tri-View Diffusion Framework for Recommendation

[查看原文](https://dblp.org/rec/conf/kdd/ChenLSLG26) · [ArXiv](https://arxiv.org/abs/2511.20122)

## 一句话结论

> 论文从热力学视角分析现有扩散推荐模型，提出基于亥姆霍兹自由能最大化的三视图扩散框架，并设计各向异性去噪器和接受-拒绝Gumbel采样以提升推荐准确性和鲁棒性。

## 论文信息

- **作者**：Ximing Chen 0002, Pui Ieng Lei, Yijun Sheng, Yanyan Liu 0003, Zhiguo Gong
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：33.0
- **DOI**：[https://doi.org/10.1145/3770854.3780157](https://doi.org/10.1145/3770854.3780157)

<details open>
<summary><strong>中文摘要</strong></summary>

扩散模型（Diffusion Models, DMs）近年来因其在推荐任务中的卓越潜力而备受关注。这主要源于其在提取、建模和生成全面用户偏好方面的突出能力。然而，以往的研究未能以严谨的视角审视DMs在推荐任务中的应用。本文首先从热力学角度通过实验探究了推荐模型的完备性。我们发现，现有基于DM的推荐模型通过最大化能量来运作，而经典推荐模型则通过降低熵来运作。基于这一发现，我们提出了一种极简扩散框架，通过最大化亥姆霍兹自由能（Helmholtz free energy）将这两个因素整合在一起。同时，为促进优化，我们的反向过程配备了一个精心设计的去噪器，以保持固有的各向异性，该各向异性在二分图（bipartite graphs）背景下衡量用户-物品的互相关性。最后，我们采用接受-拒绝Gumbel采样过程（Acceptance-Rejection Gumbel Sampling Process, AR-GSP），优先处理数量远超其他交互的未观测交互，以增强模型鲁棒性。AR-GSP集成了接受-拒绝采样，以确保为通用推荐任务提供高质量难负样本，并采用时间步依赖的Gumbel Softmax（timestep-dependent Gumbel Softmax）来处理扩散模型的自适应采样策略。理论分析与大量实验表明，我们提出的框架在准确性和效率方面均显著优于基线模型。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Diffusion models (DMs) have recently gained significant interest for their exceptional potential in recommendation tasks. This stems primarily from their prominent capability in distilling, modeling, and generating comprehensive user preferences. However, previous work fails to examine DMs in recommendation tasks through a rigorous lens. In this paper, we first experimentally investigate the completeness of recommender models from a thermodynamic view. We reveal that existing DM-based recommender models operate by maximizing the energy, while classic recommender models operate by reducing the entropy. Based on this finding, we propose a minimalistic diffusion framework that incorporates both factors via the maximization of Helmholtz free energy. Meanwhile, to foster the optimization, our reverse process is armed with a well-designed denoiser to maintain the inherent anisotropy, which measures the user-item cross-correlation in the context of bipartite graphs. Finally, we adopt an Acceptance-Rejection Gumbel Sampling Process (AR-GSP) to prioritize the far-outnumbered unobserved interactions for model robustness. AR-GSP integrates an acceptance-rejection sampling to ensure high-quality hard negative samples for general recommendation tasks, and a timestep-dependent Gumbel Softmax to handle an adaptive sampling strategy for diffusion models. Theoretical analyses and extensive experiments demonstrate that our proposed framework has distinct superiority over baselines in terms of accuracy and efficiency.

</details>

---

_知识库更新时间：2026-07-29T03:56:18.947380_
