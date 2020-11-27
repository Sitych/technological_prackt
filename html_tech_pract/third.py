#!/home/dima/botva/1semestr/technological_prackt/MLS/mls/bin/python3

# Задача 3
# Дана страница https://www.worldometers.info/world-population/world-population-by-year/

# На ней представлены данные о росте численности населения Земли. Используя удобные для вас модули Python 
# (Например requests, bs4 и pandas, но можно и любые другие) сгрузить в удобную для вас структуру данных 
# (например pandas-табличку) необходимые данные и нарисовать графики ежегодного прироста городского населения 
# и ежегодного прироста общего населения, начиная с 1951 года.

from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib.patches as mpatches

wiki = "https://www.worldometers.info/world-population/world-population-by-year/"

resp = req.get(wiki)
soup = BeautifulSoup(resp.text, 'lxml')
table = soup.find_all('tbody')

data = []
for tr in table[0].find_all('tr'):
	data.append([td.text for td in tr.find_all('td')])

data = pd.DataFrame(data, columns=["Year", "World Population", "Yearly Change", "Net Change", "Density(P/Km²)", "Urban Pop", "Urban Pop %"])
index = data.index[data.Year == '1951']

x_world = data["Year"][:index[0]+1][::-1]
y_world = [int(''.join(i.split(','))) for i in data["World Population"]][:index[0]+1][::-1]
# y_urban = [int(''.join(re.findall("\d*", i))) for i in data["Urban Pop"]][:index[0]][::-1]

y_urban = []
for i in data["Urban Pop"]:
	try:
		y_urban.append(int(''.join(re.findall("\d*", i))))
	except:
		pass
y_urban.reverse()
# for i in data["Urban Pop"][:index[0]+1]:
# 	print(''.join(re.findall("\d*", i)))

fig, ax = plt.subplots()

ax.plot(x_world, y_world, 'g', label='World Pop')
ax.plot(x_world, y_urban, 'r', label='Urban Pop')
ax.legend()
plt.autoscale(tight=True)
# Рисуем сетку пунктиром
plt.grid(True, linestyle='-', color='0.75')
plt.show()