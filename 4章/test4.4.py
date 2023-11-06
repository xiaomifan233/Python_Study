#本题设定一年利息为3%,5年利息为5%
principal = 10000
total_amount_1year = 0
total_amount_5year = 0
for i in range(20):
    interest = principal *0.03
    total_amount_1year += principal+interest
    principal += interest
principal = 10000
for i in range(4):
    interest = principal *0.05
    total_amount_5year += principal+interest
    principal += interest
print('一年：',total_amount_1year)
print('五年：',total_amount_5year)