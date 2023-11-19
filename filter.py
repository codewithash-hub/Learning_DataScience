import pandas as pd

yelp_raw_data = pd.read_csv('yelp.csv')

duplicated_text = yelp_raw_data['text'].describe()['top']
text_is_the_duplicate = yelp_raw_data['text'] == duplicated_text

print(text_is_the_duplicate.head())

