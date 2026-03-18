import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 处理加州房价数据
house=pd.read_csv('housing.csv')
# print(house.info())
# population=house["population"]
# print(population.head(8))
# 暂时不知道要处理什么


# 配合 Matplotlib 画图，用 NumPy 生成 x 轴数据，绘制正弦曲线
fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.1)
ax.plot(x,np.sin(x),color='green',linewidth=3)
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.grid(True)
plt.show()


