# statisticalLearningMethod
《统计学习方法》\
Python代码实现

### 环境依赖
- Python `3.6.8`
- Jupyter `1.0.0`
- numpy `1.16.3`
- matplotlib `3.0.3`
- scipy `1.2.1`

### 运行方法
1. 下载仓库
    ```shell script
    git clone https://github.com/wbxing/statisticalLearningMethod.git
    ```
1. 进入 `.py` 脚本文件目录
    ```shell script
    cd ./statisticalLearningMethod/
    ```
1. 安装所需要的依赖
    ```shell script
    pip install jupyter numpy matplotlib scipy
    ```
1. 运行 `.py` 文件
    ```shell script
    python *.py
    ```
   
    > 这里的 `*.py` 是指 Python 脚本文件的具体名称。
    比如需要运行第一章的`最小二乘法表示过拟合与正则化`，就需要执行：
    > ```shell script
    > python Chapter1_LeastSquaresMethod.py
    > ```

### 学习笔记
#### 第一章：统计学习方法概述
> 代码文件：最小二乘法（过拟合与正则化） \
> [Chapter1_LeastSquaresMethod.py](./Chapter1_LeastSquaresMethod.py)

> 笔记文件：[chapter1.md](./notes/chapter1.md)

#### 第二章：感知机
> 代码文件：感知机分类 \
> [Chapter2_Perception.py](./Chapter2_Perception.py)

> 笔记文件：[chapter2.md](./notes/chapter2.md)

#### 第三章：k近邻法
> 代码文件：kNN分类 \
> [Chapter3_KNN.py](./Chapter3_KNN.py)\
> [Chapter3_KdTree.py](./Chapter3_KdTree.py)

> 笔记文件：[chapter3.md](./notes/chapter3.md)

#### 第四章：朴素贝叶斯
> 代码文件：朴素贝叶斯分类

> 笔记文件：[chapter4.md](./notes/chapter4.md)
