import pandas as pd

path = 'https://raw.githubusercontent.com/sinanuozdemir/principles_of_data_science/master/data/chapter_2/drinks.csv'

# read in the CSV file from a URL
drinks = pd.read_csv(path)

print(drinks.head())

# get basic summary about continent
summary = drinks['continent'].describe()
print(summary)

summary2 = drinks['beer_servings'].describe()
print(summary2)