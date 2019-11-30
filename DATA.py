import pandas as p
df=p.read_csv("D:\\Automobile_data.csv")
#df.head(5)
#df.tail(5)
#print(df.head(5))
#print(df.tail(5))

df=p.read_csv("D:\\Automobile_data.csv",na_values={'price':["?","na"]})
#print(df)

#df=df[["company","price"]][df.price==df['price'].max()]
#print(df)
#
#car_manufactures=df.groupby('company')
#toyotadf=car_manufactures.get_group('toyota')
#print(toyotadf)
#
#car_manufactures=df.groupby('company')
#pricedf=car_manufactures['company','price'].max()
#print(pricedf)
#
#car_manufactures=df.groupby('company')
#pricedf=car_manufactures['company','average-mileage'].mean()
#print(pricedf)

df['company'].value_counts()
print(df)