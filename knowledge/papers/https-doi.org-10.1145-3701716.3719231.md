---
title: "检索增强的多智能体推荐系统"
paper_id: "https://doi.org/10.1145/3701716.3719231"
source: "www"
published: "2025-01-01T00:00:00"
score: 58.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Topic Modeling", "Advanced Graph Neural Networks"]
---

# 检索增强的多智能体推荐系统

> **英文原标题**：Retrieval Augmented Multi-agent Recommender

[查看原文](https://dblp.org/rec/conf/www/AoHLMZZ25)

## 一句话结论

> 该论文提出了一种基于大语言模型的多智能体推荐框架，通过检索增强特征提取和数据驱动策略，在Amazon、Goodreads和Yelp数据集上显著提升了推荐性能，命中率较基线提升101%。

## 论文信息

- **作者**：Xiao Ao, S. Han, Yeming Li, Haijun Ma, Pengfei Zhang, Jie Zou
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：58.0
- **DOI**：[https://doi.org/10.1145/3701716.3719231](https://doi.org/10.1145/3701716.3719231)

<details open>
<summary><strong>中文摘要</strong></summary>

在线评论平台在当今数字世界中对于塑造消费者选择与体验至关重要。AgentSociety挑战赛聚焦于利用大语言模型（LLM）智能体推进个性化推荐，旨在增强网络交互与用户满意度。本文介绍了电子科技大学团队在AgentSociety挑战赛推荐赛道中获得第一名的解决方案。我们提出了一种基于大语言模型的推荐框架，融合了检索增强的特征提取与数据驱动的多智能体策略。我们方法的核心优势体现在两个关键方面。首先，为优化产品与用户两者的表示，我们设计了一种检索增强的特征提取机制，将结构化产品属性与非结构化用户评论相结合，同时捕捉产品的客观特征与用户的主观偏好。其次，我们引入了一个数据驱动的多智能体系统，该系统根据不同数据集之间的异质性特征自适应地调整处理策略，从而有效挖掘有价值的潜在信息。我们的方法基于Qwen-72B-Instruct模型构建，并在推荐准确性与系统稳定性方面进行了进一步优化。在三个广泛使用的数据集——Amazon、Goodreads和Yelp上的实验结果表明，推荐性能得到了显著提升。最终，我们的解决方案取得了0.4744的总体命中率得分，较基线提升了101%，展示了其在个性化推荐任务中的卓越有效性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Online review platforms are vital for shaping consumer choices and experiences in today's digital world. The AgentSociety Challenge focuses on advancing personalized recommendations with large language model (LLM) agents, aiming to enhance web interactions and user satisfaction. This paper presents the first-place solution for the AgentSociety Challenge Recommendation Track, by the team of the University of Electronic Science and Technology of China. We propose a recommendation framework based on large language models, integrating retrieval-augmented feature extraction and a data-driven multi-agent strategy. The core advantages of our approach lie in two key aspects. First, to optimize the representation of both products and users, we design a retrieval-augmented feature extraction mechanism that combines structured product attributes with unstructured user reviews, capturing both the objective characteristics of products and users' subjective preferences. Second, we introduce a data-driven multi-agent system that adaptively adjusts processing strategies based on the heterogeneous characteristics of different datasets, thereby effectively uncovering valuable latent information. Our method is built upon the Qwen-72B-Instruct model, with further optimizations in recommendation accuracy and system stability. Experimental results on three widely used datasets-Amazon, Goodreads, and Yelp-demonstrate significant improvements in recommendation performance. Ultimately, our solution achieved an overall hit rate score of 0.4744, representing a 101% improvement over the baseline, showcasing its outstanding effectiveness in personalized recommendation tasks.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

在线评论平台在当今数字世界中对于塑造消费者选择和体验至关重要。AgentSociety挑战赛专注于利用大语言模型智能体推进个性化推荐，旨在增强网络交互和用户满意度。本文介绍了电子科技大学团队在AgentSociety挑战赛推荐赛道中获得第一名的解决方案。我们提出了一种基于大语言模型的推荐框架，融合了检索增强的特征提取和数据驱动的多智能体策略。该方法的核心优势在于两个方面：首先，为了优化产品和用户的表示，我们设计了一种检索增强的特征提取机制，将结构化产品属性与非结构化用户评论相结合，捕捉产品的客观特征和用户的主观偏好；其次，我们引入了一个数据驱动的多智能体系统，根据数据集的不同特征自适应调整处理策略，从而有效挖掘有价值的潜在信息。我们的方法基于Qwen-72B-Instruct模型，并在推荐准确性和系统稳定性方面进行了进一步优化。在Amazon、Goodreads和Yelp三个广泛使用的数据集上的实验结果表明，推荐性能显著提升。最终，我们的方案取得了0.4744的整体命中率分数，比基线提高了101%，展示了其在个性化推荐任务中的卓越有效性。

### 主要创新

- 提出检索增强的特征提取机制，结合结构化产品属性与非结构化用户评论，同时捕捉客观特征和主观偏好。
- 引入数据驱动的多智能体系统，根据数据集异质性自适应调整处理策略，有效挖掘潜在信息。
- 基于Qwen-72B-Instruct模型进行优化，提升推荐准确性和系统稳定性。
- 在多个数据集上实现显著性能提升，整体命中率较基线提高101%。

### 研究方法

论文提出一种基于大语言模型的推荐框架，包含两个核心部分：检索增强的特征提取机制，用于融合产品属性和用户评论；数据驱动的多智能体系统，用于自适应处理不同数据集。整体基于Qwen-72B-Instruct模型，并进行了进一步优化。

### 关键结果

在Amazon、Goodreads和Yelp三个数据集上取得显著性能提升，最终整体命中率分数为0.4744，较基线提高101%。

### 技术栈

- 摘要未提供具体算法、工具或数学方法的细节，仅提及使用Qwen-72B-Instruct模型。

### 方法优势

- 创新性地结合检索增强特征提取与多智能体策略，有效利用异构数据。
- 在多个数据集上验证了方法的有效性，性能提升显著。
- 基于强大的Qwen-72B-Instruct模型，具备良好的基础。

### 主要局限

- 论文局限：摘要未提及方法的潜在局限性，如计算成本、泛化能力等。当前证据局限：由于仅提供摘要，无法评估方法的详细实现、消融实验、对比基线等，也无法验证结果的可靠性。

### 与当前研究方向的关联

论文与关键词高度相关，涉及LLM与推荐系统结合、推荐智能体、用户建模、序列推荐等方向，但摘要未明确提及具体技术细节，如是否使用序列推荐或对话式推荐。

---

_知识库更新时间：2026-09-05T04:50:29.988606_
