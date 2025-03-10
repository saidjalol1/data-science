# installlation command -->  pip install pandas
import pandas as pd

# Creating and Copying Series¶
my_integer_series = pd.Series(dtype="int64") #we should specify using "dtype" the type of data that Series can store , 
my_string_series = pd.Series(dtype="string")
# mixed data types stores
my_mixed_series = pd.Series(dtype="object")


# check the empty series objects
series_list = [my_mixed_series, my_integer_series, my_string_series]
for s in series_list:
    print(f"{s}, length = {len(s)}")
    

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Creating series from the existing data
integer_list = [11, 12, 13, 14, 15]
string_list = ['apple', 'banana', 'cherry', 'daikon', 'eggplant']
mixed_list = integer_list + string_list

# examples of creating series objects from existing data
integers = pd.Series(integer_list, dtype="int64")
strings = pd.Series(string_list, dtype="string")
mixed_types = pd.Series(mixed_list, dtype='object')

# check the series objects
my_data = [integers, strings, mixed_types]
for s in my_data:
    print(f"{s}, length = {len(s)}")
    

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////


"""
    Creating a Series with an Index¶
    When series is bieng created pandas assign range objeect to each row 
    but you can specify what should be index and what shoulkd be data while creating pandas series
    
"""

cars_list = ["bmw", "mercedes", "supra"]
prices = [23400, 45000, 50000]

series_cars  = pd.Series(data=cars_list, index=prices)
print(series_cars)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Examinign the big series

import random
integers_random = [ random.randint(1, 1000) for i in range(100000)]

big_series = pd.Series(data=integers_random)

# defaoult 5 row from the head of the series
print(big_series.head()) 

# optional row from the head of the series
print(big_series.head(20)) 

# defaoult 5 row from the tail of the series
print(big_series.tail()) 

# optional row from the tail of the series
print(big_series.tail(30)) 