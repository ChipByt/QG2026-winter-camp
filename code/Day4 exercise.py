# 能源核心数据清洗
# 数据： raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
# 实现自动跳过非数字项、仅保留≥80 数值、归一化为 0.xx-1.xx 小数，且根据结果是否 > 1.0
# 对应报「核心过载」或输出「运转正常」

raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99","120"]
print('原始数据：',raw_data)

# 过滤非数字项
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

num_data=[]
for i in raw_data:
    if is_number(i):
        num_data.append(float(i))

# 过滤小于80的数字
num_data=list(x for x in num_data if x>=80)
print("符合要求的数字项",num_data)

# 归一化处理
max_data=max(num_data)
min_data=min(num_data)
final_data=[]
if max_data>min_data:
    for i in num_data:
        item=(i-min_data)/(max_data-min_data)+0.5
        final_data.append(round(item,2))
else:
    final_data=[1.0]*len(num_data)
print("归一化结果",final_data)

# 判断结果
for i in final_data:
    if i>1.0:
        print(f"{i:.2f} 核心过载")
    else:
        print(f"{i:.2f} 运转正常")
