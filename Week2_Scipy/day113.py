#统计
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def generate_normal_samples(size=1000, loc=0, scale=1):
    """
    生成指定大小、均值和标准差的正态分布样本
    :param size: 样本数量
    :param loc: 正态分布的均值
    :param scale: 正态分布的标准差
    :return: 生成的样本数据
    """
    return stats.norm.rvs(loc=loc, scale=scale, size=size)

def fit_normal_distribution(data):
    """
    拟合正态分布并返回拟合参数
    :param data: 样本数据
    :return: 拟合后的均值和标准差
    """
    mu, sigma = stats.norm.fit(data)
    print(f"拟合参数：μ={mu:.2f}, σ={sigma:.2f}")
    return mu, sigma

def plot_normal_fit(data, mu, sigma):
    """
    绘制样本数据的直方图和拟合的正态分布曲线
    :param data: 样本数据
    :param mu: 拟合后的均值
    :param sigma: 拟合后的标准差
    """
    # 生成用于绘制拟合曲线的 x 值
    x = np.linspace(np.min(data) - 2 * sigma, np.max(data) + 2 * sigma, 100)
    # 计算拟合正态分布的概率密度函数值
    pdf = stats.norm.pdf(x, mu, sigma)
    # 绘制样本数据的直方图
    plt.hist(data, bins=30, density=True, alpha=0.5, label='样本数据直方图')
    # 绘制拟合的正态分布曲线
    plt.plot(x, pdf, 'r--', label='拟合正态分布')
    # 添加图例
    plt.legend()
    # 设置标题
    plt.title("正态分布拟合")
    # 设置 x 轴和 y 轴标签
    plt.xlabel('值')
    plt.ylabel('概率密度')
    # 显示图形
    plt.show()

def perform_t_test():
    """
    进行独立样本 t 检验
    """
    # 生成第一组正态分布样本
    x1 = np.random.normal(0, 1, 100)
    # 生成第二组正态分布样本
    x2 = np.random.normal(0.5, 1, 100)
    # 进行独立样本 t 检验
    t_stat, p_value = stats.ttest_ind(x1, x2)
    print(f"T统计量={t_stat:.2f}, P值={p_value:.4f}")
    if p_value < 0.05:
        print("在 0.05 的显著性水平下，两组样本均值有显著差异。")
    else:
        print("在 0.05 的显著性水平下，两组样本均值没有显著差异。")

if __name__ == "__main__":
    # 生成正态分布样本
    data = generate_normal_samples()
    # 拟合正态分布并获取参数
    mu, sigma = fit_normal_distribution(data)
    # 绘制直方图和拟合曲线
    plot_normal_fit(data, mu, sigma)
    # 进行 t 检验
    perform_t_test()




