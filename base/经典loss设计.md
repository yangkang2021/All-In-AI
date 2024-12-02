# 训练-部署-技巧

## 理解各种loss
1. 距离损失：L1Loss,MSELoss,
2. KL散度，交叉熵BCELoss
3. 感知损失：PerceptionLoss
    - vgg特征的L1距离
4. 生成网络损失：GanLoss
    - 判别网络输出真和假，真假图片分别交叉熵后求和
5. 风格转换损失：
