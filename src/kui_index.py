from globals import *

def _sort_by_drank(nodes):
    return sorted(nodes, key=lambda x: x[-1], reverse=True)

def _get_kui_idx_with_hybrid_approach(data, dranks):
    '''
    data - dictionary input for data
    dranks - dictionary of dranks with itemset
    '''
    # we are using NR - alpha*NR window
    alpha = ALPHA

    # first find kui by without diversity method and then apply
    # windowed sort
    kui = _get_kui_idx_with_diversity(data, dranks, 'R')

    for i in kui.keys():
        # not applying this sorting for single itemset
        if i == 1:
            continue

        j = 0
        kui_level = []
        while j < len(kui[i]):
            # [NR, NR - alpha*NR]
            window = [kui[i][j][-2], kui[i][j][-2] - alpha*kui[i][j][-2]]

            to_sort = []
            # add all elements in window
            while j < len(kui[i]) and kui[i][j][-2] >= window[1]:
                to_sort.append(kui[i][j])
                j += 1

            kui_level.extend(_sort_by_drank(to_sort))
        kui[i] = kui_level
    return kui


def _get_kui_idx_without_diversity(data):
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
        kui[level].append(tuple(value))

    for level in range(1, K_FOR_KUI_IDX+1):
        sorted(kui[level], key=lambda x: x[-2], reverse=True)
        kui[level] = kui[level][0:LAMBDA]
        
    return kui

def _get_kui_idx_with_diversity(data, dranks, method):
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
        if level > K_FOR_KUI_IDX:
            continue
        kui[level].append(tuple(value))

    for level in range(1, K_FOR_KUI_IDX+1):
        if method == 'R':
            kui[level] = sorted(kui[level], key=lambda x: x[-2], reverse=True)
        if method == 'D':
            kui[level] = sorted(kui[level], key=lambda x: x[-1], reverse=True)
        kui[level] = kui[level][0:LAMBDA]

    return kui

def get_kui_index(data, dranks=None, method=None):
    '''
    Args -
        data: Dict. {itemset -> (sup_count, price)}
        dranks: Dict. {itemset -> drank}
        method: string. 'R', 'D' or 'H'
    '''
    
    if dranks is not None:
        print('CREATING KUI IDX WITH DIVERSITY')
        if method == 'D' or method == 'R':
            kui_idx = _get_kui_idx_with_diversity(data, dranks, method)
        elif method == 'H':
            kui_idx = _get_kui_idx_with_hybrid_approach(data, dranks)
    else:
        print ('CREATING KUI IDX WITHOUT DIVERSITY')
        kui_idx = _get_kui_idx_without_diversity(data)

    return kui_idx
