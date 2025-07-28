#image图像
# 导入 matplotlib 库中的 pyplot 模块，它是 Python 里常用的绘图工具，用于后续图像的绘制
import matplotlib.pyplot as plt
# 导入 numpy 库，该库主要用于数值计算和数组操作，方便对数据进行处理
import numpy as np

# 创建一个一维的 numpy 数组 a
# 数组中包含了 9 个浮点数，后续会将其转换为二维数组
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379])
# 使用 reshape 方法将一维数组 a 转换为 3x3 的二维数组
# 这样就形成了一个 3 行 3 列的矩阵，可用于后续图像的绘制
a = a.reshape(3, 3)

# 使用 plt.imshow 函数来显示图像
# a 是要显示的二维数组，也就是图像的数据
# interpolation='nearest' 表示使用最近邻插值方法来处理像素，这种方法会让图像的像素边缘比较清晰
# cmap='bone' 表示使用 'bone' 颜色映射，它会将数组中的数值映射为不同的颜色，这里是一种灰度风格的颜色映射
# origin='lower' 表示图像的原点位于左下角，这是一种常见的图像坐标设置方式
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')

# 使用 plt.colorbar 函数添加颜色条
# 颜色条可以帮助我们理解图像中不同颜色所代表的数值大小
# shrink=.92 表示将颜色条的长度缩小为原来的 92%，让颜色条在图中更协调
plt.colorbar(shrink=.92)

# 不显示 x 轴的刻度标签，使图像更加简洁，突出图像本身
plt.xticks(())
# 不显示 y 轴的刻度标签，同样是为了让图像更简洁
plt.yticks(())

# 显示绘制好的图像
plt.show()