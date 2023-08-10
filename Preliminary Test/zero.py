def zero(list1):
    count = 0
    n = len(list1)
    for i in range(n):
        if list1[i] != 0:
            list1[count] = list1[i]
            count += 1

    while count < n:
        list1[count] = 0
        count += 1
    print(list1)

zero([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])



