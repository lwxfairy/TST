# pyecharts

## json数据格式

JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据

JSON本质上是一个带有特定格式的字符串

**主要功能**：json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互

### json格式数据转化

通过 json.dumps(data) 方法把python数据转化为了 json数据

data = json.dumps(data)

如果有中文可以带上：ensure_ascii=False参数来确保中文正常转换

通过 json.loads(data) 方法把josn数据转化为了 python列表或字典

data = json.loads(data)

## pyecharts
### pyecharts模块安装

1. 开发可视化图表使用的技术栈是：

​		Echarts框架的Python版本：PyEcharts包

2. 如何安装PyEcharts包：

​		pip install pyecharts

3. 如何查看官方示例

​		打开官方画廊：

​		https://gallery.pyecharts.org/#/README

### pyecharts配置选项

常用的配置选项有：

1. 全局配置选项

2. 系列配置选项

#### 全局配置选项

**全局配置选项**可以通过**set_global_opts**方法来进行配置

* 配置图表的标题

* 配置图例

* 配置鼠标移动效果

* 配置工具栏

* 等整体配置项

| 配置项      | 作用             | 代码实例                                                   |
| ----------- | ---------------- | ---------------------------------------------------------- |
| title_opts  | 设置图标题和位置 | title_opts=opts.TitleOpts(title="标题", pos_left="center") |
| yaxis_opts  | y轴配置项        | yaxis_opts=opts.AxisOpts(name="累计确诊人数")              |
| xaxis_opts  | x轴配置项        | xaxis_opts=opts.AxisOpts(name="时间")                      |
| legend_opts | 图例配置项       | legend_opts=opts.legendOpts(pos_left='70%')                |

#### 系列配置选项

折线图相关配置项：

| 配置项     | 作用                   | 代码实例                                              |
| ---------- | ---------------------- | ----------------------------------------------------- |
| init_opts  | 对折线图初始化设置宽高 | init_opts=opts.InitOpts(width="160px",height="800px") |
| .add_xaxis | 添加x轴数据            | .add_xaxis(列表)                                      |
| .add_yaxis | 添加y轴数据            |                                                       |

.add_yaxis相关配置选项：

| 配置项         | 作用                   | 代码实例                                   |
| -------------- | ---------------------- | ------------------------------------------ |
| series_name    | 设置图例名称           | series_name="美国确诊人数"                 |
| y_axis         | 输入y轴数据            | y_axis=["列表"]                            |
| symbol_size    | 设置点的大小           | symbol_size=10                             |
| label_opts     | 标签设置项：不显示标签 | label_opts=opts.LabelOpts(is_show=False)   |
| linestyle_opts | 线条宽度和样式         | linestyle_opts=opts.LineStyleOpts(width=2) |







### 数据处理

