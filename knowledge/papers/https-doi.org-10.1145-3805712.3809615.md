---
title: "Time-Interval-Aware Disentangled Expert Modeling for Next-Basket Recommendation"
paper_id: "https://doi.org/10.1145/3805712.3809615"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Mobile Crowdsensing and Crowdsourcing"]
---

# Time-Interval-Aware Disentangled Expert Modeling for Next-Basket Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/DengFFTLL26) · [ArXiv](https://arxiv.org/abs/2605.00499)

## 一句话结论

> 评分失败，无法生成摘要

## 论文信息

- **作者**：Zhiying Deng, Yuan Fu, Dr. Usman Farooq, Ziwei Tian, Wei Liu, Jianjun Li
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3805712.3809615](https://doi.org/10.1145/3805712.3809615)

<details>
<summary><strong>英文摘要</strong></summary>

Next-basket recommendation (NBR) is a type of recommendation that aims to predict a set of items a user will purchase based on their historical transaction basket sequences. It is governed by a dynamic interplay between two distinct user intents: habitual repurchase, which involves repeating past behaviors, and exploratory interest, which involves discovering new items. However, existing NBR methods generally suffer from two limitations: (1) they often entangle these conflicting motives within a single representation, causing habits to overshadow discovery, and (2) they rely on discrete sequential modeling that ignores continuous-time intervals and item-specific periodicities. In this paper, we propose a novel solution named Time-Interval Disentangled Experts (TIDE) to address these challenges. TIDE incorporates a Hawkes-enhanced Fourier Time Encoding to capture item-specific temporal periodicities and dynamic decay. To decouple user intentions, TIDE utilizes a dual-expert architecture that integrates a Habit Expert for recurring needs and a Pattern-Guided Exploration Expert for discovery. Combined with an item-aware gating mechanism, TIDE adaptively balances repurchase and exploration. Extensive experiments on four diverse real-world datasets demonstrate that TIDE consistently outperforms representative state-of-the-art NBR methods.

</details>

---

_知识库更新时间：2026-07-26T04:14:36.136982_
