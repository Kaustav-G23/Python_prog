def remove_list(lst, item):
    res=[i for i in lst if i!=item]
    return res


lst = []
n = int(input("Enter the number of inputs: "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

item = int(input("Enter the number to be removed: "))

print("The original list: "+ str(lst))
