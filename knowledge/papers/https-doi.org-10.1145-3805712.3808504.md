---
title: "CASE：面向大规模下一篮回购推荐的节奏感知集合编码"
paper_id: "https://doi.org/10.1145/3805712.3808504"
source: "sigir"
published: "2026-01-01T00:00:00"
score: 42.0
tags: ["paper", "recommender-systems"]
---

# CASE：面向大规模下一篮回购推荐的节奏感知集合编码

> **英文原标题**：CASE: Cadence-Aware Set Encoding for Large-Scale Next Basket Repurchase Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/CaoRSKNA26) · [ArXiv](https://arxiv.org/abs/2604.06718)

## 一句话结论

> 提出CASE模型，通过解耦物品级节奏学习和跨物品交互，利用多尺度时间卷积和集合注意力，在下一篮回购推荐中显著提升精度和召回率。

## 论文信息

- **作者**：Yanan Cao, Ashish Ranjan, Sinduja Subramaniam, Evren Korpeoglu, Kaushiki Nag, Kannan Achan
- **来源**：SIGIR
- **发布时间**：2026-01-01
- **相关度评分**：42.0
- **DOI**：[https://doi.org/10.1145/3805712.3808504](https://doi.org/10.1145/3805712.3808504)

<details open>
<summary><strong>中文摘要</strong></summary>

回购行为是大规模零售推荐中的主要信号，尤其在频繁补货的品类中：用户下一次购物篮中的许多商品都是此前购买过的，且其购买时机遵循稳定且具有商品特定节奏的规律。然而，现有的下一次购物篮回购推荐模型通常将历史记录表示为按访问顺序索引的离散购物篮事件序列，无法显式建模已流逝的日历时间，也无法在购买间隔期间更新商品排名。我们提出了CASE（节奏感知集合编码）方法用于下一次购物篮回购推荐，该方法将商品级别的节奏学习与跨商品交互解耦，在保持生产环境可扩展性的同时实现了显式的日历时间建模。CASE将每件商品的购买历史表示为固定时间范围内的日历时间信号，应用共享的多尺度时间卷积来捕捉重复出现的节奏，并使用归纳集合注意力以次二次复杂度建模跨商品依赖关系，从而支持大规模批量高效推理。在三个公开基准数据集和一个专有数据集上，与强基线下一次购物篮推荐方法相比，CASE在多个截断点上持续提升了精确率、召回率和NDCG。在包含数千万用户和大量商品目录的生产规模评估中，CASE在top-5推荐上实现了高达8.6%的相对精确率提升和9.9%的相对召回率提升，表明可扩展的节奏感知建模在基准测试和工业场景中均能带来可衡量的性能提升。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Repurchase behavior is a primary signal in large-scale retail recommendation, particularly in categories with frequent replenishment: many items in a user's next basket were previously purchased, and their timing follows stable, item-specific cadences. Yet most next basket repurchase recommendation models represent history as a sequence of discrete basket events indexed by visit order, which cannot explicitly model elapsed calendar time or update item rankings as days pass between purchases. We present CASE (Cadence-Aware Set Encoding) for next basket repurchase recommendation, which decouples item-level cadence learning from cross-item interaction, enabling explicit calendar-time modeling while remaining production-scalable. CASE represents each item's purchase history as a calendar-time signal over a fixed horizon, applies shared multi-scale temporal convolutions to capture recurring rhythms, and uses induced set attention to model cross-item dependencies with sub-quadratic complexity, allowing efficient batch inference at scale. Across three public benchmarks and a proprietary dataset, CASE consistently improves precision, recall, and NDCG at multiple cutoffs compared to strong next basket recommendation baselines. In a production-scale evaluation with tens of millions of users and a large item catalog, CASE achieves up to 8.6% relative precision lift and 9.9% relative recall lift at top-5, showing that scalable cadence-aware modeling yields measurable gains in both benchmark and industrial settings.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

论文针对大规模零售推荐中的回购行为，提出CASE模型。现有方法将用户历史建模为购物篮序列，无法显式建模日历时间。CASE将每个物品的购买历史表示为固定时间窗口内的二进制信号，通过共享多尺度时间卷积捕获重复节奏，并利用归纳集注意力以次二次复杂度建模物品间依赖。在三个公开数据集和一个专有数据集上，CASE在多个截断点上的精确率、召回率和NDCG均优于强基线。在千万级用户的生产规模评估中，CASE在top-5上实现了高达8.6%的精确率提升和9.9%的召回率提升。

### 主要创新

- 提出日历时间表示，将物品购买历史转化为二进制时间信号，显式建模经过的日历时间。
- 采用共享多尺度时间卷积（周、双周、月、季、趋势）捕获物品级重复节奏，无需用户特定参数。
- 使用归纳集注意力块（ISAB）建模跨物品依赖，复杂度为O(nm)，支持高效批量推理。
- 在千万级用户生产环境中验证了可扩展性和性能提升。

### 研究方法

CASE首先为每个物品构建固定时间窗口内的二进制购买指示向量。然后应用共享多尺度Conv1d滤波器（核大小7,14,28,91,182）提取节奏特征，拼接后通过全连接层得到节奏嵌入。将节奏嵌入与物品嵌入拼接，输入两个ISAB层（32个归纳点，4头注意力）建模物品间交互。最后通过两层MLP输出每个物品的得分，使用二元交叉熵损失训练。

### 关键结果

在TaFeng、DC、Instacart和专有数据集上，CASE在Precision@1/3/5/10、Recall@1/3/5/10和NDCG@1/3/5/10上均取得最佳或次佳结果。在专有数据集上，CASE相比生产模型在top-5上实现Precision提升8.63%，Recall提升9.90%，NDCG提升10.46%。消融实验表明，时间CNN是主导组件，移除后性能大幅下降；ISAB和物品嵌入提供额外增益。

### 技术栈

- 多尺度一维卷积（Conv1d）
- 归纳集注意力块（ISAB）
- Set Transformer
- 二元交叉熵损失
- Adam优化器
- PCA可视化

### 方法优势

- 显式建模日历时间，克服了购物篮序列表示的时间模糊性。
- 共享参数设计，无需用户特定参数，可扩展至千万级用户。
- 在多个公开数据集和生产环境中均取得一致提升。
- 消融实验充分，验证了各组件的贡献。

### 主要局限

- 假设历史节奏相对稳定，对非平稳信号（如购买渠道变化）处理能力有限。
- 使用固定多尺度核和固定时间窗口，缺乏自适应性。
- 未在极端稀疏场景（如极长回购周期、新物品）下深入分析。

### 与当前研究方向的关联

论文聚焦于序列推荐中的下一篮推荐任务，涉及用户建模、时序建模和工业落地，与序列推荐、用户建模、工业落地关键词高度相关。

---

_知识库更新时间：2026-07-17T03:54:55.380500_
