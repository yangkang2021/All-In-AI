## 图像处理算法汇总

### 一. 基本任务
1. 整图判断用分类：
    - ResNet
    - SqueezeNet
    - MobileNetV3
    - shufflenet
    - EfficientNets
    - FixEfficientNet-L2
    - NFNets
2. 矩形框出用检测：
    - fasterRCNN
    - yolov5
    - yolox
    - yolop
    - yolov6
    - yolvv7
3. 像素级请用分割：
    - unet
    - deeplabv3
    - PaddleSeg
    - detectron2
### 二. 小任务
5. 单目标跟踪：goturn, SiamRPN++
6. 多目标跟踪: 
    - DeepSORT、StrongSORT++, ByteTrack
    - BoT-SORT [BoT-SORT](https://mp.weixin.qq.com/s/tLiKU1mwUXzZPaGeumW0Zg) 
---
7. 抠图Matting
    - U^2-Net
    - MODNet
    - skyAR
    - 毛发分割Animal Matting
    - Background Matting V2
    - 图像分割：《End-to-End Referring Video Object Segmentation with Multimodal Transformers》
    - FactorMatte：最新视频抠图算法，更适合于视频合成任务
    - [RobustVideoMatting](https://peterl1n.github.io/RobustVideoMatting) ：字节跳动的视频抠图
---
8. 超分：
    - BasicVSR++
    - EDVR，RealSR，Topaz
    - 人脸超分：VQFR，FaceFormer
9. 修复(Inpainting):
    - 修复：Bringing Old Photo Back to Life
    - [腾讯老照片修复](https://github.com/TencentARC/GFPGAN)
    - 补帧：DAIN
    - 上色：DeOldify/DeepRemaster，DeOldify：最先进的黑白图像上色技术。
10. OCR:
    - 百度paddleocr
    - easy ocr
    - tesseractOCR
    - MMOCR。
11. 人脸检测对齐识别
    - seetaface6
    - dlib
    - mtcnn+facenet
    - openface  deepid，vggface，arcface
12. 重识别：
    - cluster-contrast-reid
    - fast-reid
13. 姿态：
    - openPose
    - posenet
    - MoveNet
14. 生成对抗网络：
    - styleGanV3
15. 画像还原真人
    - ArtBreeder/GanBreeder
    - StyleGanV2
17. 图像降噪与美颜算法
    - Noise2Noise 和 Noise2Void
### 三. 大型任务
18. 换脸
    - DeepFaceLab
    - FaceSwap
    - FaceShifter
    - FaceApp
    - FaceSwap of Realistic-Neural-Talking-Head-Models
    - facePlay
19. 语音识别[参考](https://www.zhihu.com/question/538957167/answer/2541020463)
    - Kaldi系统：神经网络声学模型+解码图
    - 端到端系统：以CTC或Transducer为主导，国内WeNet，google力推的Cascaded encoder。
20. 运动模型
    - 一阶运动模型：First-Order-Model
    - 人体动作迁移：impersonator++
    - 声音转唇动Wav2Lip，Lip2Wav。
---
21. ai艺术家-diffusion扩散模型： 
    - stable diffusion
    - disco diffusion
    - ACGN diffusion(Animation, Comic, Game, Novel)
22. 艺术创作
    - DeepFaceDrawing
    - Stylized Neural Painting
    - 人物肖像画生成算法 U^2-Net
---
23. 单图三维重建
    - 三维估计:FrankMocap/3Dpose_ssl
    - PIFuHD
    - 图像转3维：https://avatarsdk.com/
24. 三维重建与slam
    - 传统方法：openMVS/openMVG
    - 视觉slam：ORB-SLAM2/ORB-SLAM3
    - 神经辐射场NeRF：NeRF/StyleNeRF/PixelNeRF/IBRNet:今年最火的AI技术！
---
25. 对抗生成网络
    - 基础：GAN/DCGAN/CGAN/ACGAN/LSGAN
    - 应用：SRGAN/CycleGAN/pix2pix/styleGan/textToImage
26. 图像生成应用   
    - https://beta.dreamstudio.ai/dream
    - https://openai.com/dall-e-2
    - https://www.artbreeder.com
3. 其他网站
    - https://zhuanlan.zhihu.com/p/547737982
    - https://mp.weixin.qq.com/mp/homepage?__biz=MzIxODg1OTk1MA==&hid=9&sn=c36dd0e197c0195507a6c6c59c89ab38&scene=1
    - https://weibo.com/p/1005052395607675