raw_info=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;\
Mission:2025-RESCUE-X "
# 清除空格
clean_info=raw_info.replace(" ","")
# 拆分数据
clean_info=clean_info.split(";")
# 分块处理
# 处理Agent
agent=clean_info[0].split(":")
agent=agent[1]

# 处理Coords
coords=clean_info[1].replace("Coords:","")
coords=coords.strip("()")
coords=coords.split(",")
for x in coords:
    int(x)
coords=tuple(coords)

# 处理Items
items=clean_info[2].replace("Items:","")
items=items.split(",")
items_set=set([])
for x in items:
    items_set.add(x)

# 处理Mission
mission=clean_info[3].replace("Mission:","")
mission=mission.split("-")
mission_real=mission[1]

# 整合到字典里
final_info={"Agent":agent,"Coords":coords,"Items":items_set,"Mission":mission_real}
print(final_info)
