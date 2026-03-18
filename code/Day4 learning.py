# range()
# for i in range(5):
#     print(i)

# for i in range(3,8):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#         if j == i:
#             print()

# for循环生成棋盘格
# size = 8
# for i in range(size):
#     for j in range(size):
#         if (i+j)%2==1:
#             print("□  ",end="")
#         else:
#             print("■  ",end="")
#     print()

# 用推导式生成 1 到 10 的平方数列表
list1=[i*i for i in range(1,11)]
print(list1)

# 用 map 结合 lambda 给全班同学的名字加上统一前缀
names=['张三','李四','王五','赵六']
new_names=map(lambda x:'QG_'+x,names)
print(list(new_names))