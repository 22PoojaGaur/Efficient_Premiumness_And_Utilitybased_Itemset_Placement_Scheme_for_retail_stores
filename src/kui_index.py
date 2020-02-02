K_FOR_KUI_IDX = 4

def get_kui_idx_without_diversity(data):
    '''
    data - dictionary input for data.
        key -> tuple of itemsets
        value -> tuple of (support, price)
    '''
    kui = {}
    
    # Initialize all levels for dict
    for i in range(1, K_FOR_KUI_IDX+1):
        kui[i] = []
    
    # Insert all itemsets in kui
    for itemset in data.keys():
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

    return kui

def get_kui_idx_with_diversity(data, dranks, method):
    '''
    data - dictionary input for data.
        key -> tuple of itemset
        value -> tuple of (support, price)
    dranks -> drank value for itemsets.
        key -> tuple of itemset
        value -> drank value of itemset

    method -> string
        'R', 'D' or 'H'
    '''
    kui = {}

    # Initialize all levels for dict
    for i in range(1, K_FOR_KUI_IDX+1):
        kui[i] = []

    # Insert all itemsets in kui
    for itemset in data.keys():
        value = list([itemset]) + list(data[itemset]) + [data[itemset][0] * data[itemset][1]] + [dranks[itemset]]
        level = len(itemset)
        if (len(itemset) > K_FOR_KUI_IDX):
            continue
        # use insertion sort to maintain sorted order at level
        for i in range(0, len(kui[level])):
            if method == 'R':
                if value[-2] < kui[level][i][-2]:
                    kui[level].insert(i, tuple(value))
                    break
            elif method == 'D':
                if value[-1] < kui[level][i][-1]:
                    kui[level].insert(i, tuple(value))
                    break
        else:
            kui[level].append(tuple(value))


    return kui

def get_kui_index(data, dranks=None, method=None):
    
    if dranks is not None:
        print('CREATING KUI IDX WITH DIVERSITY')
        kui_idx = get_kui_idx_with_diversity(data, dranks, method)
    else:
        print ('CREATING KUI IDX WITHOUT DIVERSITY')
        kui_idx = get_kui_idx_without_diversity(data)

    return kui_idx
