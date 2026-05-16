# Navier-Stokes 方程

流体运动的核心控制方程。

## 控制方程组

### 连续性方程（质量守恒）

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0$$

对于不可压缩流动：

$$\nabla \cdot \mathbf{u} = 0$$

### 动量方程（Navier-Stokes）

$$\rho\left(\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p + \mu\nabla^2\mathbf{u} + \mathbf{f}$$

其中：
- $\rho$：密度
- $\mathbf{u}$：速度矢量
- $p$：压力
- $\mu$：动力粘度
- $\mathbf{f}$：体积力（如重力）

### 能量方程

$$\rho c_p\left(\frac{\partial T}{\partial t} + \mathbf{u}\cdot\nabla T\right) = k\nabla^2 T + \Phi + \dot{q}$$

## 物理意义

$$\underbrace{\rho\frac{D\mathbf{u}}{Dt}}_{\text{惯性力}} = \underbrace{-\nabla p}_{\text{压力梯度}} + \underbrace{\mu\nabla^2\mathbf{u}}_{\text{粘性力}} + \underbrace{\mathbf{f}}_{\text{体积力}}$$

## 关键无量纲数

| 无量纲数 | 公式 | 物理意义 |
|----------|------|----------|
| 雷诺数 $Re$ | $\frac{\rho U L}{\mu}$ | 惯性力 / 粘性力 |
| 马赫数 $Ma$ | $\frac{U}{c}$ | 流速 / 声速 |
| 弗劳德数 $Fr$ | $\frac{U}{\sqrt{gL}}$ | 惯性力 / 重力 |
| 普朗特数 $Pr$ | $\frac{\nu}{\alpha}$ | 动量扩散 / 热扩散 |

## 数学性质

NS方程是非线性偏微分方程，**千禧年七大数学难题之一**——证明三维NS方程解的存在性与光滑性仍未解决。
