# 深度学习-基础知识

## 一. python相关知识
1. python中enumerate的用法：遍历时候拿到索引
2. tqdm的用法：遍历是显示进度和时间
    ```
    for i in tqdm(range(num_frames), total=num_frames, desc='mel:'):
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
    - list表过滤
        ``` a = [number for number in numbers if number >= 0]```