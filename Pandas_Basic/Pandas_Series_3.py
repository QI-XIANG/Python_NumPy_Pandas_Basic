import numpy as np
import pandas as pd
population_dict = {
    'France':65429495,
    'Germany':82408706,
    'Russia':143910127,
    'Japan':126922333
}
area_dict = {
    'France':643801,
    'Germany':357386,
    'Russia':17125200,
    'Japan':377972
}
iso_code_dict = {
    'France':'FR',
    'Germany':'DE',
    'Russia':'RU'
}

area = pd.Series(area_dict)
population = pd.Series(population_dict)
population.sort_values(inplace=True)

countries = pd.DataFrame({'Area':area,'Population':population})
print(countries)

# fill NaN if the value is not exist for a specific column
iso_code = pd.Series(iso_code_dict)

countries['ISO Code'] = iso_code
print(countries)

# get part of the DataFrame
countries['Area']
print(countries.iloc[:3,:2]) # [row,column]
print(countries.loc[:'Russia',:'Population']) # Note: 'Russia' and 'Population' are included

# add new column
countries['many_people'] = countries.Population >= 100000000
print(countries)

# delete column
del countries['many_people']
print(countries)








