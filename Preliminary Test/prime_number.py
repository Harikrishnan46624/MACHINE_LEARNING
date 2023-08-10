list1 = []
for i in range(1, 101):
    if i == 0 and i == 1:
        continue
    else:
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                break
        else:
            list1.append(i)
print(list1)