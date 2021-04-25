# 基于Python3 的 Plotly 绘图教程

> 数据可视化课程小组：金笑缘 陈科锜 李昱勇 唐陆禛
> 
> 本教程已使用Docsify部署于网页，可访问 http://plotly.fishiu.com/


本教程将分为四个部分：
- Plotly 安装指南
- Plotly 基本绘图操作
- Plotly 多子图绘图操作
- Plotly 图表案例

## Plotly简介

Plotly是一个交互式绘图库，提供了JavaScript、Python和R三种接口，本教程将重点介绍使用Plotly for Python进行绘图。

Plotly有三种不同的Python API，可以选择用不同的方法来绘图：

- 面向对象的API，通过plotly.graph_objects模块的图表对象进行绘制
- 数据驱动的API，通过构造类似JSON的数据结构进行绘制
- 高级绘图接口，是对底层绘图方法的包装，即plotly.express模块

### 面向对象API

使用graph_objects模块进行绘图时，用户需要定义画布对象`go.Figure()`、样式对象`go.Layout()`、迹线对象如散点图`go.Scatter()`、柱状图`go.Bar()`等，组合后进行渲染。

### 数据驱动API

Plotly的可视化建立在JSON数据结构之上，trace是一个字典，包含了要绘制的数据和颜色、线性等绘图指令，用于指定一组数据如何呈现；用列表组织多个trace构成了data，即在一张图表中要展示的所有trace；layout也是一个字典，用于设置图表的布局，包括标题、字体等属性，将data和layout组合在一起就构成了一张图表。这种方法直接对应于Plotly的JavaScript实现中的JSON API。

### 高级绘图接口

express模块是对绘图对象进行封装的高级API，类似于seaborn对matplotlib的封装，可以让用户用很少的代码进行绘图。

本教程主要介绍使用面向对象的graph_objects模块进行绘图的方法。

## 安装指南

### Python 环境安装
推荐使用 `conda` 包管理工具（`Anaconda` 或者 `Miniconda`）并以 `Jupyter Notebook` 为主要开发环境。

```bash
$ conda create -n plotly python=3.7  # 建立名为plotly的虚拟环境
$ conda activate plotly  # 激活虚拟环境
```

### Plotly 软件安装
使用pip进行安装
```bash
$ pip install plotly          # 不指定版本号
$ pip install plotly==4.14.3  # 指定版本号
```
或使用conda安装：
```bash
$ conda install -c plotly=4.14.3
```

本教程基于的软件版本为
- `python==3.7.10`
- `plotly==4.14.3`

如果有导出多种图片格式的需要，可以安装 plotly-orca 包
```bash
$ conda install -c plotly plotly-orca==1.2.1 psutil requests
```

### 一个demo

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[2, 3, 1]))
fig.show()
```

运行以上代码，如成功显示图表如下即说明安装成功Plotly。

<img src="http://pic.fishiu.com/uPic/bpJ0dn.png" alt="demo-bar" style="zoom:33%;" />

如有问题请联系小组成员或在讨论版留言。

