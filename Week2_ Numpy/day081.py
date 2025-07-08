import numpy as np
a = np.array([1,2,3,4])
print("a:",a)

#切片
print("反转：",a[::-1])

C = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

C.shape = 4, 3

print(C)

d = a.reshape((2,2))

#float是64位的双精度浮点类型，complex是128位的双精度复数类型
ai32 = np.array([1,2,3,4],dtype=np.int32)
af = np.array([1,2,3,4],dtype=float)
ac = np.array([1,2,3,4],dtype=complex)

np.arange(0,1,0.1)
np.linspace(0,1,10)
np.linspace(0,1,10,endpoint = False)
#等比数列
np.logspace(0,2,5)
#zeros,ones,empty
np.empty((2,3),np.int)
#full()能将数组元素华为指定的值
np.full(4,np.pi)
s = "abcdefgh"
np.fromostring(s,dtype=np.int8)
np.fromostring(s,dtype=np.int16)
buf  = np.frombuffer(s,dtype=np.int16)

#九九乘法表
def func2(i,j):
    return(i+1)*(j+1)
np.fromfunction(func2,(9,9))

#提取元素
