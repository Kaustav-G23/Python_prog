gift_presented_to = []
gift_presented_from = []

n = int(input("Enter the number of gifts presented : "))
for i in range(0, n):
    ele = int(input())
    gift_presented_to.append(ele)

x=1
y=0

for i in range(0,n):
    y=gift_presented_to[i]
    gift_presented_from.insert(y-1,x)
    x=x+1

print(gift_presented_from)
