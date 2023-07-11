# ncnn

https://github.com/zchrissirhcz/awesome-ncnn

1. linux,mac上使用ncnn的静态库崩溃：cpu数，缓存size等全局变量初始化函数没有执行，导致值是0崩溃。 换成动态库解决。
    - 解决办法：更新ncnn
    - https://github.com/Tencent/ncnn/commit/2b87dc2cf7f07416c3781e71a478fd185d4fdfcb
   
2. libvulkan.so 没有静态库，无法单文件exe部署
   -  参考：khronos vulkan loader