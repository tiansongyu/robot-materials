---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

# 可执行实验：质量与刚度一起算

本页 Python 在构建网站时执行并生成结果。网页展示结果，不提供在线 Python 执行器；修改源码后重新构建即可重算。

## 模型、单位与数据身份

比较长 200 mm、宽 20 mm、高 4 mm 的实心矩形悬臂梁，末端横向力 10 N。假设理想固定、均质线弹性、小挠度，忽略自重、孔、接头、剪切变形与制造缺陷。单位使用 N、mm、MPa。

| 模型名称 | E / GPa | 密度 / g·cm⁻³ | 数据身份 |
|---|---:|---:|---|
| 铝参考模型 | 70 | 2.71 | Hydro 6082 室温典型值，仅用于弹性估算 |
| 钢教学模型 | 210 | 7.85 | 通用教学近似，不指定牌号或交货保证 |
| 镁教学模型 | 45 | 1.80 | 教学假设，不代表任何具体 AZ 牌号 |
| 塑料教学模型 | 3 | 1.24 | 人为设定，不能视为 PLA 打印件数据 |

铝参考来源：[Hydro 6082 数据表](https://www.hydro.com/globalassets/08-about-hydro/hydro-worldwide/germany/extrusion-germany/alloy-data-sheets/hydro-en-aw-6082.pdf)。钢模量数量级可对照 [SSAB](https://www.ssab.com/en/support/how-to-design/general-design/structural-stiffness/20-questions)。

## 相同几何下的比较

```{code-cell} ipython3
from math import isclose
from IPython.display import display, Markdown
L, b, h, F = 200.0, 20.0, 4.0, 10.0
materials = [
    ("铝参考", 70000.0, 2.71),
    ("钢教学", 210000.0, 7.85),
    ("镁教学", 45000.0, 1.80),
    ("塑料教学", 3000.0, 1.24),
]
def beam(E, rho, height):
    I = b * height**3 / 12
    mass = rho * (L * b * height) / 1000  # mm³ 转换为 cm³
    delta = F * L**3 / (3 * E * I)
    stress = F * L * (height / 2) / I
    return mass, delta, stress
rows = ["| 模型 | 质量 / g | 挠度 / mm | 名义应力 / MPa |",
        "|---|---:|---:|---:|"]
for name, E, rho in materials:
    mass, delta, stress = beam(E, rho, h)
    rows.append(f"| {name} | {mass:.2f} | {delta:.3f} | {stress:.2f} |")
display(Markdown("\n".join(rows)))
assert isclose(beam(70000, 2.71, 4)[1], 25/7)
assert isclose(beam(70000, 2.71, 4)[2], 37.5)
```

同几何下，名义弯曲应力相同，因为该静定梁的应力由载荷与截面决定；挠度则随模量变化。并不意味着各材料的失效裕量相同，因为允许应力和失效模式不同。

塑料教学模型给出的挠度约为长度的 42%，已经违背小挠度假设。这个结果只能说明“该线性模型下明显不够刚，需要改设计并换模型”，不能把数值当作可信的大变形预测。薄弱的材料与不合适的模型都需要被识别。

## 改几何后再比较

```{code-cell} ipython3
m4, d4, s4 = beam(70000, 2.71, 4)
m8, d8, s8 = beam(70000, 2.71, 8)
print(f"铝参考模型，高度 4 mm：{m4:.2f} g，{d4:.3f} mm，{s4:.3f} MPa")
print(f"铝参考模型，高度 8 mm：{m8:.2f} g，{d8:.3f} mm，{s8:.3f} MPa")
assert isclose(m8/m4, 2)
assert isclose(d4/d8, 8)
assert isclose(s4/s8, 4)
```

高度翻倍让质量翻倍、挠度降为八分之一、名义应力降为四分之一。实际可以进一步比较空心截面，但必须校核壁厚、局部屈曲与接口。

## 固定挠度、宽度和长度时的材料指数

若高度可自由改变，且只受挠度限制，从 $\delta=4FL^3/(Ebh^3)$ 可得：

$$h=\left(\frac{4FL^3}{Eb\delta}\right)^{1/3},\qquad m\propto\frac{\rho}{E^{1/3}}$$

这个问题下比较的是 $E^{1/3}/\rho$，不是简单的 $E/\rho$。如果截面按比例缩放，或改成拉杆、板、屈曲约束，指数会改变。

```{code-cell} ipython3
target_delta = 0.5
rows = ["| 模型 | 理论高度 / mm | 质量 / g | 复算挠度 / mm |",
        "|---|---:|---:|---:|"]
for name, E, rho in materials:
    height = (4 * F * L**3 / (E * b * target_delta))**(1/3)
    mass, delta, stress = beam(E, rho, height)
    assert isclose(delta, target_delta)
    rows.append(f"| {name} | {height:.2f} | {mass:.2f} | {delta:.3f} |")
display(Markdown("\n".join(rows)))
```

结果只满足理想弹性挠度条件；没有核验材料强度、几何空间、剪切变形、打印方向、蠕变或连接。塑料所需截面变厚后，细长梁假设也更值得复查。

## 温度导致的装配差异

假设两件长 100 mm 的构件，一个线膨胀系数为 $23\times10^{-6}$/K，另一个为 $12\times10^{-6}$/K，均匀升温 40 K：

```{code-cell} ipython3
alpha_a, alpha_b = 23e-6, 12e-6
length, rise = 100.0, 40.0
difference = (alpha_a - alpha_b) * length * rise
print(f"自由伸长差：{difference:.3f} mm")
assert isclose(difference, 0.044)
```

这里的系数是教学假设，不是两份指定采购规格。若两件被完全约束，不能再把这 0.044 mm 当作自由位移，需要计算约束产生的力与应力。

## 继续实验

把梁长改为 150 mm，预测挠度应乘以 $(150/200)^3$，再运行检查。然后增加一个连接柔度项，观察为什么只优化材料仍可能无法改善整机精度。
