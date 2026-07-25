---
title: "MLLMRec: A Preference Reasoning Paradigm with Graph Refinement for Multimodal Recommendation"
paper_id: "https://doi.org/10.1145/3805712.3809749"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems", "Multimodal Machine Learning Applications", "Recommender Systems and Techniques", "Advanced Graph Neural Networks"]
---

# MLLMRec: A Preference Reasoning Paradigm with Graph Refinement for Multimodal Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/DangZPDCCC26) · [ArXiv](https://arxiv.org/abs/2508.15304)

## 一句话结论

> 评分失败，无法生成摘要

## 论文信息

- **作者**：Yuzhuo Dang, Xin Zhang, Zhiqiang Pan, Yuxiao Duan, Wanyu Chen, Fei Cai, Honghui Chen
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3805712.3809749](https://doi.org/10.1145/3805712.3809749)

<details>
<summary><strong>英文摘要</strong></summary>

Multimodal recommendation combines the user historical behaviors with the modal features of items to capture the tangible user preferences, presenting superior performance compared to the conventional ID-based recommender systems. However, existing methods still encounter two key problems in the representation learning of users and items, respectively: (1) the initialization of multimodal user representations is either agnostic to historical behaviors or contaminated by irrelevant modal noise, and (2) the widely used KNN-based item-item graph contains noisy edges with low similarities and lacks audience co-occurrence relationships. To address such issues, we propose MLLMRec, a novel preference reasoning paradigm with graph refinement for multimodal recommendation. Specifically, on the one hand, the item images are first converted into high-quality semantic descriptions using a multimodal large language model (MLLM), thereby bridging the semantic gap between visual and textual modalities. Then, we construct a behavioral description list for each user and feed it into the MLLM to reason about the purified user preference profiles that contain the latent interaction intents. On the other hand, we develop the threshold-controlled denoising and topology-aware enhancement strategies to refine the suboptimal item-item graph, thereby improving the accuracy of item representation learning. Extensive experiments on three publicly available datasets demonstrate that MLLMRec achieves the state-of-the-art performance with an average improvement of 21.48% over the optimal baselines. The source code is provided at https://github.com/Yuzhuo-Dang/MLLMRec.

</details>

---

_知识库更新时间：2026-07-25T03:51:56.885038_
