
def evaluate(slots, test_transactions):
    TOTAL_REVENUE = 0
    NUM_TEST_PATTERN_FOUND = 0

    for transaction in test_transactions:
        t = tuple(transaction)
        for stype in range(0,len(slots)):
            for (item, price, drank) in slots[stype]:
                #print ('comparing ' + ' '.join(set(item)) + ' and ' + ' '.join(set(t)))
                if set(item) == set(t):
                   # print ('MATCHED')
                    TOTAL_REVENUE += price
                    NUM_TEST_PATTERN_FOUND += 1
                    break
                #print ('NOT MATCHED')
    print('TOTAL REVENUE OF TEST PATTERNS PLACED ->')
    print(TOTAL_REVENUE)
    print('NUMBER OF TEST PATTERNS PLACED ->')
    print(NUM_TEST_PATTERN_FOUND)
    print(len(test_transactions))
    print (test_transactions[0:10])

    return