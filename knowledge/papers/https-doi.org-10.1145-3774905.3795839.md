---
title: "Multi-Branch Cooperation Networks for Enhanced Click-Through Rate Prediction in Large-Scale E-Commerce Search"
paper_id: "https://doi.org/10.1145/3774905.3795839"
source: "www"
published: "2026-01-01T00:00:00"
score: 36.0
tags: ["paper", "recommender-systems", "Complex Network Analysis Techniques", "Recommender Systems and Techniques", "Advanced Clustering Algorithms Research"]
---

# Multi-Branch Cooperation Networks for Enhanced Click-Through Rate Prediction in Large-Scale E-Commerce Search

[查看原文](https://dblp.org/rec/conf/www/ChenCXJLLZZ26) · [Semantic Scholar](https://www.semanticscholar.org/paper/86659f9e33a06be29ee35c27dcf9c18f708ef496)

## 一句话结论

> 该论文提出了一种多分支合作网络（MBCnet），通过分支间的协同教学和适度差异化来增强特征交互建模，从而提升大规模电商搜索中的点击率预测性能。

## 论文信息

- **作者**：Xu Chen, Zida Cheng, Shuai Xiao, Chen Ju, Xiaoming Liu, Jinsong Lan, Xiaobo Zhu, Bo Zheng
- **来源**：WWW
- **发布时间**：2026-01-01
- **相关度评分**：36.0
- **DOI**：[https://doi.org/10.1145/3774905.3795839](https://doi.org/10.1145/3774905.3795839)

<details open>
<summary><strong>中文摘要</strong></summary>

现有的点击率（CTR）预测模型采用了多种特征交互技术，每种技术各有独特优势，但仅依赖单一类型会限制其捕捉复杂关系的能力。近期研究表明，有效的CTR模型通常将MLP网络与专用特征交互网络以双并行结构相结合。然而，不同流或分支之间的相互作用及协作动态仍未得到充分研究。在本工作中，我们提出了一种新颖的多分支协作网络（MBCnet），该网络使多个分支网络能够相互协作，以更好地建模复杂的特征交互。具体而言，MBCnet由三个分支组成：可扩展特征分组与交叉（EFGC）分支，用于提升模型对特定特征组合的记忆能力；低秩Cross Net分支和Deep分支，分别增强显式和隐式特征交叉以提升泛化能力。其中，我们基于两个明确目标提出了一种新型协作方案：分支互教（branch co-teaching），鼓励学习较好的分支在特定训练样本上支持学习较差的分支；以及适度差异化（moderate differentiation），倡导各分支在同一输入上保持合理水平的特征表示差异。该协作策略通过相互知识共享改善学习过程，并促进跨分支发现多样化的特征交互。在大规模工业数据集上的广泛实验及在线A/B测试均证明了MBCnet的优越性能。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Existing Click-Through Rate (CTR) prediction models use various feature interaction techniques, each with unique strengths, but relying on a single type limits their ability to capture complex relationships. Recent research shows that effective CTR models often combine an MLP network with a dedicated feature interaction network in a two-parallel structure. However, the interplay and cooperative dynamics between different streams or branches remain under-researched. In this work, we introduce a novel Multi-Branch Cooperation Network (MBCnet) which enables multiple branch networks to collaborate with each other for better complex feature interaction modeling. Specifically, MBCnet consists of three branches: the Extensible Feature Grouping and Crossing (EFGC) branch that promotes the model's memorization ability of specific feature combinations, the low rank Cross Net branch and Deep branch to enhance explicit and implicit feature crossing for generalization. Among them, a novel cooperation scheme is proposed based on two formulated objectives: branch co-teaching that encourages well-learned branches to support poorly-learned ones on specific training samples, and moderate differentiation that advocates branches to maintain a reasonable level of difference in their feature representations on the same inputs. This cooperation strategy improves learning through mutual knowledge sharing and boosts the discovery of diverse feature interactions across branches. Extensive experiments on large-scale industrial datasets and online A/B test demonstrate MBCnet's superior performance.

</details>

---

_知识库更新时间：2026-09-06T04:59:26.702914_
