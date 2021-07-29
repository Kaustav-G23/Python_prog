lst = []
n = int(input("Enter the number of inputs: "))
for i in range(0, n):
    ele = input()
    lst.append(ele)

lst.sort(reverse = True)
print(lst)
