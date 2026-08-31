---
title: "增强冷启动序列推荐与因果扩散偏好建模"
paper_id: "https://doi.org/10.1145/3773966.3778026"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 56.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Graph Neural Networks", "Advanced Bandit Algorithms Research"]
---

# 增强冷启动序列推荐与因果扩散偏好建模

> **英文原标题**：Enhanced Cold-Start Sequential Recommendation with Causal Diffusion Preference Modeling

[查看原文](https://dblp.org/rec/conf/wsdm/DongX0Z26) · [Semantic Scholar](https://www.semanticscholar.org/paper/db3ed14bfec6bbaa0fa0e371b47519b3b35c5b21)

## 一句话结论

> 该论文提出CDMRec，一种因果扩散偏好模型，通过生成冷启动用户的偏好表示并集成到现有序列推荐模型中，有效缓解了用户冷启动问题，在多个数据集上显著提升了推荐性能。

## 论文信息

- **作者**：Hongsheng Dong, Haolong Xiang, Xiaolong Xu, Xuyun Zhang
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：56.0
- **DOI**：[https://doi.org/10.1145/3773966.3778026](https://doi.org/10.1145/3773966.3778026)

<details open>
<summary><strong>中文摘要</strong></summary>

序列推荐因其捕捉动态用户偏好的能力，在各类应用领域中取得了显著成功。然而，在用户冷启动场景下，其有效性大幅降低，因为新用户仅有有限甚至没有交互历史。现有解决方案通常设计专门的模型架构，从辅助信息（如用户属性或社交网络）中推断冷启动用户偏好。然而，此类方法忽视了与先进序列推荐模型的兼容性，从而无法高效提取序列特征。为解决这一局限，我们提出CDMRec，一种用于用户冷启动序列推荐的因果扩散偏好模型。CDMRec为冷启动用户生成基于扩散的偏好表示，可直接被现有序列推荐模型使用。该框架首先通过隔离最能指示用户兴趣的交互行为，构建偏好主导序列（PDS），以减轻无关行为带来的噪声。随后，借助因果推断，CDMRec从PDS中识别关键因果变量，以条件化扩散过程，从而生成个性化的行为偏好。在三个公开数据集上的大量实验表明，CDMRec可无缝集成到主流序列推荐模型中，并在冷启动场景下带来显著的性能提升。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Sequential recommendation has achieved remarkable success across various application domains due to its ability to capture dynamic user preferences. Therefore, its effectiveness significantly diminishes in user cold-start scenarios, where new users have limited or no interaction history. Current solutions typically design specialized model architectures to infer cold-start user preferences from auxiliary information, such as user attributes or social networks. However, such methods overlook compatibility with advanced sequential recommender models, preventing the efficient extraction of sequential features. To address this limitation, we propose CDMRec, a Causal Diffusion Preference Model for user cold-start sequential recommendation. CDMRec generates diffusion-based preference representations for cold-start users, which can be directly utilized by existing sequential recommendation models. The framework first constructs a Preference-Dominant Sequence (PDS) by isolating interactions most indicative of user interests, mitigating noise from irrelevant behaviors. Then, leveraging causal inference, CDMRec identifies key causal variables from PDS to condition the diffusion process, enabling the generation of personalized behavioral preferences. Extensive experiments on three public datasets demonstrate that CDMRec can be seamlessly integrated into mainstream sequential recommender models, yielding substantial performance gains in cold-start settings.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

序列推荐在捕捉动态用户偏好方面表现出色，但在用户冷启动场景下，由于新用户交互历史有限，其效果显著下降。现有方法通常设计专门的模型架构，从辅助信息（如用户属性或社交网络）推断冷启动用户偏好，但忽略了与先进序列推荐模型的兼容性，难以高效提取序列特征。为此，本文提出CDMRec，一种用于用户冷启动序列推荐的因果扩散偏好模型。CDMRec为冷启动用户生成基于扩散的偏好表示，可直接用于现有序列推荐模型。该框架首先构建偏好主导序列（PDS），通过隔离最能指示用户兴趣的交互来减少无关行为噪声；然后利用因果推断从PDS中识别关键因果变量，以条件化扩散过程，生成个性化行为偏好。在三个公开数据集上的大量实验表明，CDMRec能无缝集成到主流序列推荐模型中，在冷启动设置下带来显著的性能提升。

### 主要创新

- 提出CDMRec框架，将扩散模型用于冷启动用户偏好生成，可直接集成到现有序列推荐模型。
- 构建偏好主导序列（PDS），通过隔离高兴趣相关交互减少噪声。
- 利用因果推断识别关键因果变量，条件化扩散过程，生成个性化偏好。
- 在多个数据集上验证了与主流序列推荐模型的兼容性和性能提升。

### 研究方法

CDMRec首先构建偏好主导序列（PDS），从用户交互中筛选出最能反映兴趣的行为。然后，利用因果推断从PDS中提取关键因果变量，作为扩散模型的条件。扩散模型生成冷启动用户的偏好表示，该表示可直接输入到现有的序列推荐模型中进行推荐。实验在三个公开数据集上进行，评估集成后的性能。

### 关键结果

在三个公开数据集上的实验表明，CDMRec可以无缝集成到主流序列推荐模型中，并在冷启动设置下带来显著的性能提升。

### 技术栈

- 扩散模型、因果推断、序列推荐模型

### 方法优势

- 提出了一种新颖的冷启动序列推荐方法，利用扩散模型生成偏好表示。
- 方法具有通用性，可集成到现有序列推荐模型中，提升冷启动性能。
- 通过构建PDS和因果推断，有效减少了噪声并增强了偏好建模的准确性。

### 主要局限

- 摘要未提供具体局限性。当前证据仅基于摘要，无法评估模型在非冷启动场景下的表现、计算复杂度、对辅助信息的依赖程度等。

### 与当前研究方向的关联

论文与序列推荐、生成式推荐、用户建模、因果性等关键词高度相关。它聚焦于冷启动场景下的序列推荐，利用扩散模型生成偏好，并引入因果推断，符合研究背景中强调的序列推荐、生成式推荐和因果性方向。

---

_知识库更新时间：2026-08-31T05:58:38.710528_
