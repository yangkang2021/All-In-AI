
# PCA降维
> 协方差矩阵做特征值分解

1. 降维方法：任意维度 --降到--> 任意维度
2. 目标：
   - 找到数据最重要的方向，也就是方差最大的方向
   - 第一个主成分：方差最大的方向，第二个主成分：方差次大的方向，且与第一个主成分正交。
3. 过程：6步
   - 求均值
   - 求协方差矩阵
   - 对协方差矩阵做特征值分解
   - 选出top K个特征向量
   - 将原始数据投影到选取的特征向量上
    