import numpy as np
import collections
import matplotlib.pyplot as plt


def kNN(X, X_train, y_train, n):
    # 求前 N 个点到 X 的距离
    knnList = []
    for i in range(len(X_train)):
        # 计算欧式距离
        dist = np.linalg.norm(X - X_train[i], ord=2)
        knnList.append((dist, y_train[i]))
    # 按距离升序排序
    knnList.sort(key=lambda x: x[0])
    print(knnList)
    # 统计距离最小的 N 个点的 label
    # 取出label
    knn = [knnList[i][-1] for i in range(n)]
    # 计数
    # print(type(knn))
    # print(knn)
    count = collections.Counter(knn)
    # 找到数目最多的 label
    maxCount = sorted(count, key=lambda x: x)[-1]
    return maxCount


def draw(X_train, X):
    # 数据点
    plt.plot(X_train[:5, 0], X_train[:5, 1], 'go', label='1')
    plt.plot(X_train[6:, 0], X_train[6:, 1], 'ro', label='-1')
    # 测试点
    plt.plot(X[0], X[1], 'b*', label='test')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = np.array([[5.1, 3.5, 1],
                     [4.9, 3.0, 1],
                     [4.7, 3.2, 1],
                     [4.6, 3.1, 1],
                     [5.0, 3.6, 1],
                     [6.7, 3.3, -1],
                     [6.7, 3.0, -1],
                     [6.3, 2.8, -1],
                     [6.5, 3.2, -1],
                     [6.2, 3.0, -1]])
    X_train = data[:, :-1]
    y_train = data[:, -1]
    X = np.array([6.0, 3.0])
    k = 3
    predict = kNN(X, X_train, y_train, k)
    print(predict)
    draw(X_train, X)

