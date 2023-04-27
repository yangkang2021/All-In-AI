# linux(ubuntu22.04)+4090搭建AI工作站

### 一. 安装驱动
>直接安装驱动，会提示你安装gcc，libc，进而需要配置ubuntu的软件源。
1. 官网下载驱动直接安装：
   - https://blog.csdn.net/weixin_45901519/article/details/108252106
2. 依赖工具安装
   - sudo apt-get install libc6-dev build-essential
3. 清华ubuntu的软件源(版本要选对)配置
   - https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
4. 查看显卡信息
   - https://blog.csdn.net/weixin_42337304/article/details/121681264

### 二. 安装python
- 下载anconda：https://www.anaconda.com/download#downloads
- 配置anconda: https://blog.csdn.net/qq_44173974/article/details/125336916


### 三. 安装cuda，cudnn，tensorrt，pytorch,nvenc
- 未完成

### 四. 结果
![](.images/4980e471.png)