import numpy as np

# 设置随机种子
np.random.seed(42)

# 生成随机角度
t = np.random.uniform(0, 2 * np.pi, 60)

# 定义参数
alpha = 0.4
a = 0.5
b = 1.0

# 生成椭圆上的点
x = 1.0 + a * np.cos(t) * np.cos(alpha) - b * np.sin(t) * np.sin(alpha)
y = 1.0 + a * np.cos(t) * np.sin(alpha) + b * np.sin(t) * np.cos(alpha)

# 添加噪声
x += np.random.normal(0, 0.05, size=len(x))
y += np.random.normal(0, 0.05, size=len(y))

# 构建矩阵 D
D = np.c_[x ** 2, x * y, y ** 2, x, y, np.ones_like(x)]

# 计算 A = D^T * D
A = np.dot(D.T, D)

# 构建矩阵 C
C = np.zeros((6, 6))
C[0, 2] = 2
C[1, 1] = -1
C[2, 0] = 2

# 求解广义特征值问题
evalues, evectors = np.linalg.eig(A, C)

# 取实部
evectors = np.real(evectors)

# 计算误差
err = np.mean(np.dot(D, evectors) ** 2, axis=0)

# 找到最小误差对应的特征向量
p = evectors[:, np.argmin(err)]

# 打印结果
print(p)