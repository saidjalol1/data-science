import pandas as pd


pd.options.display.max_rows = 20

fname = "data.csv"

frame = pd.read_csv(fname)
print(frame.to_string())
print(frame)


fname = "data.json"

frame = pd.read_json(fname)
print(frame)

print(frame.info())