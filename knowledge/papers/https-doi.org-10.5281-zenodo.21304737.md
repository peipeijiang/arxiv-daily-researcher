---
title: "Causal-BPR: Causal Bayesian Personalized Ranking for Unbiased Recommendation under Exposure Bias"
paper_id: "https://doi.org/10.5281/zenodo.21304737"
source: "openalex"
published: "2026-07-11T00:00:00"
score: 45.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Explainable Artificial Intelligence (XAI)"]
---

# Causal-BPR: Causal Bayesian Personalized Ranking for Unbiased Recommendation under Exposure Bias

提出Causal-BPR框架，通过结构因果模型解耦用户交互中的因果兴趣路径和曝光偏差路径，结合逆倾向评分和因果感知负采样，实现无偏的贝叶斯个性化排序。

## Metadata

- Authors: Jincheng Zhang
- DOI: https://doi.org/10.5281/zenodo.21304737
- URL: https://doi.org/10.5281/zenodo.21304737
- Venue: Zenodo (CERN European Organization for Nuclear Research)
- Score: 45.0

## Abstract

Recommender systems relying on implicit feedback often suffer from severe exposure bias, as unobserved interactions are mixed with true negative feedback and items left unexposed due to system ranking policies. Standard pairwise recommendation algorithms, such as Bayesian Personalized Ranking (BPR), optimize based on observed correlations rather than true user preferences, leading to the "rich-get-richer" Matthew effect and suboptimal ranking performance. To address these challenges, this paper proposes Causal-BPR, a novel causal Bayesian personalized ranking framework that decouples user interactions into distinct pathways using structural causal models (SCMs). Specifically, we distinguish the "causal interest pathway" from the "exposure bias pathway" to isolate true user preferences from systemic visibility. Based on this causal graph decomposition, we introduce a counterfactual optimization mechanism that executes Bayesian posterior updates exclusively along the causal pathway. By incorporating inverse propensity scoring (IPS) into the pairwise loss and designing a causal-aware negative sampling strategy, Causal-BPR theoretically transforms the biased observational empirical risk into an unbiased ideal risk estimation. Theoretical analysis proves that our framework achieves asymptotic causal unbiasedness and maintains bounded gradient variance under clipping constraints. This work completes a rigorous theoretical loop from causal factorization to robust parameter estimation, providing a solid mathematical foundation for mitigating exposure bias in implicit-feedback top-N recommendation.

## Chinese Abstract

依赖隐式反馈的推荐系统常遭受严重的曝光偏差，因为未观测到的交互中混杂着真实负反馈以及因系统排序策略而未被曝光的物品。标准成对推荐算法（如贝叶斯个性化排序，BPR）基于观测到的相关性而非真实用户偏好进行优化，导致“富者愈富”的马太效应及次优的排序性能。为解决这些挑战，本文提出Causal-BPR——一种新颖的因果贝叶斯个性化排序框架，利用结构因果模型（SCM）将用户交互解耦为不同路径。具体而言，我们区分“因果兴趣路径”与“曝光偏差路径”，以将真实用户偏好与系统性可见性相分离。基于此因果图分解，我们引入反事实优化机制，该机制仅沿因果路径执行贝叶斯后验更新。通过将逆倾向评分（IPS）融入成对损失并设计因果感知负采样策略，Causal-BPR在理论上将有偏的观测经验风险转化为无偏的理想风险估计。理论分析证明，我们的框架实现了渐近因果无偏性，并在裁剪约束下保持有界梯度方差。本工作完成了从因果分解到稳健参数估计的严格理论闭环，为缓解隐式反馈Top-N推荐中的曝光偏差提供了坚实的数学基础。

## Deep Analysis

```json
{
  "chinese_title": "Causal-BPR：面向曝光偏差的无偏推荐因果贝叶斯个性化排序",
  "summary": "针对隐式反馈推荐系统中因曝光偏差导致未交互项混杂真实负反馈与未曝光项的问题，本文提出Causal-BPR框架。通过结构因果模型将用户交互解耦为因果兴趣路径和曝光偏差路径，仅沿因果路径执行贝叶斯后验更新。引入逆倾向评分加权成对损失和因果感知负采样策略，理论上将有偏观测经验风险转化为无偏理想风险估计。理论分析证明框架渐近因果无偏性，并在截断约束下保持有界梯度方差。",
  "innovations": [
    "提出因果图分解，将用户点击行为解耦为因果兴趣路径和曝光偏差路径。",
    "设计仅沿因果路径进行贝叶斯后验更新的优化机制。",
    "引入逆倾向评分（IPS）加权成对损失，实现无偏风险估计。",
    "提出因果感知负采样策略，优先采样高曝光但未点击的负样本。",
    "理论证明渐近因果无偏性和有界梯度方差。"
  ],
  "methodology": "基于结构因果模型（SCM）构建因果图，将观测点击概率分解为因果兴趣与曝光概率的乘积。采用矩阵分解架构，分别设置因果兴趣空间和曝光偏差空间的嵌入向量。通过逆倾向评分加权成对损失函数，结合因果感知负采样，使用随机梯度下降（SGD）优化因果参数。",
  "key_results": "输入内容未提供",
  "tech_stack": [
    "结构因果模型（SCM）",
    "贝叶斯个性化排序（BPR）",
    "逆倾向评分（IPS）",
    "矩阵分解（MF）",
    "随机梯度下降（SGD）",
    "sigmoid函数",
    "最大后验概率估计"
  ],
  "strengths": [
    "从因果角度系统解决了曝光偏差问题，理论框架完整。",
    "提出可操作的解耦机制和加权损失函数，具有数学严谨性。",
    "理论证明了无偏性和收敛性，为算法提供了可靠保证。",
    "设计了因果感知采样策略，提升训练效率。"
  ],
  "limitations": [
    "未进行实验验证，缺乏实际数据集上的性能评估。",
    "倾向评分估计依赖全局统计或辅助学习，准确性可能受限。",
    "截断超参数epsilon需要在偏差与方差间权衡，无自动选择方法。",
    "仅考虑曝光偏差，未涉及其他偏差（如选择偏差、流行度偏差）。"
  ],
  "relevance_to_keywords": [
    "推荐系统：核心研究领域，提出推荐算法Causal-BPR。",
    "隐式反馈：论文针对隐式反馈中的曝光偏差问题。",
    "贝叶斯个性化排序：论文基于BPR框架进行因果改进。",
    "因果推断：论文核心方法，使用SCM和IPS实现无偏推荐。",
    "曝光偏差：论文主要解决的问题。"
  ],
  "_analysis_basis": "full_text"
}
```
