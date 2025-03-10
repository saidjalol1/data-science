import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999

fname = "data.csv"
frame = pd.read_csv(fname)
print(frame.info())
print(frame)


# frame.dropna(inplace=True)
removed_nulls = frame.dropna()
print(removed_nulls.info())
print(removed_nulls)


# filled_nulls = frame.fillna("dhwqhu")
frame["Calories"].fillna(130, inplace= True)
print(frame)


x = frame["Calories"].mean()
frame["Calories"].fillna(x)


# Wrong format
frame["Calories"] = pd.to_numeric(frame["Calories"])
print(frame)

print(frame.duplicated())
frame.drop_duplicates(inplace=True)
print(frame.duplicated())

# relations 
print(frame.corr())

frame.plot(kind="hist")
plt.show()