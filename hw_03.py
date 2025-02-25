# -*- coding: utf-8 -*-
"""ДЗ3_Свертока_Віктор_Васильович.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19nXvIv9sxFx07A51npEjPZkl48Qqe4zG

Дано 4 точки: $M_0(0, 0, 0), M_1(1, \frac{1}{3}, 0), M_2(0, 2, \frac{1}{4}), M_3(\frac{1}{2}, \frac{1}{2}, 1)$.

Також дано 3 вектори, які задають паралелепіпед із зазначеними точками:
- $\overline{a}=\overline{M_0M_1}$
- $\overline{b}=\overline{M_0M_2}$
- $\overline{c}=\overline{M_0M_3}$

Порахуй координати векторів через задані точки.  
Порахуй об'єм, площу повної поверхні паралелепіпеда та кути між ребрами паралелепіпеда, координати решти вершин паралелепіпеда.

$\overline{a} = ? = \left (\begin{array}{cc}
?\\
?\\
?
\end{array}\right)
\\
\overline{b} = ? = \left (\begin{array}{cc}
?\\
?\\
?
\end{array}\right)
\\
\overline{c} = ? = \left (\begin{array}{cc}
?\\
?\\
?
\end{array}\right)
$

$
V = ?\\
S = ?\\
\angle(a, b) = ?\\
\angle(a, c) = ?\\
\angle(b, c) = ?\\
M_4 = ?\\
M_5 = ?\\
M_6 = ?\\
M_7 = ?
$

Для обчислення координат векторів, які задають паралелепіпед, нам необхідно визначити вектори $\overline{a}$, $\overline{b}$ та $\overline{c}$ за допомогою заданих точок $M_0$, $M_1$, $M_2$ та $M_3$. Необхідно знайти різницю координат відповідних точок $M_1$, $M_2$ та  $M_3$ відносно точки $M_0$.

Вектор $\overline{a}$ визначається як $\overline{𝑀_0𝑀_1}$:
$$
\overline{a} = \overline{𝑀_0𝑀_1} = 𝑀_1 - 𝑀_0
\\
\overline{a} = (1 - 0,\frac{1}{3}-0,0-0) = (1,\frac{1}{3},0)
$$
\
\
Вектор $\overline{b}$ визначається як $\overline{𝑀_0𝑀_2}$:
$$
\overline{b} = \overline{𝑀_0𝑀_2} = 𝑀_2 - 𝑀_0
\\
\overline{b} = (0 - 0,2-0,\frac{1}{4}-0) = (0,2,\frac{1}{4})
$$
\
\
Вектор $\overline{c}$ визначається як $\overline{𝑀_0𝑀_3}$:
$$
\overline{c} = \overline{𝑀_0𝑀_3} = 𝑀_3 - 𝑀_0
\\
\overline{c} = (\frac{1}{2} - 0,\frac{1}{2}-0,1-0) = (\frac{1}{2},\frac{1}{2},1)
$$
"""

import plotly.graph_objects as go

M0 = (0, 0, 0)
M1 = (1, 1/3, 0)
M2 = (0, 2, 1/4)
M3 = (1/2, 1/2, 1)

def vector_between_points(P1, P0):
    return (P1[0] - P0[0], P1[1] - P0[1], P1[2] - P0[2])

a = vector_between_points(M1, M0)
b = vector_between_points(M2, M0)
c = vector_between_points(M3, M0)

print(f"Вектор a: {a}")
print(f"Вектор b: {b}")
print(f"Вектор c: {c}")

fig = go.Figure()

fig.add_trace(go.Scatter3d(x=[M0[0], M1[0], M2[0], M3[0]],
                           y=[M0[1], M1[1], M2[1], M3[1]],
                           z=[M0[2], M1[2], M2[2], M3[2]],
                           mode='markers',
                           marker=dict(size=5),
                           name='Точка на площині'))

def add_vector(fig, start, vector, name):
    fig.add_trace(go.Scatter3d(x=[start[0], start[0] + vector[0]],
                               y=[start[1], start[1] + vector[1]],
                               z=[start[2], start[2] + vector[2]],
                               mode='lines',
                               line=dict(width=5),
                               name=name))

add_vector(fig, M0, a, 'Вектор a')
add_vector(fig, M0, b, 'Вектор b')
add_vector(fig, M0, c, 'Вектор c')

fig.update_layout(scene=dict(
                    xaxis_title='вісь X',
                    yaxis_title='вісь Y',
                    zaxis_title='вісь Z'),
                  title="3D-графік з точкою 𝑀0 та трьома векторами",
                  width=800,
                  height=700,
                  showlegend=True)

fig.show()

"""Для обчислення об'єму паралелепіпеда, заданого векторами $\overline{a}$, $\overline{b}$ та
$\overline{𝑐}$, можна скористатися визначником матриці, складеної з координат цих векторів. Об'єм паралелепіпеда визначається як абсолютне значення змішаного добутку цих векторів:
\
$$
V = \left|\overline{a} \cdot \left(\overline{b} \times \overline{c}\right)\right|
$$
\
Обчислимо змішаний добуток:
\
$$
V = \left|\left|\begin{array}{cc} 1 & \frac{1}{3}0 &  \\ 0 & 2 & \frac{1}{4} \\ \frac{1}{2} & \frac{1}{2} & 1 \\  \end{array}\right|\right|
$$
\
###Об'єм паралелепіпеда рахуємо як обчислення визначника матриці:
\
$$
V = \left|1 \cdot \left(2 \cdot 1- \frac{1}{4} \cdot \frac{1}{2}\right) - \frac{1}{3} \cdot \left(0 \cdot 1 - \frac{1}{4} \cdot \frac{1}{2}\right) + 0 \cdot \left(0 \cdot \frac{1}{2} - 2 \cdot \frac{1}{2}\right)\right|
$$
\
\
$$
V = \left|1 \cdot \left(2 - \frac{1}{8}\right) - \frac{1}{3} \cdot \left(0 - \frac{1}{8} \right) + 0 \right|
$$
\
\
$$
V = \left|1 \cdot \frac{15}{8} + \frac{1}{3} \cdot \frac{1}{8} \right|= \left|\frac{15}{8} + \frac{1}{24} \right|= \left|\frac{45}{24} + \frac{1}{24} \right|= \left|\frac{46}{24} \right|
$$

###Об'єм паралелепіпеда:
$$
V = \left|\frac{23}{12} \right|
$$
нижче приведено програмне обчислення об'єма паралелепіпеда

Щоб обчислити площу повної поверхні паралелепіпеда, потрібно знайти площі всіх його шести граней і скласти їх.
Для паралелепіпеда, утвореного векторами $\overline{a}$, $\overline{b}$ та $\overline{c}$, площі граней можна знайти за допомогою векторного добутку:

1. Обчислюємо площу грані, утвореної векторами $\overline{a}$ та $\overline{b}$:
$A_1=\left|\overline{a}\times\overline{b}\right|$

Обчислимо векторні добутки:

$$
\overline{a}\times\overline{b}=\left|\begin{array}{cc} i & j & k \\ 1 & \frac{1}{3} & 0 \\ 0 & 2 & \frac{1}{4} \\  \end{array}\right| = i\left(\frac{1}{3} \cdot \frac{1}{4} - 0 \cdot 2\right) - j\left(1 \cdot \frac{1}{4} - 0 \cdot 0\right) + k\left(1 \cdot 2 - 0 \cdot \frac{1}{3}\right)
$$

$$
\overline{a}\times\overline{b}=
\left(\frac{1}{12}, - \frac{1}{4},2\right)
$$

$$
\left|\overline{a} \times \overline{b}\right| = \sqrt{\left(\frac{1}{12}\right)^2 + \left( - \frac{1}{4}\right)^2 + 2^2} = \sqrt{\frac{1}{144} + \frac{1}{16} + 4} = \sqrt{\frac{1 + 9 + 576}{144}} = \sqrt{\frac{586}{144}} = \frac{\sqrt{586}}{12}
$$

2. Обчислюємо площу грані, утвореної векторами $\overline{b}$ та $\overline{c}$:
$A_2=\left|\overline{b}\times\overline{c}\right|$

Обчислимо векторні добутки:

$$
\overline{b}\times\overline{c}=\left|\begin{array}{cc} i & j & k \\ 0 & 2 & \frac{1}{4}  \\ \frac{1}{2} &  \frac{1}{2} & 1\\  \end{array}\right| = i\left(2 \cdot 1-\frac{1}{4} \cdot \frac{1}{2}\right) - j\left(0 \cdot 1 - \frac{1}{4} \cdot \frac{1}{2}\right) + k\left(0 \cdot \frac{1}{2} - 2 \cdot \frac{1}{2}\right)
$$

$$
\overline{b}\times\overline{c}=
\left(2 - \frac{1}{8}, - \frac{1}{8},-1\right)=
\left(\frac{15}{8}, - \frac{1}{8},-1\right)
$$

$$
\left|\overline{b} \times \overline{c}\right| = \sqrt{\left(\frac{15}{8}\right)^2 + \left( - \frac{1}{8}\right)^2 + (-1)^2} = \sqrt{\frac{225}{64} + \frac{1}{64} + 1} = \sqrt{\frac{225 + 1 + 64}{64}} = \sqrt{\frac{290}{64}}
$$

3. Обчислюємо площу грані, утвореної векторами $\overline{a}$ та $\overline{c}$:
$A_3=\left|\overline{a}\times\overline{c}\right|$

Обчислимо векторні добутки:

$$
\overline{a}\times\overline{c}=\left|\begin{array}{cc} i & j & k \\ 1 & \frac{1}{3} & 0  \\ \frac{1}{2} &  \frac{1}{3} & 1\\  \end{array}\right| = i\left(\frac{1}{3} \cdot 1-0 \cdot \frac{1}{2}\right) - j\left(1 \cdot 1 - 0 \cdot \frac{1}{2}\right) + k\left(1 \cdot \frac{1}{2} - \frac{1}{3} \cdot \frac{1}{2}\right)
$$

$$
\overline{b}\times\overline{c}=
\left(\frac{1}{3}, - 1, \frac{1}{2}-\frac{1}{6}\right)=
\left(\frac{1}{3}, - 1,\frac{1}{3}\right)
$$

$$
\left|\overline{a} \times \overline{c}\right| = \sqrt{\left(\frac{1}{3}\right)^2 +  (-1)^2 + \left(\frac{1}{3}\right)^2} = \sqrt{\frac{1}{9} + 1 + \frac{1}{9}}= \sqrt{\frac{1 + 9 + 1}{9}} = \sqrt{\frac{11}{9}}= \frac{\sqrt{11}}{3}
$$

##Площа повної поверхні паралелепіпеда дорівнює:

$$
S = 2 \cdot \left(\frac{\sqrt{586}}{12} + \frac{\sqrt{290}}{8} + \frac{\sqrt{11}}{3}\right)
$$

Нижче наведено програмний код для обчислення площі повної поверхні паралелепіпеда

Щоб знайти кути між ребрами паралелепіпеда, потрібно розглянути кути між векторами $\overline{a},\overline{b}$ та $\overline{c}$. Використовуватимемо скалярний добуток векторів для обчислення кутів між ними.

1. Кут між  $\overline{a}$ та  $\overline{b}$

Обчислимо скалярний добуток:  
$$
\overline{a} \cdot \overline{b} = 1 \cdot 0 + \frac{1}{3} \cdot 2 + 0 \cdot \frac{1}{4} = \frac{2}{3} $$
Обчислимо довжини векторів:
$$
\left|\overline{a}\right| = \sqrt{1^2 + \left(\frac{1}{3}\right)^2 + 0^2} = \sqrt{1 + \frac{1}{9}} = \sqrt{\frac{10}{9}} = \frac{\sqrt{10}}{3}$$
$$
\left|\overline{b}\right| = \sqrt{0^2 + 2^2 + \left(\frac{1}{4}\right)^2} = \sqrt{4 + \frac{1}{16}} = \sqrt{\frac{65}{16}} = \frac{\sqrt{65}}{4}$$

Обчислимо $cos\left(\theta \right)$:

$$
cos\left(\theta_{ab}\right) = \frac{\frac{2}{3}}{\frac{\sqrt{10}}{3} \cdot \frac{\sqrt{65}}{4}} = \frac{\frac{2}{3}}{\frac{\sqrt{650}}{12}} = \frac{2 \cdot 12}{3\sqrt{650}} = \frac{8}{\sqrt{650}}
$$

2. Кут між  $\overline{a}$ та  $\overline{c}$

Обчислимо скалярний добуток:  
$$
\overline{a} \cdot \overline{c} = 1 \cdot \frac{1}{2} + \frac{1}{3} \cdot \frac{1}{2} + 0 \cdot 1 = \frac{2}{3} $$
Обчислимо довжини векторів:
$$
\left|\overline{c}\right| = \sqrt{\left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2+ 1^2} = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2}$$

Обчислимо $cos\left(\theta \right)$:

$$
cos\left(\theta_{ac}\right) = \frac{\frac{2}{3}}{\frac{\sqrt{10}}{3} \cdot \frac{\sqrt{6}}{2}} = \frac{\frac{2}{3}}{\frac{\sqrt{60}}{6}} = = \frac{4}{\sqrt{60}}
$$

3. Кут між  $\overline{b}$ та  $\overline{c}$

Обчислимо скалярний добуток:  
$$
\overline{b} \cdot \overline{c} = 0 \cdot \frac{1}{2} + 2 \cdot \frac{1}{2} + \frac{1}{4} \cdot 1 = 1 + \frac{1}{4}= \frac{5}{4} $$

Обчислимо $cos\left(\theta \right)$:

$$
cos\left(\theta_{bc}\right) = \frac{\frac{5}{4}}{\frac{\sqrt{65}}{4} \cdot \frac{\sqrt{6}}{2}} = \frac{\frac{5}{4}}{\frac{\sqrt{390}}{8}} = = \frac{10}{\sqrt{390}}
$$
нижче приведено програмне обчислення кутів.

Порахуємо координати інших чотирьох вершин паралелепіпеда.

$$
M_4 = M_1 + \overline{b} = \left(1,\frac{1}{3},0\right) + \left(0,2,\frac{1}{4}\right) = \left(1,\frac{7}{3},\frac{1}{4}\right)
$$

$$
M_5 = M_1 + \overline{c} = \left(1,\frac{1}{3},0\right) + \left(\frac{1}{2},\frac{1}{2},1\right) = \left(\frac{3}{2},\frac{5}{6},1\right)
$$

$$
M_6 = M_2 + \overline{c} = \left(0,2,\frac{1}{4}\right) + \left(\frac{1}{2},\frac{1}{2},1\right) = \left(\frac{1}{2},\frac{5}{2},\frac{5}{4}\right)
$$

$$
M_7 = M_1 + \overline{b}+ \overline{c} = \left(1,\frac{1}{3},0\right) + \left(0,2,\frac{1}{4}\right) + \left(\frac{1}{2},\frac{1}{2},1\right) = \left(\frac{3}{2},\frac{7}{6},\frac{5}{4}\right)
$$
"""

import numpy as np
import plotly.graph_objs as go

a = np.array([1, 1/3, 0])
b = np.array([0, 2, 1/4])
c = np.array([1/2, 1/2, 1])

cross_product = np.cross(b, c)

scalar_triple_product = np.dot(a, cross_product)

volume = abs(scalar_triple_product)

print("Об'єм паралелепіпеда:", volume)

surface_area = 2 * (np.linalg.norm(a)*np.linalg.norm(b) + np.linalg.norm(b)*np.linalg.norm(c) + np.linalg.norm(c)*np.linalg.norm(a))

print("Площа повної поверхні паралелепіпеда:", surface_area)

def angle_between_vectors(u, v):
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    cos_theta = dot_product / (norm_u * norm_v)
    theta_radians = np.arccos(cos_theta)
    theta_degrees = np.degrees(theta_radians)
    return theta_radians, theta_degrees

theta_ab_rad, theta_ab_deg = angle_between_vectors(a, b)
theta_ac_rad, theta_ac_deg = angle_between_vectors(a, c)
theta_bc_rad, theta_bc_deg = angle_between_vectors(b, c)

print("Кут між векторами a і b в радіанах:", theta_ab_rad)
print("Кут між векторами a і b в градусах:", theta_ab_deg)
print("Кут між векторами a і c в радіанах:", theta_ac_rad)
print("Кут між векторами a і c в градусах:", theta_ac_deg)
print("Кут між векторами b і c в радіанах:", theta_bc_rad)
print("Кут між векторами b і c в градусах:", theta_bc_deg)

vertices = np.array([[0, 0, 0], a, b, c, a + b, a + c, b + c, a + b + c])

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=vertices[:,0],
    y=vertices[:,1],
    z=vertices[:,2],
    mode='markers',
    name='Вершини паралелепіпеда',
    marker=dict(size=6, color='blue')
))

lines = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 4], [2, 6], [3, 5], [3, 6], [4, 7], [5, 7], [6, 7]]
for line in lines:
    fig.add_trace(go.Scatter3d(
        x=[vertices[line[0], 0], vertices[line[1], 0]],
        y=[vertices[line[0], 1], vertices[line[1], 1]],
        z=[vertices[line[0], 2], vertices[line[1], 2]],
        mode='lines',
        line=dict(color='black', width=3)
    ))

fig.update_layout(scene=dict(
                    xaxis=dict(title='вісь X'),
                    yaxis=dict(title='вісь Y'),
                    zaxis=dict(title='вісь Z')),
                  title='Паралелепіпед')

fig.show()

pip install plotly