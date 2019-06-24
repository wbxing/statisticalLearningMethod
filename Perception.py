import numpy as np
import matplotlib.pyplot as plt


# 符号函数
def sign(x, w, b):
    y = np.dot(x, w) + b
    return y


# 随机梯度下降
def fit(X_train, y_train):
    w = np.zeros(X_train.shape[1])
    b = 0
    l_rate = 1
    i = 0
    while i < X_train.shape[0]:
            X = X_train[i]
            y = y_train[i]
            if y * sign(X, w, b) <= 0:
                w = w + l_rate * np.dot(y, X)
                b = b + l_rate * y
                i = 0
            else:
                i += 1
    return w, b


# 可视化
def draw(X, y, w, b):
    pos = 0
    neg = 0
    X_pos = []
    X_neg = []
    for i in range(X.shape[0]):
        if y[i] == 1:
            X_pos.append(X[i])
            pos += 1
        else:
            X_neg.append(X[i])
            neg += 1
    X_pos = np.mat(X_pos).reshape(pos, 2)
    X_neg = np.mat(X_neg).reshape(neg, 2)
    plt.plot(X_pos[:, 0], X_pos[:, 1], 'go', label='Pos')
    plt.plot(X_neg[:, 0], X_neg[:, 1], 'ro', label='Neg')
    plt.plot([-b/w[0], 0], [0, -b/w[1]], 'b-', label='Perception')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = np.array([[3, 3, 1],
                     [3, 2, 1],
                     [1, 1, -1],
                     [1.2, 1.5, -1],
                     [2, 0, -1],
                     [.5, 2, -1],
                     [2.2, 1.5, 1],
                     [2, 2, 1],
                     [2.8, 0.1, -1],
                     [1.7, 1.6, 1]])
    # Data
    X_train = data[:, :-1]
    # Label
    y_train = data[:, -1]
    w, b = fit(X_train, y_train)
    print(w, b)
    draw(X_train, y_train, w, b)
