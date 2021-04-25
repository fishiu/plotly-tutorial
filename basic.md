## Plotly基本绘图操作

```python
import plotly.graph_objects as go
import numpy as np
```

### 图表的创建和更改

首先通过`go.Figure()`来生成一个`Figure`画布对象，`Figure`对象拥有`trace`和`layout`两个主要的属性。其中`trace`代表图表中的迹线对象，`layout`代表图表的样式对象。
二者可以通过使用`Figure`对象的` .add_trace()`方法和`.update_layout()` 方法来进行更改


```python
fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_layout(title=dict(text="plotly生成的第一张图"))
fig.show()
```

或者在生成`Figure`对象时定义`trace`和`layout`属性


```python
fig=go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],layout=dict(title=dict(text="plotly生成的第一张图")))
fig.show()
```

| <img src="http://pic.fishiu.com/uPic/lyy/1.jpg" alt="1" style="zoom:100%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/2.jpg" alt="2" style="zoom:100%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                           第一张图                           |                          更改后的图                          |

也可以继续进行更改，并且在更改`trace`属性的时候，也可以使用`selector`选择某一个`trace`来进行更改，如图2所示


```python
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_traces(line=dict(dash="dot"),selector=dict(type='scatter'))
fig.update_layout(yaxis=dict(showgrid=False),title=dict(text="使用选择器来修改属性"))
fig.show()
```

### 坐标轴

这里主要涉及的是`Figure`对象的`.update_xaxes()`和`.update_yaxes()`两个方法

#### 更改坐标轴的显示范围

在`.update_xaxes`的`range`方法中设置


```python
x=10*np.random.rand(20)
y=np.random.randn(20)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x,y=y,mode='markers'))
fig.update_xaxes(range=[0, 20])
fig.show()
```

| <img src="http://pic.fishiu.com/uPic/lyy/3.jpg" alt="3" style="zoom:100%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/4.jpg" alt="4" style="zoom:100%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                     调整坐标轴的显示范围                     |                      调整坐标轴的标记值                      |

#### 更改坐标轴的标记值

首先介绍较为自由的自己设置坐标轴的标记的方法，如下所示，其中`tickvals`为选定的值，`ticktext`为改变后的值。也可以只设置`tickvals`，这时只会显示`tickvals`中的值。

其次也可以通过设置标记的个数、设置标记的起点以及标记之间的间隔的方法来自动更改标记值

也可以通过对`update_xaxes`下的`tickangle`、`tickfont`以及`tickformat`属性进行更改，来设置坐标轴标记的 字体、颜色、角度等显示样式


```python
fig.update_xaxes(range=[0, 10])
fig.update_xaxes(ticktext=["Half", "End"],tickvals=[5,10])
#fig.update_yaxes(nticks=5) 设置标记的个数
fig.update_yaxes(tick0=-3, dtick=0.25) #设置标记的起点以及标记之间的间隔
#设置坐标轴标记的显示样式
fig.update_xaxes(ticktext=["Half", "End"],tickvals=[5,10])
fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='crimson', size=14))
fig.update_yaxes(tickformat = '%')
fig.show()
```



#### 设置多坐标轴

当有设置多坐标轴的需要时，需要通过`make_subplots`来生成`Figure`对象，并且设置其中的`secondary_y`或者`secondary_x`


```python
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),secondary_y=False,)
fig.add_trace(go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),secondary_y=True,)
fig.show()
```

| <img src="http://pic.fishiu.com/uPic/lyy/5.jpg" alt="5" style="zoom:100%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/6.jpg" alt="6" style="zoom:67%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                         设置多坐标轴                         |                   调整图表大小以及画布背景                   |

### 图表大小 画布背景

其中`width`和`height`表示画布的大小，`margin`代表图表与画布边界之间的距离


```python
fig.update_layout(width=500,height=500,margin=dict(l=50,r=50,b=100,t=100,),paper_bgcolor="LightSteelBlue",)
fig.show()
```

### 图标题、坐标轴标题、图例

#### 图标题、坐标轴标题、图例标题的生成
图例标题的生成可以在`add_trace`的时候，为每一个`trace`给一个名称，该名称将会在图例中显示出来

图标题、坐标轴标题可以在`update_layout`中生成，同时也可以通过`font`为所有的标题设置字体样式


```python
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8],y=[0, 1, 2, 3, 4, 5, 6, 7, 8],name="直线"))
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8],y=[1, 0, 3, 2, 5, 4, 7, 6, 8],name="波动线"))
fig.update_layout(title="这里是标题",xaxis_title="X 轴",yaxis_title="Y 轴",legend_title="图例",
    font=dict(family="Courier New, monospace",size=15,color="RebeccaPurple"))
fig.show()
```

#### 独立更改某一部分标题的位置、字体样式

其中`title_x=0.5`的形式是一种简写，相当于`title=dict(x=0.5)`，这种方法能够方便组织代码的结构。
其中`xanchor`和`yanchor`代表选定的标题的锚定点，这里选择的是标题的上边界的中间，`x`和`y`代表上述标题选定的位置在画布中的位置比例。这里以`title`举例，将`title`换成`legend`也是一样的。


```python
fig.update_layout(title_font_family="Times New Roman",title_font_color='red',
    title_y=0.85,title_x=0.5,title_xanchor='center',title_yanchor='top')
fig.show()
```

| <img src="http://pic.fishiu.com/uPic/lyy/7.jpg" alt="7" style="zoom:200%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/8.jpg" alt="8" style="zoom:200%;" /> |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
|              图标题、坐标轴标题、图例标题的生成              | 独立更改某一部分标题的位置、字体样式                         |

#### 调整图例的样式


```python
#调整图例的顺序
fig.update_layout(legend_traceorder="reversed")
#调整图例的排列方式
fig.update_layout(legend_orientation='h',legend_y=1,legend_x=0.9,
                  legend_xanchor='center',legend_yanchor='bottom')
#调整图例的背景，边框
fig.update_layout(legend=dict(x=0.88,bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
fig.show()
```

​    <img src="http://pic.fishiu.com/uPic/lyy/9.jpg" alt="9" style="zoom:50%;" />

### 注释与辅助图形

#### 在`add_trace`时系统自动添加的注释
可以通过`textposition`和`textfont`属性来设置注释的字体样式,并且可以通过`uniformtext`来调节这类自动生成的注释的显示情况，其中`minsize`设置字体大小，`mode`设置当字体的总大小大于设置的大小时如何展示 这里设置为`hide`，即饼图中较小的区不展示注释


```python
df = px.data.gapminder().query("continent == 'Asia' and year == 2007")
fig = go.Figure()
fig.add_trace(go.Pie(values=df['pop'], labels=df['country']))
fig.update_traces(textposition='inside',textfont_size=12)
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()
```

<img src="http://pic.fishiu.com/uPic/lyy/10.jpg" alt="10" style="zoom:67%;" />



#### 使用`add_annotation`来自由添加注释

其中`xref`和`yref`代表注释的参考系的选择，可以是当前的坐标的形式，也可以是上文中提到的按照整个画布的比例的形式  
而`ax`和`ay`则代表与选定的点的相对距离，可以自行调整。其余的内容则是对箭头以及边框、字体的样式进行调整的内容，不再赘述。


```python
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8],y=[0, 1, 3, 2, 4, 3, 4, 6, 5]))
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4, 5, 6, 7, 8],y=[0, 4, 5, 1, 2, 2, 3, 4, 2]))
fig.add_annotation(x=2,y=5,xref="x",yref="y",text="max=5",
                   font=dict(family="Courier New, monospace",size=16,color="#ffffff"),
                   showarrow=True,align="center",arrowhead=2,
                   arrowsize=1,arrowwidth=2,arrowcolor="#636363",
                   ax=50, ay=-30,
                   bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="#ff7f0e",opacity=0.8)
fig.update_layout(showlegend=False)
fig.show()
```
#### 使用`add_shape`来添加辅助图形

在这里我们添加了一条`y=x`的辅助线，以及将最大值的标识注释用一个长方形圈出。
```python
fig.add_shape(type="line",x0=0, y0=0, x1=8, y1=8,
    line=dict(color="orange",dash="dot",width=3))
fig.add_shape(type="rect",x0=2, y0=5, x1=3, y1=7, #这里要标识出长方形的左下顶点和右上顶点
    line=dict(color="RoyalBlue"))
fig.show()
```
| <img src="http://pic.fishiu.com/uPic/lyy/11.jpg" alt="11" style="zoom:67%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/11-1.jpg" alt="11-1" style="zoom:67%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                           添加注释                           |                         添加辅助图形                         |



### `Hover`和`Marker`

`plotly`里的`Hover`是指鼠标悬停在某个点上时，与该点之间的交互，`Marker`是指对图表中点的标记

#### 设置Hover的模式
closest模式（默认模式），浮现一个文本框；x或y模式，只展示x轴或者y轴的值；x(y) unfined 模式，与x(y)模式的区别在于，将同一方向的不同值，放入了一个文本框中共同展示。


```python
t = np.linspace(0, 2 * np.pi, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=np.sin(t), name='sin(t)'))
fig.add_trace(go.Scatter(x=t, y=np.cos(t), name='cost(t)'))
fig.update_layout(hovermode='closest')
fig.show()
```


```python
fig.update_layout(hovermode='x')
fig.show()
```


```python
fig.update_layout(hovermode="x unified")
fig.show()
```

<img src="http://pic.fishiu.com/uPic/lyy/12.jpg" alt="12" style="zoom:67%;" />



#### 设置`Hover`中展示的内容以及背景、字体样式
可以通过`hoverinfo`来调整展示的内容，其中`hoverinfo`的取值可以是`x`,`y`,`name`,`text`，其中`name`为当前`trace`的名称，`text`可以是自己定义的值。`hoverinfo`也可以是其中数者之间的相加，如下文的举例的`’name+x+text’`

可以通过设置`hoverlabel`这个属性来设置Hover的背景、字体样式


```python
fig.update_layout(hovermode="closest")
fig.update_traces(text='三角函数',hoverinfo='name+x+text')
#设置Hover的背景、字体样式
fig.update_layout(hoverlabel=dict(bgcolor="white",font_size=16,font_family="Rockwell"))
fig.show()
```
同时还可以使用模板来为hover定制个性化的展示内容,其中%{}中的内容是显示的值，其余的部分是对其样式的调整。


```python
fig = go.Figure(go.Scatter(x = [1,2,3,4,5],y = [2.02825,1.63728,6.83839,4.8485,4.73463],
    hovertemplate ='<i>Price</i>: $%{y:.2f}'+'<br><b>X</b>: %{x}<br>'+ '<b>%{text}</b>',
    text = ['Custom text {}'.format(i + 1) for i in range(5)],showlegend = False))
fig.show()
```
| <img src="http://pic.fishiu.com/uPic/lyy/13.jpg" alt="13" style="zoom:67%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/14.jpg" alt="14" style="zoom:67%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                   设置`Hover`中展示的内容                    |            使用模板来为hover定制个性化的展示内容             |

#### 设置marker的边框、颜色以及透明度等

主要是在trace下面的marker属性中设置整个marker的大小颜色等，在marker_line属性中设置marker的边框。


```python
np.random.seed(1)
x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))
fig = go.Figure()
fig.add_trace(go.Scatter(mode='markers',x=x,y=y,
                         marker=dict(color='LightSkyBlue',size=20,opacity=0.5,
                                     line=dict(color='MediumPurple',width=2)),showlegend=False))

fig.add_trace(go.Scatter(mode='markers',x=[2],y=[4.5],
                         marker=dict(color='LightSkyBlue',size=120,opacity=1,
                                     line=dict(color='MediumPurple',width=12)),showlegend=False))
fig.show()
```
#### 设置marker的样式

可以在trace属性下面设置marker_symbol属性来调整marker的样式


```python
fig.update_traces(
    marker_symbol='square-open'
)
fig.show()
```
| <img src="http://pic.fishiu.com/uPic/lyy/15.jpg" alt="15" style="zoom:67%;" /> | <img src="http://pic.fishiu.com/uPic/lyy/16.jpg" alt="16" style="zoom:67%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|               设置marker的边框、颜色以及透明度               |              将marker的样式设置为`square-open`               |

其中所有可选择的样式点击图片链接即可查看：http://pic.fishiu.com/uPic/lyy/%E6%A0%B7%E5%BC%8F.png




## 多子图绘图

Plotly的多子图绘图主要使用了`make_subplots()`函数，从`subplots`模块导入。

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
```

### 子图布局

#### 网格布局
`plotly.subplots`是用于绘制子图的模块，其中的核心函数为`make_subplots()`，用参数`rows`和`cols`确定网格状布局，默认每个格子容纳一张子图，子图用`add_trace()`方法的`row`和`col`参数进行索引定位。

`column_widths`和`row_heights`参数用来控制网格的列宽和行高，值为每列（行）宽度占整个图宽度的百分比组成的列表，列表的长度分别为列数和行数。

子图的标题可以用`subplot_titles`参数设置，值为字符串构成的列表，子图标题按照列表的顺序进行分配，所以如果某个子图的标题暂未确定，也需要用空字符串在列表中占据一个位置。


```python
temp= go.Scatter(x=[1, 2], y=[1, 2])
fig = make_subplots(rows=3, cols=3,
                    column_widths=[0.2, 0.3, 0.5],
                   row_heights=[0.1, 0.6, 0.3],
                   subplot_titles=["trace0", "trace1", "trace2",
                                  "trace3", "", "trace5",
                                  "trace6", "trace7", "trace8"])
for row in range(1,4):
    for col in range(1, 4):
        fig.add_trace(temp, row=row, col=col)
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210425080422.png" alt="截图_20210425080422" style="zoom: 50%;" />

#### 网格复杂布局

`make_subplots()`函数通过`specs`参数进行复杂布局，`specs`为以`rows`和`cols`确定的二维列表，每个子图用一个字典表示，用`colspan`和`rowspan`属性控制子图所占的网格数，`colspan`表示合并列，`rowspan`表示合并行，`None`表示不在该网格上绘图，因为该网格会被占据多个网格的其他子图覆盖。


```python
fig = make_subplots(rows=3, cols=3,
                   specs=[[{"colspan": 2},None,{"rowspan":2}],
                          [{"rowspan":2},{},None],
                          [None,{"colspan": 2},None]],
                   subplot_titles=["trace0", "trace1", "trace2", "trace3", "trace4"])
fig.add_trace(temp, row=1, col=1)
fig.add_trace(temp, row=1, col=3)
fig.add_trace(temp, row=2, col=1)
fig.add_trace(temp, row=2, col=2)
fig.add_trace(temp, row=3, col=2)
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210425080446.png" alt="截图_20210425080446" style="zoom:50%;" />

#### 调整边距

`horizontal_spacing`参数和`vertical_spacing`参数用于调整网格的列间距和行间距，取值为0~1之间的浮点数。

`specs`参数可以调整每个子图的上下左右边距，在每个子图的字典中分别用`t`、`b`、`l`、`r`代表，取值为0-1的浮点数，可以取负值,但无法超出整个图像最外围的网格，如下图中右下角的下边距和右边距不起作用。


```python
fig = make_subplots(rows=3, cols=3,
                    horizontal_spacing=0.05,
                   vertical_spacing=0.1,
                   specs=[[{"l":0.05},{"t":0.1},{"r":0.05}],
                          [{"r":-0.03},{"t":-0.05},{"l":-0.02}],
                          [{},{"b":0.2},{"b":-0.2, "r":-0.2}]])
for row in range(1,4):
    for col in range(1, 4):
        fig.add_trace(temp, row=row, col=col)
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20211525081514.png" alt="截图_20211525081514" style="zoom:50%;" />

#### 贴图式子图

`make_subplots()`函数使用insets属性进行非网格化布局，用于在主图中以贴图的方式增加子图，每个子图用一个字典表示，位置用`l`、`b`、`w`、`h`四个参数调整，用`xaxis`和`yaxis`进行索引，主图为`x1`和`y1`，子图往后类推。


```python
fig = make_subplots(insets=[{'l': 0.7, 'b': 0.5, 'w': 0.2, 'h': 0.3},
                           {'l': 0.4, 'b': 0.6, 'w': 0.2, 'h': 0.3}])
fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,1]))
fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2'))
fig.add_trace(go.Scatter(x=[1,2,3], y=[1,3,2], xaxis='x2', yaxis='y2'))
fig.add_trace(go.Scatter(x=[1,2,3], y=[1,3,2], xaxis='x3', yaxis='y3'))
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/image-20210425202028250.png" alt="image-20210425202028250" style="zoom:50%;" />

#### 通过domain参数布局子图（底层的实现方法）

子图布局的底层实现方法是`layout`中的`domain`参数，创建`fig`画布之后，可以通过`layout`增加第二、第三坐标轴，此时相当于多个子图重合，`domain`参数可以设置每个坐标轴的布局范围，相当于将子图分离开来。

如下图示例，`domain`参数为列表类型，元素为两个0-1的浮点数，表示轴的布局范围，x轴的`domain`为`[0.2,0.6]`就表示x轴占整个画布从左到右的20%到60%宽度。当子图浮动时，需要指定轴的`anchor`，所有坐标轴默认定位在画布的边缘，指定anchor可以使其脱离，附着在指定的子图上。


```python
trace1 = go.Scatter(x=[1, 2], y=[1, 2])
trace2 = go.Scatter(x=[1, 2], y=[1, 2], xaxis="x2", yaxis="y2")
fig = go.Figure(data=[trace1,trace2],
               layout={
                   "xaxis": {"domain": [0, 0.6]},
                   "xaxis2": {"domain": [0.5, 0.8], "anchor": "y2"},
                   "yaxis2": {"domain": [0.4, 0.7], "anchor": "x2"}})
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20212325082334.png" alt="截图_20212325082334" style="zoom:50%;" />

### 子图个性化

#### 设置子图类型

`specs`参数中，代表每个子图的字典不仅可以指定该子图的网格跨度，还可以用`type`指定该子图的类型。子图共有6种类型：

- `xy`：2维笛卡尔图（平面直角坐标系），如散点图、条形图等，`type`属性的默认值。
- `scene`：3维笛卡尔图（三维直角坐标系），如3维散点图、3维矢量图等。
- `polar`：极坐标图，如极坐标散点图、极坐标条形图等。
- `ternary`：三元相图。
- `mapbox`：地图，如散点地图、热力地图等。
- `domain`：其他特殊迹线类型对应的图，如饼图、桑基图等。

除了6种类型之外，`type`的取值也可以为迹线类型，如`bar`、`sacttergeo`、`parcats`等，plotly会自动选择适合的图表类型。


```python
fig = make_subplots(rows=2, cols=2,
                    specs=[[{'type': 'xy'},    {'type': 'polar'}],
                           [{'type': 'scene'}, {'type': 'ternary'}]])
fig.add_traces(
    [go.Scatter(y=[2, 3, 1]),
     go.Scatterpolar(r=[1, 3, 2], theta=[0, 45, 90]),
     go.Scatter3d(x=[1, 2, 1], y=[2, 3, 1], z=[0, 3, 5]),
     go.Scatterternary(a=[0.1, 0.2, 0.1],
                       b=[0.2, 0.3, 0.1],
                       c=[0.7, 0.5, 0.8])],
    rows=[1, 1, 2, 2],
    cols=[1, 2, 1, 2]) 
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210625080606.png" alt="截图_20210625080606" style="zoom:50%;" />

#### 设置子图坐标轴

使用`make_subplots()`创建子图之后，可以使用`fig`的`update_xaxes()`方法和`update_yaxes()`方法来设置子图坐标轴的属性，如设置轴标题、文字颜色、网格线颜色等，用`row`和`col`进行定位，需要设置的属性可以用字典表示（如示例中对`xaxis2`的设置），也可以用方法参数的形式表示（如示例中对`yaxis1`的设置）。


```python
fig = make_subplots(rows=1, cols=2)
fig.add_trace(temp, row=1, col=1)
fig.add_trace(temp, row=1, col=2)
fig.update_layout(height=300, width=800)
fig.update_xaxes({
                "linecolor": "#303030",    #坐标轴颜色
                "color": "#636efa",    #文字颜色
                "gridcolor": "#e0e1e3",    #网格线颜色
                "linewidth": 2,    #坐标轴宽度
                "gridwidth": 3    #网格线宽度
                }, row=1, col=2)
fig.update_yaxes(title="trace0-yaxis-title",    #轴标题 
                showgrid=False,    #不显示网格线
                tickvals=[1, 1.2, 1.8, 2],    #坐标轴刻度取值
                tickangle=-45,    #刻度旋转角度
                ticksuffix="cm",  #刻度值后缀
                col=1, row=1)
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210625080620.png" alt="截图_20210625080620" style="zoom: 67%;" />

#### 设置子图迹线

`add_traces()`方法可以同时在多个子图中添加迹线，使用`rows`属性和`cols`属性选择子图，如`rows=[1,2]，cols=[2,1]`代表选择了`(1,2)`和`(2,1)`的两个子图。`data`、`rows`和`cols`取值的列表长度应该相等。

使用`update_traces()`可以更新子图的迹线属性，如`marker`、`label`等，可以用`row`和`col`来选择要设置的子图，还可以用`selector`参数来选择要更新的迹线类型。


```python
fig = make_subplots(rows=2, cols=2)
trace1 = go.Scatter(y=[2, 3, 1])
trace2 = go.Bar(y=[1, 4, 3])
trace3 = go.Scatter(y=[4, 2, 3])
fig.add_traces([trace1, trace2, trace3, trace2, trace3, trace3], 
               rows=[1, 2, 1, 2, 1, 2], 
               cols=[1, 2, 1, 1, 2, 1])
fig.update_traces(col=1,selector={"type": "scatter"},
                 marker=dict(color="RoyalBlue"))   #将第一列子图中的折线图设置为蓝色
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210625080636.png" alt="截图_20210625080636" style="zoom:50%;" />

#### 其他子图设置

针对单个子图的设置可以使用`fig`的`add_XXX()`系列方法，如设置注释`add_annotation()`、绘制垂直线`add_vline()`等，使用`row`和`col`参数来选择需要绘制的子图。


```python
fig = make_subplots(rows=1, cols=2)
fig.add_trace(temp, row=1, col=1)
fig.add_trace(temp, row=1, col=2)
fig.update_layout(height=300, width=800)
fig.add_annotation(row=1, col=2, text="annotation",x=2,y=1.5)    #设置注释
fig.add_vline(row=1, col=1, x=1.8, annotation_text="vertical-line")    #画一条垂直的线
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210625080651.png" alt="截图_20210625080651" style="zoom:67%;" />

### 子图共用元素

#### 共用坐标轴

`make_subplots()`函数的`share_xaxes`参数和`share_yaxes`参数可以设置子图之间是否共用坐标轴，默认为`False`，`share_xaxes`设置为`True`时，同一列的子图会共用一个横坐标轴，`share_yaxes`设置为`True`时，同一行的子图会共用一个纵坐标轴。


```python
fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.02)
fig.add_trace(go.Scatter(x=[0, 1, 2], y=[10, 11, 12]), row=3, col=1)
fig.add_trace(go.Scatter(x=[2, 3, 4], y=[100, 110, 120]), row=2, col=1)
fig.add_trace(go.Scatter(x=[3, 4, 5], y=[1000, 1100, 1200]), row=1, col=1)
fig.update_layout(height=600, width=800, title_text="Stacked Subplots with Shared X-Axes")
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210725080707.png" alt="截图_20210725080707" style="zoom:50%;" />


```python
np.random.seed(0)
y = np.random.randn(100).cumsum()
fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0.01)
fig.update_layout(height=400, width=800, title_text="Stacked Subplots with Shared Y-Axes")
fig.add_traces([go.Scatter(y=y), go.Bar(y=y)], 
               rows=[1, 1], cols=[1, 2])
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210725080719.png" alt="截图_20210725080719" style="zoom:67%;" />

`share_xaxes`和`share_yaxes`只能实现网格中全部子图的坐标轴共用，如果想要设置某两个子图共用坐标轴而其他子图拥有单独的坐标轴，则需要用到底层的布局实现方法。坐标轴共享通过`trace`的`xaxis`和`yaxis`参数实现，同时在`fig`的`layout`中只设置显示的坐标轴，完整的坐标轴用`anchor`属性来互相定位。如下示例，前两个子图共用y轴，故`trace2`的`yaxis`设置为`y`，`layout`中不设置`yaxis2`，结果如下所示。


```python
trace1 = go.Scatter(y=[2, 4, 1])
trace2 = go.Scatter(y=[1, 3, 5], xaxis="x2", yaxis="y")
trace3 = go.Scatter(y=[2, 1, 3], xaxis="x3", yaxis="y3")
layout = go.Layout({
    'xaxis': {'domain': [0, 0.3]},
    'xaxis2': {'domain': [0.31, 0.65]},
    'xaxis3': {'anchor': 'y3', 'domain': [0.7, 1]},
    'yaxis': {'domain': [0, 1]},
    'yaxis3': {'anchor': 'x3', 'domain': [0, 1]}
})
fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
fig.update_layout(height=300)
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210725080736.png" alt="截图_20210725080736" style="zoom:67%;" />

#### 共用配色方案

绘制每条迹线时可以用`marker`的`colorscale`属性来指定plotly内置的渐变式配色方案，如

````python
go.Bar(y=[2,3,1], marker=dict(color=[2,3,1],colorscale="Bluered_r"))
````

如果子图要共用一套配色方案的话，需要用到`coloraxis`，在子图迹线的`marker`中加入这个参数，再在`fig`的`layout`中设置`coloraxis`，即可实现子图共用配色。


```python
N = 50
np.random.seed(1)
x1 = np.random.rand(N)
y1 = np.random.rand(N)
np.random.seed(2)
x2 = np.random.rand(N)
y2 = np.random.rand(N)
colors = np.random.rand(N)
size = np.random.rand(N) * 30
fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0.03)
fig.add_trace(go.Scatter(x=x1, y=y1, mode="markers",
                        marker=dict(size=size, color=colors, opacity=0.6, coloraxis="coloraxis")),
             row=1, col=1)
fig.add_trace(go.Bar(y=y2,
                        marker=dict(color=colors, opacity=0.6, coloraxis="coloraxis")),
             row=1, col=2)
fig.update_layout(coloraxis=dict(colorscale='Viridis'), showlegend=False)
fig.update_yaxes(row=1, col=1, range=[0,1.1])
fig.show()
```

<img src="http://pic.fishiu.com/uPic/ckq/%E6%88%AA%E5%9B%BE_20210725080750.png" alt="截图_20210725080750" style="zoom:50%;" />