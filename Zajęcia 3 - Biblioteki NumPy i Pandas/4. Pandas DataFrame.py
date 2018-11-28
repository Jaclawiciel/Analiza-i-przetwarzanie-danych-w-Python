import numpy as np
import pandas as pd

voivoideships_data_source = {
    'dolnosląskie': {
        'nr rejestru': 2,
        'miasto wojewódzkie': 'Wrocław',
        'powierzchnia [km2]': 19946.70,
        'ludność': 2904198
    },
    'kujawsko-pomorskie': {
        'nr rejestru': 4,
        'miasto wojewódzkie': 'Bydgoszcz / Toruń',
        'powierzchnia [km2]': 17971.34,
        'ludność': 2086210
    },
    'lubelskie': {
        'nr rejestru': 6,
        'miasto wojewódzkie': 'Lublin',
        'powierzchnia [km2]': 25122.46,
        'ludność': 2139726
    },
    'lubuskie': {
        'nr rejestru': 8,
        'miasto wojewódzkie': 'Gorzów Wielkopolski / Zielona Góra',
        'powierzchnia [km2]': 13987.93,
        'ludność': 1018084
    },
    'łódzkie': {
        'nr rejestru': 10,
        'miasto wojewódzkie': 'Łódź',
        'powierzchnia [km2]': 18218.95,
        'ludność': 2493603
    },
    'małopolskie': {
        'nr rejestru': 12,
        'miasto wojewódzkie': 'Kraków',
        'powierzchnia [km2]': 15182.79,
        'ludność': 3372618
    },
    'mazowieckie': {
        'nr rejestru': 14,
        'miasto wojewódzkie': 'Warszawa',
        'powierzchnia [km2]': 35558.47,
        'ludność': 5349114
    },
}
# 4
voivoideships = pd.DataFrame.from_dict(voivoideships_data_source, orient='index')

# 4.1
print("4.1. Small cities")
small_cities = voivoideships['powierzchnia [km2]'] < 20000
print(voivoideships.loc[small_cities, ['miasto wojewódzkie']])

# 4.2
print("4.2. Cities with biggest population")
cities_with_biggest_population = pd.DataFrame.from_records(voivoideships[voivoideships['ludność'] > 2000000])
print(cities_with_biggest_population)

# 4.3
print('4.3. New row')
wielkopolska = [30, 'Poznań', 29826.50, 3475323]
voivoideships.loc['wielkopolska'] = wielkopolska
print(voivoideships)

# 4.4
print('4.4. Sort by population')
print(voivoideships.sort_values(by='ludność', ascending=False))

# 4.5
print('4.5. Reordering')
voivoideships = voivoideships[['nr rejestru', 'powierzchnia [km2]', 'ludność', 'miasto wojewódzkie']]
print(voivoideships)

# 4.6
print('4.6. Capitalized')
voivoideships.index = voivoideships.index.str.capitalize()
print(voivoideships)

# 4.7
print('4.7. Series with index and boolean')
index_and_boolean = pd.Series((voivoideships['ludność'] / voivoideships['powierzchnia [km2]']) > 140,
                              index=voivoideships.index)
print(index_and_boolean)

# 4.8
print('4.8. Delete row')
voivoideships.drop(['Lubuskie'], axis=0, inplace=True)
print(voivoideships)

# 4.9
print('4.9. describe()')
print(voivoideships.describe())
