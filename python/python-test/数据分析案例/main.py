# 进行数据需求逻辑计算(计算每一天的销售额)

from file_define import FileReader, TextFileReader, jsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("D:/python/python-test/2011年1月销售数据.txt")
json_file_reader = jsonFileReader("D:/python/python-test/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将2个月份的数合并为1个list存储
all_data: list[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for record in all_data:
   # 当前日期已经有记录了，所以和老记录做累加即可
   if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date] += record.money
   else:
       data_dict[record.date] = record.money


# 可视化图标开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))  # 添加x轴的数据
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  #添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")

)
bar.render("每日销售额柱状图.html")

