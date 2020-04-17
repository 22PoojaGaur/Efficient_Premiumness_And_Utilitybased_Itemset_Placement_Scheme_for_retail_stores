
def evaluate(slots, test_transactions):
    f = open('evaluation.txt', 'w')
    TOTAL_REVENUE = 0
    NUM_TEST_TRANSACTION = 0
    NUM_TEST_PATTERN_FOUND = 0
    TEST_DRANK_MEAN = 0

    for transaction in test_transactions:
        NUM_TEST_TRANSACTION += 1
        t = tuple(transaction)
        for stype in range(0,len(slots)):
            for (item, price, drank) in slots[stype]:
                #print ('comparing ' + ' '.join(set(item)) + ' and ' + ' '.join(set(t)))
                if set(item) == set(t):
                   # print ('MATCHED')
                    TOTAL_REVENUE += price
                    NUM_TEST_PATTERN_FOUND += 1
                    TEST_DRANK_MEAN += drank
                    break
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

    return (TOTAL_REVENUE, str(TEST_DRANK_MEAN/float(NUM_TEST_PATTERN_FOUND)),
                NUM_TEST_PATTERN_FOUND, NUM_TEST_TRANSACTION)