---
title: "VL-CLIP：通过视觉定位和LLM增强的CLIP嵌入提升多模态推荐"
paper_id: "https://doi.org/10.1145/3705328.3748064"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 62.0
tags: ["paper", "recommender-systems", "Multimodal Machine Learning Applications", "Topic Modeling", "Natural Language Processing Techniques"]
---

# VL-CLIP：通过视觉定位和LLM增强的CLIP嵌入提升多模态推荐

> **英文原标题**：VL-CLIP: Enhancing Multimodal Recommendations via Visual Grounding and LLM-Augmented CLIP Embeddings

[查看原文](https://dblp.org/rec/conf/recsys/GiahiYKZMXBKA25) · [ArXiv](https://arxiv.org/abs/2507.17080) · [Semantic Scholar](https://www.semanticscholar.org/paper/30034c4e50c81ca93cd589ce9688a03b4d5d70d2)

## 一句话结论

> 该论文提出VL-CLIP框架，通过视觉定位和LLM增强CLIP嵌入，显著提升多模态推荐系统的检索和推荐性能，CTR提升18.6%。

## 论文信息

- **作者**：Ramin Giahi, Kehui Yao, Sriram Kollipara, Kai Zhao, Vahid Mirjalili, Jianpeng Xu, Topojoy Biswas, Evren Körpeoğlu, Kannan Achan
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：62.0
- **DOI**：[https://doi.org/10.1145/3705328.3748064](https://doi.org/10.1145/3705328.3748064)

<details open>
<summary><strong>中文摘要</strong></summary>

多模态学习在当今电子商务推荐平台中发挥着关键作用，能够实现精准推荐和产品理解。然而，现有的视觉-语言模型（如CLIP）在电子商务推荐系统中面临几个关键挑战：1）对象级对齐较弱，全局图像嵌入无法捕捉细粒度的产品属性，导致检索性能欠佳；2）文本表示模糊，产品描述往往缺乏上下文清晰度，影响跨模态匹配；3）领域不匹配，通用视觉-语言模型可能无法很好地泛化到电子商务特定数据。为解决这些局限，我们提出了一种框架VL-CLIP，通过整合视觉定位（Visual Grounding）实现细粒度视觉理解，并利用基于大语言模型（LLM）的智能体生成增强的文本嵌入，从而提升CLIP嵌入效果。视觉定位通过定位关键产品来细化图像表示，而LLM智能体则通过消除产品描述的歧义来增强文本特征。我们的方法在美国最大的电子商务平台之一上，对数千万个商品显著提升了检索准确性、多模态检索效果和推荐质量，点击率（CTR）提高了18.6%，加入购物车率（ATC）提高了15.5%，商品交易总额（GMV）提高了4.0%。额外的实验结果表明，我们的框架在精度和语义对齐方面均优于包括CLIP、FashionCLIP和GCL在内的视觉-语言模型，展示了将对象感知的视觉定位与LLM增强的文本表示相结合用于稳健多模态推荐的潜力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Multimodal learning plays a critical role in e-commerce recommendation platforms today, enabling accurate recommendations and product understanding. However, existing vision-language models, such as CLIP, face key challenges in e-commerce recommendation systems: 1) Weak object-level alignment, where global image embeddings fail to capture fine-grained product attributes, leading to suboptimal retrieval performance; 2) Ambiguous textual representations, where product descriptions often lack contextual clarity, affecting cross-modal matching; and 3) Domain mismatch, as generic vision-language models may not generalize well to e-commerce-specific data. To address these limitations, we propose a framework, VL-CLIP, that enhances CLIP embeddings by integrating Visual Grounding for fine-grained visual understanding and an LLM-based agent for generating enriched text embeddings. Visual Grounding refines image representations by localizing key products, while the LLM agent enhances textual features by disambiguating product descriptions. Our approach significantly improves retrieval accuracy, multimodal retrieval effectiveness, and recommendation quality across tens of millions of items on one of the largest e-commerce platforms in the U.S., increasing CTR by 18.6%, ATC by 15.5%, and GMV by 4.0%. Additional experimental results show that our framework outperforms vision-language models, including CLIP, FashionCLIP, and GCL, in both precision and semantic alignment, demonstrating the potential of combining object-aware visual grounding and LLM-enhanced text representation for robust multimodal recommendations.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出VL-CLIP框架，旨在解决CLIP在多模态推荐中的三大挑战：弱对象级对齐、文本表示模糊和领域不匹配。通过集成视觉定位（Grounding DINO）裁剪产品区域，以及利用LLM代理生成结构化、语义丰富的文本查询，增强CLIP嵌入。在Walmart.com的大规模数据集上，VL-CLIP在检索准确率、多模态检索效果和推荐质量上显著优于CLIP、FashionCLIP和GCL等基线，在线A/B测试中CTR提升18.6%，ATC提升15.5%，GMV提升4.0%。

### 主要创新

- 提出VL-CLIP框架，结合视觉定位和LLM增强的文本嵌入，提升多模态推荐性能。
- 利用Grounding DINO进行视觉定位，裁剪产品区域，增强细粒度视觉理解。
- 设计LLM驱动的文本查询合成流程，包括摘要、评估和迭代优化，生成视觉对齐的查询。
- 在Walmart.com大规模部署，验证了框架的实用性和可扩展性。

### 研究方法

VL-CLIP框架包括三个主要阶段：1) 图像区域细化：使用Grounding DINO根据产品类型文本提示生成候选框，选择最高置信度框裁剪图像，若置信度低于阈值则保留原图。2) LLM驱动的文本查询合成：将产品元数据拼接，通过LLM摘要生成初始查询，然后由评估器和优化器迭代优化，直到满足停止条件。3) 对比微调：使用对称对比损失（InfoNCE）微调CLIP模型，对齐图像和文本嵌入。部署时使用pHash去重、HNSW索引和产品类型分组索引。

### 关键结果

在Fashion和Home数据集上，VL-CLIP的HITS@5分别为0.6758和0.6692，MRR分别为0.5252和0.5100，均优于CLIP、GCL和FashionCLIP。消融实验表明，移除视觉定位和LLM组件会显著降低性能。零样本分类中，VL-CLIP在领口和图案分类准确率分别为0.937和0.959。VLM评估中，查询检索和相似物品推荐的Precision@1分别为0.8586和0.9925。在线A/B测试显示CTR提升18.6%，ATC提升15.5%，GMV提升4.0%。

### 技术栈

- CLIP
- Grounding DINO
- LLM（大型语言模型）
- 对比学习（InfoNCE损失）
- HNSW索引
- pHash（感知哈希）
- ViT-B/32
- Transformer文本编码器

### 方法优势

- 创新性地结合视觉定位和LLM增强，针对CLIP在电商领域的不足提出有效解决方案。
- 在真实大规模电商平台（Walmart.com）上验证，具有实际应用价值。
- 实验全面，包括离线检索、零样本分类、VLM评估和在线A/B测试。
- 框架具有可扩展性，支持大规模部署。

### 主要局限

- 依赖LLM和Grounding DINO，可能增加计算成本和推理延迟。
- LLM查询优化过程可能受限于LLM的固有偏见或错误。
- 视觉定位的阈值选择可能影响性能，需要调优。
- 论文未提供代码或详细实现，可复现性有限。

### 与当前研究方向的关联

该论文与多模态推荐、LLM与推荐系统结合、推荐系统工业落地等关键词高度相关。它提出了一种结合视觉定位和LLM增强的多模态推荐方法，并在工业环境中验证了效果，符合推荐系统领域的前沿研究方向。

---

_知识库更新时间：2026-08-10T02:48:30.664646_
