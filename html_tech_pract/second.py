#!/home/dima/botva/1semestr/technological_prackt/MLS/mls/bin/python3

# Задача 2
# Дана страница https://ru.wikipedia.org/wiki/Премия_«Оскар»_за_лучшую_женскую_роль

# Используя удобные для вас модули Python (Например requests, bs4 и pandas, но можно и любые другие) сгрузить в удобную для вас структуру данных (например pandas-табличку) данные о номинантах и победителях премии Оскар за лучшую женскую роль за всю историю существования премии. Заметьте, на страничке эта информация в нескольких таблицах. По данным ответьте на вопросы. P.S. Результат нужно именно посчитать, если на странице в явном виде указан ответ на вопрос, просто выгрузить этот ответ нельзя:

# 1. Какая актриса чаще всего номинировалась на Оскар?
# 2. Насколько отличается количество номинаций самой часто номинировавшейся актрисы и второй по частоте?

from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import re

wiki = "https://ru.wikipedia.org/wiki/Премия_«Оскар»_за_лучшую_женскую_роль"

resp = req.get(wiki)
soup = BeautifulSoup(resp.text, 'lxml')
res_table = soup.find_all('table', {'class' : 'wikitable'})

data_actress = []
for table in res_table:
	for tr in table.find_all('tr'):
		buf = filter(lambda x: False if re.findall(".*\d.*|Церемония|Фото лауреата|Актриса|Фильм|Роль", x) or x == "" else True, tr.text.split('\n'))
		data_actress.append(buf)

data_actress.pop(2)
data_actress.pop(2)

data_actress = pd.DataFrame(filter(None, data_actress), columns=["Actress", "Film", "Role"])
new = data_actress[~pd.isnull(data_actress).all(1)]
col_nom = dict.fromkeys(set(new['Actress']), 0)

for actress in new['Actress']:
	col_nom[actress] += 1

max_nom = max(col_nom.values())
second_nom = max(filter(lambda x: False if x == max_nom else True, col_nom.values()))
for key in col_nom:
	if col_nom[key] == max_nom:
		first_actress = key
	elif col_nom[key] == second_nom:
		second_actress = key

print(f"Какая актриса чаще всего номинировалась на Оскар? {first_actress}")
print(f"Насколько отличается количество номинаций самой часто номинировавшейся актрисы и второй по частоте? {col_nom[first_actress]-col_nom[second_actress]}")