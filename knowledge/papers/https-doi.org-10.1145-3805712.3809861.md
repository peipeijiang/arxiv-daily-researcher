---
title: "FEDIN：用于点击率预测的频率增强深度兴趣网络"
paper_id: "https://doi.org/10.1145/3805712.3809861"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 44.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Emotion and Mood Recognition", "Advanced Bandit Algorithms Research"]
---

# FEDIN：用于点击率预测的频率增强深度兴趣网络

> **英文原标题**：FEDIN: Frequency-Enhanced Deep Interest Network for Click-Through Rate Prediction

[查看原文](https://dblp.org/rec/conf/sigir/DaiWPLXX26) · [ArXiv](https://arxiv.org/abs/2605.01726)

## 一句话结论

> 针对序列推荐中用户兴趣的周期性模式难以捕捉的问题，提出频域增强的深度兴趣网络（FEDIN），利用目标感知的频谱过滤机制分离噪声和真实兴趣，在三个数据集上显著优于现有方法。

## 论文信息

- **作者**：Z. Dai, Jinpeng Wang, Junwei Pan, Dapeng Liu, Lei Xiao, Shu‐Tao Xia
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：44.0
- **DOI**：[https://doi.org/10.1145/3805712.3809861](https://doi.org/10.1145/3805712.3809861)

<details open>
<summary><strong>中文摘要</strong></summary>

序列推荐模型通常难以捕捉用户兴趣中潜在的周期性模式，这主要是由于时域行为数据中固有的噪声。虽然频域分析为解决这一问题提供了全局视角，但现有方法通常孤立地处理用户序列，忽略了目标物品的关键上下文。在本工作中，我们提出了一项新颖的实证观察：当以正样本与负样本目标物品为条件时，用户注意力分数会呈现出不同的频谱熵分布。具体而言，真实的用户兴趣在频域中表现为高度集中的频谱模式且熵值较低，而不相关行为则表现为高熵噪声。基于这一发现，我们提出了频率增强深度兴趣网络（Frequency-Enhanced Deep Interest Network, FEDIN）。FEDIN引入了一个频域分支，该分支利用目标感知的频谱过滤机制来分离这些周期性兴趣信号。在三个公开数据集上进行的大量实验表明，FEDIN在性能上持续优于最先进的序列推荐基线模型，展现出卓越的噪声鲁棒性。我们已在以下地址公开代码：https://github.com/otokoneko/FEDIN。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation models often struggle to capture latent periodic patterns in user interests, primarily due to the noise inherent in time-domain behavioral data. While frequency-domain analysis offers a global perspective to address this, existing approaches typically treat user sequences in isolation, overlooking the crucial context of the target item. In this work, we present a novel empirical observation: user attention scores exhibit distinct spectral entropy distributions when conditioned on positive versus negative target items. Specifically, true user interests manifest as highly concentrated spectral patterns with lower entropy in the frequency domain, whereas irrelevant behaviors appear as high-entropy noise. Leveraging this insight, we propose the Frequency-Enhanced Deep Interest Network (FEDIN). FEDIN introduces a frequency-domain branch that utilizes a target-aware spectrum filtering mechanism to isolate these periodic interest signals. Extensive experiments on three public datasets demonstrate that FEDIN consistently outperforms state-of-the-art sequential recommendation baselines, demonstrating superior robustness against noise. We have released our code at: https://github.com/otokoneko/FEDIN.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

针对序列推荐模型难以捕捉用户兴趣中潜在周期性模式的问题，本文提出频率增强深度兴趣网络（FEDIN）。作者通过实证发现，用户注意力分数在正负目标项条件下呈现不同的频谱熵分布：正样本表现为低熵的集中频谱模式，负样本则为高熵噪声。基于此，FEDIN引入频率分支，采用目标感知频谱过滤机制分离周期性兴趣信号，并与时间域分支并行融合。在三个公开数据集上的实验表明，FEDIN持续优于现有基线，尤其在噪声环境下表现出更强的鲁棒性。

### 主要创新

- 发现用户兴趣在目标项条件下呈现低熵频谱特征，为频谱推荐提供理论依据。
- 提出目标感知频谱过滤机制，利用目标项激活特定共振模式。
- 设计双分支架构，融合时间域局部演化与频率域全局周期性。
- 引入自适应共振缩放门控，根据频谱清晰度动态调整频率分支权重。

### 研究方法

采用双分支架构：时间分支通过目标注意力粗过滤和分片Transformer捕捉局部演化；频率分支对目标注意力分数进行FFT，经可学习复值MLP过滤后逆变换，并利用自适应缩放门控。最后通过Top-k目标注意力聚合双分支表示。

### 关键结果

在Tmall、Alipay、Taobao三个数据集上，FEDIN的GAUC和AUC均优于所有基线（如DIN、DIEN、SASRec、DIFF等），且提升统计显著（p<0.05）。消融实验验证了各组件必要性，噪声鲁棒性实验显示频率分支在噪声下更稳定。

### 技术栈

- 快速傅里叶变换（FFT）
- 复值MLP
- 分片（Patching）
- Transformer编码器
- 可逆实例归一化（RevIN）
- Top-k目标注意力
- Adam优化器

### 方法优势

- 创新性地将目标感知引入频率域分析，理论动机清晰。
- 双分支设计兼顾全局周期性与局部演化，互补性强。
- 在多个数据集上一致超越SOTA，鲁棒性突出。
- 代码已开源，可复现。

### 主要局限

- 频率分支依赖FFT，对序列长度有要求，极短序列可能效果有限。
- 未讨论不同频率过滤策略的对比（如固定滤波器）。
- 实验仅在三个电商数据集上进行，泛化性需更多验证。

### 与当前研究方向的关联

论文聚焦CTR预测和序列推荐，提出频率增强方法，与关键词“CTR/CVR预测”、“序列推荐”、“用户建模”高度相关。同时涉及注意力机制和噪声鲁棒性，与“排序与重排”、“推荐系统鲁棒性”相关。

## 代码与复现

- [otokoneko/FEDIN](https://github.com/otokoneko/FEDIN)：official，置信度 100，Stars 5

---

_知识库更新时间：2026-07-24T04:05:55.201083_
