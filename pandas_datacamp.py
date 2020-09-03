import pandas as pd

df = pd.DataFrame()

df.head()
df.info()
df.shape
df.describe()

df.values
df.columns
df.index

df.sort_values('columns_name', ascending=True)

df['columns_name'].mean()
df['columns_name'].median()
df['columns_name'].min()
df['columns_name'].max()
df['columns_name'].var()
df['columns_name'].std()

df['columns_name'].agg(pd.sum)

df['columns_name'].cumsum()
df['columns_name'].cummax()
df.drop_duplicates(subset=['name', 'breed'])  # 删除重复项
df['breed'].value_counts(sort=True, normalize=True)

dogs.groupby('color')['weight_kg'].mean()
dogs.groupby('color')['weight_kg'].agg([min, max, std])
dogs.groupby(['color', 'breed'])['weight_kg'].mean()

dogs.pivot_table(values='weight_kg', index='color', columns='breed')  # 数据透视表，默认求平均值
dogs.pivot_table(values='weight_kg', index='color', aggfunc=np.median)
dogs.pivot_table(values='weight_kg', index='color', fill_value=0, margins=True)

dogs = dogs.set_index('name')
dogs = dogs.set_index(['Labrador', 'Chihuahua'])
dogs.reset_index()

dogs.loc[['Labrador', 'Chihuahua']]
dogs.loc[[('Labrador', 'Brown'), ('Chihuahua', 'Tan')]]

dogs.sort_index()
dogs.sort_index(level=['color', 'breed'], ascending=[True, False])

dogs_srt = dogs.set_index(['breed', 'color']).sort_index()
dogs_srt.loc['Chow Chow':'Poodle']
dogs_srt.loc[('Labrador', 'Brown'):('Schnauzer', 'Gray')]
dogs_srt.loc[:, 'name':'height_cm']
dogs.iloc[2:5, 1:4]

temperatures['year'] = temperatures['date'].dt.year

import matplotlib.pyplot as plt

dog_pack['height_cm'].hist()
dog_pack['height_cm'].hist(bins=20)
plt.show()

avg_weight_by_breed.plot(kind='bar', title='Mean Weight by Dog Breed')

sully.plot(x='date', y='weight_kg', kind='line', rot=45)

dog_pack.plot(x='height_cm', y='weight_kg', kind='scatter')

dog_pack[dog_pack['sex'] == 'F']['height_cm'].hist(alpha=0.7)
dog_pack[dog_pack['sex'] == 'M']['height_cm'].hist(alpha=0.7)
plt.legend(['F', 'M'])
plt.show()

dogs.isna().any()
dogs.isna().sum()
dogs.isna().sum().plot(kind='bar')

dogs.dropna()
dogs.fillna(0)

new_dogs = pd.read_csv('new_dogs.csv')
new_dogs.to_csv('new_dogs_with_bmi.csv')