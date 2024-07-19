import requests
from bs4 import BeautifulSoup

def get_weather_forecasts():
 
    url = 'https://weather.com/pt-BR/clima/10dias/l/7a3907d638f0859a71d6d5157963e94178e937023bea047b618b542c89844aa1'

    response = requests.get(url)
    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')

    # Extraindo temperatura
    current_temperature = parsed_html.select_one('#detailIndex0 > div > div:nth-child(1) > div > div:nth-child(1) > span').text

    # Extraindo a condição do tempo
    about_current_weather = parsed_html.select_one('#detailIndex0 > div > div.DailyContent--DailyContent--1yRkH > p').text
    dot = about_current_weather.find('.')
    current_weather_condition = about_current_weather[:dot]

    # Extraindo a temperatura e condição do tempo dos próximos 3 dias
    def get_data_about_days(index, selector):
        data = parsed_html.select(f'#detailIndex{index} > summary > div > div > {selector}')[0].text
        return data

    selector_about_temperature = 'div.DetailsSummary--temperature--1kVVp > span.DetailsSummary--highTempValue--3PjlX'
    temperature_first_day = get_data_about_days(1, selector_about_temperature)
    temperature_second_day = get_data_about_days(2, selector_about_temperature)
    temperature_third_day = get_data_about_days(3, selector_about_temperature)

    selector_about_weather_condition = 'div.DetailsSummary--condition--2JmHb > span'

    weather_condition_first_day = get_data_about_days(1, selector_about_weather_condition)
    weather_condition_second_day = get_data_about_days(2, selector_about_weather_condition)
    weather_condition_third_day = get_data_about_days(3, selector_about_weather_condition)


    weather_forecasts = {
    'current_weather': [current_temperature, current_weather_condition],
    'first_day_after': [temperature_first_day, weather_condition_first_day],
    'second_day_after': [temperature_second_day, weather_condition_second_day],
    'third_day_after': [temperature_third_day, weather_condition_third_day]
    }

    return weather_forecasts

