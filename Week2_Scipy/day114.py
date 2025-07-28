<<<<<<< HEAD
import numpy as np

# 定义半圆函数
def half_circle(x):
    return (1 - x**2)**0.5

# 定义x的值
x = np.linspace(-1, 1, 1000)
y = half_circle(x)

# 使用np.trapz计算半圆的面积并乘以2得到圆的面积
circle_area = np.trapz(y, x) * 2
print(circle_area)

from scipy import integrate

# 使用scipy.integrate.quad函数计算半圆的面积
pi_half, err = integrate.quad(half_circle, -1, 1)
print(pi_half * 2)

# 定义半球函数
def half_sphere(x, y):
    return (1 - x**2 - y**2)**0.5

# 使用scipy.integrate.dblquad函数计算半球的体积
volume, error = integrate.dblquad(half_sphere, -1, 1,
                                 lambda x: -half_circle(x),
                                 lambda x: half_circle(x))
print(volume, error, np.pi * 4 / 3 / 2)




#解常微分方程
from scipy.integrate import odeint
import numpy as np
def lorenz(w,t,p,r,b):
    #给出位置矢量w，三个参数p，r，b
    #计算出偏导
    x,y,z = w.tolist()
    #直接与lorenz的计算公式
    return p*(y-x),x*(r-z)-y,x*y-b*z
t = np.arange(0,30,0.02)#创建时间点
#调用ode对lorenze进行求解，用两个不同的初始值
track1 = odeint(lorenz,(0.0,1.00,0.0),t,args=(10.0,28.0))
=======
#数值积分
#球的体积
import numpy as np
def half_circle(x):
    return(1- x**2)**0.5
np.trapz(y,x)*2
from scipy import integrate
>>>>>>> origin/main
