#非线性方程组求解
from math import sin,cos
from scipy import optimize
def f(x):
    x0,x1,x2 = x.tolist()
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]
result = optimize.fsolve(f,[1,1,1])
print(result)
print(f(result))


# 定义 f 函数
def f(x):
    x0, x1, x2 = x
    return [
        2 * x0 - x1 + x2 - 3,
        x0 + x1 + x2 - 6,
        x0 - 2 * x1 + 3 * x2 - 4
    ]

# 定义雅可比矩阵函数 j
def j(x):
    x0, x1, x2 = x
    return [
        [2, -1, 1],
        [1, 1, 1],
        [1, -2, 3]
    ]

# 使用 fsolve 求解非线性方程组
result = optimize.fsolve(f, [1, 1, 1], fprime=j)

print("方程组的解：", result)
print("将解代入 f 函数的结果：", f(result))

# Day 11 - 线性代数与优化练习
# 📌 主题：线性系统求解、矩阵运算、最小值问题
# ✅ 建议用时：约1小时，注意在每段代码后写注释说明！

import numpy as np
from scipy import linalg, optimize

# ------------------------
# 练习1：解超定方程组（最小二乘法）
# ------------------------
print("【练习1】解超定方程组 Ax = b")

# 构造一个 4×2 的矩阵 A 和常数项向量 b
A = np.array([[1, 2],
              [2, 3],
              [3, 4],
              [4, 5]])
b = np.array([5, 8, 11, 14])

# 用最小二乘解 Ax = b
x_ls, residuals, rank, s = linalg.lstsq(A, b)
print("最小二乘解 x =", x_ls)
print("残差 =", residuals)

# ------------------------
# 练习2：矩阵逆、秩、范数与条件数
# ------------------------
print("\n【练习2】矩阵性质分析")

B = np.array([[1, 2], [3, 4]])

B_inv = linalg.inv(B)
rank_B = np.linalg.matrix_rank(B)
norm_B = linalg.norm(B)
cond_B = np.linalg.cond(B)

print("B 的逆矩阵：\n", B_inv)
print("秩 rank(B) =", rank_B)
print("范数 ||B|| =", norm_B)
print("条件数 cond(B) =", cond_B)

# ------------------------
# 练习3：函数最小值求解（optimize.minimize）
# ------------------------
print("\n【练习3】数值优化：寻找函数最小值")

# 要最小化的函数
def f(x):
    return (x - 2)**2 + np.sin(x)

# 初始猜测
x0 = [0.0]

# 使用 BFGS 算法进行优化
res = optimize.minimize(f, x0, method='BFGS')

print("最小值点 x =", res.x)
print("最小值 f(x) =", res.fun)

#最小二进制

x = np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
y = np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
def residuals(p):
    k,b = p
    return y - (k*x +b)
r = optimize.leastsq(residuals,[1,0])
k,b = r[0]
print("k=",k,"b=",b)



#最小二乘法
import numpy as np
from scipy import optimize

from scipy.optimize import curve_fit

# 假设模型函数：指数衰减
def model_func(x, a, b):
    return a * np.exp(-b * x)

x_data = np.linspace(0, 4, 50)
y_data = model_func(x_data, 2.5, 1.3) + 0.1 * np.random.normal(size=50)

# 拟合
popt, pcov = curve_fit(model_func, x_data, y_data)


#计算函数局域最小值
import numpy as np
from scipy import optimize

def target_function(x, y):
    return 100 * (y - x**2)**2 + (1 - x)**2

class TargetFunction:
    def __init__(self):
        self.f_points = []
        self.fprime_points = []
        self.fhess_points = []

    def f(self, p):
        x, y = p.tolist()
        z = target_function(x, y)
        self.f_points.append((x, y))
        return z

    def fprime(self, p):
        x, y = p.tolist()
        self.fprime_points.append((x, y))
        dx = -2 + 2*x - 400*x*(y - x**2)
        dy = 200*y - 200*x**2
        return np.array([dx, dy])

    def fhess(self, p):
        x, y = p.tolist()
        self.fhess_points.append((x, y))
        return np.array([[2*(600*x**2 - 200*y + 1), -400*x],
                         [-400*x, 200]])

def fmin_demo(method):
    target = TargetFunction()
    init_point = (-1, -1)
    res = optimize.minimize(target.f, init_point,
                            method=method,
                            jac=target.fprime,
                            hess=target.fhess)
    return res, [np.array(points) for points in
                 (target.f_points, target.fprime_points, target.fhess_points)]

methods = ("Nelder-Mead", "Powell", "CG", "BFGS", "Newton-CG", "L-BFGS-B")
for method in methods:
    res, (f_points, fprime_points, fhess_points) = fmin_demo(method)
    print("{:12s}: min={:-12g}, f_count={:3d}, fprime_count={:3d}, fhess_count={:3d}".format(
        method, float(res["fun"]), len(f_points), len(fprime_points), len(fhess_points)))



