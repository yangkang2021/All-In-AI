# pytorch

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
   - torch.view/reshape  view要求is_contiguous。**数据顺序不变**
   - torch.premute/transpose 调换维度顺序
   - torch.flatten(x,1)代表从第二维开始平坦化。
   - torch.flatten(x,0,1)代表在第一维和第二维之间平坦化。
   - torch.cat/concat 拼接数组或者列表或者元组
   - torch.split 拆成数组
   - torch.stack 增加一维的拼接相同矩阵
   - torch.expand/expand_as/repeat 重复扩展矩阵
   - torch.clamp 限制范围
   - torch.matmul
   - torch.nn.functional.grid_sample: 实现特征图采样，如矩阵变换
   - torch.zeors/ones: 快速的参数tensor

1. Pytorch实现RGByuv转换
  - https://github.com/Aaron7noraA/MIMT_final/blob/0c640b48352648333a4c5fbca0db9ec4776d402a/util/vision.py#L64
  - https://github.com/LARG/spl_yolov5/blob/b70367759975c63d0a426a94bd085d772cb63eb3/models/common.py#L332
  - https://blog.csdn.net/Jerry_Leo_liu/article/details/90143024

## libtorch
1. libtorch踩坑指南 https://mp.weixin.qq.com/s/MbACadrA2c53jyATyaGEyQ

## 代码片段
   ```
     #只保留修改层的权重
     checkpoint_syncnet = {k: v for k, v in checkpoint_syncnet.items() if not k.startswith('audio_encoder.audio_conv.0.conv')}
     #只训练一部分参数
     for name, value in net_lipsync.named_parameters():
         if name.startswith('audio_encoder.audio_conv.0.conv'):
             value.requires_grad = True
         else:
             value.requires_grad = False
   ```