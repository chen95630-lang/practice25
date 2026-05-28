import pandas as pd

# 讀取 CSV
df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset 2.csv")

# 顯示前幾筆資料
print("資料前五筆：")
print(df.head())

# (1) 計算每個商品的總庫存價值
# 假設：
# Inventory = 庫存數量
# Price = 單價

df["Total_Inventory_Value"] = df["Inventory"] * df["Price"]

print("\n每個商品的總庫存價值：")
print(df[["Product", "Total_Inventory_Value"]])

# (2) 找出最暢銷商品
# 假設 Sales 欄位代表銷售量

best_selling = df.loc[df["Sales"].idxmax()]

print("\n最暢銷商品：")
print(best_selling["Product"])
print("銷售量：", best_selling["Sales"])

# (3) 計算 9 折後收入

df["Revenue_After_Discount"] = df["Sales"] * df["Price"] * 0.9

total_revenue = df["Revenue_After_Discount"].sum()

print("\n9折後總收入：")
print(total_revenue)