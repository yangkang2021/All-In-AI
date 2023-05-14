# sd源码分析1：概述
>四大核心功能：模型使用，扩展插件，lora模型，脚本

## 一. SD核心功能
1. 扩散模型使用：文生图，图生图，局部重绘等
2. 脚本：接管图像的生成调用，可以重新组织调整参数
3. 附加网络：Embedding Hypernetworks 模型 Lora
4. 扩展插件：用来编写项目的扩展，可以包含脚本、功能、翻译等等。
5. 外挂模型VAE：

## 二. 常见的扩展，插件，扩展网络
5.ControlNet：用扩展实现的一个脚本功能
6. vae和lora：一类附加网络


## 三. 准备基础知识
1. [linux(ubuntu22.04)+4090搭建AI工作站](linux搭建环境.md)
2. [gradio学习总结.md](gradio学习总结.md)

## 四. 参考源码分析
https://zhuanlan.zhihu.com/p/617742414
