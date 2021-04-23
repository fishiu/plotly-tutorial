# 基于Python3 的 Plotly 绘图教程

> 数据可视化课程小组：金笑缘 陈科锜 李昱勇 唐陆禛
> 
> 本教程已使用Docsify部署于网页，可访问。

本教程将分为四个部分：
- Plotly 安装指南
- Plotly API 入门
- Plotly 使用进阶
- Plotly 图表案例

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

