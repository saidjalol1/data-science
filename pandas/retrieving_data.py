import pandas as pd

car_names = ["bmw", "mercedes", "supra"]
car_price = [120000, 130000, 10000]

series = pd.Series(data=car_price, index=car_names)
# print(series.index)
# print(series.values)


# accessign the data with index
# print(series.loc[120000:10000])
# print(series[120000])

# like python list
# print(series.iloc[1:3])


mask_to_filter = (series >= 100000)

print(series.loc[mask_to_filter])

