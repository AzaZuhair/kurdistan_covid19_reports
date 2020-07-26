from spyre import server
import requests
import pandas as pd
import io
import datetime

links = [
    'https://raw.githubusercontent.com/DevelopersTree/Kovid19/master/data/governorates/erbil.csv',
    'https://raw.githubusercontent.com/DevelopersTree/Kovid19/master/data/governorates/sulaymaniyah.csv',
    'https://raw.githubusercontent.com/DevelopersTree/Kovid19/master/data/governorates/halabja.csv',
    'https://raw.githubusercontent.com/DevelopersTree/Kovid19/master/data/governorates/duhok.csv',
]

governorates = [
    'erbil',
    'sulaymani',
    'halabja',
    'duhok'
]

governorates_data = dict()
for i in range(4):
    response = requests.get(links[i])
    covid_df = pd.read_csv(io.StringIO(response.text), parse_dates=['Date'])
    governorates_data[governorates[i]] = covid_df

class SimpleApp(server.App):
    title = "Kurdistan Covid19 Reports"
    inputs = []

    tabs = ['Erbil', 'Sulaymaniyah', 'Halabja', 'Duhok']

    outputs = []

app = SimpleApp()
app.launch()