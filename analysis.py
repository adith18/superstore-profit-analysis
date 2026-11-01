'''import pandas as pd
 df = pd.read_csv(r'E:\data analyst\storedata\Sample - Superstore.csv', encoding='latin1')
df.columns = df.columns.str.strip()

profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)

# Print ALL 17
for i, (name, value) in enumerate(profit.items(), 1):
    print(f"{i}. {name} = {round(value,2)}")'''



import pandas as pd
df = pd.read_csv(r'E:\data analyst\storedata\Sample - Superstore.csv', encoding='latin1')
df.columns = df.columns.str.strip()
profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False).head(5)
print(profit)
print("Rows:", len(profit))



import matplotlib.pyplot as plt

# Your Top 5 data
top5 = df.groupby('Sub-Category')['Profit'].sum().nlargest(5)

# Plot
top5.plot(kind='bar', color='green')
plt.title('Top 5 Profitable Sub-Categories')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



