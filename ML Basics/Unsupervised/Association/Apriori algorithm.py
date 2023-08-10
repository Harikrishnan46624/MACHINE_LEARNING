def generate_candidates(prev_candidates, k):
    candidates = set()
    for itemset1 in prev_candidates:
        for itemset2 in prev_candidates:
            union_set = itemset1.union(itemset2)
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count / len(transactions)

def apriori(transactions, min_support, min_confidence):
    # Step 1: Generate frequent 1-itemsets
    itemsets = set()
    for transaction in transactions:
        for item in transaction:
            itemsets.add(frozenset([item]))

    frequent_itemsets = {itemset for itemset in itemsets if calculate_support(itemset, transactions) >= min_support}
    k = 2

    # Step 2: Generate frequent k-itemsets (k > 1)
    while frequent_itemsets:
        candidates = generate_candidates(frequent_itemsets, k)
        frequent_itemsets = {
            itemset for itemset in candidates if calculate_support(itemset, transactions) >= min_support
        }
        itemsets.update(frequent_itemsets)
        k += 1

    # Step 3: Generate association rules
    association_rules = []
    for itemset in itemsets:
        if len(itemset) > 1:
            for item in itemset:
                antecedent = frozenset([item])
                consequent = itemset - antecedent
                confidence = calculate_support(itemset, transactions) / calculate_support(antecedent, transactions)
                if confidence >= min_confidence:
                    association_rules.append((antecedent, consequent, confidence))

    return itemsets, association_rules


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

min_support = 0.3
min_confidence = 0.7

frequent_itemsets, association_rules = apriori(transactions, min_support, min_confidence)

print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)

print("\nAssociation Rules:")
for rule in association_rules:
    antecedent, consequent, confidence = rule
    print(f"{antecedent} => {consequent} (Confidence: {confidence:.2f})")
