# -*- coding: utf-8 -*-
import pandas
file = pandas.read_csv("country_data.csv")
print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan

"""

print(file.info())

"""
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes
None

"""
print(file.describe())

"""
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000

"""

file2 = pandas.read_csv("iris.csv")
print(file2)

"""
     sepal_length  sepal_width  petal_length  petal_width         species
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica

[150 rows x 5 columns]

"""

file3 = pandas.read_csv("diab_data.csv")
print(file3)

"""
     preg_count  glucose  bp  skinfold  insulin   BMI  predigree  age  class
0             6      148  72        35        0  33.6      0.627   50      1
1             1       85  66        29        0  26.6      0.351   31      0
2             8      183  64         0        0  23.3      0.672   32      1
3             1       89  66        23       94  28.1      0.167   21      0
4             0      137  40        35      168  43.1      2.288   33      1
..          ...      ...  ..       ...      ...   ...        ...  ...    ...
763          10      101  76        48      180  32.9      0.171   63      0
764           2      122  70        27        0  36.8      0.340   27      0
765           5      121  72        23      112  26.2      0.245   30      0
766           1      126  60         0        0  30.1      0.349   47      1
767           1       93  70        31        0  30.4      0.315   23      0

[768 rows x 9 columns]

"""

file4 = pandas.read_csv("housing_data.csv")
print(file4)

"""
     0.00632   18   2.31    0  0.538  6.575  ...  1    296  15.3   396.9  4.98    24
0    0.02731  0.0   7.07  0.0  0.469  6.421  ...  2  242.0  17.8  396.90  9.14  21.6
1    0.02729  0.0   7.07  0.0  0.469  7.185  ...  2  242.0  17.8  392.83  4.03  34.7
2    0.03237  0.0   2.18  0.0  0.458  6.998  ...  3  222.0  18.7  394.63  2.94  33.4
3    0.06905  0.0   2.18  0.0  0.458  7.147  ...  3  222.0  18.7  396.90  5.33  36.2
4    0.02985  0.0   2.18  0.0  0.458  6.430  ...  3  222.0  18.7  394.12  5.21  28.7
..       ...  ...    ...  ...    ...    ...  ... ..    ...   ...     ...   ...   ...
500  0.06263  0.0  11.93  0.0  0.573  6.593  ...  1  273.0  21.0  391.99  9.67  22.4
501  0.04527  0.0  11.93  0.0  0.573  6.120  ...  1  273.0  21.0  396.90  9.08  20.6
502  0.06076  0.0  11.93  0.0  0.573  6.976  ...  1  273.0  21.0  396.90  5.64  23.9
503  0.10959  0.0  11.93  0.0  0.573  6.794  ...  1  273.0  21.0  393.45  6.48  22.0
504  0.04741  0.0  11.93  0.0  0.573  6.030  ...  1  273.0  21.0  396.90  7.88  11.9

[505 rows x 14 columns]

"""
column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
file4 = pandas.read_csv("housing_data.csv",names=column_names)
print(file4)
file5 = pandas.read_csv("insurance_data.csv",skiprows=(6))
print(file5)

"""
      X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5

[63 rows x 2 columns]

"""

# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)

"""
30
40

"""

#Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

"""
[30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39]

"""

#Lists indexes start at 0 which has the value of 30

print(age[0])
print(age[1])
print(age[10])

"""
30
40
39

"""

#This will give an error since there is no value in index 11

#print(age[11])

#Basic stats

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

"""
22
49
11
367
33.36363636363637

"""

#Storing text

#C2 = M
#C3 = M
#C4 = F

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

"""
M
M
F

"""

#Gender list

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])


"""
M
M
F
M

"""
#Country list

country = ["South Africa","Botswanna","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])

"""
['South Africa', 'Botswanna', 'South Africa', 'South Africa', 'Kenya', 'Mozambique', 'Lesotho', 'Kenya', 'Kenya', 'Egypt', 'Sudan']
South Africa
Mozambique

"""

# Data storage with lists

my_list = [42, -2021, 6.283, "tau", "node"]
print(my_list)

"""
[42, -2021, 6.283, 'tau', 'node']

"""

print(my_list[:])

"""
[42, -2021, 6.283, 'tau', 'node']

"""

my_list.append("pi")
print(my_list)

"""
[42, -2021, 6.283, 'tau', 'node', 'pi']

"""

my_list.insert(1,"pi2")
print(my_list)

"""
[42, 'pi2', -2021, 6.283, 'tau', 'node', 'pi']

"""

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)

"""
[42, -2021, 6.283, 'node']

"""

print(len(my_list))

"""
4

"""

#View certain range of items

print(my_list[0:3])

"""
[42, -2021, 6.283]

"""

#d = {'key1': 'value1', 'key2': 'value2'}
person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'
print(person['phone'])

"""
John Doe
30
555-555-5555

"""


import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

#Displaying the DataFrame
print(df)

"""
    age gender       country
0    30      M  South Africa
1    40      M      Botswana
2    30      F  South Africa
3    49      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    46      M         Kenya
8    29      M         Kenya
9    25      F         Egypt
10   39      M         Sudan

"""

# Accessing specific columns
print(df['age'])
print(df['gender'])

"""
0     30
1     40
2     30
3     49
4     22
5     35
6     22
7     46
8     29
9     25
10    39

0     M
1     M
2     F
3     M
4     F
5     F
6     F
7     M
8     M
9     F
10    M

"""

# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

"""
22
49
33.36363636363637

"""

# Filtering data
print(df[df['age'] > 30])

"""
    age gender       country
1    40      M      Botswana
3    49      M  South Africa
5    35      F    Mozambique
7    46      M         Kenya
10   39      M         Sudan

"""

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

"""
   age gender       country
1   40      M      Botswana
2   30      F  South Africa
3   49      M  South Africa

"""


# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

"""
    age gender       country  new_column
0    30      M  South Africa           1
1    40      M      Botswana           2
2    30      F  South Africa           3
3    49      M  South Africa           4
4    22      F         Kenya           5
5    35      F    Mozambique           6
6    22      F       Lesotho           7
7    46      M         Kenya           8
8    29      M         Kenya           9
9    25      F         Egypt          10
10   39      M         Sudan          11

"""

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)

"""
    age gender       country
0    30      M  South Africa
1    40      M      Botswana
2    30      F  South Africa
3    49      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    46      M         Kenya
8    29      M         Kenya
9    25      F         Egypt
10   39      M         Sudan
"""
