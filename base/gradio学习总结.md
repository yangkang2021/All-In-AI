# gradio学习总结
> https://www.gradio.app/
> 
> 难点：并发控制和用户数据隔离

## 一. 简介
Gradio是用友好的web界面演示机器学习模型的最快方式，任何人都可以在任何地方使用它!

## 二. 两种方式来构建应用程序：
> 简单布局用Interface，复杂定制用Blocks。
1. Interface：高阶的封装API。
2. Blocks：更底层的API，更加灵活。

## 三. 受欢迎的11个功能
1. 添加示例输入：提供一个输入示例表，点一下就输入。
2. 传递自定义错误消息：显示错误信息。
3. 添加描述性内容：标题，标识，article。
4. 设置标记
5. 预处理和后处理
6. 支持css style
7. 并发控制：队列和并发数设置
8. 迭代输出：如sd观察图片生成过程
9. 进度条
10. 批处理功能：支持并行处理
11. 在各种notebooks上运行：jupyter notebooks，Google Colab

## 四. 组件
> 熟悉所有的组件
https://www.gradio.app/docs

## 五. api，分享，client

## 六. 典型应用场景
1. 聊天机器人：gr.Chatbot()
2. 麦克风数据获取：gr.Audio(source="microphone")
3. 摄像头数据获取：gr.Image(source="webcam", streaming=True)

## 七. 常见问题
1. 并发：demo.queue(concurrency_count=2)
2. 用户数据隔离：参考chatbot，保存state
