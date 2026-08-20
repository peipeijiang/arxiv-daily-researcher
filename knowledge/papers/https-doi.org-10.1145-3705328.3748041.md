---
title: "HiDePCC: A Novel Dual-Pronged Untargeted Attack on Federated Recommendation via Gradient Perturbation and Cluster Crafting"
paper_id: "https://doi.org/10.1145/3705328.3748041"
source: "recsys"
published: "2025-01-01T00:00:00"
score: 25.0
tags: ["paper", "recommender-systems", "Privacy-Preserving Technologies in Data", "Recommender Systems and Techniques", "Cryptography and Data Security"]
---

# HiDePCC: A Novel Dual-Pronged Untargeted Attack on Federated Recommendation via Gradient Perturbation and Cluster Crafting

[查看原文](https://dblp.org/rec/conf/recsys/JhaTP25) · [Semantic Scholar](https://www.semanticscholar.org/paper/7d7c169a033847fbcef94041f4bad3f51cd90123)

## 一句话结论

> 本文提出一种针对联邦推荐系统的双重对抗攻击方法HiDePCC，通过梯度扰动和层次聚类操纵物品嵌入，显著降低推荐性能，揭示了联邦推荐系统的脆弱性。

## 论文信息

- **作者**：Yamini Jha, Krishna Tewari, Sukomal Pal
- **来源**：RecSys
- **发布时间**：2025-01-01
- **相关度评分**：25.0
- **DOI**：[https://doi.org/10.1145/3705328.3748041](https://doi.org/10.1145/3705328.3748041)

<details open>
<summary><strong>中文摘要</strong></summary>

联邦推荐系统通过分散用户数据并防止客户端之间的直接数据共享，提供了隐私保护优势。尽管这种架构限制了传统攻击策略的有效性，但它仍然容易受到微妙的对抗性攻击，这些攻击可能显著降低推荐的准确性。为了揭示这些漏洞，我们提出了一种新颖的非定向攻击方法（HiDePCC），通过结合自适应梯度扰动和基于层次聚类的嵌入操纵的双管齐下策略，来降低整体系统性能。我们在训练过程中对项目梯度施加自适应扰动，并采用多种链接方法的层次聚类来形成连贯的项目簇。在这些簇内，我们收敛项目嵌入并操纵边界点，以诱导项目误分类。这导致系统为聚类项目分配相似分数并错误排序。我们在两个基准数据集上评估了我们的攻击，即MovieLens（包含0.5%和1%的恶意用户）和Gowalla（1%），使用矩阵分解作为基础推荐模型，并评估了在各种鲁棒聚合技术下的影响。我们还考察了使用层次聚类、自适应梯度扰动和边界点误分类的多种配置组合。结果表明，完整的设置优于现有的最先进非定向攻击，在MovieLens上HR@5的性能下降范围为13.93%至68.02%，在Gowalla数据集上范围为40.02%至99.76%。这些发现揭示了联邦推荐系统中的重要漏洞。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Federated recommender systems offer privacy benefits by decentralizing user data and preventing direct data sharing among clients. Although this architecture limits the effectiveness of traditional attack strategies, it remains susceptible to subtle adversarial attacks that can significantly degrade the accuracy of recommendations. To expose these vulnerabilities, we propose a novel untargeted attack (HiDePCC) that degrades overall system performance through a dual-pronged strategy combining adaptive gradient perturbation and hierarchical cluster-based embedding manipulation. We apply adaptive perturbations to item gradients during training and employ hierarchical clustering using several linkage methods to form coherent item clusters. Within these clusters, we converge item embeddings and manipulate boundary points to induce item misclassification. This causes the system to assign similar scores to clustered items and misrank them. We evaluated our attack on two benchmark datasets, MovieLens (with 0.5% and 1% malicious users) and Gowalla (1%), using Matrix Factorization as the base recommendation model and assessing the impact in various robust aggregation techniques. We also examined several permutations of configurations using hierarchical clustering, adaptive gradient perturbation and boundary points misclassification. Our results show that the complete setup outperforms existing state-of-the-art untargeted attacks, with performance drops for HR@5 ranging from 13.93% to 68.02% on MovieLens and ranging from 40.02% and 99.76% on Gowalla dataset. These findings reveal important vulnerabilities in federated recommendation systems.

</details>

---

_知识库更新时间：2026-08-20T02:19:08.957189_
