---
title: "Pay Attention to Sequence Split: Uncovering the Impacts of Sub-Sequence Splitting on Sequential Recommendation Models"
paper_id: "https://doi.org/10.1145/3805712.3808548"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 0.0
tags: ["paper", "recommender-systems"]
---

# Pay Attention to Sequence Split: Uncovering the Impacts of Sub-Sequence Splitting on Sequential Recommendation Models

[查看原文](https://dblp.org/rec/conf/sigir/DangWHZMGWS26) · [ArXiv](https://arxiv.org/abs/2604.05309)

## 一句话结论

> 评分失败，无法生成摘要

## 论文信息

- **作者**：Yizhou Dang, Yifan Wu, Minhan Huang, Chuang Zhao, Lianbo Ma, Guibing Guo, Xingwei Wang, Zhu Sun
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：0.0
- **DOI**：[https://doi.org/10.1145/3805712.3808548](https://doi.org/10.1145/3805712.3808548)

<details>
<summary><strong>英文摘要</strong></summary>

Sub-sequence splitting (SSS) has been demonstrated as an effective approach to mitigate data sparsity in sequential recommendation (SR) by splitting a raw user interaction sequence into multiple sub-sequences. Previous studies have demonstrated its ability to enhance the performance of SR models significantly. However, in this work, we discover that \textbf{(i). SSS may interfere with the evaluation of the model's actual performance.} We observed that many recent state-of-the-art SR models employ SSS during the data reading stage (not mentioned in the papers). When we removed this operation, performance significantly declined, even falling below that of earlier classical SR models. The varying improvements achieved by SSS and different splitting methods across different models prompt us to analyze further when SSS proves effective. We find that \textbf{(ii). SSS demonstrates strong capabilities only when specific splitting methods, target strategies, and loss functions are used together.} Inappropriate combinations may even harm performance. Furthermore, we analyze why sub-sequence splitting yields such remarkable performance gains and find that \textbf{(iii). it evens out the distribution of training data while increasing the likelihood that different items are targeted.} Finally, we provide suggestions for overcoming SSS interference, along with a discussion on data augmentation methods and future directions. We hope this work will prompt the broader community to re-examine the impact of data splitting on SR and promote fairer, more rigorous model evaluation. All analysis code and data will be made available upon acceptance. We provide a simple, anonymous implementation at https://github.com/KingGugu/SSS4SR.

</details>

---

_知识库更新时间：2026-07-25T03:51:56.884751_
