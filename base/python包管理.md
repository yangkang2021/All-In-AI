# python包管理

## 一. python虚拟环境
1. 删除创建conda激活虚拟环境
```
# 1.删除创建conda激活虚拟环境
conda remove -n neuman_env --all
conda create -n neuman_env python=3.9.13
conda activate neuman_env
```
2. python env虚拟环境--**推荐使用**
> 推荐使用这种方式：在每个项目的目录下，创建只属于本项目的环境
```
 pip install virtualenv 安装virtualenv
 virtualenv venv  创建虚拟环境
 venv\Scripts\activate  激活
 venv\Scripts\deactivate 反激活
 
 venv\bin\activate  linux激活
 venv\bin\deactivate linux反激活
```

## 二. pip从指定的国内源安装
```
pip install xxx -i https://pypi.douban.com/simple/
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

## 三. 安装python包的N种方法
| 序号  | 方式  | 说明                                                                       |
|-----|-----|--------------------------------------------------------------------------|
| 1 | conda install | conda安装                                                                  |
| 2 | pip install | pip安装                                                                    |
| 3 | pip install | xxx.whl 离线包                                                              |
| 4 | pip install | "git+https://github.com/facebookresearch/pytorch3d.git@stable" 从github安装 |
| 5 | python setup.py install | windows从源码安装                                                             |
| 6 | pip install .| mac和linux从源码安装, -e创建链接可以实时更改                                             |

## 四. 查看包信息
```
pip list
conda list
```