def duplicate(list1):
    for i in list1:
        for j in range(i+1, len(list1)):
            if list1[i] == list1[j]:
                print(list1[i])
duplicate([1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7])


# list1 = [7,2,3,4,5,7,5]
# for i in range(len(list1)):
#     for j in range(0,i):
#         if list1[i] == list1[j]:
#             print(list1[i])