
def delete_duplicate(list1):
    l = len(list1)
    i = 0
    while i < l:
        j = i + 1
        while j < l:
            if list1[i] == list1[j]:
                del list1[j]
                l -= 1
            else:
                j += 1
        i += 1
numbers = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7]
delete_duplicate(numbers)
print(numbers)
