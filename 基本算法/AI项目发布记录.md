# AI项目发布记录

## 一. 主要项目
1. whisper：openapi发布语音识别
1. Segment Anything：4 月初，Meta 发布了史上首个图像分割基础模型--SAM（Segment Anything Model）
1. Inpaint Anything：基于 SAM，提出「修补一切」（Inpaint Anything，简称 IA）模型
1. dragGAN：AI图像拖动编辑, 有人实现并开源
   - https://github.com/XingangPan/DragGAN
1. Massively Multilingual Speech:Meta 的开源语音 AI 项目 MMS 可识别 4000 多种口头语言
1. Rask.AI：AI视频配音转译 付费
1. sadtalker：语音驱动图像的数字人 开源
1. 最强文本转语音工具：Bark https://github.com/suno-ai/bark
1. google发布styledrop：https://styledrop.github.io/
1. runway gen2 文字视频生成
1. Meta 开源了一个 AI 生成音乐工具 Audiocraft
   - 可以直接在线体验：https://huggingface.co/spaces/facebook/MusicGen
   - 可以离线部署，项目地址：https://github.com/facebookresearch/audiocraft
1. ControlNet
   - 1.1发布，支持tile
   - refrence only
   - inpaint
1. Rerender A Video：视频转绘，解决mj和sd逐帧处理视频带来的抖动
1. 一键换装，被谷歌给实现了！
   - https://tryondiffusion.github.io/
   - https://mp.weixin.qq.com/s/kKh5FsxxqYe9378GDw41kw
   - 没有demo，也没开源
1. Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale
   - 大规模文本引导多语言通用语音生成
   - https://voicebox.metademolab.com/
   - https://github.com/SpeechifyInc/Meta-voicebox
1. FastSAM：Segment Anything算法加速50倍+！
   - 论文链接-https://arxiv.org/pdf/2306.12156.pdf
   - 代码链接-https://github.com/CASIA-IVA-Lab/FastSAM
   - demo链接-https://huggingface.co/spaces/An-619/FastSAM
1. ChatGLM2-6B：性能大幅提升，8-32k上下文，推理提速42%
1. MATEBIT：基于参考样本的新图像转换方法
1. MobileSAM来啦 | 比SAM小60倍，比FastSAM快4倍
1. phi-1: 用规模仅为 7B token 的「教科书质量」数据训练了一个 1.3B（13 亿参数）的语言模型
2. CVPR2023| GamutMLP:一个轻量级 MLP用于颜色损失恢复
1. CVPR2023
   - 候选：https://blog.csdn.net/Mikasa33/article/details/131207123
   - 全部论文：https://openaccess.thecvf.com/CVPR2023?day=all
   - 分类整理：https://github.com/amusi/CVPR2023-Papers-with-Code
1. ChatLaw: 北大打造法律大模型
   - 官方地址：https://www.chatlaw.cloud
   - GitHub地址：https://github.com/PKU-YuanGroup/ChatLaw
   - 论文地址：https://arxiv.org/abs/2306.16092

## 二. NeRF+数字人+三维重建
### 单图三维重建
1. ECON: Explicit Clothed humans Optimized via Normal integration
   - 通过正常法向优化的显性穿衣人类
1. MobileNeRF：利用多边形光栅化管道在移动架构上实现高效神经场渲染
1. Zero-1-to-3: 大模型时代的单视图三维重建
   - https://zero123.cs.columbia.edu/
   - https://github.com/cvlab-columbia/zero123
   - https://huggingface.co/spaces/cvlab/zero123-live
1. NeRDi: 使用语义引导图像扩散模型的单视图NeRF三维重建
1. AvatarBooth：几张照片即可定制自己的3D化身，还能换装！
1. PanoHead: 几何感知的3D头部360度合成。
   - Geometry-Aware 3D Full-Head Synthesis in 360°
   - https://github.com/SizheAn/PanoHead
   - https://sizhean.github.io/panohead
   
### 其他
2. IM Avatar，Point Avatar: 从视频中重建可驱动的三维数字头像模型
   - https://github.com/zhengyuf/IMavatar
   - https://github.com/zhengyuf/PointAvatar
1. BAD-NeRF，针对图像退化！CVPR23
1. [CVPR 2023] Removing Objects From Neural Radiance Fields
   - https://github.com/nianticlabs/nerf-object-removal
1. Kaedim：3D工具

## 三. LLM
![](.images/cd2e8ab3.png)

## 四. 主要课程
1. 【生成式AI】李宏毅2023春季课程:https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php
2.  B站Stable Duffison使用教程
2. 【promot工程】吴恩达
2. 吴恩达的三门课，主题包括LangChain、扩散模型，以及用ChatGPT API搭建系统
5. 大模型参数高效微调技术原理综述 七篇 https://mp.weixin.qq.com/s/M-7ZudD0dvscsApryiPIYw
6. 小工蚁创始人系列课程
7. GPT大模型微调方法系列