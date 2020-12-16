import random
import math


# 树类
def HST(r):
    """
    param r: 新的节点\n
    """
    return [r]

def dis(i,j):
    """
    :param i: 二维坐标下的点\n
    :param j: 二维坐标下的点\n
    """
    return math.sqrt(math.pow((i['x'] - j['x']), 2) + math.pow((i['y'] - j['y']), 2))

def max_dis(V):
    """
    :param v: 用于求最远距离的点集\n
    """
    d = 0.0
    for i in V:
        for j in V:
            d = max(d, dis(i, j))
    return d


def construct(tree, i):
    """
    构建HST树\n
    :param tree: 待划分的父亲结点\n
    :param i: 新结点的层数\n
    """
    # 一棵只有根结点的树
    if i < 0:
        return
    T = tree[0]
    r[i] = beta*pow(2,i)
    global c
    # print(r[i])
    for vertex_i in PI:
        if len(T) == 0:
            return
        temp = []
        U = []
        new_T = []
        for vertex_j in metrixs:
            if dis(vertex_i,vertex_j) <= r[i]:
                temp.append(vertex_j)
        # temp 和 T 的交集
        for vertex in temp:
            if vertex in T:
                U.append(vertex)
        # T - U
        for vertex in T:
            if vertex not in U:
                new_T.append(vertex)
        # U 不为空，新建结点，递归构建树
        if len(U) != 0:
            HST_U = HST(U)
            # print('距离点', vertex_i, r[i], '的点有', U)
            tree.append(HST_U)
            construct(HST_U, i-1)
            T = new_T
            # print('当前T为 ',T)

    c = max(c, len(tree))    
        

def add_fake_nodes(HST_tree, level):
    """
    添加fake nodes\n
    :param HST_tree: 树\n
    :param level: 递归的层数\n
    """
    if level < 0:
        return
    l = len(HST_tree)
    # print(c,l)
    for i in range(c-l):
        HST_tree.append([])

    for i in range(len(HST_tree)-1):
        add_fake_nodes(HST_tree[i+1], level-1)


def print_tree(HST_tree, level):
    """
    先序遍历树\n
    :param HST_tree: 树\n
    :param level: 当前根结点的层数\n
    """
    if level < 0:
        return
    if len(HST_tree) != 0:
        print(HST_tree[0])
    if level == 0:
        print(HST_tree)
    for i in range(len(HST_tree)-1):
        print_tree(HST_tree[i+1], level-1)

def print_leaf(HST_tree, level):
    if level == 0:
        print(HST_tree)
        return
    for i in range(len(HST_tree)-1):
        print_leaf(HST_tree[i+1], level-1)

# 每两个结点之间的最近公共祖先所在层数
def LCA_level(HST_tree, level, start, end):
    if start == end:
        LCA[start][end] = 0
        return
    for i in range(c-1):
        for j in range(c-1):
            if i != j:
                for k in range(pow(c-1, level-1)):
                    for l in range(pow(c-1, level-1)):
                        LCA[start+i*pow(c-1, level-1)+k][start+j*pow(c-1, level-1)+l] = level
    for i in range(c-1):
        LCA_level(HST_tree[i+1], level-1, start+i*pow(c-1, level-1), start+(i+1)*pow(c-1, level-1)-1)

def print_format(M):
    for i in range(len(M)):
        print(M[i])


# 算法1
def algorithm_1(V):
    """
    :param V: 原空间上的点的集合\n
    """
    # 构造HST树
    S[D].append(V)
    HST_tree = HST(V)
    construct(HST_tree, D-1)
    add_fake_nodes(HST_tree, D-1)
    # print(HST_tree)
    return HST_tree


# 算法2

# 算法3

# 算法4


# 初始化点
metrixs = [
    {'x': 1,'y': 1},
    {'x': 2,'y': 3},
    {'x': 5,'y': 3},
    {'x': 4,'y': 4}
]
# V的一个随机序列PI 
PI = metrixs
# random.shuffle(PI) 
print('V的一个随机序列：',PI)
# 树的最高层D
maxD = max_dis(metrixs) 
D = math.ceil(math.log(2*maxD,2))
print(D)
# beta
beta = random.uniform(0.5,1)
beta = 0.5
print(beta)
# 每一层的结点(好像没用到呢)
S = [[],[],[],[],[]]
# 划分距离
r = [0]*D
# maximum number of branches in the tree
c = 0



# algorithm_1构造树
HST_tree = algorithm_1(metrixs)
print_tree(HST_tree, D)
print_leaf(HST_tree, D)
# 叶子结点数
num_of_nodes = pow(c-1, D)
print(num_of_nodes)
# LCA[x][a]，任意两个结点的最近公共祖先所在层
LCA = [[0 for i in range(num_of_nodes)] for i in range(num_of_nodes)]
LCA_level(HST_tree, D, 0, num_of_nodes-1)
print_format(LCA)