---
title: "基于情感向量的大型语言模型微调用于年龄感知的青少年图书推荐"
paper_id: "https://doi.org/10.1145/3705328.3748037"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 41.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Mental Health via Writing", "Sentiment Analysis and Opinion Mining"]
---

# 基于情感向量的大型语言模型微调用于年龄感知的青少年图书推荐

> **英文原标题**：Emotion Vector-Based Fine-Tuning of Large Language Models for Age-Aware Teenage Book Recommendations

[查看原文](https://dblp.org/rec/conf/recsys/HillNS25) · [Semantic Scholar](https://www.semanticscholar.org/paper/74d39faa8267de20d4083bf9b33015fe1fdc163d)

## 一句话结论

> 该论文提出一种基于情感向量的LLM微调方法，用于为青少年提供符合年龄和情感需求的图书推荐，实验证明该方法能显著提升推荐准确性和适龄性。

## 论文信息

- **作者**：K. Hill, Yiu‐Kai Ng, Joey Sherrill
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：41.0
- **DOI**：[https://doi.org/10.1145/3705328.3748037](https://doi.org/10.1145/3705328.3748037)

<details open>
<summary><strong>中文摘要</strong></summary>

阅读是青少年的一项关键技能，正如美国国家儿童健康与人类发展研究所所述：“阅读是获得幸福、充实且成功人生所必需的唯一最重要技能。”然而，青少年及其家长往往在琳琅满目的书籍选择中难以找到引人入胜的作品。此外，现有的图书推荐系统高度依赖用户数据，如个人资料、评论或浏览行为——而由于隐私法律，这些信息对未成年人通常受到限制。为解决这一问题，我们提出了一种注重隐私的青少年图书推荐系统，该系统利用NRC情绪强度词典（NRC Emotion Intensity Lexicon, NRC-EIL）分析书籍的情绪内容。通过从书籍描述中提取情绪向量，我们捕捉每本书的情绪基调和强度。我们的系统随后利用不同年龄群体间情绪偏好的模式，推荐与青少年读者发展及情感需求相符的书籍。尽管大语言模型（LLMs）也能为青少年提供基于内容的图书推荐，但它们仍面临训练偏差、对年龄特定细微差异的敏感度有限以及缺乏透明度等挑战。通过整合我们的情绪向量方法，我们对LLMs进行微调，使其更好地识别与年龄相关的情绪线索，增强其为青少年受众推荐有意义且适当内容的能力。实验结果证实，使用我们的情绪向量方法对LLMs进行微调，显著提升了其为青少年生成准确、适龄图书推荐的能力。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Reading is a vital skill for teenagers as described by the National Institute of Child Health and Human Development, “Reading is the single most important skill necessary for a happy, productive, and successful life." Yet, teens and their parents often struggle to find engaging books amid an overwhelming number of options. Moreover, existing book recommender systems rely heavily on user data such as profiles, reviews, or browsing behavior—information often restricted for minors due to privacy laws. To address this, we propose a privacy-conscious, teenage book recommender system that analyzes the emotional content of books using the NRC Emotion Intensity Lexicon (NRC-EIL). By extracting emotion vectors from book descriptions, we capture each book’s emotional tone and intensity. Our system then uses patterns in emotional preferences across age groups to recommend books that align with teen readers’ developmental and emotional needs. While LLMs can make content-based book recommendations for teenagers as well, they still face challenges like training bias, limited sensitivity to age-specific nuances, and lack of transparency. By integrating our emotion vector approach, we fine-tune LLMs to better detect age-relevant emotional cues, enhancing their ability to suggest meaningful and appropriate content for teen audiences. Experimental results confirm that fine-tuning LLMs with our emotional vector approach significantly enhances their ability to generate accurate, age-appropriate book recommendations for teenagers.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

本文针对青少年图书推荐中隐私限制和现有推荐系统依赖用户数据的问题，提出了一种隐私保护的推荐系统。该系统利用NRC情感强度词典从图书描述中提取情感向量，捕捉每本书的情感基调和强度，并根据不同年龄群体的情感偏好模式进行推荐。同时，通过将情感向量方法集成到大型语言模型（LLM）的微调中，增强其对年龄相关情感线索的敏感度，提高推荐准确性和适龄性。实验结果表明，该方法显著提升了LLM生成准确、适龄图书推荐的能力。

### 主要创新

- 提出基于情感向量的隐私保护推荐方法，不依赖用户个人数据
- 利用NRC情感强度词典提取图书情感向量，捕捉情感基调和强度
- 结合年龄群体的情感偏好模式，实现年龄感知的推荐
- 将情感向量集成到LLM微调中，增强模型对年龄相关情感线索的敏感度
- 实验验证了情感向量微调方法在青少年图书推荐中的有效性

### 研究方法

论文采用内容分析的方法，首先使用NRC情感强度词典从图书描述中提取情感向量，然后分析不同年龄群体的情感偏好模式，构建推荐系统。同时，将情感向量作为辅助特征，对大型语言模型进行微调，使其能够更好地捕捉年龄相关的情感线索，从而生成更准确的推荐。

### 关键结果

实验结果表明，将情感向量方法集成到LLM微调中，显著增强了模型生成准确、适龄图书推荐的能力。

### 技术栈

- NRC情感强度词典
- 情感向量提取
- 大型语言模型微调

### 方法优势

- 隐私保护：不依赖用户个人数据，符合青少年隐私法规
- 创新性：将情感向量与LLM结合，提升年龄感知能力
- 实用性：针对青少年图书推荐的实际问题，具有应用价值
- 实验验证：通过实验证明了方法的有效性

### 主要局限

- 摘要未提供具体实验细节，如数据集、基线、消融实验等，因此无法评估方法的泛化性和对比优势。

### 与当前研究方向的关联

该论文与关键词高度相关：涉及LLM与推荐系统结合（生成式推荐）、用户建模（年龄群体情感偏好）、以及推荐系统的鲁棒性（隐私保护）。

---

_知识库更新时间：2026-08-18T02:08:11.551682_
