
import globals

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
                NUM_TEST_PATTERN_FOUND, NUM_TEST_TRANSACTION)