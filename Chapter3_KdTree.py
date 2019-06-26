from math import sqrt
from collections import namedtuple
import numpy as np


# kdTree结点
class KdNode(object):
    def __init__(self, dom_elt, split, left, right):
        # k 维向量节点（ k 维空间中的一个样本点）
        self.dom_elt = dom_elt
        # 整数（进行分割维度的序号）
        self.split = split
        # 该结点分割超平面左子空间构成的kdTree
        self.left = left
        # 该结点分割超平面右子空间构成的kdTree
        self.right = right


# kdTree
class KdTree(object):
    def __init__(self, data):
        # 数据维度
        k = len(data[0])
        # 按第 split 维划分数据集 exset 创建KdNode
        def CreateNode(split, dataSet):
            dataSet = list(dataSet)
            # 数据集为空
            if not dataSet:
                return None
            # key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较
            # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为需要获取的数据在对象中的序号
            # data_set.sort(key=itemgetter(split))
            # 按要进行分割的那一维数据排序
            dataSet.sort(key=lambda x: x[split])
            # 整数
            splitPos = len(dataSet) // 2
            # 中位数分割点
            median = dataSet[splitPos]
            # cycle coordinates
            splitNext = (split + 1) % k
            # 递归的创建 kd 树
            return KdNode(median, split,
                          CreateNode(splitNext, dataSet[:splitPos]),
                          CreateNode(splitNext, dataSet[splitPos + 1:]))
        # 从第0维分量开始构建 kd 树，返回根节点
        self.root = CreateNode(0, data)


# KDTree的前序遍历
def preorder(root):
    print(root.dom_elt)
    # 节点不为空
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


def findNearest(tree, point, result):
    # 数据维度
    k = len(point)
    def travel(kd_node, target, maxDist):
        if kd_node is None:
            # python 中用 float("inf") 和 float("-inf") 表示正负无穷
            return result([0] * k, float("inf"), 0)
        nodesVisited = 1
        # 进行分割的维度
        s = kd_node.split
        # 进行分割的“轴”
        pivot = kd_node.dom_elt
        # 如果目标点第 s 维小于分割轴的对应值(目标离左子树更近)
        if target[s] <= pivot[s]:
            # 下一个访问节点为左子树根节点
            nearer_node = kd_node.left
            # 同时记录下右子树
            further_node = kd_node.right
        # 目标离右子树更近
        else:
            # 下一个访问节点为右子树根节点
            nearer_node = kd_node.right
            further_node = kd_node.left
        # 进行遍历找到包含目标点的区域
        temp1 = travel(nearer_node, target, maxDist)
        # 以此叶结点作为当前最近点
        nearest = temp1.nearestPoint
        # 更新最近距离
        dist = temp1.nearestDistance
        nodesVisited += temp1.nodesVisited
        if dist < maxDist:
            # 最近点将在以目标点为球心，maxDist 为半径的超球体内
            maxDist = dist
        # 第 s 维上目标点与分割超平面的距离
        tempDist = abs(pivot[s] - target[s])
        # 判断超球体是否与超平面相交
        if maxDist < tempDist:
            # 不相交则可以直接返回，不用继续判断
            return result(nearest, dist, nodesVisited)
        # 计算目标点与分割点的欧氏距离
        tempDist = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(pivot, target)))
        if tempDist < dist:
            # 更新最近点
            nearest = pivot
            # 更新最近距离
            dist = tempDist
            # 更新超球体半径
            maxDist = dist
        # 检查另一个子结点对应的区域是否有更近的点
        temp2 = travel(further_node, target, maxDist)
        nodesVisited += temp2.nodesVisited
        # 如果另一个子结点内存在更近距离
        if temp2.nearestDistance < dist:
            # 更新最近点
            nearest = temp2.nearestPoint
            # 更新最近距离
            dist = temp2.nearestDistance
        return result(nearest, dist, nodesVisited)
    # 从根节点开始递归
    return travel(tree.root, point, float("inf"))


if __name__ == '__main__':
    # 对构建好的kd树进行搜索，寻找与目标点最近的样本点
    # 定义一个 namedtuple ，分别存放最近坐标点、最近距离和访问过的节点数
    result = namedtuple("Result", "nearestPoint  nearestDistance  nodesVisited")
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
    data = data[:, :-1]
    kd = KdTree(data)
    preorder(kd.root)
    ret = findNearest(kd, [3, 4.5], result)
    print(ret)
