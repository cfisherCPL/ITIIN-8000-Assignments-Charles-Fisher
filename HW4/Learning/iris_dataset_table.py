from sklearn.datasets import load_iris
import pandas as pd


data = load_iris()
df = pd.DataFrame(data.data,
                  columns=data.feature_names)

print(df.to_string())

df.to_csv('iris_table.csv')
