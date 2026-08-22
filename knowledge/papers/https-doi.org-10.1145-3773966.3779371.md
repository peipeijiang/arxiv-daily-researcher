---
title: "ChorusCVR: Chorus Supervision for Entire Space Post-Click Conversion Rate Modeling"
paper_id: "https://doi.org/10.1145/3773966.3779371"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 29.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Mobile Crowdsensing and Crowdsourcing", "Text and Document Classification Technologies"]
---

# ChorusCVR: Chorus Supervision for Entire Space Post-Click Conversion Rate Modeling

[查看原文](https://dblp.org/rec/conf/wsdm/ChengLXCXWJZLHG26) · [Semantic Scholar](https://www.semanticscholar.org/paper/7534a68a55e8de91ff4f8fbf4998b1ec865bb36c)

## 一句话结论

> The paper proposes ChorusCVR, a model with negative sample discrimination and soft alignment modules to debias CVR estimation in entire-space, validated on Kuaishou's e-commerce platform.

## 论文信息

- **作者**：Wei Cheng, Yucheng Lu, Boyang Xia, Jiangxia Cao, Kuan Xu, Ming-xing Wen, Wei Jiang, Jiaming Zhang, Zhaojie Liu, Liyin Hong, Kun Gai, Guorui Zhou
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：29.0
- **DOI**：[https://doi.org/10.1145/3773966.3779371](https://doi.org/10.1145/3773966.3779371)

<details open>
<summary><strong>中文摘要</strong></summary>

后点击转化率（CVR）估计是许多营收型推荐系统（如电子商务和广告）中的关键任务。从样本角度来看，典型的CVR正样本通常经历曝光→点击→转化的漏斗过程。由于未点击样本缺乏事后标签，CVR学习任务通常仅利用点击样本，而非像点击率（CTR）学习任务那样使用所有曝光样本。然而，在线推理时，CVR和CTR在相同的假设曝光空间上进行估计，这导致训练与推理之间的样本空间不一致，即样本选择偏差（SSB）。为缓解SSB，以往的研究提出设计新颖的辅助任务，使CVR学习能够在未点击的训练样本上进行，例如CTCVR和反事实CVR等。尽管这些方法在一定程度上缓解了SSB，但它们在建模过程中均未关注模糊负样本（未点击）与事实负样本（已点击但未转化）之间的区分，这使得CVR模型缺乏鲁棒性。为填补这一空白，我们提出了一种新颖的ChorusCVR模型，以实现全空间上的去偏CVR学习。我们提出一个负样本判别模块（NDM），旨在提供具有区分事实负样本（已点击但未转化）与模糊负样本（未点击）能力的鲁棒软标签。此外，我们提出一个软对齐模块（SAM），利用生成的软标签通过多个对齐目标来监督CVR学习。在快手电商直播服务上进行的大量离线实验和在线A/B测试验证了我们的ChorusCVR模型的有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Post-click conversion rate (CVR) estimation is a vital task in many recommender systems of revenue businesses, e.g., e-commerce and advertising. In a perspective of sample, a typical CVR positive sample usually goes through a funnel of exposure?click?conversion. For lack of post-event labels for un-clicked samples, CVR learning task commonly only utilizes clicked samples, rather than all exposed samples as for click-through rate (CTR) learning task. However, during online inference, CVR and CTR are estimated on the same assumed exposure space, which leads to a inconsistency of sample space between training and inference, i.e., sample selection bias (SSB). To alleviate SSB, previous wisdom proposes to design novel auxiliary tasks to enable the CVR learning on un-click training samples, such as CTCVR and counterfactual CVR, etc. Although alleviating SSB to some extent, none of them pay attention to the discrimination between ambiguous negative samples (un-clicked) and factual negative samples (clicked but un-converted) during modelling, which makes CVR model lacks robustness. To full this gap, we propose a novel ChorusCVR model to realize debiased CVR learning in entire-space. We propose a Negative sample Discrimination Module (NDM), which aims to provide robust soft labels with the ability to discriminate factual negative samples (clicked but un-converted) from ambiguous negative samples (un-clicked). Moreover, we propose a Soft Alignment Module (SAM) to supervise CVR learning with several alignment objectives using generated soft labels. Extensive offline experiments and online A/B testing at Kuaishou's e-commerce live service validates our ChorusCVR.

</details>

---

_知识库更新时间：2026-08-22T02:17:50.834946_
