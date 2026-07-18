---
title: "通过多模态嵌入和语义ID增强大语言模型用于序列推荐"
paper_id: "https://doi.org/10.1145/3746252.3761169"
source: "cikm"
published: "2025-01-01T00:00:00"
score: 70.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Machine Learning in Healthcare", "Advanced Graph Neural Networks"]
---

# 通过多模态嵌入和语义ID增强大语言模型用于序列推荐

> **英文原标题**：Empowering Large Language Model for Sequential Recommendation via Multimodal Embeddings and Semantic IDs

[查看原文](https://dblp.org/rec/conf/cikm/0006P0000LJ025) · [ArXiv](https://arxiv.org/abs/2509.02017) · [Semantic Scholar](https://www.semanticscholar.org/paper/58f675de28bfc716ede80dd16e0a19853bf67439)

## 一句话结论

> 该论文提出MME-SID框架，通过多模态嵌入和语义ID缓解嵌入坍塌和灾难性遗忘问题，提升大语言模型在序列推荐中的性能。

## 论文信息

- **作者**：Yuhao Wang, Junwei Pan, Xinhang Li, Maolin Wang, Yuan Wang, Yue Liu, Dapeng Liu, Jie Jiang, Xiangyu Zhao
- **来源**：CIKM
- **发布时间**：2025-01-01
- **相关度评分**：70.0
- **DOI**：[https://doi.org/10.1145/3746252.3761169](https://doi.org/10.1145/3746252.3761169)

<details open>
<summary><strong>中文摘要</strong></summary>

序列推荐（Sequential Recommendation, SR）旨在基于用户的历史交互行为捕捉其动态兴趣与序列模式。近年来，大语言模型（Large Language Models, LLMs）的强大能力推动了其在SR中的应用。然而，我们指出现有基于LLM的SR方法存在两个关键挑战：1）在融入预训练协同嵌入时出现嵌入坍缩（embedding collapse）；2）在使用语义ID时发生量化嵌入的灾难性遗忘（catastrophic forgetting）。这些问题削弱了模型的可扩展性，并导致推荐性能欠佳。为此，基于Llama3-8B-instruct等大语言模型，我们提出了一种名为MME-SID的新型SR框架，该框架通过融合多模态嵌入与量化嵌入来缓解嵌入坍缩。此外，我们提出了一种多模态残差量化变分自编码器（Multimodal Residual Quantized Variational Autoencoder, MM-RQ-VAE），采用最大均值差异作为重构损失，并利用对比学习进行对齐，从而分别有效保留模态内距离信息并捕获模态间相关性。为进一步缓解灾难性遗忘，我们使用训练好的多模态码嵌入对模型进行初始化。最后，我们采用低秩适配（LoRA）以多模态频率感知融合方式高效微调大语言模型。在三个公开数据集上的大量实验验证了MME-SID的优越性能，这得益于其缓解嵌入坍缩与灾难性遗忘的能力。实现代码与数据集已公开以供复现：https://github.com/Applied-Machine-Learning-Lab/MME-SID。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation (SR) aims to capture users' dynamic interests and sequential patterns based on their historical interactions. Recently, the powerful capabilities of large language models (LLMs) have driven their adoption in SR. However, we identify two critical challenges in existing LLM-based SR methods: 1) embedding collapse when incorporating pre-trained collaborative embeddings and 2) catastrophic forgetting of quantized embeddings when utilizing semantic IDs. These issues dampen the model scalability and lead to suboptimal recommendation performance. Therefore, based on LLMs like Llama3-8B-instruct, we introduce a novel SR framework named MME-SID, which integrates multimodal embeddings and quantized embeddings to mitigate embedding collapse. Additionally, we propose a Multimodal Residual Quantized Variational Autoencoder (MM-RQ-VAE) with maximum mean discrepancy as the reconstruction loss and contrastive learning for alignment, which effectively preserve intra-modal distance information and capture inter-modal correlations, respectively. To further alleviate catastrophic forgetting, we initialize the model with the trained multimodal code embeddings. Finally, we fine-tune the LLM efficiently using LoRA in a multimodal frequency-aware fusion manner. Extensive experiments on three public datasets validate the superior performance of MME-SID thanks to its capability to mitigate embedding collapse and catastrophic forgetting. The implementation code and datasets are publicly available for reproduction: https://github.com/Applied-Machine-Learning-Lab/MME-SID.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对现有基于大语言模型（LLM）的序列推荐方法中存在的两个关键问题：嵌入崩溃（embedding collapse）和灾难性遗忘（catastrophic forgetting），提出了一种名为MME-SID的新框架。该框架利用多模态嵌入和量化嵌入来缓解嵌入崩溃，并设计了一种多模态残差量化变分自编码器（MM-RQ-VAE），采用最大均值差异（MMD）作为重构损失，结合对比学习来捕捉模态间相关性。为减轻灾难性遗忘，模型使用训练好的多模态码嵌入进行初始化，并通过LoRA以多模态频率感知融合方式高效微调LLM。在三个Amazon数据集上的实验表明，MME-SID在缓解嵌入崩溃和灾难性遗忘方面表现优越，推荐性能显著提升。

### 主要创新

- 首次系统性地识别并解决了LLM用于推荐时的嵌入崩溃和灾难性遗忘问题。
- 提出MM-RQ-VAE，使用MMD作为重构损失以更好地保留距离信息，并通过对比学习对齐模态。
- 利用训练好的多模态码嵌入初始化语义ID嵌入，有效缓解灾难性遗忘。
- 提出多模态频率感知融合模块，自适应融合不同模态的分数。
- 同时利用原始嵌入和语义ID嵌入，避免仅使用语义ID的常见次优做法。

### 研究方法

首先，使用LLM2CLIP提取文本和视觉嵌入，并训练SASRec获得协同嵌入。然后，提出MM-RQ-VAE对三种模态嵌入进行量化，生成语义ID，其中重构损失采用MMD，并加入对比学习对齐协同与文本/视觉模态。接着，在微调阶段，将训练好的码嵌入初始化为语义ID嵌入，并将原始嵌入与语义ID嵌入拼接后通过MLP输入LLM。最后，使用LoRA高效微调LLM，并通过多模态频率感知融合模块计算预测分数。

### 关键结果

MME-SID在Beauty、Toys & Games和Sports & Outdoors三个数据集上均优于所有基线方法，nDCG@5分别提升10.47%、4.42%和8.12%。；MME-SID有效缓解了嵌入崩溃，超过98%的维度未发生崩溃，而基线方法在64维后即崩溃。；使用MMD重构损失比MSE保留更多距离信息（Kendall's tau从0.3714提升至0.4436），推荐性能更优。；使用训练好的码嵌入初始化比随机初始化显著减轻灾难性遗忘（Kendall's tau从0.0508提升至0.2727）。

### 技术栈

- LLM: Llama3-8B-instruct
- 多模态编码器: LLM2CLIP
- 量化模型: RQ-VAE
- 重构损失: 最大均值差异 (MMD)
- 对比学习: InfoNCE损失
- 微调方法: LoRA
- 序列推荐模型: SASRec
- 评估指标: HR@k, nDCG@k

### 方法优势

- 创新性地同时解决嵌入崩溃和灾难性遗忘两个关键问题。
- 提出MMD重构损失，理论上有保留分布信息的优势。
- 实验充分，在三个数据集上验证了有效性，并进行了详细的分析实验。
- 代码和数据集公开，可复现。
- 对现有使用语义ID的常见做法提出了改进，具有潜在颠覆性。

### 主要局限

- 输入内容未提供消融实验中各组件贡献的具体数值。
- 输入内容未讨论模型在更大规模数据集或工业场景下的性能。
- 输入内容未分析多模态频率感知融合模块的复杂度。
- 输入内容未讨论不同LLM backbone的影响。

### 与当前研究方向的关联

序列推荐: 论文聚焦于序列推荐任务，使用历史交互序列预测用户兴趣。；生成式推荐: 论文使用语义ID进行生成式推荐，但提出改进方案。；LLM与推荐系统结合: 论文核心是利用LLM增强序列推荐。；多模态推荐: 论文融合协同、文本、视觉三种模态。；推荐智能体: 输入内容未涉及。；对话式推荐: 输入内容未涉及。；排序与重排: 输入内容未涉及。；用户建模: 输入内容未涉及。；CTR/CVR预测: 输入内容未涉及。；因果性、公平性、鲁棒性: 输入内容未涉及。；工业落地: 论文提及工业规模场景，但未具体实验。

## 代码与复现

- [Applied-Machine-Learning-Lab/MME-SID](https://github.com/Applied-Machine-Learning-Lab/MME-SID)：official，置信度 100，Stars 30

---

_知识库更新时间：2026-07-18T03:48:20.893273_
