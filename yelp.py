import pandas as pd


yelp_raw_data = pd.read_csv('yelp.csv')
dataframe = yelp_raw_data.head()
series = yelp_raw_data['business_id'].describe()

# print(type(dataframe))
# print(series)

des = yelp_raw_data['stars'].describe()
val_counts = yelp_raw_data['stars'].value_counts()
sorted(val_counts)
val_counts.plot(kind='bar')

