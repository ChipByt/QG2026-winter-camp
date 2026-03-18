import numpy as np
# 创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
a=np.arange(0,12).reshape(3,4)
print(a)
# 查看数组的 shape 、 dtype 、 ndim 属性
print(a.shape)
print(a.dtype)
print(a.ndim)
# 将数组变形为 (4,3)，并展平为一维数组
a.resize(4,3)
print(a)
print(a.ravel())

