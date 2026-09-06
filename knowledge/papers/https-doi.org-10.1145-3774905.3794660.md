---
title: "Post-Training Fairness Control: A Single-Train Framework for Dynamic Fairness in Recommendation"
paper_id: "https://doi.org/10.1145/3774905.3794660"
source: "www"
published: "2026-01-01T00:00:00"
score: 35.0
tags: ["paper", "recommender-systems", "Ethics and Social Impacts of AI", "Recommender Systems and Techniques", "Mobile Crowdsensing and Crowdsourcing"]
---

# Post-Training Fairness Control: A Single-Train Framework for Dynamic Fairness in Recommendation

[查看原文](https://dblp.org/rec/conf/www/ChenCZ26) · [ArXiv](https://arxiv.org/abs/2601.20848) · [Semantic Scholar](https://www.semanticscholar.org/paper/ee695cbffcfbe63f8372964c04573e9198b03efd)

## 一句话结论

> 该论文提出Cofair框架，通过单次训练实现推荐系统的动态公平性控制，无需针对不同公平性要求重新训练，在多个数据集上取得了与最先进基线相当或更好的公平性-准确性权衡。

## 论文信息

- **作者**：Weixin Chen, Li Chen, Yuhan Zhao
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：35.0
- **DOI**：[https://doi.org/10.1145/3774905.3794660](https://doi.org/10.1145/3774905.3794660)

<details open>
<summary><strong>中文摘要</strong></summary>

尽管在缓解推荐系统不公平性方面已有越来越多的努力，现有的公平性感知方法通常仅在训练时固定公平性要求，并在训练后提供有限的灵活性。然而，在现实场景中，不同利益相关者可能随时间提出不同的公平性要求，因此针对不同公平性要求进行重新训练变得不可行。为解决这一局限，我们提出了Cofair，一种单次训练框架，能够在推荐中实现训练后的公平性控制。具体而言，Cofair引入了一个共享表示层，并配备公平性条件适配器模块，以生成针对不同公平性水平专门化的用户嵌入，同时加入用户级正则化项，以保证跨这些水平的用户级单调公平性提升。我们从理论上证明，Cofair的对抗目标上界约束了人口统计均等性，且正则化项在用户层面强制实现渐进式公平性。在多个数据集和骨干模型上的综合实验表明，我们的框架能够提供不同水平的动态公平性，在公平性-准确性曲线上达到与最先进基线相当或更优的表现，且无需针对每个新的公平性要求重新训练。我们的代码公开于 https://github.com/weixinchen98/Cofair。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Despite growing efforts to mitigate unfairness in recommender systems, existing fairness-aware methods typically fix the fairness requirement at training time and provide limited post-training flexibility. However, in real-world scenarios, diverse stakeholders may demand differing fairness requirements over time, so retraining for different fairness requirements becomes prohibitive. To address this limitation, we propose Cofair, a single-train framework that enables post-training fairness control in recommendation. Specifically, Cofair introduces a shared representation layer with fairness-conditioned adapter modules to produce user embeddings specialized for varied fairness levels, along with a user-level regularization term that guarantees user-wise monotonic fairness improvements across these levels. We theoretically establish that the adversarial objective of Cofair upper bounds demographic parity and the regularization term enforces progressive fairness at user level. Comprehensive experiments on multiple datasets and backbone models demonstrate that our framework provides dynamic fairness at different levels, delivering comparable or better fairness-accuracy curves than state-of-the-art baselines, without the need to retrain for each new fairness requirement. Our code is publicly available at https://github.com/weixinchen98/Cofair.

</details>

---

_知识库更新时间：2026-09-06T04:59:26.703414_
