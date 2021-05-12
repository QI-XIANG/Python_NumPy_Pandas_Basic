# Python Pandas Module Basic - Series 2
# Use Dictionary to create Series
import pandas as pd
import numpy as np
population_dict = {
    'France':65429495,
    'Germany':82408706,
    'Russia':143910127,
    'Japan':126922333
}
population = pd.Series(population_dict)
'''
df = pd.DataFrame(population,columns=['Population'])
df
'''
#=================================================================================================

# Sorting Series by first letter of the country name
country_name_sorted = np.sort(population.index)
# Use the sorted index to create Series
'''
population_sorted = pd.Series(population_dict,['Russia','Japan','Germany','France'])
'''
population_sorted = pd.Series(population_dict,country_name_sorted)
print(population_sorted)

#=================================================================================================

# Sorting Series by country population
population_sorted.sort_values(ascending=False,inplace=True)
print(population_sorted)

#=================================================================================================

# Series's name attribute and index's name attribute

# add name attribute to Series
population_sorted.name = 'Population'

# add name attribute to index
population_sorted.index.name = 'Country Name'

population_sorted

#=================================================================================================










