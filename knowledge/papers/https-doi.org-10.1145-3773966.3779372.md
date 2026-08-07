---
title: "预见性预测增强的直播推荐"
paper_id: "https://doi.org/10.1145/3773966.3779372"
source: "wsdm"
published: "2026-01-01T00:00:00"
score: 50.0
tags: ["paper", "recommender-systems", "Recommender Systems and Techniques", "Image and Video Quality Assessment", "Video Analysis and Summarization"]
---

# 预见性预测增强的直播推荐

> **英文原标题**：Foresight Prediction Enhanced Live-Streaming Recommendation

[查看原文](https://dblp.org/rec/conf/wsdm/CaoYCLLHTWYLZ26) · [ArXiv](https://arxiv.org/abs/2512.06700)

## 一句话结论

> 该论文提出了一种通过语义量化直播片段并预测未来内容来增强直播推荐排序模型的方法，离线与在线实验证明其有效性并已部署于大规模平台。

## 论文信息

- **作者**：Jiangxia Cao, Ruochen Yang, Xiang Chen, Changxin Lao, Yueyang Liu, Yusheng Huang, Yuanhao Tian, Xiangyu Wu, Shuang Yang, Zhaojie Liu, Guorui Zhou
- **来源**：WSDM
- **发布时间**：2026-01-01
- **相关度评分**：50.0
- **DOI**：[https://doi.org/10.1145/3773966.3779372](https://doi.org/10.1145/3773966.3779372)

<details open>
<summary><strong>中文摘要</strong></summary>

直播作为一种新兴媒体，实现了作者与用户之间的实时互动，已引起广泛关注。不同于传统电视直播的固定播放时间或短视频的固定内容，直播因其内容与时间的动态性，对平台的推荐算法提出了更高要求——需实时理解不断变化的内容，并在恰当的时刻将其推送给用户。通过分析，我们发现用户在直播的高光时刻会获得更好的体验，并表现出更积极的行为。此外，由于模型在推荐时无法获取未来内容，而用户参与度取决于后续内容与其兴趣的匹配程度，一个直观的解决方案是预测未来的直播内容。因此，我们对直播片段进行语义量化以获得语义ID（Semantic ids, Sid），编码历史Sid序列以捕捉作者特征，并对Sid演变趋势进行建模，以实现对未来内容的预见性预测。这种预见性通过精细化特征增强了排序模型。大量离线和在线实验证明了我们方法的有效性，该方法已部署于我们的平台，每天服务数亿用户，带来了显著的商业价值。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Live-streaming, as an emerging media enabling real-time interaction between authors and users, has attracted significant attention. Unlike the stable playback time of traditional TV live or the fixed content of short video, live-streaming, due to the dynamics of content and time, poses higher requirements for the recommendation algorithm of the platform - understanding the ever-changing content in real time and push it to users at the appropriate moment. Through analysis, we find that users have a better experience and express more positive behaviors during highlight moments of the live-streaming. Furthermore, since the model lacks access to future content during recommendation, yet user engagement depends on how well subsequent content aligns with their interests, an intuitive solution is to predict future live-streaming content. Therefore, we perform semantic quantization on live-streaming segments to obtain Semantic ids (Sid), encode the historical Sid sequence to capture the author's characteristics, and model Sid evolution trend to enable foresight prediction of future content. This foresight enhances the ranking model through refined features. Extensive offline and online experiments demonstrate the effectiveness of our method, which has been deployed on our platform serving hundreds of millions of users every day, bring significant commercial value.

</details>

## 深度解读

> 分析依据：**全文深读**

### 核心结论

本文针对直播推荐中内容动态变化、用户兴趣匹配难的问题，提出了一种通过语义量化将直播内容离散为语义ID（Sid），并利用历史Sid序列编码作者特征、建模Sid演化趋势以实现未来内容预见性预测的方法。该方法将预测的未来内容特征注入排序模型，以提升推荐效果。离线实验和在线A/B测试表明，该方法能有效提升直播推荐的核心指标和互动指标，验证了内容理解与未来预测在直播推荐中的有效性。

### 主要创新

- 提出将直播内容分割为30秒片段，并通过LLM语义嵌入和K-Means量化得到语义ID（Sid），实现内容的结构化表示。
- 设计基于Transformer的语义编码器和解码器，对历史Sid序列进行压缩和建模，并预测下一个Sid，实现未来内容预见。
- 将编码器输出（历史内容理解）和解码器输出（未来内容预测）作为增强特征注入多任务排序模型，提升推荐准确性。
- 在工业级直播推荐平台上进行了离线实验和在线A/B测试，验证了方法的有效性。

### 研究方法

论文采用以下技术路线：1）利用LLM对直播片段进行多模态语义理解，得到片段语义嵌入；2）通过K-Means聚类将嵌入量化为语义ID（Sid），形成Sid序列；3）对Sid序列进行压缩（去重和频率统计），并采用Transformer编码器-解码器结构，编码器建模历史序列，解码器预测下一个Sid；4）将编码器输出和解码器预测作为特征，与用户ID、作者ID等拼接，输入多任务排序模型（MMoE）进行CTR、WTR等预测；5）采用流式训练方式，实时更新Sid序列。

### 关键结果

离线实验表明，加入历史内容特征（I）后，CTR GAUC提升0.03%，WTR GAUC提升0.48%，LVTR GAUC提升0.02%，GTR GAUC提升0.21%；加入预见性预测特征（D）后，CTR GAUC提升0.24%，WTR GAUC提升0.65%，LVTR GAUC提升0.32%，GTR GAUC提升0.36%。在线A/B测试中，曝光量提升0.457%，观看次数提升0.243%，观看时长提升0.370%，点赞提升1.754%，关注提升0.922%，礼物数提升2.480%，礼物用户提升1.011%。预测准确率方面，模型预测准确率为21.35%，显著高于基于规则的方法（Last: 8.32%，Max Freq: 8.94%，Max Weight: 9.03%）。

### 技术栈

- LLM（大语言模型）
- K-Means聚类
- 向量量化（VQ）
- Transformer编码器-解码器
- 自注意力机制
- 交叉注意力机制
- 多任务学习（MMoE）
- Softmax分类
- 交叉熵损失

### 方法优势

- 创新性地将未来内容预测引入直播推荐，为推荐系统提供了新的视角。
- 利用语义ID将连续内容离散化，便于建模和存储。
- 在工业级平台上进行了充分的离线实验和在线A/B测试，验证了方法的实际效果。
- 通过案例分析展示了Sid在内容聚类和用户行为关联方面的有效性。

### 主要局限

- 论文未提供模型的具体超参数设置（如层数、隐藏维度等），可复现性受限。
- 未讨论Sid数量（20000）对模型性能的影响，可能缺乏敏感性分析。
- 未提及预测模型的训练细节（如优化器、学习率等）。
- 在线A/B测试的置信区间较宽，部分指标提升可能不显著。

### 与当前研究方向的关联

论文与关键词高度相关：涉及序列推荐（Sid序列建模）、生成式推荐（预测未来内容）、LLM与推荐系统结合（使用LLM进行语义理解）、多模态推荐（融合视频、语音、评论等多模态信息）、CTR/CVR预测（多任务排序模型）、工业落地（在快手平台进行A/B测试）。

## 代码与复现

- [chinghaolai/Recommendation-paper-daily](https://github.com/chinghaolai/Recommendation-paper-daily)：likely，置信度 69，Stars 0

---

_知识库更新时间：2026-08-07T03:44:30.773676_
