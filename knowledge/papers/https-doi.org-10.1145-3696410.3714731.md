---
title: "Ranking Items by the Current-Preferences and Profits: A List-wise Learning-to-Rank Approach to Profit Maximization"
paper_id: "https://doi.org/10.1145/3696410.3714731"
source: "www"
published: "2025-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Consumer Market Behavior and Pricing", "Advanced Bandit Algorithms Research"]
---

# Ranking Items by the Current-Preferences and Profits: A List-wise Learning-to-Rank Approach to Profit Maximization

[查看原文](https://dblp.org/rec/conf/www/BaeJSK25)

## 一句话结论

> The paper proposes a list-wise learning-to-rank approach for profit-aware recommender systems that incorporates user current preferences and item profits to improve both accuracy and profit.

## 论文信息

- **作者**：Hong-Kyun Bae, Hae-Ri Jang, Won-Yong Shin, Sang‐Wook Kim
- **来源**：WWW
- **发布时间**：2025-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3696410.3714731](https://doi.org/10.1145/3696410.3714731)

<details open>
<summary><strong>中文摘要</strong></summary>

在电子商务平台中，利润感知推荐系统旨在提升平台利润，同时通过将高利润商品置于排名前列来保持整体准确性。我们探讨了现有基于模型的利润感知方法（即MBA）在训练推荐模型以提升利润时所面临的两个问题。首先，现有的MBA倾向于在不考虑用户当前对每个商品偏好的情况下，通过其基于利润的加权方案不准确地推断商品排名。其次，通过逐点学习排序（LTR），模型仅针对每个商品的偏好得分独立优化，而非直接针对商品的整体排名进行优化。为解决这些问题，我们提出了一种新颖的MBA方法，包含三个关键步骤：（S1）定义结合当前偏好与利润（即CPP）的商品指标；（S2）通过CPP对商品进行分类；（S3）基于CPP采用列表式LTR训练模型。使用真实平台数据集的广泛实验结果表明，与最优对比方法相比，我们的方法在准确性上提升了约4%，在利润上提升了约24%。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

In e-commerce platforms, profit-aware recommender systems aim to improve the platform's profits while maintaining high overall accuracy by recommending items with high profits as top-ranked items. We explore two issues faced by existing model-based profit-aware approaches (i.e., MBAs) when training recommendation models for profit enhancement. First, existing MBAs tend to inaccurately infer the item ranking without considering the user's current preference for each item through their profit-based weighting scheme. Second, through the point-wise learning-to-rank (LTR), the model is optimized solely for the preference score of each item independently rather than being directly optimized for the overall ranking of items. To tackle these issues, we propose a novel MBA that involves three key steps: (S1) defining the Current Preference incorporated with Profit (i.e., CPP) for items; (S2) classifying items through CPP; and (S3) training the model by list-wise LTR based on CPP. Extensive experimental results using real-world platform datasets demonstrate that our approach improves accuracy by approximately 4% and profits by about 24% compared to the best-competing method.

</details>

---

_知识库更新时间：2026-09-07T05:05:20.798128_
