import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


# 目标函数
def goalFunction(x):
    goal = np.sin(2*x*np.pi)
    return goal


# 拟合函数
def fitFunction(p, x):
    f = np.poly1d(p)
    return f(x)


# 残差函数
def resFunction(p, x, y):
    res = fitFunction(p, x) - y
    return res


# 带正则化的残差函数
def resFunctionWithRegularization(p, x, y, regularization=0.0001):
    res = resFunction(p, x, y)
    # L2范数作为正则化项
    resR = np.append(res, np.sqrt(0.5*regularization*np.square(p)))
    return resR


# 训练
def fit(M, flag=0):
    # M 为拟合函数最高次数
    # 随机初始化多项式参数
    p_init = np.random.rand(M + 1)
    name = 'prediction, M=' + str(M)
    # 最小二乘法
    if flag == 0:
        p_lsq = leastsq(resFunction, p_init, args=(x, y))
    else:
        p_lsq = leastsq(resFunctionWithRegularization, p_init, args=(x, y))
        name += ' with regularization'
    print('Fitting Parameters:', p_lsq[0])

    # 可视化
    # 数据点
    plt.plot(x, y, 'ro', label='data')
    # 目标函数真实曲线
    plt.plot(x_points, goalFunction(x_points), label='Real')
    # 拟合曲线
    plt.plot(x_points, fitFunction(p_lsq[0], x_points), label=name)
    plt.legend()
    plt.show()
    return p_lsq


if __name__ == '__main__':
    # 均匀生成十个点
    x = np.linspace(0, 1, 10)
    # print(x)
    # 目标函数值
    y_ = goalFunction(x)
    # 加上正态分布噪音的目标函数值
    y = [np.random.normal(0, 0.1) + y1 for y1 in y_]
    # 可视化
    x_points = np.linspace(0, 1, 1000)

    # M = 0
    fit(M=0)
    # M = 1
    fit(M=1)
    # M = 3
    fit(M=3)
    # M = 9
    fit(M=9)
    # M = 9, 正则化项
    fit(M=9, flag=1)
