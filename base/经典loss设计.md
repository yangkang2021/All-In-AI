# 训练-部署-技巧

## 理解各种loss
1. 距离损失：L1Loss,MSELoss,
2. 交叉熵BCELoss，KL散度
   - 信息量：事件信息量和事件发送的概率成反比：I(x)=log2(1/p(x))
   - 熵：一个概率分布的平均信息量: 对概率分布的每个pi求pi x I(pi)的和。 
   - 交叉熵：用观测概率qi计算的估计信息量：对概率分布的每个pi求pi x I(qi)的和。 
   - K-L散度：交叉熵 与 熵的差值。
3. 感知损失：PerceptionLoss
    - vgg特征的L1距离
4. 生成网络损失：GanLoss
    - 判别网络输出真和假，真假图片分别交叉熵后求和
5. 风格转换损失：
6. CTC Loss
7. Clip Score: 衡量生成图片和文字的配对好坏的程度。
8. RF-Loss: 无法优化，把loss当初强化学习的奖励


