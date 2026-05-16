# OpenFOAM 入门

最流行的开源 CFD 工具箱。

## 什么是 OpenFOAM？

- 基于**有限体积法**的 C++ 库
- 支持不可压/可压、多相、燃烧、颗粒流等几乎所有流动类型
- 前后处理、求解器、并行计算一体化

## 安装

```bash
# Windows (WSL2 中)
sudo apt install openfoam11-default

# macOS
brew install openfoam
```

## 典型工作流

```
前处理              求解                后处理
  │                  │                   │
blockMesh      →   simpleFoam   →   paraFoam
snappyHexMesh       pimpleFoam       paraview
```

## 目录结构

```text
案例目录/
├── 0/              初始条件和边界条件
│   ├── U           速度
│   └── p           压力
├── constant/       物理参数
│   ├── transportProperties
│   └── turbulenceProperties
├── system/         求解设置
│   ├── controlDict     时间、输出控制
│   ├── fvSchemes       离散格式
│   └── fvSolution      求解器设置
```

## 常用求解器

| 求解器 | 用途 |
|--------|------|
| `simpleFoam` | 不可压稳态（SIMPLE 算法） |
| `pimpleFoam` | 不可压瞬态（PIMPLE 算法） |
| `rhoSimpleFoam` | 可压缩稳态 |
| `interFoam` | 两相不可压（VOF 方法） |
| `reactingFoam` | 化学反应流 |

## 推荐学习资源

- [OpenFOAM User Guide](https://www.openfoam.com/documentation/user-guide/)
- [Wolf Dynamics Tutorials](http://www.wolfdynamics.com/tutorials.html)
- J. Józsa 的 YouTube 教程系列
