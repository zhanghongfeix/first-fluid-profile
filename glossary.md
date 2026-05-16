# 术语表

流体力学常用专业术语中英对照。

## 基础概念

| 英文 | 中文 | 说明 |
|------|------|------|
| Fluid Mechanics | 流体力学 | 研究流体运动规律的学科 |
| Viscosity | 粘度 | 流体抵抗剪切变形的能力 |
| Density | 密度 | 单位体积的质量 |
| Pressure | 压力/压强 | 单位面积上的法向力 |
| Shear Stress | 剪应力 | 单位面积上的切向力 |
| Boundary Layer | 边界层 | 壁面附近粘性主导的薄层 |
| Inviscid Flow | 无粘流动 | 忽略粘性的理想化模型 |
| Laminar Flow | 层流 | 各层流体规则平行流动 |
| Turbulence | 湍流 | 不规则、含多尺度涡的混沌流动 |

## 流动参数

| 英文 | 中文 | 公式 / 说明 |
|------|------|-------------|
| Reynolds Number | 雷诺数 | $Re = \rho U L / \mu$ |
| Mach Number | 马赫数 | $Ma = U / c$ |
| Froude Number | 弗劳德数 | $Fr = U / \sqrt{gL}$ |
| Prandtl Number | 普朗特数 | $Pr = \nu / \alpha$ |
| Nusselt Number | 努塞尔数 | $Nu = hL / k$ |
| Strouhal Number | 斯特劳哈尔数 | $St = fL / U$，涡脱落频率 |
| Weber Number | 韦伯数 | $We = \rho U^2 L / \sigma$ |
| Knudsen Number | 克努森数 | $Kn = \lambda / L$ |
| Cavitation Number | 空化数 | $\sigma = (p - p_v)/(0.5\rho U^2)$ |
| Drag Coefficient | 阻力系数 | $C_d = F_d / (0.5 \rho U^2 A)$ |
| Lift Coefficient | 升力系数 | $C_l = F_l / (0.5 \rho U^2 A)$ |

## 涡与流动结构

| 英文 | 中文 | 说明 |
|------|------|------|
| Vorticity | 涡量 | $\omega = \nabla \times \mathbf{u}$ |
| Circulation | 环量 | $\Gamma = \oint \mathbf{u} \cdot d\mathbf{l}$ |
| Vortex Street | 涡街 | 交替脱落的涡列（如卡门涡街） |
| Horseshoe Vortex | 马蹄涡 | 障碍物根部绕流形成的 U 形涡 |
| Hairpin Vortex | 发卡涡 | 边界层湍流中的 Ω 形涡 |
| Vortex Shedding | 涡脱落 | 周期性产生并释放涡 |
| Eddy | 旋涡/涡团 | 泛指各种尺度的涡 |
| Wake | 尾流/尾迹 | 物体后的低动量区 |
| Jet | 射流 | 从喷口高速喷出的流体束 |
| Plume | 浮力羽流 | 由浮力驱动的上升流（如烟囱） |

## CFD 术语

| 英文 | 中文 | 说明 |
|------|------|------|
| Mesh / Grid | 网格 | 计算域的空间离散 |
| Cell / Element | 单元 | 网格的基本单位 |
| Node | 节点 | 网格线的交点 |
| Discretization | 离散化 | 将 PDE 转为代数方程 |
| Courant Number (CFL) | 库朗数 | $CFL = U\Delta t / \Delta x$ |
| Residual | 残差 | 离散方程不满足的误差 |
| Convergence | 收敛 | 解趋于稳定的过程 |
| Wall Function | 壁面函数 | 近壁湍流的简化建模 |
| Solvers | 求解器 | 求解代数方程组的算法 |
| SIMPLE | — | Semi-Implicit Method for Pressure-Linked Equations |
| PISO | — | Pressure-Implicit with Splitting of Operators |
| DNS | 直接数值模拟 | 解析所有湍流尺度 |
| LES | 大涡模拟 | 解析大尺度，建模小尺度 |
| RANS | 雷诺平均 | 全湍流建模 |

## 可压缩流

| 英文 | 中文 | 说明 |
|------|------|------|
| Shock Wave | 激波 | 超音速流动中压力和密度的突变面 |
| Expansion Wave | 膨胀波 | 流动加速并降压的扇形波系 |
| Sonic Line | 声速线 | Ma = 1 的等值线 |
| Subsonic / Supersonic / Hypersonic | 亚/超/高超声速 | 按马赫数划分的速度区间 |
| Stagnation Point | 驻点 | 速度为 0 的点 |
| Total / Stagnation Temperature | 总温 | 理想绝热减速到 0 的温度 |

## 无量纲数

| 英文 | 中文 | 物理意义 |
|------|------|----------|
| Reynolds | 雷诺数 | 惯性力 / 粘性力 |
| Mach | 马赫数 | 流速 / 声速 |
| Froude | 弗劳德数 | 惯性力 / 重力 |
| Prandtl | 普朗特数 | 动量扩散 / 热扩散 |
| Nusselt | 努塞尔数 | 对流 / 导热 |
| Strouhal | 斯特劳哈尔数 | 非定常惯性力 / 对流传热 |
| Weber | 韦伯数 | 惯性力 / 表面张力 |
| Rayleigh | 瑞利数 | 浮力驱动稳定性 |
| Rossby | 罗斯贝数 | 惯性力 / 科里奥利力（地球旋转） |
