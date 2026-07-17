---
title: "When Vision Meets Texts in Listwise Reranking"
paper_id: "https://doi.org/10.1145/3805712.3809723"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 18.0
tags: ["paper", "recommender-systems", "Multimodal Machine Learning Applications", "Topic Modeling", "Advanced Image and Video Retrieval Techniques"]
---

# When Vision Meets Texts in Listwise Reranking

[查看原文](https://dblp.org/rec/conf/sigir/Cai26) · [ArXiv](https://arxiv.org/abs/2601.20623)

## 一句话结论

> 论文提出Rank-Nexus，一种轻量级多模态重排序模型，通过渐进式跨模态训练策略在文本和图像重排序基准上取得优异性能。

## 论文信息

- **作者**：Hongyi Cai
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：18.0
- **DOI**：[https://doi.org/10.1145/3805712.3809723](https://doi.org/10.1145/3805712.3809723)

<details open>
<summary><strong>中文摘要</strong></summary>

近期信息检索领域的研究进展揭示了视觉与文本信息融合的潜力，然而由于模态差异和对齐数据集的稀缺，图像-文本文档的有效重排序仍面临挑战。同时，现有方法通常依赖基于推理蒸馏的大规模模型（7B-32B参数），在主要关注文本模态的同时引入了不必要的计算开销。本文提出Rank-Nexus，一种多模态图像-文本文档重排序器，能够对同时包含图像和文本的检索列表执行列表级定性重排序。为弥合模态差异，我们引入了一种渐进式跨模态训练策略。首先分别训练各模态：利用丰富的文本重排序数据，以GPT-4o作为教师模型，将排序知识蒸馏至文本分支；针对标注数据稀缺的图像模态，我们在图像检索基准上从多模态大语言模型（MLLM）生成的描述中构建蒸馏对。随后，我们在联合图像-文本重排序数据集上进行训练。Rank-Nexus仅使用轻量级2B预训练视觉-语言模型，便在文本重排序基准（TREC, BEIR）及具有挑战性的图像重排序基准（INQUIRE, MMDocIR）上取得了卓越性能。这种高效设计确保了在无需过多参数或推理开销的情况下，跨多种多模态场景的强泛化能力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recent advancements in information retrieval have highlighted the potential of integrating visual and textual information, yet effective reranking for image-text documents remains challenging due to the modality gap and scarcity of aligned datasets. Meanwhile, existing approaches often rely on large models (7B--32B parameters) with reasoning-based distillation, incurring unnecessary computational overhead while primarily focusing on textual modalities. In this paper, we propose Rank-Nexus, a multimodal image-text document reranker that performs listwise qualitative reranking on retrieved lists incorporating both images and texts. To bridge the modality gap, we introduce a progressive cross-modal training strategy. We first train each modality separately: leveraging abundant text reranking data, we distill ranking knowledge into the text branch using GPT-4o as the teacher model. For images, where labeled data is scarce, we construct distilled pairs from multimodal large language model (MLLM) captions on image retrieval benchmarks. Subsequently, we train on a joint image-text reranking dataset. Rank-Nexus achieves outstanding performance on text reranking benchmarks (TREC, BEIR) and the challenging image reranking benchmarks (INQUIRE, MMDocIR), using only a lightweight 2B pretrained visual-language model. This efficient design ensures strong generalization across diverse multimodal scenarios without excessive parameters or reasoning overhead.

</details>

---

_知识库更新时间：2026-07-17T03:54:55.380328_
