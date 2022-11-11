"""
演示JSON数据和Python字典的相互转换
"""
import json
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "小明", "age": 18}, {"name": "李华", "age": 22}, {"name": "小新", "age": 21}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为JSON
d = {"name": "小航", "age": 21}
json_str=json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转换为python数据类型[{k: v, k: v},{k: v, k: v}]
s = '[{"name": "小明", "age": 18}, {"name": "李华", "age": 22}, {"name": "小新", "age": 21}]'
l = json.loads(s)
print(type(l))
print(l)

# 将json字符串转换为python数据类型{k: v, k: v}
s = '{"name": "小航", "age": 21}'
d = json.loads(s)
print(type(d))
print(d)