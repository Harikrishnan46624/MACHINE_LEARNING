from itertools import combinations

def generate_combinations(itemset, k):
    return combinations(itemset, k)

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if set(itemset).issubset(transaction):
            count += 1
    return count

def eclat(transactions, min_support):
    itemsets = set()
    for transaction in transactions:
        for item in transaction:
            itemsets.add(frozenset([item]))

    frequent_itemsets = {itemset for itemset in itemsets if calculate_support(itemset, transactions) >= min_support}
    k = 2

    while frequent_itemsets:
        new_itemsets = set()
        for itemset1 in frequent_itemsets:
            for itemset2 in frequent_itemsets:
                if len(itemset1.union(itemset2)) == k:
                    new_itemset = itemset1.union(itemset2)
                    support = calculate_support(new_itemset, transactions)
                    if support >= min_support:
                        new_itemsets.add(new_itemset)
        frequent_itemsets = new_itemsets
        itemsets.update(frequent_itemsets)
        k += 1
    return itemsets


# Sample transactions (replace this with your own dataset)
transactions = [
    {'A', 'B', 'C', 'D'},
    {'A', 'C'},
    {'B', 'D'},
    {'A', 'B', 'C'},
    {'A', 'B', 'D'},
    {'B', 'C', 'D'},
    {'A', 'B', 'C', 'D'},
]

min_support = 2

frequent_itemsets = eclat(transactions, min_support)

print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)
