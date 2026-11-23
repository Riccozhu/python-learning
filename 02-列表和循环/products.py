# 第 2 课：列表和循环 —— 一次算多个产品的利润

# ① 列表：用方括号 [ ] 把多个数据装在一起，用逗号隔开
names  = ["手机壳", "数据线", "充电头", "支架"]
prices = [29.99,    12.99,    19.99,    15.99]
costs  = [8.50,     3.20,     6.80,     4.10]

shipping = 4.20
commission_rate = 0.15

# ② 循环：for ... in range(...) 让同一段代码重复执行
#    len(names) 是列表里有几个东西（这里是 4）
#    i 会依次变成 0, 1, 2, 3 —— 列表的“位置编号”从 0 开始数
for i in range(len(names)):
    profit = prices[i] - costs[i] - shipping - prices[i] * commission_rate
    print(names[i], "利润：", round(profit, 2))

# 🧩 小练习：在三个列表最后各加一个新产品
#    比如 "耳机套"，售价 9.99，成本 2.50，看看它的利润是多少？
