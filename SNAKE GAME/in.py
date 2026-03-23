import pandas as pd
data = {'name': ['Ali', 'Bob', 'Charl', 'Dav', 'Emil', 'Fran'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 35, 40, 28, 30, 45],
        'salary': [50000, 70000, 60000, 80000, 65000, 90000]}
df = pd.DataFrame(data)
grouped = df.groupby('gender').mean()['salary']
print(grouped)