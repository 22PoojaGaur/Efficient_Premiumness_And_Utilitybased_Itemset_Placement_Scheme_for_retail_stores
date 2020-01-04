K_FOR_KUI_IDX = 4

def get_kui_index_and_arc(data):
    '''
    data - dictionary input for data.
        key -> tuple of itemsets
        value -> tuple of (support, price)
    '''
    kui = {}
    arc = {}
    # Initialize all levels for dict
    for i in range(1, K_FOR_KUI_IDX+1):
        kui[i] = []
    
    # Insert all itemsets in kui
    for itemset in data.keys():
        for item in itemset:
            if item not in arc:
                arc[item] = (data[itemset][0] * data[itemset][1]) / len(itemset)
            arc[item] += (data[itemset][0] * data[itemset][1]) / len(itemset)
        value = list([itemset]) + list(data[itemset]) + [data[itemset][0] * data[itemset][1]]
        level = len(itemset)
        if (len(itemset) > K_FOR_KUI_IDX):
            continue
        # use insertion sort to maintain sorted order at level
        for i in range(0, len(kui[level])):
            if value[-1] < kui[level][i][-1]:
                kui[level].insert(i, tuple(value))
                break
        else:
            kui[level].append(tuple(value))

    return (kui, arc)
