import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/pt-BR/clima/10dias/l/7a3907d638f0859a71d6d5157963e94178e937023bea047b618b542c89844aa1'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# Extraindo temperatura
temperature = parsed_html.select_one('#detailIndex0 > div > div:nth-child(1) > div > div:nth-child(1) > span').text

# Extraindo a condição do tempo
about_weather = parsed_html.select_one('#detailIndex0 > div > div.DailyContent--DailyContent--1yRkH > p').text
dot = about_weather.find('.')
weather_condition = about_weather[:dot]

# Extraindo a temperatura dos próximos 3 dias
def get_data_about_days(index, selector):
 data = parsed_html.select(f'#detailIndex{index} > summary > div > div > {selector}')[0].text
 return data
 
selector_about_date = 'h2'
first_day = get_data_about_days(1, selector_about_date)
second_day = get_data_about_days(2, selector_about_date)
third_day = get_data_about_days(3, selector_about_date)

selector_about_temperature = 'div.DetailsSummary--temperature--1kVVp > span.DetailsSummary--highTempValue--3PjlX'
weather_first_day = get_data_about_days(1, selector_about_temperature)
weather_second_day = get_data_about_days(2, selector_about_temperature)
weather_third_day = get_data_about_days(3, selector_about_temperature)

print(weather_first_day)
print(weather_second_day)
print(weather_third_day)

#detailIndex1 > summary > div > div > div.DetailsSummary--temperature--1kVVp > span.DetailsSummary--highTempValue--3PjlX