import pandas as pd

# Series is the column in the table 
# The data frame is whole table

data = {
    "calories":[234,456,123],
    "durations":[20, 45, 67]
}

data_frame = pd.DataFrame(data)
print(data_frame)
print(data_frame.loc[1])

data_frame = pd.DataFrame(data=data, index= ["day1", "day2", "day3"])
print(data_frame)