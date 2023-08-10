
def odd_num(list1):
    odd = []
    for i in list1:
        if i % 2 != 0:
            odd.append(i)
    print(odd)
odd_num([7,8,9,5,3,44,8])