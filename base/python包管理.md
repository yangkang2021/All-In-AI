# python包管理
> 总结：
> 1. 用conda管理python各个版本，用venv管理项目版本
> 2. pip配置管理华为云最快
> 3. pip安装包的各种方法

## 一. python各版本管理
1. conda激活虚拟环境
   ```
   conda info --envs
   conda remove -n py39 --all
   conda create -n py39 python=3.9.13
   conda activate py39
   ```
2. 自己编译python版本以及对应pip版本
    - c++环境
    - 需要编译openssl
    - 自己编译的python和pip的对应
    - 使用python内置的pip模块：python -m pip install torch

## 二. 项目依赖管理
1. 用python env虚拟环境--**推荐使用**
   > 推荐使用这种方式：在每个项目的目录下，创建只属于本项目的环境
   ```
    先激活相应的python版本
    pip install virtualenv 安装virtualenv
    virtualenv venv  创建虚拟环境
    venv\Scripts\activate  激活
    venv\Scripts\deactivate 反激活
    
    venv\bin\activate  linux激活
    venv\bin\deactivate linux反激活
   ```

## 三. pip从指定的国内源安装
   > 华为云最快
   ```
   pip install xxx -i https://pypi.douban.com/simple/
   pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple/
   pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
   pip config set global.index-url https://mirrors.huaweicloud.com/repository/pypi/simple
   ```

## 四. 安装python包的N种方法
| 序号  | 方式  | 说明                                                                      |
|-----|-----|-------------------------------------------------------------------------|
| 1   | conda install | conda安装                                                                 |
| 2   | pip install | pip安装                                                                   |
| 3   | pip install | xxx.whl 离线包                                                             |
| 4   | pip install | "git+https://github.com/facebookresearch/pytorch3d.git@stable" 从github安装 |
| 5   | python setup.py install | 从源码安装                                                             |
| 6   | pip install .| 从源码安装, -e创建链接可以实时更改                                             |
 | 7   |python3 setup.py bdist_wheel|生成whl后安装pip install ./dist/*.whl|

## 五. 查看包信息
   ```
   pip list
   conda list
   ```