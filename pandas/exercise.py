import pandas as pd

data = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age":[25, 30, 35],
    "City":["New York", "Chicago", "Los Angels"],
    "Salary":[70000, 80000, 90000]
}

frame = pd.DataFrame(data)

# Whole frame
print(frame)

# first and last row
print(frame.loc[0])
print(frame.iloc[-1])

# Add column
series = [2,5,10]
frame["Experiece"] = series
print(frame)

# find avarage salary
# frame = frame.groupby(by=frame["Salary"])

# filter
sorted_vlas = frame.sort_values(by="Salary")
print(sorted_vlas.loc[frame["Salary"] > 75000])

