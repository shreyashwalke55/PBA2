import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print(df.head())
print(df.describe())
print(df.isnull().sum())

df["Salary"].plot(kind="hist")
plt.title("Salary Distribution")
plt.show()

df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.show()