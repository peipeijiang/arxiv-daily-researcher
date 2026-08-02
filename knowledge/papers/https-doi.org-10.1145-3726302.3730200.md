---
title: "GEAR：用于多行为序列推荐的广义交替回归器"
paper_id: "https://doi.org/10.1145/3726302.3730200"
source: "sigir"
published: "2025-01-01T00:00:00"
score: 43.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Advanced Bandit Algorithms Research", "Topic Modeling"]
---

# GEAR：用于多行为序列推荐的广义交替回归器

> **英文原标题**：GEAR: Generalized Alternating Regressor for Multi-Behavior Sequential Recommendation

[查看原文](https://dblp.org/rec/conf/sigir/00010KLG25)

## 一句话结论

> 本文提出GEAR框架，通过交替回归器统一建模多行为序列推荐中的行为、物品和时间动态，在真实数据集上验证了其有效性、泛化性和计算效率。

## 论文信息

- **作者**：Jiying Jiang, Kai Zhang, Junfeng Kang, Yucong Luo, Min Gao
- **来源**：SIGIR
- **发布时间**：2025-01-01
- **相关度评分**：43.0
- **DOI**：[https://doi.org/10.1145/3726302.3730200](https://doi.org/10.1145/3726302.3730200)

<details open>
<summary><strong>中文摘要</strong></summary>

现代推荐系统在建模用户多行为交互（如点击、加入购物车和购买）与驱动偏好演变的时序动态之间的复杂相互作用时，面临关键挑战。尽管现有的多行为序列推荐方法试图捕捉这些信号，但它们往往存在碎片化建模的问题，例如将行为与物品解耦为独立序列、忽略时间感知的转换，或依赖计算密集型架构而阻碍实际场景中的可扩展性。为解决上述局限，我们提出广义交替回归器（GEAR），一种新颖框架，通过交替架构将行为、物品和时间上下文统一到单一自回归序列中。其核心在于，GEAR将用户交互表示为三元组，并通过模块化Transformer架构进行处理。在该架构中，每个三元组在低层交替建模以解耦细粒度模式，而高层则联合学习跨信号依赖关系。这种设计模拟了齿轮的互锁机制，实现了多行为动态与物品转换之间的无缝过渡。此外，我们引入时间偏置项，以量化行为影响在短期和长期时间跨度上的衰减。在真实数据集上的大量实验验证了所提框架的有效性、泛化性和计算效率。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Modern recommender systems face a critical challenge in modeling the intricate interplay between multi-behavior interactions of users (e.g., clicks, adds-to-cart and purchases) and temporal dynamics that drive evolving preferences. While existing multi-behavior sequential recommendation methods attempt to capture these signals, they often suffer from fragmented modeling, such as decoupling behaviors and items into separate sequences, neglecting time-aware transitions, or relying on computationally intensive architectures that hinder real-world scalability. To address these limitations, we propose GEneralized Alternating Regressor (GEAR), a novel framework that unifies behaviors, items, and temporal contexts into a single autoregressive sequence through an alternating architecture. At its core, GEAR represents user interactions as triplets and processes them through a modular transformer architecture. In this architecture, each triplet is alternately modeled at lower layers to disentangle fine-grained patterns, while upper layers jointly learn cross-signal dependencies. This design mimics the interlocking mechanism of gears, enabling the seamless transitions between multi-behavior dynamics and item transitions. Additionally, we incorporate a time-bias term to quantify the decay of behavioral influence across both short- and long-term horizons. Extensive experiments on real-world datasets validate the effectiveness, generalizability, and computational efficiency of the proposed framework.

</details>

## 深度解读

> 分析依据：**摘要分析**

### 核心结论

现代推荐系统在建模用户多行为交互（如点击、加购、购买）与时间动态之间的复杂关系时面临挑战。现有方法存在碎片化建模问题，如将行为与物品分离、忽略时间感知转换或依赖高计算架构。为此，本文提出GEAR框架，通过交替架构将行为、物品和时间上下文统一到单一自回归序列中。GEAR将用户交互表示为三元组，并通过模块化Transformer处理：低层交替建模以解耦细粒度模式，高层联合学习跨信号依赖，模拟齿轮互锁机制，实现多行为动态与物品转换的无缝衔接。此外，引入时间偏置项量化行为影响在短期和长期内的衰减。在真实数据集上的实验验证了框架的有效性、泛化性和计算效率。

### 主要创新

- 提出统一行为、物品和时间的单一自回归序列框架，避免碎片化建模。
- 设计交替架构，低层解耦细粒度模式，高层学习跨信号依赖，模拟齿轮机制。
- 引入时间偏置项，量化行为影响在短期和长期内的衰减。
- 在保持性能的同时提升计算效率，适合实际部署。

### 研究方法

GEAR将用户交互表示为三元组，通过模块化Transformer架构处理。该架构采用交替设计：低层交替建模每个三元组以解耦细粒度模式，高层联合学习跨信号依赖。同时，引入时间偏置项来调整行为影响的时间衰减。整体采用自回归方式生成序列。

### 关键结果

在真实世界数据集上的实验验证了框架的有效性、泛化性和计算效率。具体指标和数据集名称摘要未提供。

### 技术栈

- Transformer架构
- 自回归模型
- 交替建模机制
- 时间偏置项

### 方法优势

- 统一建模多行为和时间动态，克服碎片化问题。
- 交替架构设计新颖，模拟齿轮机制，增强跨信号依赖学习。
- 时间偏置项有效处理短期和长期影响。
- 计算效率高，适合实际应用。

### 主要局限

- 论文局限：摘要未提及具体局限性。当前证据局限：仅基于摘要，无法评估模型细节、实验对比、泛化边界等。

### 与当前研究方向的关联

该论文与序列推荐、多行为推荐、时间动态建模、Transformer架构、自回归生成等关键词高度相关。

---

_知识库更新时间：2026-08-02T04:11:29.700231_
