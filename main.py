import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset 2.csv")

# 將價格欄位轉換成數字格式
df["Unit_Price"] = (
    df["Unit_Price"]
    .replace("[$,]", "", regex=True)
    .astype(float)
)

# 顯示資料前五筆
print("===== 資料前五筆內容 =====")
print(df.head())

# (1) 計算每個商品的總庫存價值
df["商品總庫存價值"] = (
    df["Stock_Quantity"] * df["Unit_Price"]
)

print("\n===== (1) 各商品的總庫存價值 =====")
print(df[["Product_Name", "商品總庫存價值"]])

# (2) 找出最暢銷商品
best_selling = df.loc[df["Sales_Volume"].idxmax()]

print("\n===== (2) 最暢銷商品分析 =====")
print("最暢銷商品名稱：", best_selling["Product_Name"])
print("商品銷售量：", best_selling["Sales_Volume"])

# (3) 計算 9 折後收入
df["9折後收入"] = (
    df["Sales_Volume"] * df["Unit_Price"] * 0.9
)

total_revenue = df["9折後收入"].sum()

print("\n===== (3) 商品 9 折後的總收入 =====")
print("9折後總收入：", total_revenue)