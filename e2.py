import numpy as np
import matplotlib.pyplot as plt
import pylab as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def data_x():
    f = open('./Iris_KNN', 'r')
    x = []
    for line in f.readlines():
        str = line.split(',')[0]
        x.append(int(str))
    f.close()
    return x


def data_y():
    f = open('./Iris_KNN', 'r')
    y = []
    for line in f.readlines():
        str = line.split(',')[1]
        y.append(float(str.split('\n')[0]))
    f.close()
    return y


def tendency_chart():
    # 生成图像
    plt.plot(data_x(), data_y(), color='red', linewidth=2)
    # 设置刻度
    plt.yticks([i for i in np.arange(0, 1.05, 0.05)])
    # 显示趋势图


def least_square_method():
    # 定义用到的变量,假设用a1*t+a2*t^2+a3*t^3拟合
    t0 = np.matrix([1 for i in range(0, 97)])
    t1 = np.matrix([i for i in range(0, 97)])
    t2 = np.matrix([i*i for i in range(0, 97)])
    t3 = np.matrix([i*i*i for i in range(0, 97)])
    t = [t0, t1, t2, t3]
    f = np.matrix(data_y())
    matirx_solve = np.matrix(np.zeros((4, 4)))
    for i in range(0, 4):
        for j in range(0, 4):
            matirx_solve[i, j] = t[i]*t[j].T
    b = np.matrix(np.zeros((4, 1)))
    for i in range(0, 4):
        b[i, 0] = t[i]*f.T
    x = np.linalg.solve(matirx_solve, b)
    k = np.array([0, 0, 0, 0], dtype=float)
    for i in range(0, 4):
        k[i] = x[3-i, 0]
    p = np.poly1d(k)
    x = np.linspace(0, 110, 500)
    print("自己求的拟合曲线多项式\n%s" % p)
    y = np.polyval(p, x)
    plt.plot(x, y, color='black', linewidth=2, linestyle=':')


def least_square_method2():
    # 定义用到的变量,假设用a1*t+a2*t^2+a3*t^3拟合
    # t0 = np.matrix([1 for i in range(0, 60, 5)])
    t1 = np.matrix([i for i in range(1, 98)])
    t2 = np.matrix([i*i for i in range(1, 98)])
    t3 = np.matrix([i*i*i for i in range(1, 98)])
    t = [t1, t2, t3]
    # print(np.matrix(data_y()))
    f = np.matrix(data_y())
    matirx_solve = np.matrix(np.zeros((3, 3)))
    for i in range(0, 3):
        for j in range(0, 3):
            matirx_solve[i, j] = t[i]*t[j].T
    b = np.matrix(np.zeros((3, 1)))
    for i in range(0, 3):
        b[i, 0] = t[i]*f.T
    x = np.linalg.solve(matirx_solve, b)
    k = np.array([0, 0, 0, 0], dtype=float)
    for i in range(0, 3):
        k[i] = x[2-i, 0]
    p = np.poly1d(k)
    x = np.linspace(0, 110, 500)
    print("自己求的拟合曲线多项式\n%s" % p)
    y = np.polyval(p, x)
    plt.plot(x, y, color='black', linewidth=2, linestyle=':')


def direct_1():
    z1 = np.polyfit(data_x(), data_y(), 2)
    print(z1)
    x = np.poly1d(z1)
    print("用x^2逼近的拟合曲线多项式\n%s\n" % x)
    xi = np.linspace(0, 110, 500)
    y = np.polyval(x, xi)
    plt.plot(xi, y, linewidth=2)


def buidTK():
    # plt.xlabel('时间t(分)')
    # plt.ylabel('含碳量y(吨)')
    # plt.title('钢的含碳量与时间的关系')
    plt.xlabel('k的取值')
    plt.ylabel('准确率')
    plt.title('k的取值与准确率的关系')


buidTK()
least_square_method2()
# least_square_method()
tendency_chart()
direct_1()
plt.show()
plt.savefig('./Iris_KNN.png')
