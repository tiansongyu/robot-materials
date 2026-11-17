"""Regenerate editable teaching SVGs; silhouettes are not manufacturing profiles."""
from pathlib import Path
from math import sin, cos, pi
from html import escape
OUT = Path(__file__).resolve().parents[1] / 'docs/_static/drives'
INK='#203347'; FIX='#65788a'; INPUT='#c46a13'; MID='#3575ad'; OUTPUT='#187b68'; BG='#f5f8fb'
def text(x,y,s,size=18,color=INK):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{escape(s)}</text>'
def circle(x,y,r,fill,stroke=INK,width=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
def line(x,y,a,b,color=FIX,dash=''):
    return f'<path d="M{x},{y} L{a},{b}" fill="none" stroke="{color}" stroke-width="2" {dash}/>'
def gear(x,y,r,n,fill,inner=False):
    pts=[]
    for k in range(n*4):
        a=2*pi*k/(n*4); rr=r+(3 if k%4 in (1,2) else -3)
        pts.append(f'{x+rr*cos(a):.2f},{y+rr*sin(a):.2f}')
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
def ring(x,y,r):
    return circle(x,y,r+18,'#dce4eb')+gear(x,y,r,48,'white')
def label(y,title,desc,col):
    return circle(535,y-6,6,col,col)+text(555,y,title,20,col)+text(555,y+30,desc,16)
def save(name,title,body,footer='教学概念图 · 非等比例 · 齿形简化 · 不作为加工或装配依据',h=570):
    OUT.mkdir(exist_ok=True,parents=True)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(footer)}</desc><rect width="1000" height="{h}" rx="12" fill="{BG}"/><g font-family="Noto Sans CJK SC,Microsoft YaHei,sans-serif">{text(32,45,title,26)}{body}{text(32,h-22,footer,15,FIX)}</g></svg>'''
    (OUT/f'{name}.svg').write_text(svg)
# Assembled planetary: pitch radii 48 / 48 / 144.
cx,cy=260,285
s=ring(cx,cy,144)
for a in (-pi/2,pi/6,5*pi/6):
    x,y=cx+96*cos(a),cy+96*sin(a)
    s+=line(cx,cy,x,y,OUTPUT)+gear(x,y,48,18,'#b7d7ee')+circle(x,y,8,OUTPUT)
s+=gear(cx,cy,48,18,'#f3c88e')+circle(cx,cy,13,'white')
s+=label(130,'① 太阳轮｜输入','电机轴驱动中心齿轮',INPUT)+label(215,'② 行星轮｜自转 + 公转','同时啮合太阳轮和内齿圈',MID)+label(300,'③ 内齿圈｜固定','与壳体连接，提供反力矩',FIX)+label(385,'④ 行星架｜输出','连接各行星轮的轴销',OUTPUT)
s+=text(95,490,'本图：内齿圈固定，太阳轮输入',17)
save('planetary-section','01 / 行星减速器：端面结构',s)
# Harmonic end view, deliberately conceptual tooth envelope.
s=ring(cx,cy,144)
s+=f'<ellipse cx="{cx}" cy="{cy}" rx="139" ry="108" fill="#d8e8f6" stroke="{MID}" stroke-width="8"/>'
s+=f'<ellipse cx="{cx}" cy="{cy}" rx="129" ry="98" fill="#f3c88e" stroke="{INPUT}" stroke-width="6"/>'+circle(cx,cy,16,'white')
for x in (cx-142,cx+142): s+=circle(x,cy,12,'#b44255')
s+=label(135,'① 波发生器｜输入','椭圆凸轮 + 柔性轴承',INPUT)+label(225,'② 柔轮｜输出','薄壁杯口随波发生器变形',MID)+label(315,'③ 刚轮｜固定','内齿圈包围柔轮齿部',FIX)+label(405,'④ 两个主要啮合区','位于椭圆长轴两端', '#b44255')
s+=text(70,490,'柔轮材料缓慢转动；变形方向随输入转动',16)
save('harmonic-section','02 / 谐波减速器：双波杯形结构',s, '教学概念图 · 省略单齿细节 · 椭圆变形夸大 · 圆点表示啮合区域')
# Cycloidal: schematic lobes, center offset and output holes.
s=circle(cx,cy,167,'#dce4eb')+circle(cx,cy,150,'white')
for k in range(12):
    a=2*pi*k/12;s+=circle(cx+140*cos(a),cy+140*sin(a),10,'#8797a5')
pts=[]
for k in range(440):
    a=2*pi*k/440;r=116+9*cos(11*a);pts.append(f'{cx+10+r*cos(a):.2f},{cy+r*sin(a):.2f}')
s+=f'<polygon points="{" ".join(pts)}" fill="#c9e1f3" stroke="{MID}" stroke-width="3"/>'
for k in range(6):
    a=2*pi*k/6;x,y=cx+72*cos(a),cy+72*sin(a)
    s+=circle(x+10,y,18,'white')+circle(x,y,8,OUTPUT)
s+=circle(cx+10,cy,30,'#f3c88e')+circle(cx,cy,5,INK)+circle(cx+10,cy,4,INPUT)
s+=line(cx,cy-38,cx+10,cy-38,INPUT)+text(cx-10,cy-48,'e',19,INPUT)+text(cx-18,cy+23,'O',14)+text(cx+14,cy+23,'C',14,INPUT)
s+=label(130,'① 偏心轴 / 轴承｜输入','盘心 C 围绕主轴心 O 运动',INPUT)+label(215,'② 摆线盘｜复合运动','绕 O 公转，同时慢速反向自转',MID)+label(300,'③ 针齿圈｜固定','外圈针齿约束摆线盘',FIX)+label(385,'④ 输出销｜定轴输出','大孔容许偏心，销提取慢速转动',OUTPUT)
s+=text(80,490,'12 根针齿 / 11 个波瓣：仅示意数量关系',16)
save('cycloidal-section','03 / 摆线针轮减速器：单盘原理',s,'教学概念图 · 波瓣非共轭齿形 · 偏心与孔隙夸大 · 不能用于碰撞仿真')
# Exploded views: axial separation plus oblique front faces.
def face(x,body): return f'<g transform="translate({x},270) matrix(.55,-.18,0,1,0,0)">{body}</g>'
def disc(r,col,hole=15): return circle(0,0,r,col)+circle(0,0,hole,BG)
def shaft(x1,x2,y,col):
    return f'<path d="M{x1},{y-9} H{x2} V{y+9} H{x1} Z" fill="{col}" stroke="{INK}" stroke-width="2"/>'
def explode(name,title,parts,notes):
    s=line(45,270,940,270,FIX,'stroke-dasharray="7 7"')
    for x,shape,caption,detail in parts:
        s+=shape+line(x,380,x,415)+text(x-63,445,caption,18)+text(x-63,472,detail,14,FIX)
    s+=text(35,90,notes,17)
    save(name,title,s,'轴向分离的概念爆炸图 · 虚线为装配轴线 · 省略紧固件、密封和部分支承')
planet= ''.join(gear(94*cos(a),94*sin(a),46,18,'#b7d7ee')+circle(94*cos(a),94*sin(a),9,'white') for a in (-pi/2,pi/6,5*pi/6))
carrier=disc(125,'#b8dfd5')
for a in (-pi/2,pi/6,5*pi/6): carrier+=circle(94*cos(a),94*sin(a),9,OUTPUT)
explode('planetary-exploded','01 / 行星减速器：轴向分解',[(115,shaft(45,140,270,'#efbd7f')+face(115,gear(0,0,46,18,'#f3c88e')),'① 太阳轮','与输入轴连接'),(335,face(335,planet),'② 三个行星轮','装在行星架轴销上'),(565,face(565,ring(0,0,144)),'③ 固定内齿圈','组装后包住齿轮组'),(805,shaft(805,945,270,'#73b3a5')+face(805,carrier),'④ 行星架','轴销 / 输出轴')],'阅读：① 与 ② 在同一啮合平面；③ 从径向包围它们；④ 支承 ②。')
# Cup shown with front opening on left and closed diaphragm at right.
cup='<path d="M480,155 L610,182 L610,358 L480,385 Z" fill="#bbd9ef" stroke="#3575ad" stroke-width="2"/>'
cup+=face(610,disc(88,'#a4cbe6',20))+face(480,circle(0,0,115,'#92bedf')+circle(0,0,104,BG))
wg=face(140,'<ellipse rx="90" ry="65" fill="#f3c88e" stroke="#c46a13" stroke-width="10"/>'+circle(0,0,15,'white'))
explode('harmonic-exploded','02 / 谐波减速器：杯形柔轮分解',[(140,shaft(45,145,270,'#efbd7f')+wg,'① 波发生器','插入柔轮杯口'),(330,face(330,ring(0,0,125)),'② 刚轮','包围柔轮外齿'),(545,cup,'③ 杯形柔轮','杯口齿部 → 杯底'),(835,shaft(835,940,270,'#73b3a5')+face(835,disc(95,'#b8dfd5')),'④ 输出法兰','连接柔轮杯底')],'① 椭圆柔性轴承撑开 ③ 的杯口；② 固定在壳体；输出从杯底引出。')
cyc=gear(0,0,105,11,'#c9e1f3')
for k in range(6):
    a=k*pi/3;cyc+=circle(65*cos(a),65*sin(a),18,BG)
cyc+=circle(0,0,26,BG)
pr=circle(0,0,148,'#dce4eb')+circle(0,0,130,BG)
for k in range(12):
    a=k*pi/6;pr+=circle(121*cos(a),121*sin(a),9,FIX)
pins=''
for k in range(6):
    a=k*pi/3;y=270+65*sin(a)-.18*65*cos(a);x=835+.55*65*cos(a)
    pins+=shaft(x-70,x,y,'#73b3a5')
explode('cycloidal-exploded','03 / 摆线针轮减速器：单盘分解',[(120,shaft(45,170,270,'#efbd7f')+face(120,circle(10,0,35,'#f3c88e')+circle(0,0,10,'white')),'① 偏心输入','偏心轴 + 轴承'),(340,face(340,pr),'② 固定针齿圈','包围摆线盘'),(565,face(565,cyc),'③ 摆线盘','中心轴承孔 / 输出孔'),(835,pins+face(835,disc(108,'#b8dfd5')),'④ 输出法兰','输出销伸入盘上大孔')],'针齿与输出销是两组不同的零件：针齿约束盘，输出销传递慢速自转。')
# Motor cutaway schematic, not a specific winding topology.
s=circle(255,285,165,'#dce4eb')+circle(255,285,145,'#adc0d0')+circle(255,285,107,'white')
for k in range(9):
    a=k*2*pi/9;s+=circle(255+125*cos(a),285+125*sin(a),16,'#efbd7f')
s+=circle(255,285,92,'#b8dfd5')
for k in range(8):
    a=k*pi/4;x,y=255+75*cos(a),285+75*sin(a);s+=circle(x,y,13,'#c55f66' if k%2==0 else '#588dbb')
s+=circle(255,285,22,'#748b9d')
s+=label(135,'① 定子铁芯与绕组｜固定','驱动器控制电流，形成旋转磁场',INPUT)+label(225,'② 永磁转子｜旋转','磁场相互作用产生电磁转矩',OUTPUT)+label(315,'③ 气隙｜不接触','定子与转子之间的间隙',FIX)+label(405,'④ 轴与支承轴承','轴将动力送入减速器；轴承未画',MID)
save('motor-section','00 / 电机本体：内转子永磁电机示意',s,'教学概念图 · 槽数与磁极数仅为图示 · 不表示实际绕组方案')
print('Generated 7 SVG figures')
