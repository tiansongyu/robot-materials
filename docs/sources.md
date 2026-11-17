# 资料来源与进阶阅读

核对日期：2026-11-16。正文链接优先指向原始机构或材料制造商。网页更新时间不等于材料数据表版本；采购时应保存实际采用的文件版本。制造商典型值不能自动当作交货保证值。

## 基础力学

- [MIT 3.11 课程目标](https://web.mit.edu/3.11/www/abet.html)：应力、应变、扭转、弯曲与组合载荷的学习范围。
- [MIT 梁弯曲讲义 Lecture 13](https://web.mit.edu/course/3/3.11/www/Lectures/Lecture13.pdf)：截面、弯曲与圆轴扭转模型。本站推导与数值例题为独立教学编写。
- [SSAB 结构刚度问答](https://www.ssab.com/en/support/how-to-design/general-design/structural-stiffness/20-questions)：钢的弹性模量与结构刚度关系。

## 金属材料与加工

- [Hydro 挤压合金目录](https://www.hydro.com/en/global/aluminium/products/extruded-profiles/alloys-for-extruded-profiles/)：牌号初筛，具体性能应进入相应产品数据表。
- [Hydro 6061 数据表](https://www.hydro.com/globalassets/01-products--services/extruded-profiles/americas/ena-resources/alloy-data-sheets/hydro_2019_data_sheet_6061.pdf)：状态与挤压产品信息，2019 文件。
- [Hydro 6082 数据表](https://www.hydro.com/globalassets/08-about-hydro/hydro-worldwide/germany/extrusion-germany/alloy-data-sheets/hydro-en-aw-6082.pdf)：Rev.2，01/2019；本站铝弹性计算的典型参数来源。
- [Luxfer 挤压镁合金](https://www.luxfermeltechnologies.com/extruded-magnesium-alloys/)：变形镁合金的产品路线。
- [Luxfer 镁加工指南](https://www.luxfermeltechnologies.com/knowledge-hub/machined-magnesium-guide/)：加工、切屑与火灾处置注意事项。
- [DGUV 镁作业指南](https://publikationen.dguv.de/widgets/pdf/download/article/3784)：镁作业的系统性风险控制参考，不作为家庭加工教程。
- [Outokumpu 不锈钢手册入口](https://www.outokumpu.com/en/expertise/2021/handbook-of-stainless-steel)：组织、产品、性能和制造进一步阅读。
- [Outokumpu 大气腐蚀说明](https://www.outokumpu.com/en/expertise/2025/stainless-steel-and-atmospheric-corrosion-what-you-need-to-know)：环境、表面和不锈钢选择。
- [Outokumpu 腐蚀表使用说明](https://www.outokumpu.com/en/products/corrosion-tables)：实验条件与实际介质的差别。

## 聚合物与复合材料

- [Prusa 材料指南](https://help.prusa3d.com/filament-material-guide)：打印材料与设备条件初筛。
- [Prusa PLA](https://help.prusa3d.com/article/pla_2062)、[PETG](https://help.prusa3d.com/article/petg_2059)、[ASA](https://help.prusa3d.com/article/asa_1809)：相应材料的打印使用说明。
- [Prusament PLA TDS](https://prusament.com/wp-content/uploads/2022/10/PLA_Prusament_TDS_2021_10_EN.pdf)：学习如何识别具体产品与测试条件；不能推广到所有 PLA。
- [Ensinger POM](https://www.ensingerplastics.com/en/thermoplastic-materials/pom)：机加工聚甲醛的材料特点。
- [Ensinger 工程塑料手册](https://www.ensingerplastics.com/en-us/-/media/ensinger/files/document-teaser-files/brochures/shapes/engineering-plastics-manual-english.ashx)：湿度、温度、尺寸与性能的进一步阅读。
- [Toray 尼龙加工前说明](https://www.plastics.toray/technical/amilan/tec_007.html)：干燥、吸湿及加工前条件。
- [Hexcel 预浸料技术手册](https://www.hexcel.com/wp-content/uploads/2026/01/Prepreg_Technology.pdf)：纤维、基体、方向与层合结构。
- [Momentive TPG](https://www.momentivetech.com/materials/ceramic-materials/thermal-pyrolytic-graphite-tpg)：确认 TPG 在热管理材料中的含义。

## 连接与专业深入

- [NASA RP-1228：Fastener Design Manual](https://ntrs.nasa.gov/api/citations/19900009424/downloads/19900009424.pdf)，1990：连接基础与计算参考。历史手册不等同于项目当前强制标准。

继续深入可按课题阅读：材料科学与工程教材中的晶体缺陷、相图、相变与聚合物章节；机械设计教材中的疲劳、轴、齿轮与连接章节；材料选择教材中的约束与材料指数。若使用 ASM Handbook 等数据库，应注明卷册、章节、产品状态和获取权限，不以未经核对的二手表格替代原始数据。

## 下一步可以深入的专题

| 专题 | 需要的前置知识 | 最终要回答的问题 |
|---|---|---|
| 疲劳与断裂力学 | 应力、缺口、载荷谱 | 连杆在重复动作中能工作多久？ |
| 摩擦学与齿轮材料 | 接触、润滑、热 | 为什么齿轮没断却已经失效？ |
| 热管理与热膨胀 | 热传导、界面、装配 | 电机热量怎样影响精度与寿命？ |
| 有限元与试验相关 | 梁理论、边界条件 | 模型与实物差异来自哪里？ |
| 聚合物粘弹性 | 时间、温度、应力应变 | 塑料结构怎样保持长期精度？ |
| 复合材料层合理论 | 各向异性与力学 | 铺层和端接怎样共同传力？ |

## 内容边界与维护

本站覆盖机器人制造的材料基础与工程入门方法，不是材料数据库，也不是经过第三方审定的产品设计规范。尚无特定机器人的实测数据；案例与实验中已区分教学假设和公开典型值。新证据应连同批次、工艺、环境和适用范围加入，不能把单件测试扩写成材料族的普遍结论。

## 电机与减速器结构

[图解专题](drives.md)及其三个分页面在相关段落列出 Oriental Motor、Neugart、Harmonic Drive、Sumitomo 和 Nabtesco 的官方来源。图示为本站依据典型机构绘制的教学模型，不是厂商 CAD 或实物拆解记录。资料核对日期：2026-11-16。
