a = int(input("請輸入一個三位數： "))
h = a//100
t = (a//10)%10
n = a%10
ans = ((n*100)+(t*10)+h)
print("結果： ",ans)