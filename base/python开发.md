# 深度学习-基础知识

## 一. python相关知识
1. python中enumerate的用法：遍历时候拿到索引
2. tqdm的用法：遍历是显示进度和时间
    ```
    for i in tqdm(range(num_frames), 'mel:'):
        print(i)
    ```
3. 单元数转tuple:tuple_2 = (20,)
4. 前缀运算符*和**：http://www.ay1.cc/article/1672389218013810589.html
5. python简写
    - for in range
    - 单行if-else
    - 字符串格式三种方法（%，format，f-string)：
       ```
          s1 = "xxxxxx %s xxxxxx" % (value1, value2)
          s2 = "xxxx {age} xxxx {name}".format(age=18, name="hangman")
          s3 = f"半径r圆的周长为{2 * math.pi * r}" 
       ```
    - for in 单行遍历处理
       ```
        j = ' '.join(str(i) for i in range(10))
      ```
    - 解包
        ```a,b,c = ['a', 'b', 'c']```
    
## 二. numpy
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

## 三. pytorch
1. Pytorch中的Embedding https://blog.51cto.com/u_15127639/4079442
1. [【PyTorch】torch.utils.data.Dataset 介绍与实战](https://blog.csdn.net/weixin_44211968/article/details/123744513)
1. PyTorch的DataParallel
1. PyTorch的train和eval：切换训练和评估(推断)的模式
1. PyTorch遍历参数:
    - model.parameters()
    - model.named_parameters():keepvars?
    - model.state_dict()
1. Pytorch导出模型
    ```
    #导出模型看看
    torch.onnx.export(model, (torch.randn(1, 90)), "./nerf-model.onnx", verbose=True,training=torch.onnx.TrainingMode.EVAL);
    
    #传递dict
    torch.onnx.export(self.decoder, {"batch":batch},"./audio2pose_model_decoder.onnx", verbose=True,training=torch.onnx.TrainingMode.EVAL);

    # 导出torchscript
    mod = torch.jit.trace(torch_model,  (x_dense,x_sparse))
    mod.save("wide_deep.pt")
    
    # 加载torchscript测试一下
    model_reload = torch.jit.load('wide_deep.pt')
    output = model_reload.forward(x_dense,x_sparse)

    ```
1. Pytorch的tensor矩阵操作
   - torch的类型转换https://codeleading.com/article/20665429954/
   - torch.unsqueeze/squeeze 在指定的位置插入/删除一个维度
   - torch.premute/transpose 调换维度顺序
   - torch.flatten(x,1)代表从第二维开始平坦化。
   - torch.flatten(x,0,1)代表在第一维和第二维之间平坦化。
   - torch.view/reshape  view要求is_contiguous
   - torch.cat/concat 拼接数组或者列表或者元组
   - torch.stack 增加一维的拼接相同矩阵
   - torch.expand/expand_as/repeat 重复扩展矩阵
   - torch.clamp 限制范围
1. Pytorch实现RGByuv转换
  - https://github.com/Aaron7noraA/MIMT_final/blob/0c640b48352648333a4c5fbca0db9ec4776d402a/util/vision.py#L64
  - https://github.com/LARG/spl_yolov5/blob/b70367759975c63d0a426a94bd085d772cb63eb3/models/common.py#L332
  - https://blog.csdn.net/Jerry_Leo_liu/article/details/90143024

## libtorch
1. libtorch踩坑指南 https://mp.weixin.qq.com/s/MbACadrA2c53jyATyaGEyQ