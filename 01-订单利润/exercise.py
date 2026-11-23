# 第 1 课练习：加入广告费（你自己写的答案）
price = 29.99
cost = 8.50
shipping = 4.20
commission_rate = 0.15
ads = 3.00             # 新增：广告费

commission = price * commission_rate
profit = price - cost - shipping - commission - ads

print("利润：", round(profit, 2))
print("利润率：", round(profit / price * 100, 1), "%")
