---
title: "连接兴趣与真相：迈向个性化且真实的推荐以缓解假新闻"
paper_id: "https://doi.org/10.1145/3726302.3729912"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 46.0
tags: ["paper", "recommender-systems", "Misinformation and Its Impacts", "Spam and Phishing Detection", "Topic Modeling"]
---

# 连接兴趣与真相：迈向个性化且真实的推荐以缓解假新闻

> **英文原标题**：Bridging Interests and Truth: Towards Mitigating Fake News with Personalized and Truthful Recommendations

[查看原文](https://dblp.org/rec/conf/sigir/0001LHZKW25) · [Semantic Scholar](https://www.semanticscholar.org/paper/fb353ae010c144531db075c33e9860f97c13eda8)

## 一句话结论

> 论文提出PRISM框架，利用扩散模型生成个性化且真实的新闻推荐，以缓解假新闻传播问题。

## 论文信息

- **作者**：Zihan Ma, Minnan Luo, Yiran Hao, Zhi Zeng, Xiangzheng Kong, Jiahao Wang
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：46.0
- **DOI**：[https://doi.org/10.1145/3726302.3729912](https://doi.org/10.1145/3726302.3729912)

<details open>
<summary><strong>中文摘要</strong></summary>

尽管虚假新闻的泛滥对信息完整性构成了重大威胁，但现有的应对措施，尤其是在个性化新闻推荐系统中的应用，已被证明效果不足。传统方法通常依赖分类器过滤虚假内容，但其准确性有限，且无法充分捕捉用户的多样化兴趣。为解决这些挑战，我们提出了PRISM——一种基于扩散模型的兴趣感知序列建模的增强推荐保护框架。PRISM利用扩散模型的生成与控制能力，从用户的阅读历史中逐步学习其隐含兴趣分布，从而生成既符合用户语言偏好又契合其兴趣领域的个性化推荐。此外，PRISM在内容生成过程中引入预训练的真实性表征作为约束，确保推荐新闻的可信度，并有效遏制虚假新闻的传播。多维度综合评估证明了我们模型的优越性。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

While the proliferation of fake news poses a significant threat to information integrity, existing efforts to counter it, especially within personalized news recommendation systems, have proven inadequate.Traditional methods, which often rely on classifiers to filter out fake content, are limited by their accuracy and their inability to fully capture the diverse interests of users.To address these challenges, we proposed PRISM-Protection-enhanced Recommendation with Interest-aware Sequential Modeling-a novel framework based on diffusion models.PRISM harnesses the generative and control capabilities of diffusion models to progressively learn the implicit distribution of user interests from their reading history, thereby generating personalized recommendations that align with both their linguistic preferences and interest domains.Furthermore, PRISM incorporates pre-trained authenticity representations as constraints during content generation, ensuring the credibility of the recommended news and effectively curbing the spread of fake news.Comprehensive evaluations from multiple dimensions demonstrate the superiority of our model.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

假新闻的泛滥对信息完整性构成严重威胁，而现有的应对措施，尤其是在个性化新闻推荐系统中，效果不佳。传统方法依赖分类器过滤虚假内容，受限于准确性和无法充分捕捉用户多样化的兴趣。为此，本文提出PRISM（保护增强的推荐与兴趣感知序列建模），一种基于扩散模型的新框架。PRISM利用扩散模型的生成和控制能力，从用户阅读历史中逐步学习用户兴趣的隐式分布，从而生成既符合语言偏好又符合兴趣领域的个性化推荐。此外，PRISM在内容生成过程中融入预训练的真实性表征作为约束，确保推荐新闻的可信度，有效遏制假新闻的传播。多维度综合评估证明了该模型的优越性。

### 主要创新

- 提出基于扩散模型的PRISM框架，用于个性化新闻推荐，同时兼顾真实性和用户兴趣。
- 利用扩散模型逐步学习用户兴趣的隐式分布，实现个性化推荐。
- 将预训练的真实性表征作为生成约束，确保推荐内容的可信度。
- 通过生成式方法而非传统分类器，克服了分类器准确性和用户兴趣捕捉的局限。

### 研究方法

PRISM框架基于扩散模型，通过序列建模捕捉用户阅读历史中的兴趣模式，并利用扩散模型的生成能力产生推荐。在生成过程中，引入预训练的真实性表征作为约束，以平衡个性化与真实性。

### 关键结果

摘要未提供具体实验数据，但指出多维度综合评估证明了模型的优越性。

### 技术栈

- 扩散模型、序列建模、预训练真实性表征

### 方法优势

- 创新性地将扩散模型应用于假新闻缓解，结合生成式推荐。
- 同时考虑用户兴趣和内容真实性，解决传统方法的局限。
- 利用生成式方法可能更灵活地适应多样化用户兴趣。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估实验细节、数据集、基线等。

### 与当前研究方向的关联

该论文与序列推荐、生成式推荐、用户建模等关键词高度相关，同时涉及推荐系统的鲁棒性和真实性，与假新闻缓解相关。

---

_知识库更新时间：2026-08-22T02:17:50.833484_
