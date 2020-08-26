import random
import globals

def calculate_diversification(itemsets):
    ''' Calculates diversification of itemsets using Parul's approach'''
    assert type(itemsets) == list

    unique_items = set()

    for itemset in itemsets:
        for item in itemset:
            unique_items.add(item)

    return len(unique_items) / len(itemsets)


def evaluate_new(slots, test_transactions):
    TOTAL_REVENUE = 0
    NUM_TEST_TRANSACTION = 0 
    NUM_TEST_PATTERN_FOUND = 0
    TEST_DRANK_MEAN = 0

    for transaction in test_transactions:
        itemset = tuple(transaction)
        NUM_TEST_TRANSACTION += 1

        for stype in range (0, len(slots)):
            for (item, price, drank) in slots[stype]:
                if tuple(item) == itemset:
                    prob_value = random.randint(0, 1000)
                    if stype == 2 and prob_value < 600:
                            TOTAL_REVENUE += price
                            NUM_TEST_PATTERN_FOUND += 1
                            TEST_DRANK_MEAN += drank

                    elif stype == 1 and prob_value < 800:
                            TOTAL_REVENUE += price
                            NUM_TEST_PATTERN_FOUND += 1
                            TEST_DRANK_MEAN += drank

                    elif stype ==0 :
                        TOTAL_REVENUE += price
                        NUM_TEST_PATTERN_FOUND += 1
                        TEST_DRANK_MEAN += drank

    print('\nTOTAL REVENUE OF TEST PATTERNS PLACED ->\n')
    print(str(TOTAL_REVENUE))
    print('\n\nNUMBER OF TEST PATTERNS PLACED ->\n')
    print(str(NUM_TEST_PATTERN_FOUND))
    print('\n\nTOTAL NUMBER OF TEST PATTERNS ->\n')
    print(str(NUM_TEST_TRANSACTION))
    print('\n\nMEAN DRANK OF TESTING ->\n')
    drank_mean = 0
    if NUM_TEST_PATTERN_FOUND != 0:
        drank_mean = TEST_DRANK_MEAN / float(NUM_TEST_PATTERN_FOUND)
    #print(str(TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND)))

    all_transactions = []

    for stype in range(len(slots)):
        for slot in slots[stype]:
            all_transactions.append(slot[0])
    diversification = calculate_diversification(all_transactions)

    return (TOTAL_REVENUE, drank_mean, NUM_TEST_PATTERN_FOUND, NUM_TEST_TRANSACTION, diversification)


def evaluate(slots, test_transactions):
    f = open('evaluation.txt', 'w')
    TOTAL_REVENUE = 0
    NUM_TEST_TRANSACTION = 0
    NUM_TEST_PATTERN_FOUND = 0
    TEST_DRANK_MEAN = 0

    all_transactions = []
    prices = {}
    dranks = {}
    for stype in range (0, len(slots)):
        for (item, price, drank) in slots[stype]:
            all_transactions.append(set(item))
            prices[tuple(item)] = price
            dranks[tuple(item)] = drank

    NOT_IN_TEST = []

    for transaction in test_transactions:
        t = tuple(transaction)
        if len(t) > globals.K_FOR_KUI_IDX:
            continue
        NUM_TEST_TRANSACTION += 1
        if set(t) in all_transactions:
            try:
                TOTAL_REVENUE += prices[t]
                NUM_TEST_PATTERN_FOUND += 1
                TEST_DRANK_MEAN += dranks[t]
            except KeyError:
                continue

        else:
            NOT_IN_TEST.append(t)

        # for stype in range(0,len(slots)):
        #     for (item, price, drank) in slots[stype]:
        #         #print ('comparing ' + ' '.join(set(item)) + ' and ' + ' '.join(set(t)))
        #         if set(item) == set(t):
        #            # print ('MATCHED')
        #             TOTAL_REVENUE += price
        #             NUM_TEST_PATTERN_FOUND += 1
        #             TEST_DRANK_MEAN += drank
        #             break
                #print ('NOT MATCHED')
    f.write('\nTOTAL REVENUE OF TEST PATTERNS PLACED ->\n')
    f.write(str(TOTAL_REVENUE))
    f.write('\n\nNUMBER OF TEST PATTERNS PLACED ->\n')
    f.write(str(NUM_TEST_PATTERN_FOUND))
    f.write('\n\nTOTAL NUMBER OF TEST PATTERNS ->\n')
    f.write(str(NUM_TEST_TRANSACTION))
    f.write('\n\nMEAN DRANK OF TESTING ->\n')
    f.write(str(TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND)))

    print('\nTOTAL REVENUE OF TEST PATTERNS PLACED ->\n')
    print(str(TOTAL_REVENUE))
    print('\n\nNUMBER OF TEST PATTERNS PLACED ->\n')
    print(str(NUM_TEST_PATTERN_FOUND))
    print('\n\nTOTAL NUMBER OF TEST PATTERNS ->\n')
    print(str(NUM_TEST_TRANSACTION))
    print('\n\nMEAN DRANK OF TESTING ->\n')
    print(str(TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND)))


    print ('NOT IN TESTING \n')
    # print (NOT_IN_TEST)

    return (TOTAL_REVENUE, TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND),
                NUM_TEST_PATTERN_FOUND, NUM_TEST_TRANSACTION, diversification)