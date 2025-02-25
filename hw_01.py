# -*- coding: utf-8 -*-
"""ДЗ1_Свертока_Віктор_Васильович.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bQAG1nQO2covXASkvZJY13_LYQAodqB4

# Нагадування по Markdown

Надаємо невелике нагадування записів в
[Markdown](https://colab.research.google.com/notebooks/markdown_guide.ipynb) (LaTeX):

Markdown | Preview
--- | ---
`**bold text**` | **bold text**
 \\$\frac{x}{y}\\$ | $\frac{x}{y}$
 \\$p^{x}_{y}\\$ | $p^{x}_{y}$
\\$x \cdot y\\$ | $x \cdot y$
\\$\sqrt{x}\\$ | $\sqrt{x}$
\\$\pi\\$ | $\pi$
\\$\approx\\$ | $\approx$

І ще декілька прикладів:

```markdown
$y=x^2$

$e^{i\pi} + 1 = 0$

$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$

$\frac{n!}{k!(n-k)!} = {n \choose k}$

$A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}$

 $$
 I =
 \left (\begin{array}{cc}
 1 & 0\\
 0 & 1
 \end{array}\right)
 $$
```

$y=x^2$

$e^{i\pi} + 1 = 0$

$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$

$\frac{n!}{k!(n-k)!} = {n \choose k}$

$A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}$

$I =
\left (\begin{array}{cc}
1 & 0\\
0 & 1
\end{array}\right)$
 ---

# Завдання 1.
В шаблоні наведені числові вектори $\overline{a}$ та $\overline{b}$. Порахуй наступне:
- сума $\overline{a}$ та $\overline{b}$
- різниця $\overline{a}$ та $\overline{b}$
- сума $\overline{a}$ та $\overline{b}^T$. Поясни отриманий результат.
- матричний добуток (dot product) $\overline{a}$ та $\overline{b}^T$.
- матричний добуток (dot product) $\overline{a}$ та $\overline{b}$. Поясни отриманий результат.
- добуток Адамара (Hadamard product) $\overline{a}$ та $\overline{b}$. Поясни отриманий результат.
- ділення $\overline{a}$ та $\overline{b}$. Поясни отриманий результат.
- ділення $\overline{a}$ та $\overline{b}^T$. Поясни отриманий результат.
"""

import numpy as np
a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])

res = a + b
print(res)

res = a - b
print(res)

res = a * b
print(res)

res = a / b
print(res)

# Пояснення: Ми маємо два вектори: a (розміром 1x5) та b (розміром 1x5). Транспонування вектора перетворює його в вектор-стовпець 𝑏𝑇 (розміром 5x1). А потім виконуємо додавання.
b_T = b.T
res = a + b_T
print(res)

b_T = b.T
res = np.dot(a, b_T)
print(res)

# Пояснення: Виникає помилка, щоб виправити це, потрібно транспонувати один з векторів. У даному випадку транспонуємо вектор 𝑏
res = np.dot(a, b)
print(res)

# Пояснення: Добуток Адамара (Hadamard product) – це елементний добуток двох матриць однакового розміру. Це операція, коли кожні відповідні елементи векторів множаться один на одного.
res = a * b
print(res)

# Пояснення: Кожен елемент вектора a був поділений на відповідний елемент вектора b.
res = a / b
print(res)

# Пояснення: Ми маємо два вектори: a (розміром 1x5) та b (розміром 1x5). Транспонування вектора перетворює його в вектор-стовпець 𝑏𝑇 (розміром 5x1). А потім виконуємо ділення.
b_T = b.T
res = a / b_T
print(res)

"""# Завдання 2
В цьому завданні ти навчишся перетворювати вектори за допомогою афінних перетворень.  
Дано вектор:
$$
x =
\left(\begin{array}{cc}
2\\
1
\end{array}\right)
$$


Виконай аналітично наступні завдання задавши матрицю перетворення та застосуй її до вектора $x$:

1. Зменши вектор $x$ в 2 рази по вісі $OX$ та збільш в 3 рази по вісі $OY$.
2. Відобрази вектор $x$ відносно початку координат.
3. Перенеси вектор $x$ на -3 по вісі $OX$ та на 1 по вісі $OY$.
4. Змісти вектор $x$ на 60° по вісі $OY$.
5. Поверни вектор $x$ на 30°.
6. Об'єднай перетворення з кроків 1, 2, 4, 5 в одну матрицю та застосуй її до вектору $x$.

#### 2.1 Зменши вектор  $x$  в 2 рази по вісі  OX  та збільш в 3 рази по вісі  OY .

$$
M_1 =
\left (\begin{array}{cc}
\frac{1}{2} & 0\\
0 & 3
\end{array}\right)
$$

$$
M_1x =
\left (\begin{array}{cc}
\frac{1}{2} & 0\\
0 & 3
\end{array}\right)
\left (\begin{array}{cc}
2\\
1
\end{array}\right)=
\left(\begin{array}{cc}
\frac{1}{2} \cdot 2 + 0 \cdot 1\\
0 \cdot 2 + 3 \cdot 1
\end{array}\right)=
\left(\begin{array}{cc}
1+0\\
0+3
\end{array}\right) =
\left (\begin{array}{cc}
1\\
3
\end{array}\right)
$$

#### 2.2 Відобрази вектор $x$ відносно початку координат.

$$
M_2 =
\left (\begin{array}{cc}
-1 & 0\\
0 & -1
\end{array}\right)
\\
M_2x =
\left (\begin{array}{cc}
-1 & 0\\
0 & -1
\end{array}\right)
\left (\begin{array}{cc}
2\\
1
\end{array}\right)=
\left(\begin{array}{cc}
-1 \cdot 2 + 0 \cdot 1\\
0 \cdot 2 + 1 \cdot -1
\end{array}\right) =
\left (\begin{array}{cc}
-2\\
-1
\end{array}\right)
$$

#### 2.3 Перенеси вектор $x$ на -3 по вісі $OX$ та на 1 по вісі $OY$.

$$
M_3 =
\left (\begin{array}{cc}
1 & 0 & -3\\
0 & 1 & 1\\
0 & 0 & 1
\end{array}\right)\\
x=
\left (\begin{array}{cc}
2\\
1\\
1
\end{array}\right)
\\
M_3x =
\left (\begin{array}{cc}
1 & 0 & -3\\
0 & 1 & 1\\
0 & 0 & 1
\end{array}\right)\cdot
\left (\begin{array}{cc}
1 \cdot 2 + 0 \cdot 1 + (-3) \cdot 1\\
0 \cdot 2 + 1 \cdot 1 + 1 \cdot 1\\
0 \cdot 2 + 0 \cdot 1 + 1 \cdot 1
\end{array}\right)=
\left (\begin{array}{cc}
-1\\
2\\
1
\end{array}\right)\\
\\
$$

#### 2.4 Змісти вектор $x$ на 60° по вісі $OY$.

$$
M_4 =
\left (\begin{array}{cc}
1 & 0\\
tan(θ) & 1
\end{array}\right)=
\left (\begin{array}{cc}
1 & 0\\
tan\frac{\pi}{3} & 1
\end{array}\right)=
\left (\begin{array}{cc}
1 & 0\\
\sqrt{3} & 1
\end{array}\right)
\\
M_4x =
\left (\begin{array}{cc}
1 & 0\\
\sqrt{3} & 1
\end{array}\right)\cdot
\left (\begin{array}{cc}
2\\
1
\end{array}\right)=
\left (\begin{array}{cc}
1 \cdot 2 + 0 \cdot 1\\
\sqrt{3} \cdot 2 + 1 \cdot 1
\end{array}\right)=
\left (\begin{array}{cc}
2\\
2\sqrt{3} + 1
\end{array}\right)
$$
"""



"""#### 2.5 Поверни вектор $x$ на 30°.

$$
M_5 = \begin{bmatrix} \cos\left(\frac{\pi}{6}\right) & -\sin\left(\frac{\pi}{6}\right) \\ \sin\left(\frac{\pi}{6}\right) & \cos\left(\frac{\pi}{6}\right) \end{bmatrix}
\\
\\
M_5x = \begin{pmatrix} \frac{\sqrt{3}}{2} \times 2 + (-\frac{1}{2}) \times 1 \\ \frac{1}{2} \times 2 + \frac{\sqrt{3}}{2} \times 1 \end{pmatrix} =
\begin{pmatrix} \sqrt{3} - \frac{1}{2} \\ 1 + \frac{\sqrt{3}}{2} \end{pmatrix}
$$

#### 2.6 Об'єднай перетворення з кроків 1, 2, 4, 5 в одну матрицю та застосуй її до вектору $x$.

$$
M_6 = M_5 \cdot M_4 \cdot M_2 \cdot M_1 = ?
$$

$$
M_6 =
\begin{pmatrix} \sqrt{3} - \frac{1}{2} \\ 1 + \frac{\sqrt{3}}{2} \end{pmatrix} ⋅
\begin{pmatrix} 1 - \frac{\sqrt{3}}{2} \\ \sqrt{3} + \frac{1}{2} \end{pmatrix} ⋅
\left (\begin{array}{cc}
-2\\
-1
\end{array}\right) ⋅
\left (\begin{array}{cc}
1\\
3
\end{array}\right)
\\
M_6 = 2\sqrt{3} - \frac{7}{2}
$$
"""



"""# Завдання 2 (Альтернативне)"""

import cv2 as cv
import urllib.request
import numpy as np
from google.colab.patches import cv2_imshow as cv_imshow
from PIL import Image
import io
import cairosvg

def read_svg_image_by_url(url):
    try:
        req = urllib.request.urlopen(url)
        svg_data = req.read()

        png_data = cairosvg.svg2png(bytestring=svg_data)

        img = Image.open(io.BytesIO(png_data))
        img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        return img

    except Exception as e:
        print(f"Помилка при завантаженні або обробці зображення: {e}")
        return None

url = 'https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg'

img = read_svg_image_by_url(url)

if img is not None:
    cv_imshow(img)
else:
    print("Неможливо завантажити зображення.")

angle = 30

def rotate_image(image, angle_degrees, scale_x, scale_y):
    # Визначення розмірів зображення
    height, width = image.shape[:2]

    # Перетворення кута на радіани
    angle_radians = np.deg2rad(angle_degrees)

    # Визначення матриці перетворення для повороту та масштабування
    rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), angle_degrees, 1)
    scaling_matrix = np.array([[scale_x, 0, 0], [0, scale_y, 0], [0, 0, 1]], dtype=np.float32)

    # Поворот та масштабування зображення
    rotated_scaled_image = cv.warpAffine(image, rotation_matrix.dot(scaling_matrix), (width, height))

    return rotated_scaled_image


# Поворот зображення
rotated_scaled_img = rotate_image(img, angle_degrees=30, scale_x=0.5, scale_y=0.33)

# Відображення зображення до та після повороту
cv_imshow(rotated_scaled_img)

pip install numpy

!pip install cairosvg