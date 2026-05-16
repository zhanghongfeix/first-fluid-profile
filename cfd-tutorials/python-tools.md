# Python CFD 工具链

Python 生态系统中有丰富的 CFD 相关工具。

## 基础数值库

```python
import numpy as np          # 数组计算
from scipy import sparse    # 稀疏矩阵（CFD 矩阵求解器之间）
from scipy import integrate # 数值积分
from scipy import optimize  # 优化
```

## 网格处理

| 库 | 用途 |
|----|------|
| `meshio` | 读写各种网格格式（.msh, .vtk, .su2 等） |
| `pygmsh` | 调用 Gmsh 生成网格 |
| `pyDistMesh` | 简单二维网格生成 |

```python
import meshio
mesh = meshio.read("airfoil.msh")
print(f"点数: {mesh.points.shape[0]}")
print(f"单元数: {sum(len(c[1]) for c in mesh.cells)}")
```

## 教学级求解器

| 库 | 特点 |
|----|------|
| `FluidSim` | 简单易懂的教学代码 |
| `pyhpfem` | 有限元 CFD |
| `pyLBM` | 格子玻尔兹曼方法 |

## 后处理与可视化

```python
import matplotlib.pyplot as plt
import numpy as np

# 涡量图
u, v = ...  # 速度场
vorticity = np.gradient(v, axis=0) - np.gradient(u, axis=1)
plt.contourf(vorticity, levels=50, cmap='RdBu_r')
```

| 库 | 用途 |
|----|------|
| `matplotlib` | 基础二维图 |
| `plotly` | 交互式三维图 |
| `pyvista` | VTK 绑定，三维可视化 |
| `vedo` | 更简洁的三维可视化 API |

## 机器学习 + CFD

```python
# PINNs (Physics-Informed Neural Networks)
import deepxde as dde

# 替代模型
import torch
import jax
```

| 库 | 用途 |
|----|------|
| `DeepXDE` | PINNs 框架 |
| `Modulus` (NVIDIA) | 工业级物理 ML |
| `SimNet` (NVIDIA) | Modulus 前身 |

## 数据获取

```python
import arxiv

# 搜索 CFD 相关论文
search = arxiv.Search(
    query="computational fluid dynamics",
    max_results=10,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

for paper in search.results():
    print(f"{paper.title} — {paper.published.date()}")
```
