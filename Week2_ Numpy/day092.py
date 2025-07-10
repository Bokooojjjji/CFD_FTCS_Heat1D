import numpy as np
#自定义ufunc
def triangle_wave(x,c,c0,hc):
    x = x - int(X)
    if x >=c:
        r = 0.0
    elif x < c0:
        r = x / c0*hc
    else:
        r = (c - x)/(c-c0)*hc
    return r
import numpy as np

a = np.arange(0, 60, 10).reshape(-1, 1)
b = np.arange(0, 5)
c = a + b
print(c)
b.shape = (1,5)
b = b.repeat(6, axis=0)
print(b)
a = a.repeat(5, axis=0)
x,y = np.orgid[:5,:5]
m,n = np.mgrid[:5,:5]



import numpy as np

# 生成一个包含 12 个元素的一维数组
arr = np.arange(12)
print("原始数组:", arr)
print("原始数组的形状:", arr.shape)

# 使用 reshape 方法将数组转换为二维数组，其中第一维大小为 3，第二维用 -1 表示
reshaped_arr_1 = arr.reshape(3, -1)
print("重塑后数组 1 的形状:", reshaped_arr_1.shape)
print("重塑后数组 1:")
print(reshaped_arr_1)

# 使用 reshape 方法将数组转换为二维数组，其中第二维大小为 4，第一维用 -1 表示
reshaped_arr_2 = arr.reshape(-1, 4)
print("重塑后数组 2 的形状:", reshaped_arr_2.shape)
print("重塑后数组 2:")
print(reshaped_arr_2)




import numpy as np
A = np.array([[1],[2],[3]])
B = np.array([10,20,30,40])
C = A + B
print("A + B 的结果是： \n", C)

#np.dot 矩阵乘法
M1 = np.array([[1,2],[3,4]])
M2 = np.array([[5,6],[7,8]])
dot_result = np.dot(M1,M2)
print(dot_result)

#特征值与特征向量

S = np.array([[2,-1],[-1,2]])
eig_vals,eig_vecs = np.linalg.eig(S)
print(S)
print("特征值：",eig_vals)
print("特征向量：\n",eig_vecs)

#单位矩阵与随机矩阵的相加
I = np.eye(3)
R = np.random.rand(3,3)
sum_matrix = I + R
print("单位矩阵I: \n",I)
print("随机矩阵： \n",R)
print(sum_matrix)