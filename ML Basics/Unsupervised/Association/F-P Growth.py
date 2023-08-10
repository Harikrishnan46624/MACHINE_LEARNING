from collections import defaultdict



class FPNode:
    def __init__(self, item, count=1, parent=None):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = defaultdict(lambda: FPNode(None))
        self.node_link = None

def construct_FP_tree(transactions, min_support):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    frequent_items = {item: count for item, count in item_counts.items() if count >= min_support}
    if not frequent_items:
        return None, {}

    sorted_frequent_items = sorted(frequent_items.items(), key=lambda x: (-x[1], x[0]))

    root = FPNode(None, 0, None)
    header_table = {}
    for item, count in sorted_frequent_items:
        header_table[item] = None

    for transaction in transactions:
        filtered_transaction = [item for item in transaction if item in frequent_items]
        if filtered_transaction:
            insert_transaction(filtered_transaction, root, header_table)

    return root, header_table

def insert_transaction(transaction, node, header_table):
    if not transaction:
        return

    item = transaction[0]
    child = node.children[item]
    child.count += 1

    if not header_table[item] or header_table[item] is child:
        header_table[item] = child

    if len(transaction) > 1:
        insert_transaction(transaction[1:], child, header_table)

def find_prefix_paths(item, header_table):
    node = header_table[item]
    prefix_paths = []

    while node is not None:
        prefix_path = []
        current_node = node
        while current_node.parent is not None:
            prefix_path.append(current_node.item)
            current_node = current_node.parent
        if prefix_path:
            prefix_paths.append((prefix_path[::-1], node.count))
        node = node.node_link

    return prefix_paths

def fp_growth(header_table, prefix, min_support, frequent_itemsets):
    sorted_items = [item[0] for item in sorted(header_table.items(), key=lambda x: (x[1].count, x[0]))]
    for item in sorted_items:
        new_prefix = prefix.copy()
        new_prefix.append(item)
        support = header_table[item].count
        frequent_itemsets.append((new_prefix, support))

        prefix_paths = find_prefix_paths(item, header_table)
        conditional_tree, conditional_header_table = construct_FP_tree([path for path, _ in prefix_paths], min_support)

        if conditional_header_table:
            fp_growth(conditional_header_table, new_prefix, min_support, frequent_itemsets)

def fpgrowth(transactions, min_support):
    frequent_itemsets = []
    root, header_table = construct_FP_tree(transactions, min_support)
    if root is not None:
        fp_growth(header_table, [], min_support, frequent_itemsets)
    return frequent_itemsets


# Sample transactions (replace this with your own dataset)
transactions = [
    ['A', 'B', 'C', 'D'],
    ['A', 'C'],
    ['B', 'D'],
    ['A', 'B', 'C'],
    ['A', 'B', 'D'],
    ['B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
]

min_support = 2

frequent_itemsets = fpgrowth(transactions, min_support)

print("Frequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(itemset, support)
