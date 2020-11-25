#!/home/dima/botva/1semestr/technological_prackt/MLS/mls/bin/python3

# Задача 1
# Дана страница https://ru.wikipedia.org/wiki/Премия_«Оскар»_за_лучший_фильм#Достижения_по_другим_номинациям_Оскара

# Используя удобные для вас модули Python (Например requests, bs4 и pandas, но можно и любые другие) сгрузить в удобную для вас структуру данных (например pandas-табличку) данные о номинантах и победителях премии Оскар за лучший фильм за всю историю существования премии. Заметьте, на страничке эта информация в нескольких таблицах. По данным ответьте на вопросы. P.S. Результат нужно именно посчитать, если на странице в явном виде указан ответ на вопрос, просто выгрузить этот ответ нельзя:

# 1. Сколько раз были номинированы фильмы, созданные при участии Стивена Спилберга?
# 2. Фильмы какой компании получили больше Оскаров за лучший фильм: Warner Bros. или Paramount Pictures и насколько больше?

from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import re

wiki = "https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D0%BC%D0%B8%D1%8F_%C2%AB%D0%9E%D1%81%D0%BA%D0%B0%D1%80%C2%BB_%D0%B7%D0%B0_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%B9_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC#%D0%94%D0%BE%D1%81%D1%82%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BF%D0%BE_%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%BC_%D0%BD%D0%BE%D0%BC%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D1%8F%D0%BC_%D0%9E%D1%81%D0%BA%D0%B0%D1%80%D0%B0"

resp = req.get(wiki)
soup = BeautifulSoup(resp.text, 'lxml')
res_table = soup.find_all('table', {'class' : 'wikitable'})


# all_data = []
# for table in res_table:
# 	for tr in table.find_all('tr'):
# 		all_data.append(' '.join(tr.text.split('\n')))

# victory_data = []
# for table in res_table:
# 	for tr in table.find_all('tr', {'style' : 'background:#FAEB86'}):
# 		victory_data.append(' '.join(tr.text.split('\n')))

# for table in res_table:
# 	year = []
# 	for td in filter(None,table.find_all('td', {'style' : 'background:#FAEB86'})):
# 		victory_data.append(td.text)

all_data = []
victory_data = []
for table in res_table:
	for tr in table.find_all('tr'):
		all_data.append(' '.join(tr.text.split('\n')))
	for tr in table.find_all('tr', {'style' : 'background:#FAEB86'}):
		victory_data.append(' '.join(tr.text.split('\n')))
	for td in filter(None,table.find_all('td', {'style' : 'background:#FAEB86'})):
		victory_data.append(td.text)

nomination = -1

for data in all_data:
	if re.findall(".*Стивен Спилберг.*",data):
		nomination += 1

W_B = 0
P_P = 0
for data in victory_data:
	if re.findall(".*Стивен Спилберг.*",data):
		nomination -= 1
	if re.findall(".*Paramount Pictures.*", data):
		P_P += 1
	if re.findall(".*Warner Bros.*", data):
		W_B += 1

victory = "Warner Bros." if max(P_P, W_B) == W_B else "Paramount Pictures"
print(f"Сколько раз были номинированы фильмы, созданные при участии Стивена Спилберга? {nomination}")
print(f"Фильмы какой компании получили больше Оскаров за лучший фильм: Warner Bros. или Paramount Pictures и насколько больше? {victory}; {abs(W_B - P_P)}")

# Задача 2
# Дана страница https://ru.wikipedia.org/wiki/Премия_«Оскар»_за_лучшую_женскую_роль

# Используя удобные для вас модули Python (Например requests, bs4 и pandas, но можно и любые другие) сгрузить в удобную для вас структуру данных (например pandas-табличку) данные о номинантах и победителях премии Оскар за лучшую женскую роль за всю историю существования премии. Заметьте, на страничке эта информация в нескольких таблицах. По данным ответьте на вопросы. P.S. Результат нужно именно посчитать, если на странице в явном виде указан ответ на вопрос, просто выгрузить этот ответ нельзя:

# 1. Какая актриса чаще всего номинировалась на Оскар?
# 2. Насколько отличается количество номинаций самой часто номинировавшейся актрисы и второй по частоте?

wiki = "https://ru.wikipedia.org/wiki/Премия_«Оскар»_за_лучшую_женскую_роль"
