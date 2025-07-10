#多维数组的下标存取
import numpy as np
a = np.arange(3*4*5).reshape(3, 4, 5)
aidx = np.array([0, 1])
print(a)
print(a[aidx])

#整数数组作为下标

# 创建三维数组 a
a = np.arange(3*4*5).reshape(3, 4, 5)

# 定义索引数组
i0 = np.array([[1, 2, 1], [0, 1, 0]])
i1 = np.array([[[0]], [[1]]])
i2 = np.array([[[2, 3, 2]]])

# 使用索引数组对 a 进行索引
b = a[i0, i1, i2]

# 广播索引数组
ind0, ind1, ind2 = np.broadcast_arrays(i0, i1, i2)

# 定义索引值
i, j, k = 0, 1, 2

# 打印结果
print(b[i, j, k], a[ind0[i, j, k], ind1[i, j, k], ind2[i, j, k]])



#布尔数组作为下标
b1 = np.array([True,False,True,False])
np.nonzero(b1)
