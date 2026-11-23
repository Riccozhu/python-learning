# 第 2 课练习：加入「耳机套」（你的答案，修正了一个中文逗号）
names  = ["手机壳", "数据线", "充电头", "支架", "耳机套"]
prices = [29.99, 12.99, 19.99, 15.99, 9.99]
costs  = [8.50, 3.20, 6.80, 4.10, 2.50]

shipping = 4.20
commission_rate = 0.15

for i in range(len(names)):
    profit = prices[i] - costs[i] - shipping - prices[i] * commission_rate
    print(names[i], "利润：", round(profit, 2))
