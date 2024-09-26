a = int(input("請輸入一個三位數： "))
h = a//100
t = (a//10)%10
n = a%10
ans = h+t+n
print("每位數字的總和： ",ans)
