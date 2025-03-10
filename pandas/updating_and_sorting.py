import pandas as pd
# Updating and sorting


books_names = ["Game of thrones", "Crime and Sentence","Sumerki"]
books_price = [50000, 30000, 10000]

series = pd.Series(data=books_price, index=books_names)
print(series)

series.loc["Sumerki"] = 100000
print(series)


# basic operations
series = series - 10000
print(series)

series = series + 10000
print(series)

series = series * 10000
print(series)

series = series / 10000
print(series)

