---
title: "ConciseExplain: Reducing Redundancy and Spuriousness in Persuasive Recommendation Explanation"
paper_id: "https://doi.org/10.1145/3711896.3737206"
source: "kdd"
published: "2025-01-01T00:00:00"
score: 20.0
tags: ["paper", "recommender-systems", "Explainable Artificial Intelligence (XAI)", "Topic Modeling", "Recommender Systems and Techniques"]
---

# ConciseExplain: Reducing Redundancy and Spuriousness in Persuasive Recommendation Explanation

[查看原文](https://dblp.org/rec/conf/kdd/0001LWWWX025) · [Semantic Scholar](https://www.semanticscholar.org/paper/d59389414bce9c2f26fe4ad70bee3b3ad1dae4d5)

## 一句话结论

> 本文提出ConciseExplain方法，通过掩码训练和梯度下降生成简洁的解释特征，以减少冗余和虚假信息，从而提升推荐系统在专业场景中的说服力，并在真实部署中验证了其有效性。

## 论文信息

- **作者**：Yixuan Cao, J.J. Liu, Haodong Wang, J. Wang, Kun Wan, Gang Xiao, Ping Luo
- **来源**：KDD
- **发布时间**：2025-01-01
- **相关度评分**：20.0
- **DOI**：[https://doi.org/10.1145/3711896.3737206](https://doi.org/10.1145/3711896.3737206)

<details open>
<summary><strong>中文摘要</strong></summary>

推荐系统是信息过滤和发现的有效工具。这些系统广泛应用于各类消费领域，并在专业领域中展现出提升工作效率的巨大潜力。然而，在专业背景下支持决策不仅需要提供推荐结果，还需要给出解释以说服用户采纳建议。以一级债券市场中的任务为例，销售人员需要为债券寻找潜在投资者，本文介绍了一个面向专业场景的推荐系统的开发与部署。该系统为其推荐提供一组关键特征作为解释。在此过程中，我们观察到现有的解释方法可能选择冗余和虚假的特征，这会削弱解释的说服力。为解决这一问题，我们提出了一种名为ConciseExplain的方法，该方法利用掩码训练策略和梯度下降直接识别出一组简洁的特征。我们在真实数据集和合成数据集上进行了实验。我们的方法在冗余度和虚假性指标上分别比最优基线方法取得了6.1%和12.4%的相对提升。此外，在在线人工评估中，我们的方法也优于基线方法。更重要的是，在我们系统于中信证券股份有限公司（中国领先的券商之一）正式部署的一年期间，我们观察到推荐系统准确率的持续提升。这表明，借助简洁的解释，推荐结果与投资决策之间可能建立起一种正向反馈循环。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Recommendation systems are effective tools for information filtering and discovery. These systems are widely applied across various consumer sectors and hold significant potential for applications in professional domains to enhance work efficiency. However, supporting decision-making in professional contexts requires not only providing recommendation results but also offering explanations to persuade users to adopt the suggestions. Taking the task in the primary bond market as an example, where sales staff seek potential investors for bonds, this paper presents the development and deployment of a recommendation system designed for a professional setting. The system provides a set of key features as explanations for its recommendations. In this process, we observe that current explanation methods may select redundant and spurious features, which can undermine the persuasive impact of the explanations. To address this issue, we propose a method named ConciseExplain, which leverages a mask training strategy and gradient descent to directly identify a concise set of features. We conduct experiments on real-world and synthetic datasets. Our method achieves relative improvements of 6.1% and 12.4% over the best-performing baseline on redundant and spurious metrics, respectively. Our method also outperforms the baseline method in online manual evaluations. Moreover, during the one-year official deployment of our system at China Securities Co., Ltd. (a leading brokerage firm in China), we observed a continuous improvement in the accuracy of the recommendation system. This suggests that, with concise explanations, a positive feedback loop might be established between recommendation outcomes and investment decisions.

</details>

---

_知识库更新时间：2026-08-01T04:05:05.966825_
