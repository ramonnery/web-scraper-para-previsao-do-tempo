import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/pt-BR/clima/10dias/l/7a3907d638f0859a71d6d5157963e94178e937023bea047b618b542c89844aa1'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

temperature = parsed_html.select_one('#detailIndex0 > div > div:nth-child(1) > div > div:nth-child(1) > span').text
