---
title: "When Modalities Go Missing: Early Fusion for Multimodal Recommendation"
paper_id: "https://doi.org/10.1145/3773966.3779385"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 30.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Emotion and Mood Recognition"]
---

# When Modalities Go Missing: Early Fusion for Multimodal Recommendation

[查看原文](https://dblp.org/rec/conf/wsdm/ChenYH0C26) · [Semantic Scholar](https://www.semanticscholar.org/paper/b1bfccc0ad7f27c06d714f24ee31270949793419)

## 一句话结论

> 该论文提出了一种缺失感知的早期融合框架EFMRec，通过利用预训练多模态模型将可用模态投影到共享语义空间并进行早期融合，以应对多模态推荐中模态缺失的问题，实验表明其在完整和缺失模态设置下均优于强基线。

## 论文信息

- **作者**：Lu Chen, Peng Yi, Xiaoyue Hou, Cheng Yang, Xiongcai Cai
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：30.0
- **DOI**：[https://doi.org/10.1145/3773966.3779385](https://doi.org/10.1145/3773966.3779385)

<details open>
<summary><strong>中文摘要</strong></summary>

现有多模态推荐系统大多依赖晚期融合，即各模态在融合前被分别编码并对齐。这类设计在内容完整时表现良好，但在实际应用中往往较为脆弱：模态经常缺失、对齐容易失效，而插补方法不仅增加了复杂性，收益也有限。我们提出EFMRec，一种缺失感知的早期融合框架，遵循“模态可用时利用、缺失时忽略”的宽松原则。通过利用预训练多模态模型，EFMRec将可用模态投影到共享语义空间，并通过缺失感知的早期融合进行聚合，无需重建或辅助损失即可生成统一表示。这些表示进一步通过基于图卷积网络（GCN）的架构传播，并与协同过滤主干集成，以联合建模多模态信号与协同信号。在三个基准数据集上的实验表明，EFMRec在完整模态和缺失模态设置下均持续优于强基线模型，凸显了其对模态不完整性的鲁棒性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Existing multimodal recommenders largely rely on late fusion, where modalities are separately encoded and aligned before fusion. Such designs work well with complete content but become fragile in practice: modalities are often missing, alignment breaks down, and imputation adds complexity with limited benefit. We propose EFMRec, a missing-aware early-fusion framework that follows a relaxed principle of leveraging modalities when available and ignoring them when absent. By exploiting pretrained multimodal models, EFMRec projects available modalities into a shared semantic space and aggregates them through a missing-aware early fusion, producing unified representations without reconstruction or auxiliary losses. These representations are further propagated via a GCN-based architecture and integrated with a collaborative filtering backbone to jointly model multimodal and collaborative signals. Experiments on three benchmarks demonstrate that EFMRec consistently outperforms strong baselines under both full- and missing-modality settings, highlighting its robustness to modality incompleteness.

</details>

---

_知识库更新时间：2026-08-22T02:17:50.834475_
