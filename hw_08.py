# -*- coding: utf-8 -*-
"""ДЗ8_Свертока_Віктор_Васильович.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VZwKdYzrCPX7xtcz8uLxehm4Lz7yVaTA

# Домашнє завдання. Математична статистика

##Завдання 1

Візьми код симуляції із завдання 7 домашнього завдання до теми 7 “Теорія ймовірностей. Комбінаторика”. Будемо вважати, що зміна ціни акцій у кожний момент часу дорівнює $x \sim Г(0.3, 1.1)$, де $Г$ — позначення гамма-розподілу.\
Необхідно запустити симуляцію $n = 100$ разів для різних значень часу $t$.\
a) Побудуй гістограму розподілу $x$\
б) Запусти симуляцію з $t$, від 1 до, наприклад, $\sim 60$ з кроком, наприклад, 1 або 2.\
\
**Примітка:** кінцеве значення $t$ взято умовно рівним 60, але це не відіграє великої ролі, головне, щоб воно було достатнім для проходження тесту на нормальність, а значення кроку — дозволяло побачити динаміку зміни розподілу. Конкретні значення не так важливі.\
\
Для кожного значення $t$ побудуй гістограму розподілу ціни та перевір його на нормальність. Зроби висновки про зміну розподілу зі збільшенням $t$.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Гамма-розподіл з параметрами α = 0.3 і β = 1.1
alpha = 0.3
beta = 1.1

# Функція для симуляції зміни ціни за t кроків
def stock_price_at_time_gamma(t):
    price = 0
    for _ in range(t):
        change = np.random.gamma(alpha, beta)
        price += change
    return price

# Функція для симуляції n разів за t кроків
def simulate_n_times_gamma(n, t):
    prices = [stock_price_at_time_gamma(t) for _ in range(n)]
    return prices

# Частина (a): Побудова гістограми розподілу x
sample_size = 10000
gamma_samples = np.random.gamma(alpha, beta, sample_size)

plt.figure(figsize=(10, 6))
plt.hist(gamma_samples, bins=50, density=True, edgecolor='k', alpha=0.7)
x = np.linspace(0, np.max(gamma_samples), 1000)
pdf = stats.gamma.pdf(x, alpha, scale=beta)
plt.plot(x, pdf, 'r-', lw=2, label=f'Gamma PDF (α={alpha}, β={beta})')
plt.title('Гістограма зразків гамма-розподілу')
plt.xlabel('Значення')
plt.ylabel('Щільність')
plt.legend()
plt.grid(True)
plt.show()

# Частина (b): Симуляція і побудова гістограм для різних t
max_t = 60
step_t = 1
n_simulations = 100

for t in range(1, max_t + 1, step_t):
    prices = simulate_n_times_gamma(n_simulations, t)
    mean_price = np.mean(prices)

    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=20, edgecolor='k', alpha=0.7)
    plt.title(f'Гістограма курсів акцій на t={t} для {n_simulations} моделювання\nСередня ціна = {mean_price:.2f}')
    plt.xlabel('Ціна акцій')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

    # Test for normality
    k2, p = stats.normaltest(prices)
    print(f"t = {t}, Normality test p-value = {p:.3f}")

import numpy as np
import matplotlib.pyplot as plt

def stock_price_at_time(t):
    price = 0
    for _ in range(t):
        change = np.random.choice([2, -1])
        price += change
    return price

def simulate_n_times(n, t):
    prices = [stock_price_at_time(t) for _ in range(n)]
    return prices

for n in [10, 100, 1000, 10000]:
    prices = simulate_n_times(n, 3)
    mean_price = np.mean(prices)

    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=20, edgecolor='k', alpha=0.7)
    plt.title(f'Гістограма курсів акцій при t=3 фор {n} моделювання\nСередня ціна = {mean_price:.2f}')
    plt.xlabel('Ціна акцій')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

"""####Висновки:

- Збільшення значення $𝑡$ призводить до того, що розподіл цін акцій стає ближчим до нормального розподілу (за центральною граничною теоремою).
- Розподіл змін ціни $x$, який є гамма-розподілом, спричиняє асиметричність на малих значеннях $𝑡$, але з часом ця асиметричність зменшується.

##Завдання 2

Є набір даних Product Advertising Data. Набір даних складається із семи стовпчиків, що відображають витрати на рекламу на різних платформах —
телебачення, білборди, Google Ads, соціальні медіа, інфлюенс-маркетинг та партнерський маркетинг

Останній стовпчик, "Product_Sold", містить кількісну оцінку відповідної кількості проданих одиниць товару. Для кожної колонки порахуй середнє значення, дисперсію, стандартне відхилення, побудуй гістограму розподілу показника, перевір на нормальність розподілу та порахуй кореляцію з Product_Sold.
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, normaltest, pearsonr
from google.colab import files
import io

# Завантаження файла з Google Диску
!gdown --id '1xxUxDZOafQ6ZNhX6Kfc3jvUcUtAZ2Kji'

# Завантаження даних з Google Диску
data_path = '/content/Advertising_Data.csv'
data = pd.read_csv(data_path)

# Описова статистика
stats = data.describe()

# Середнє значення, дисперсія, стандартне відхилення
means = data.mean()
variances = data.var()
std_devs = data.std()

# Кореляція з Product_Sold
correlations = data.corr()['Product_Sold']

# Виведення результатів
print("Means:")
print(means)
print("\nVariances:")
print(variances)
print("\nStandard Deviations:")
print(std_devs)
print("\nCorrelations with Product_Sold:")
print(correlations)

# Гістограми та тест на нормальність
columns = data.columns[:-1]  # Всі колонки, крім Product_Sold

for column in columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True, bins=30)
    plt.title(f'Гістограма {column}')
    plt.xlabel(column)
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

    # Тест на нормальність
    stat, p = shapiro(data[column])
    print(f'Shapiro-Wilk тест для {column}: Statistics={stat}, p={p}')

    stat, p = normaltest(data[column])
    print(f'D\'Agostino\'s K^2 тест для {column}: Statistics={stat}, p={p}')

    if p < 0.05:
        print(f'Розповсюдження {column} це не нормально (p < 0.05)')
    else:
        print(f'Розповсюдження {column} це нормально (p >= 0.05)')
    print(" ")

# Побудова кореляційної матриці
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

pip install pandas