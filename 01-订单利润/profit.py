# 第 1 课：用 Python 算一笔亚马逊订单的利润
# 以 # 开头的行是“注释”，给人看的，Python 会跳过。

# ① 变量：给一个数字起个名字，方便后面使用
price = 29.99          # 售价（美元）
cost = 8.50            # 进货成本
shipping = 4.20        # 头程运费 + FBA 配送费
commission_rate = 0.15 # 亚马逊佣金比例 15%

# ② 计算：和计算器一样，用 + - * /
commission = price * commission_rate
profit = price - cost - shipping - commission
margin = profit / price

# ③ 输出：print() 把结果显示出来
print("佣金：", round(commission, 2))
print("利润：", round(profit, 2))
print("利润率：", round(margin * 100, 1), "%")

# 🧩 小练习（自己动手改改看）：
# 1. 把 price 改成 24.99，利润变成多少？
# 2. 再加一个变量 ads = 3.00（广告费），把它也从利润里减掉。
