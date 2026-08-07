---
title: "FARM: Frequency-Aware Model for Cross-Domain Live-Streaming Recommendation"
paper_id: "https://doi.org/10.1145/3770854.3783955"
source: "kdd"
published: "2026-01-01T00:00:00"
score: 33.0
tags: ["paper", "recommender-systems", "Image and Video Quality Assessment", "Recommender Systems and Techniques", "Peer-to-Peer Network Technologies"]
---

# FARM: Frequency-Aware Model for Cross-Domain Live-Streaming Recommendation

[查看原文](https://dblp.org/rec/conf/kdd/LiYWWLWHLSLCYL26) · [ArXiv](https://arxiv.org/abs/2502.09375)

## 一句话结论

> 论文提出了一种频率感知的跨域直播推荐模型FARM，通过离散傅里叶变换和对比学习对齐并融合用户偏好，以解决数据稀疏问题，并在快手平台上验证了其有效性。

## 论文信息

- **作者**：Xiaodong Li, Ruochen Yang, Shuangchun Wen, Shen Wang, Yueyang Liu, Guoquan Wang, W. Hu, Qiang Luo, Jiawei Sheng, Tingwen Liu, Jiangxia Cao, Shuang Yang, Zhaojie Liu
- **来源**：KDD
- **发布时间**：2026-01-01
- **相关度评分**：33.0
- **DOI**：[https://doi.org/10.1145/3770854.3783955](https://doi.org/10.1145/3770854.3783955)

<details open>
<summary><strong>中文摘要</strong></summary>

直播服务因其实时互动性和娱乐价值而广受欢迎。用户可以通过参与实时聊天、点赞或发送虚拟礼物来与直播主播互动，以表达他们的偏好和支持。然而，直播服务面临着严重的数据稀疏问题，这可以归因于以下两点：（1）用户的宝贵行为通常是稀疏的，例如点赞、评论和送礼，这些行为容易被模型忽视，难以描述用户的个性化偏好。（2）我们平台上的主要曝光内容是短视频，其曝光量是直播曝光的9倍，导致直播内容无法充分建模用户偏好。为此，我们提出了一种面向跨域直播推荐的频率感知模型，称为FARM。具体而言，我们首先引入了域内频率感知模块，使我们的模型能够感知用户稀疏但宝贵的行为，即高频信息，该模块由离散傅里叶变换（DFT）支持。为了在短视频和直播域之间迁移用户偏好，我们提出了一种新颖的先对齐后融合策略，该策略由两部分组成：跨域偏好对齐模块，利用对比学习对齐两个域中的用户偏好；以及跨域偏好融合模块，通过一系列定制设计的注意力机制进一步融合两个域中的用户偏好。在快手直播服务上进行的大量离线实验和在线A/B测试证明了FARM的有效性和优越性。我们的FARM已部署在在线直播服务中，目前为快手的数亿用户提供服务。

</details>

<details>
<summary><strong>英文摘要</strong></summary>

Live-streaming services have attracted widespread popularity due to their real-time interactivity and entertainment value. Users can engage with live-streaming authors by participating in live chats, posting likes, or sending virtual gifts to convey their preferences and support. However, the live-streaming services faces serious data-sparsity problem, which can be attributed to the following two points: (1) User's valuable behaviors are usually sparse, e.g., like, comment and gift, which are easily overlooked by the model, making it difficult to describe user's personalized preference. (2) The main exposure content on our platform is short-video, which is 9 times higher than the exposed live-streaming, leading to the inability of live-streaming content to fully model user preference. To this end, we propose a Frequency-Aware Model for Cross-Domain Live-Streaming Recommendation, termed as FARM. Specifically, we first present the intra-domain frequency aware module to enable our model to perceive user's sparse yet valuable behaviors, i.e., high-frequency information, supported by the Discrete Fourier Transform (DFT). To transfer user preference across the short-video and live-streaming domains, we propose a novel preference align before fuse strategy, which consists of two parts: the cross-domain preference align module to align user preference in both domains with contrastive learning, and the cross-domain preference fuse module to further fuse user preference in both domains using a serious of tailor-designed attention mechanisms. Extensive offline experiments and online A/B testing on Kuaishou live-streaming services demonstrate the effectiveness and superiority of FARM. Our FARM has been deployed in online live-streaming services and currently serves hundreds of millions of users on Kuaishou.

</details>

---

_知识库更新时间：2026-08-07T03:44:30.774372_
