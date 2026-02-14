# 列表的创建、索引、切片访问
list_test=[1,2,3,"hello","world",1]
# print(list_test)

# print(list_test[2])
# print(list_test[-1])

# print(list_test[::])
# print(list_test[1:4])
# print(list_test[::2])

# 修改列表
# list_test[1]="two"
# list_test.append("!")
# list_test.extend([4,5,6])
# list_test.insert(3,"hi")
# print(list_test)

# 删除列表元素
# del list_test[2]
# print(list_test.pop(2))
# list_test.remove(1)
# list_test.clear()
# print(list_test)

# +,*,in,for
# print(list_test+[4,5,6])
# print(list_test*3)
# print(1 in list_test)
# print(9 in list_test)
# for x in list_test:
#     print(x)

# 列表函数
# print(len(list_test))
# list1=[2,4,7]
# print(max(list1))
# print(min(list1))

# 列表方法
# print(list_test.count(1))
# print(list_test.index("hello"))
# list2=[5,3,6,7,2,9]
# list2.reverse()
# list2.sort(reverse=True)
# print(list2)


# 创建元组，索引，截取
tup=(1,2,3,'hello','world')
# print(tup[2])
# print(tup[4:1:-1])

# +,*,in,for
# print(tup+(4,5,6))
# print(tup * 3)
# print(2 in tup)
# print(5 in tup)
# for x in tup:
#     print(x)

# 删除整个元组
# del tup


# 创建字典
dic_people={"name":"沈沈","age":19}
# print(dic_people)

# 访问字典
# print(dic_people['name'])

# 修改字典
# dic_people["age"]=20
# dic_people["gender"]="女"
# print(dic_people)

# 删除字典
# del dic_people["age"]
# dic_people.clear()
# del dic_people
# print(dic_people)

# 字典函数及方法
dic_other={'gender':'女','city':'广州'}
# print(str(dic_people))
# dic_new=dic_people.fromkeys(dic_other,"hello")
# print(dic_new)
# print(dic_people.get("name"))
# print(dic_people.get("gender"))
# print(dic_people.items())
# print(dic_people.keys())
# print(dic_people.values())
# print(dic_people.setdefault("school"))
# dic_people.update(dic_other)
# print(dic_people.pop("name"))
# dic_people.popitem()
# print(dic_people)


# 创建集合
set1={1,2,3,4}
set2=set([5,6,7,8])
# print(type(set1),type(set2))

# 访问集合 in,for
# print(1 in set1)
# print(7 in set1)
# for x in set1:
#     print(x)

# 添加元素至集合中
# set1.add(4)
# print(set1)
# set1.add(9)
# print(set1)
# set1.update([11,12,13,14])
# print(set1)

# 移除元素
# set1.remove(1)
# set1.discard(5)
# set1.pop()
# print(set1)

# 并集
# set3=set1|set2
# set3=set1.union(set2)
# print(set3)

# 交集
set4={10,20,30,40,50}
set5={10,50,100}
# set6=set4&set5
# set6=set4.intersection(set5)
# print(set6)

# 差集
# set7=set5-set4
# set7=set4.difference(set5)
# print(set7)

# 对称差集
# set8=set4^set5
# set8=set4.symmetric_difference(set5)
# print(set8)

# 集合内置方法
# print(set4.issubset(set5))
# print(set4.issuperset((set5)))
# print(set4.isdisjoint(set5))

