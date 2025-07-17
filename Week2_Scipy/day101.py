# Day 10 - SciPy 入门练习
# 主题：常量查询 + 特殊函数库使用


import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, special

# ------------------------
# 练习1：查询常用物理常数
# ------------------------
print("【练习1】常用物理常数查询")
print("π =", constants.pi)
print("重力加速度 g =", constants.g)
print("普朗克常数 h =", constants.Planck)
print("真空光速 c =", constants.c)
print("阿伏伽德罗常数 =", constants.Avogadro)

# ------------------------
# 练习2：Gamma 函数与对数 Gamma
# ------------------------
print("\n【练习2】Gamma 与 LogGamma 计算")
gamma_5 = special.gamma(5)
gamma_10 = special.gamma(10)
log_gamma_5 = special.loggamma(5)
print("Γ(5) =", gamma_5)
print("Γ(10) =", gamma_10)
print("log(Γ(5)) =", log_gamma_5)

# ------------------------
# 练习3：绘制 Bessel 函数 J₀(x)
# ------------------------
print("\n【练习3】绘制 Bessel 函数 J₀(x)")

x = np.linspace(0, 20, 400)
y = special.jn(0, x)  # J₀(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="J₀(x)", color='purple')
plt.title("Bessel 函数 J₀(x)")
plt.xlabel("x")
plt.ylabel("J₀(x)")
plt.grid(True)
plt.legend()
plt.show()