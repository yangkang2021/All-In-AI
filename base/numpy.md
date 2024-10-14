# numpy

## 一. numpy
1. np.atleast_1d():函数用于将输入数据转换为至少一维的数组。
   - 标量转一维数组
   - 多个参数/多个数组转换为一维数组
2. 在指定精度下比较：两个矩阵是否相对，已经不相等元素格式
    ```
    x2 = st.mel(wav)
    diff = np.absolute(x2 - x1) < 0.0001
    print("signal.lfilter diff: ", np.all(diff), np.sum(diff == False))
    ```
3. np.flipud()函数可以将矩阵里面的值倒序，只是在第一个维度上
4. np.hypot(x1,x2)逐元素计算，相当于给定了两个直角边求斜边大小