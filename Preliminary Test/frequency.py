def frequency(list1):
    freq = {}
    for i in list1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i, j in freq.items():
        print(f"The Number {i} appears {j}")
frequency([1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7])