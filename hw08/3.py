potato_demand = int(input())

# 使用动态规划计算斐波那契数列
fib = [1, 1]
total_potato = sum(fib)
while total_potato < potato_demand:
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)
    total_potato += next_fib

# 输出最少需要几天才能种出所需土豆
print(len(fib))
