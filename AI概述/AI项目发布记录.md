# AI项目发布记录

## 一. 顶级会议
1. CVPR2023
   - 候选：https://blog.csdn.net/Mikasa33/article/details/131207123
   - 全部论文：https://openaccess.thecvf.com/CVPR2023?day=all
   - 分类整理：https://github.com/amusi/CVPR2023-Papers-with-Code
1. ICCV2023
   - https://github.com/amusi/ICCV2023-Papers-with-Code
   
## 二. 大语言模型（LLM）
1. ChatGLM2-6B：性能大幅提升，8-32k上下文，推理提速42%
1. llama2开源可商用
1. llama2.c
   - https://github.com/karpathy/llama2.c
   - 仅仅500行的一个C文件(run.c)跑llama2
1. phi-1:
   - 用规模仅为 7B token 的「教科书质量」数据训练了一个 1.3B（13 亿参数）的语言模型
1. Qwen-7B 阿里通义千问开源
   - https://github.com/QwenLM/Qwen-7B
1. 鸭嘴兽（Platypus 2-70B）
   - 登顶Hugging Face大模型排行榜，超越llama2
1. ChatLaw: 北大打造法律大模型
   - 官方地址：https://www.chatlaw.cloud
   - GitHub地址：https://github.com/PKU-YuanGroup/ChatLaw
   - 论文地址：https://arxiv.org/abs/2306.16092
1. Code Llama
   - Meta开源史上最强代码大模型
   - https://github.com/facebookresearch/codellama
1. CareLlama(关怀羊驼)
   - 医疗大模型，开源驱动，共创健康未来
   - https://github.com/WangRongsheng/CareLlama
1. StarGLM
   - 天文大语言模型
   - http://github.com/Yu-Yang-Li/StarGLM
1. MathGPT
   - 国内首个数学大模型MathGPT 1300亿参数
1. DoctorGPT发布，免费的私人医疗咨询
   - https://github.com/ingyamilmolinar/doctorgpt
1. MindChat心理大模型
   - https://github.com/X-D-Lab/MindChat
1. open-interpreter开源版代码解释器
   - https://github.com/KillianLucas/open-interpreter

## 三. 语音模型
1. whisper：openapi发布语音识别
1. MMS(Massively Multilingual Speech):Meta 的开源语音 AI 项目 MMS 可识别 4000 多种口头语言
1. Rask.AI：AI视频配音转译 付费
1. 最强文本转语音工具：Bark https://github.com/suno-ai/bark
1. Meta 开源了一个 AI 生成音乐工具 Audiocraft
   - 可以直接在线体验：https://huggingface.co/spaces/facebook/MusicGen
   - 可以离线部署，项目地址：https://github.com/facebookresearch/audiocraft
1. AudioCraft Plus
   - 基于原始AudioCraft的全功能WebUI。
1. Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale
   - 大规模文本引导多语言通用语音生成
   - https://voicebox.metademolab.com/
   - https://github.com/SpeechifyInc/Meta-voicebox
1. Mega-TTS 2 没有开源
   - 浙江大学联手字节跳动推出的 Mega-TTS 2，目前最强中文语音AI，在音色、韵律方便处理得非常出色
1. SeamlessM4T
   - Meta开源多语音、语言，翻译、转录大模型
   - [1]开源地址：https://github.com/facebookresearch/seamless_communication
   - [2]论文：https://ai.meta.com/research/publications/seamless-m4t/
   - [3]在线演示：https://seamless.metademolab.com/
   - [4]huggingface演示：https://huggingface.co/spaces/facebook/seamless_m4t
1. 微软最新的语音生成和转换模型
   - https://github.com/Plachtaa/VALL-E-X

## 四. AI绘画与视觉模型
1. ControlNet
   - 1.1发布，支持tile
   - refrence only
   - inpaint
1. Segment Anything：4 月初，Meta 发布了史上首个图像分割基础模型--SAM（Segment Anything Model）
1. Inpaint Anything：基于 SAM，提出「修补一切」（Inpaint Anything，简称 IA）模型
1. dragGAN：AI图像拖动编辑, 有人实现并开源
   - https://github.com/XingangPan/DragGAN
1. Rerender A Video：视频转绘，解决mj和sd逐帧处理视频带来的抖动
1. google发布styledrop：https://styledrop.github.io/
1. runway gen2 文字视频生成
1. FastSAM：Segment Anything算法加速50倍+！
   - 论文链接-https://arxiv.org/pdf/2306.12156.pdf
   - 代码链接-https://github.com/CASIA-IVA-Lab/FastSAM
   - demo链接-https://huggingface.co/spaces/An-619/FastSAM
1. MATEBIT：基于参考样本的新图像转换方法
1. MobileSAM来啦 | 比SAM小60倍，比FastSAM快4倍
1. CVPR2023| GamutMLP:一个轻量级 MLP用于颜色损失恢复
1. CoTracker
   - 跟踪任意长视频中的任意多个点，并且可以随时添加新的点进行跟踪！
   - Meta最新开源！跟踪一切升级版！性能超越OmniMotion！
   - https://mp.weixin.qq.com/s/9UtGiWOBnoQ5qMQ_a-RInA
1. SegNetr
   - 超越UNeXit/U-Net/U-Net++/SegNet，精度更高模型更小的UNet家族
1. Semantic-SAM
   - 多粒度的语义通用分割模型
1. DWPose
   - 全身关键点检测SOTA模型DWPose,超越RTMPose，登顶 COCO-WholeBody
1. VCT
   - 风格迁移新方案
   - https://github.com/CrystalNeuro/visual-concept-translator
1. CoDeF
   - 视频版ControlNet开源 CoDeF靠提示词就能精准切换画风
   - https://github.com/qiuyu96/CoDeF
1. DALL·E 3
   - DALL·E 3+ChatGPT强强联合，画面直接细节爆炸

## 五. 修复+超分+上色+补帧+增强
1. CodeFormer 
2. GFPGAN
2. Bringing Old Photo Back to Life
2. realSR
1. Bicubic++
   - 实时超分方案
   - https://github.com/Ysnower/bicubic-plusplus
1. FaceFusion
   - 下一代的换脸和修复方案
   - https://github.com/facefusion/facefusion
   
## 六. NeRF + 数字人 + 三维重建 + 换脸 
1. MotionBERT: 人体运动表征学习的统一视角
   - ICCV 2023
   - 论文链接：https://arxiv.org/pdf/2210.06551.pdf
   - 开源代码：https://github.com/Walter0807/MotionBERT
   - 项目主页：https://motionbert.github.io/
   - 视频介绍：https://www.youtube.com/watch?v=slSPQ9hNLjM
   - https://mp.weixin.qq.com/s/pSrT41h_042B70fKx4Y9Rw
1. GeneFace
   - 代码：https://github.com/yerfor/GeneFace
   - 论文：https://arxiv.org/pdf/2301.13430.pdf
   - 数字人生成新算法，优于RAD-NERF，AD-NERF
1. facechain
   - https://github.com/modelscope/facechain
   - 【妙鸭相机】开源版
   - 数字人图像生成
1. 一键换装，被谷歌给实现了！
   - https://tryondiffusion.github.io/
   - https://mp.weixin.qq.com/s/kKh5FsxxqYe9378GDw41kw
   - 没有demo，也没开源
1. sadtalker：语音驱动图像的数字人 开源
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
1. IM Avatar，Point Avatar: 从视频中重建可驱动的三维数字头像模型
   - https://github.com/zhengyuf/IMavatar
   - https://github.com/zhengyuf/PointAvatar
1. BAD-NeRF，针对图像退化！CVPR23
1. [CVPR 2023] Removing Objects From Neural Radiance Fields
   - https://github.com/nianticlabs/nerf-object-removal
1. Kaedim：3D工具
1. SketchFaceNeRF
   - NeRF基于线稿生成逼真三维人脸，细节风格随意改
   - https://mp.weixin.qq.com/s/36nDnxg4z9vXO0L0kQSSag
1. StyleRF: Zero-shot 3D Style Transfer of Neural Radiance Fields
2. 字节跳动提出MagicAvatar：多模态Avatar生成和动画
   - MagicAvatar: Multimodal Avatar Generation and Animation 
   - 主页：https://magic-avatar.github.io/ 
   - 代码：https://github.com/magic-research/magic-avatar 
   - 论文：https://arxiv.org/abs/2308.14748
   
## 七. 主要课程
1. 【生成式AI】李宏毅2023春季课程:https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php
2.  B站Stable Duffison使用教程
2. 【promot工程】吴恩达
2. 吴恩达的三门课，主题包括LangChain、扩散模型，以及用ChatGPT API搭建系统
5. 大模型参数高效微调技术原理综述 七篇 https://mp.weixin.qq.com/s/M-7ZudD0dvscsApryiPIYw
6. 小工蚁创始人系列课程
7. GPT大模型微调方法系列
8. 刘烨斌《基于NeRF的三维视觉年度进展报告》：https://www.bilibili.com/video/BV16x4y1X7WG/
9. 加速NeRF的移动端实时渲染方法MobileR2L
10. 学习moss的原理：openmmlab 
11. chatGPT的18个能力
12. Intel 的大模型课程: https://www.igbacenter.com/special/aipc
13. Karpathy和吴恩达关于 chatgpt和大模型的课程
