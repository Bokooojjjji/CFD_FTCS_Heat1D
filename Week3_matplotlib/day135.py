'''
Show all different interpolation methods for imshow
'''
# 导入 matplotlib 库中的 pyplot 模块，它提供了类似 MATLAB 的绘图接口，用于创建各种可视化图表
import matplotlib.pyplot as plt
# 导入 numpy 库，这是 Python 中用于科学计算的基础库，能高效处理多维数组和进行数值运算
import numpy as np

# 以下是从 matplotlib 文档中摘录的关于 imshow 函数 interpolation 参数的说明
# from the docs:
# 如果 interpolation 参数为 None，将使用 rc 配置中的 image.interpolation 默认值。
# 同时可以参考 filternorm 和 filterrad 参数。
# 如果 interpolation 为 'none'，在 Agg、ps 和 pdf 后端不会进行插值处理，其他后端会回退到 'nearest' 插值方法。
# 文档链接：http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow


# 定义一个包含多种插值方法名称的列表
# 后续会用这些方法来展示 imshow 函数不同的插值效果
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

# 设置随机数种子为 0
# 这样做可以确保每次运行代码时生成的随机数序列是相同的，保证结果的可重复性
np.random.seed(0)
# 生成一个 4 行 4 列的随机数组
# 数组中的元素是从 0 到 1 之间均匀分布随机选取的，这个数组将作为图像数据用于展示插值效果
grid = np.random.rand(4, 4)

# 创建一个包含 3 行 6 列共 18 个子图的图形窗口
# figsize=(12, 6) 表示图形窗口的大小，宽为 12 英寸，高为 6 英寸
# subplot_kw={'xticks': [], 'yticks': []} 表示每个子图都不显示 x 轴和 y 轴的刻度标签，让图形更简洁
fig, axes = plt.subplots(3, 6, figsize=(12, 6),
                         subplot_kw={'xticks': [], 'yticks': []})

# 调整子图之间的间距
# hspace=0.3 表示子图之间的垂直间距为 0.3
# wspace=0.05 表示子图之间的水平间距为 0.05
fig.subplots_adjust(hspace=0.3, wspace=0.05)

# 使用 zip 函数将子图对象数组 axes.flat（将二维的子图数组展平为一维）和插值方法列表 methods 进行配对
# 然后遍历每一对子图和插值方法
for ax, interp_method in zip(axes.flat, methods):
    # 在当前子图中使用指定的插值方法显示随机生成的网格数据
    # cmap='viridis' 表示使用 viridis 颜色映射来显示图像
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    # 为当前子图设置标题，标题就是当前使用的插值方法名称
    ax.set_title(interp_method)

# 显示绘制好的包含所有子图的图形
plt.show()