#线性代数
#解线性方程组
import numpy as np
from scipy import linalg
import timeit

# 定义矩阵的维度
m, n = 500, 50

# 生成随机矩阵 A 和 B
A = np.random.rand(m, n)
B = np.random.rand(m, n)

# 使用 linalg.solve 求解线性方程组
X1 = linalg.solve(A.T @ A, A.T @ B)  # 这里使用 A.T @ A 使其成为方阵，因为 solve 要求第一个参数是方阵

# 使用矩阵求逆和矩阵乘法求解线性方程组
X2 = np.dot(np.linalg.inv(A.T @ A), A.T @ B)

# 检查两种方法的结果是否接近
print(np.allclose(X1, X2))

# 衡量 linalg.solve 的执行时间
solve_time = timeit.timeit(lambda: linalg.solve(A.T @ A, A.T @ B), number=100)
print(f"linalg.solve 的执行时间: {solve_time} 秒")

# 衡量 np.dot(linalg.inv(A), B) 的执行时间
inv_dot_time = timeit.timeit(lambda: np.dot(np.linalg.inv(A.T @ A), A.T @ B), number=100)
print(f"np.dot(linalg.inv(A), B) 的执行时间: {inv_dot_time} 秒")


import numpy as np
import matplotlib.pyplot as pl
from scipy import optimize

def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p, y, x):
    """
    实验数据x,y和拟合函数之间的差, p为拟合需要找到的系数
    """
    return y - func(x, p)

x = np.linspace(0, 2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6  # 真实数据的函数参数
y0 = func(x, [A, k, theta])  # 真实数据
# 加入噪声之后的实验数据
np.random.seed(0)
y1 = y0 + 2 * np.random.randn(len(x))

p0 = [7, 0.40, 0]  # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = optimize.leastsq(residuals, p0, args=(y1, x))

print("真实参数:", [A, k, theta])
print("拟合参数", plsq[0])  # 实验数据拟合后的参数

pl.plot(x, y1, "o", label="带噪声的实验数据")
pl.plot(x, y0, label="真实数据")
pl.plot(x, func(x, plsq[0]), label="拟合数据")
pl.legend(loc="best")
pl.show()



#最小二乘解
import numpy as np
from numpy.lib.stride_tricks import as_strided
from numpy import linalg

def make_data(m, n, noise_scale):
    np.random.seed(42)
    # 生成 m 个服从标准正态分布的随机数
    x = np.random.standard_normal(m)
    # 生成 n 个服从标准正态分布的随机数
    h = np.random.standard_normal(n)
    # 对 x 和 h 进行卷积操作
    y = np.convolve(x, h)
    # 给卷积结果添加噪声
    yn = y + np.random.standard_normal(len(y)) * noise_scale * np.max(y)
    return x, yn, h

def solve_h(x, y, n):
    # 使用 as_strided 函数构造矩阵 X
    X = as_strided(x, shape=(len(x) - n + 1, n), strides=(x.itemsize, x.itemsize))
    # 提取 Y 向量
    Y = y[n - 1:len(x)]
    # 使用最小二乘法求解线性方程组
    h_estimated, _, _, _ = linalg.lstsq(X, Y, rcond=None)
    return h_estimated[::-1]

# 调用示例
if __name__ == "__main__":
    m = 100
    n = 20
    noise_scale = 0.1

    # 生成数据
    x, yn, h_true = make_data(m, n, noise_scale)

    # 求解 h
    h_estimated = solve_h(x, yn, n)

    print("真实的卷积核 h:", h_true)
    print("估计的卷积核 h:", h_estimated)



#特征值evalues和特征向量evectors
A = np.array([[1,-0.3],[-0.1,0.9]])
evalues,evectors = linalg.eig(A)




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



#奇异值分解
import numpy as np

# 定义一个矩阵
A = np.array([[1, 2], [3, 4], [5, 6]])

# 进行奇异值分解
U, Sigma, Vt = np.linalg.svd(A)

print("左奇异矩阵 U:")
print(U)
print("奇异值矩阵 Sigma:")
print(Sigma)
print("右奇异矩阵 V 的转置 Vt:")
print(Vt)





