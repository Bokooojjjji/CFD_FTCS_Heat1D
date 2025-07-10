import numpy as np
#取第i行
a[i]
#i行j列
a[i,j]
#从第0行/列开始。每个一行/列取一个,步长为2的切片
a[::2]
a[:,1]#取所有行的第二列
#布尔索引
a[a > 50]#取所有大于50的元素
#reshape改变形状
b = np.arange(12)
b2 = np.arange(b,(3,4))
#调换维度
a = np.array([[1,2,3],[4,5,6]])
a_T = np.transpose(a)
#沿轴拼接
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b),axis=0)
#axis = 0上下拼接
#axis = 1左右拼接
#np.stack
a = np.array([1,2,3])
b = np.array([4,5,6])
s = np.stack((a,b))
s1 = np.stack((a,b),axis = 1)

x = np.arange(9)
x1, x2, x3 = np.split(x, 3)  # 切成 3 份
np.split(x, [2, 5])
# 得到三个数组：[0,1]、[2,3,4]、[5,6,7,8]




#统计函数与通用数学函数


print("📊 NumPy 统计函数演示")

a = np.array([[1, 2, 3], [4, 5, 6]])

print("数组 a：\n", a)
print("平均值：", np.mean(a))
print("按列平均值：", np.mean(a, axis=0))
print("中位数：", np.median(a))
print("标准差：", np.std(a))
print("方差：", np.var(a))
print("最大值：", np.max(a))
print("最小值：", np.min(a))
print("元素总和：", np.sum(a))

print("\n🧮 通用函数（逐元素运算）演示")

b = np.array([1, 4, 9])
c = np.array([2, 2, 3])

print("b:", b)
print("c:", c)

print("加法 np.add(b, c):", np.add(b, c))
print("减法 np.subtract(b, c):", np.subtract(b, c))
print("乘法 np.multiply(b, c):", np.multiply(b, c))
print("除法 np.divide(b, c):", np.divide(b, c))
print("幂运算 np.power(b, 0.5):", np.power(b, 0.5))  # 开平方

print("指数 np.exp(b):", np.exp(b))
print("对数 np.log(b):", np.log(b))
print("正弦 np.sin(b):", np.sin(b))
print("余弦 np.cos(b):", np.cos(b))
print("绝对值 np.abs([-3, -1, 0, 1]):", np.abs(np.array([-3, -1, 0, 1])))