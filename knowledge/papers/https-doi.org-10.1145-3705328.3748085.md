---
title: "面向基于大语言模型推荐的异构用户建模"
paper_id: "https://doi.org/10.1145/3705328.3748085"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Web Data Mining and Analysis"]
---

# 面向基于大语言模型推荐的异构用户建模

> **英文原标题**：Heterogeneous User Modeling for LLM-based Recommendation

[查看原文](https://dblp.org/rec/conf/recsys/Bao0LZSFC25) · [ArXiv](https://arxiv.org/abs/2507.04626) · [Semantic Scholar](https://www.semanticscholar.org/paper/a4f0f155108625ffe6e4d68559090be2a3b6718c)

## 一句话结论

> 提出异构用户建模方法HUM，通过压缩增强器和鲁棒增强器解决LLM推荐中跨域用户建模的泛化性差、噪声交互压缩难和领域跷跷板问题。

## 论文信息

- **作者**：Honghui Bao, Wenjie Wang, Xinyu Lin, Fengbin Zhu, Teng Sun, Fuli Feng, Tat‐Seng Chua
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3705328.3748085](https://doi.org/10.1145/3705328.3748085)

<details open>
<summary><strong>中文摘要</strong></summary>

利用大型语言模型（LLMs）进行推荐已在多个领域展现出显著成效，彰显了其在开放域推荐中的潜力。推进开放域推荐的核心挑战在于如何从用户跨多个领域的异质性行为中有效建模用户偏好。现有方法（包括基于ID的建模和基于语义的建模）存在泛化能力差、无法有效压缩噪声交互以及领域跷跷板现象等问题。为解决这些挑战，我们提出了一种异质性用户建模（HUM）方法，该方法为基于LLM的推荐引入了压缩增强器与鲁棒性增强器。压缩增强器通过定制化提示将异质性行为压缩为定制化令牌，同时利用掩码机制增强跨域知识提取与理解；鲁棒性增强器则引入领域重要性分数，通过引导领域优化来缓解领域跷跷板现象。在异质性数据集上的大量实验表明，HUM通过实现高效能与高鲁棒性，有效建模了用户异质性，从而在开放域推荐中取得了优越性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Leveraging Large Language Models (LLMs) for recommendation has demonstrated notable success in various domains, showcasing their potential for open-domain recommendation. A key challenge to advancing open-domain recommendation lies in effectively modeling user preferences from users’ heterogeneous behaviors across multiple domains. Existing approaches, including ID-based and semantic-based modeling, struggle with poor generalization, an inability to compress noisy interactions effectively, and the domain seesaw phenomenon. To address these challenges, we propose a Heterogeneous User Modeling (HUM) method, which incorporates a compression enhancer and a robustness enhancer for LLM-based recommendation. The compression enhancer uses a customized prompt to compress heterogeneous behaviors into a tailored token, while a masking mechanism enhances cross-domain knowledge extraction and understanding. The robustness enhancer introduces a domain importance score to mitigate the domain seesaw phenomenon by guiding domain optimization. Extensive experiments on heterogeneous datasets validate that HUM effectively models user heterogeneity by achieving both high efficacy and robustness, leading to superior performance in open-domain recommendation.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对开放域推荐中用户异构行为建模的挑战，提出异构用户建模方法HUM。现有方法（基于ID和基于语义）存在泛化性差、无法有效压缩噪声交互以及领域跷跷板现象等问题。HUM包含压缩增强器和鲁棒性增强器：压缩增强器通过定制提示压缩异构行为到专用用户令牌，并利用掩码机制增强跨域知识提取；鲁棒性增强器引入领域重要性分数平衡各领域优化，缓解领域跷跷板现象。在异构数据集上的实验表明，HUM在多个领域上优于现有方法，并展现出良好的鲁棒性、噪声抵抗性、泛化性和可扩展性。

### 主要创新

- 提出压缩增强器，利用定制提示和专用用户令牌[USER]引导LLM压缩异构用户行为，并设计掩码机制促进跨域知识提取。
- 提出鲁棒性增强器，通过领域重要性分数和领域平滑策略动态调整各领域优化权重，缓解领域跷跷板现象。
- 在LLM-based推荐中系统分析了异构用户建模的两个关键目标：强压缩能力和强鲁棒性。
- 在多个异构数据集上验证了方法在噪声抵抗、冷启动泛化和可扩展性方面的优势。

### 研究方法

基于Qwen2.5-1.5b作为骨干LLM，采用LoRA参数高效微调。压缩增强器：设计压缩提示和[USER]令牌，将用户历史交互序列（物品标题）输入LLM，提取[USER]令牌的隐藏向量作为用户表示；采用对比学习优化，并随机掩码部分目标域物品以增强跨域学习。鲁棒性增强器：基于每个域的平均训练损失计算领域重要性分数，并通过KL散度正则化进行平滑更新，最终加权各域损失。推理时去激活掩码机制，计算用户表示与目标域物品表示的内积进行排序推荐。

### 关键结果

HUM在六个域（Books, Office, Scientific, CDs, Auto, Tools）上全面优于所有基线，包括ID-based和语义-based方法。；消融实验表明压缩提示、用户令牌和掩码机制均对性能有贡献。；HUM在包含多域交互的序列上提升显著，验证了压缩异构行为的能力。；HUM在噪声注入实验中表现出更强的噪声抵抗性。；HUM在四个未见域（Instruments, Games, Arts, Sports）上展现出良好的泛化能力。；随着域数量增加（2域→6域→10域），HUM与基线性能差距扩大，表明可扩展性。

### 技术栈

- Qwen2.5-1.5b
- LoRA
- 对比学习
- KL散度
- AdamW优化器
- 早停策略
- 内积相似度

### 方法优势

- 针对异构用户建模的两个关键目标（压缩和鲁棒性）提出了系统性的解决方案。
- 设计了简单有效的压缩提示和专用用户令牌，引导LLM更好地压缩异构信息。
- 通过领域重要性分数动态调整优化，有效缓解了领域跷跷板现象。
- 实验全面，包括主实验、消融、噪声抵抗、泛化和可扩展性分析。
- 代码和数据集已开源，可复现。

### 主要局限

- 仅使用了Qwen2.5-1.5b一个LLM作为骨干，未探索更大模型或其他LLM的影响。
- 掩码机制中的掩码比例r需要手动调节，可能影响性能。
- 领域重要性分数的计算依赖于训练损失，可能受噪声影响。
- 实验仅在Amazon数据集上进行，未在更多真实场景验证。

### 与当前研究方向的关联

LLM与推荐系统结合：核心方法基于LLM进行用户建模和推荐。；用户建模：直接研究异构用户行为建模，提出压缩和鲁棒性增强。；序列推荐：用户历史按时间顺序组织，采用序列建模。；生成式推荐：虽未直接生成，但利用LLM的生成能力进行压缩。；多模态推荐：仅使用文本标题，未涉及多模态。；鲁棒性：专门设计鲁棒性增强器缓解领域跷跷板现象。

## 代码与复现

- [HonghuiBao2000/HUM](https://github.com/HonghuiBao2000/HUM)：official，置信度 100，Stars 9
- [TinyMirable/hum_research](https://github.com/TinyMirable/hum_research)：possible，置信度 30，Stars 0

---

_知识库更新时间：2026-07-23T04:05:05.422331_
