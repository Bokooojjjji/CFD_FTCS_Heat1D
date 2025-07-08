import numpy as np
#床头早一个1到20的数组，提取偶数项
a = np.arange(1,21)
even = a [a % 2 == 0]
print("1-20的偶数项" , even)

#构造出5*5的矩阵，选出主对角线与反对角线
m= np.arange(1,26).reshape(5,5)
main_diag = np.diag(m)
anti_diag = np.diag(np.fliplr(m))
print("5*5矩阵是：\n",m)
print(main_diag)
print(anti_diag)

#提取大于平均值的元素

avg = np.mean(a)
greater_than_avg = a[a > avg]
print(avg)
print(greater_than_avg)

#把数组反转

reversed_array = a[::-1]
print(reversed_array)