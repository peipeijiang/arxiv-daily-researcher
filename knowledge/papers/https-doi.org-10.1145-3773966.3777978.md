---
title: "SimDifRec：语义相似性引导的扩散模型用于对比序列推荐"
paper_id: "https://doi.org/10.1145/3773966.3777978"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 43.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Image Retrieval and Classification Techniques"]
---

# SimDifRec：语义相似性引导的扩散模型用于对比序列推荐

> **英文原标题**：SimDiffRec: Semantic Similarity-Guided Diffusion for Contrastive Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/wsdm/ChoiNP26) · [ArXiv](https://arxiv.org/abs/2507.11866) · [Semantic Scholar](https://www.semanticscholar.org/paper/f448e568118f13b6ebbe5bbecb53681b62d8a9a7)

## 一句话结论

> SimDiffRec proposes a semantic similarity-guided diffusion model for contrastive sequential recommendation, which generates semantically consistent noise and selects augmentation positions based on confidence scores, outperforming baselines on five datasets.

## 论文信息

- **作者**：Jinkyeong Choi, Yejin Noh, Donghyeon Park
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：43.0
- **DOI**：[https://doi.org/10.1145/3773966.3777978](https://doi.org/10.1145/3773966.3777978)

<details open>
<summary><strong>中文摘要</strong></summary>

在序列推荐系统中，近期引入了基于扩散模型的数据增强与对比学习技术，以实现鲁棒的表示学习。然而，现有方法大多采用随机增强，这可能会破坏原始序列的上下文信息。为此，我们提出了SimDiffRec：一种基于语义相似性引导的扩散模型，用于对比序列推荐。我们的框架利用物品嵌入向量之间的相似性来生成语义一致的噪声。此外，我们在去噪过程中利用高置信度分数来选择增强位置。与在随机位置进行增强相比，该方法能更有效地反映上下文和结构信息。从对比学习的角度来看，所提出的增强技术结合困难负样本采样，能够提供更具判别性的正样本和负样本，同时提升训练效率和推荐性能。在五个基准数据集上的实验结果表明，SimDiffRec优于现有的基线模型。我们的框架代码可在https://github.com/zingyon/SimDiffRec获取。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In sequential recommendation systems, data augmentation and contrastive learning techniques have recently been introduced using diffusion models to achieve robust representation learning. However, most of the existing approaches use random augmentation, which risks damaging the contextual information of the original sequence. Accordingly, we propose SimDiffRec: a Semantic Similarity-Guided Diffusion for Contrastive Sequential Recommendation. Our framework leverages the similarity between item embedding vectors to generate semantically consistent noise. Moreover, we utilize high confidence scores in the denoising process to select our augmentation positions. This approach more effectively reflects contextual and structural information compared to augmentation at random positions. From a contrastive learning perspective, the proposed augmentation technique, combined with hard negative sampling, provides more discriminative positive and negative samples, simultaneously improving training efficiency and recommendation performance. Experimental results on five benchmark datasets show that SimDiffRec outperforms the existing baseline models. The code of our framework is available at https://github.com/zingyon/SimDiffRec.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文提出SimDifRec，一种用于增强序列推荐模型的数据增强框架。现有基于扩散模型的增强方法使用随机噪声，可能破坏序列的上下文信息。SimDifRec利用物品嵌入向量间的语义相似性生成结构化噪声，并基于扩散模型的重建置信度选择增强位置，结合硬负采样进行对比学习，以保留上下文和结构信息。在五个基准数据集上的实验表明，SimDifRec优于现有基线模型，验证了其有效性和泛化性。

### 主要创新

- 基于语义相似性生成噪声，而非随机噪声，保持语义一致性。
- 利用扩散模型的重建置信度选择增强位置，保留结构和上下文信息。
- 结合硬负采样，增强对比学习的判别能力。
- 作为即插即用的增强框架，可提升现有序列推荐模型性能。

### 研究方法

SimDifRec包含三个核心模块：1）语义相似性噪声生成：计算物品嵌入与所有物品嵌入的相似度，选取top-k相似物品的平均嵌入作为噪声；2）扩散前向和反向过程：前向过程使用确定性噪声，反向过程通过去噪重建序列，并利用置信度选择增强位置；3）对比学习：使用硬负采样构建正负样本，优化InfoNCE损失。总损失为序列推荐损失、对比损失和扩散损失的加权和。

### 关键结果

在Beauty、Toys、Sports、Yelp和ML-1m五个数据集上，SimDifRec在HR@5、HR@10、NDCG@5、NDCG@10指标上均优于所有基线模型。消融实验表明各组件均有效，超参数分析显示最佳权重因数据集而异。T-SNE可视化显示置信度增强使序列内物品表示更紧凑。

### 技术栈

- Transformer
- 扩散模型（DDPM）
- 对比学习（InfoNCE）
- 硬负采样
- T-SNE可视化
- PyTorch（隐含）
- RecBole框架

### 方法优势

- 创新性地使用语义相似性噪声替代随机噪声，增强语义一致性。
- 置信度引导的增强位置选择，减少上下文失真。
- 硬负采样提升对比学习效果。
- 在多个数据集上取得一致性能提升，且推理开销低。

### 主要局限

- 输入内容未提供明确的局限性讨论。
- 超参数（如α、β）需要针对数据集调整，可能增加调参成本。
- 扩散模型训练可能增加训练时间（但推理无额外开销）。

### 与当前研究方向的关联

论文与序列推荐、扩散模型、数据增强、对比学习、语义相似性等关键词高度相关，属于推荐系统领域的前沿研究。

## 代码与复现

- [zingyon/SimDiffRec](https://github.com/zingyon/SimDiffRec)：official，置信度 100，Stars 4

---

_知识库更新时间：2026-08-25T02:16:23.901388_
