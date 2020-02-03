'''
Given arc, kui index, data dictionary, slots
Runs PRIP algorithm and returns slots.
'''

def PRIP(data_dict, kui_idx, arc, slot_sizes):
    #print(kui_idx.keys())
    ITEMS_PLACED = 0
    TOTAL_REVENUE = 0
    SLOT_WISE_REVENUE = {}

    # print(slot_sizes)
    s_type = 0
    item_placed = 0
    slot_type_arr = []
    CAS = []

    num_slots = len(slot_sizes)
    for i in range(0, num_slots):
        SLOT_WISE_REVENUE[i] = 0
    # print('NUM_SLOTS')
    # print(num_slots)
    total_slots = 0
    slots = []
    for i in range(0, num_slots):
        CAS.append(len(slot_sizes[i]))
        total_slots += len(slot_sizes[i])
        slots.append([])
    
    # placing 1 itemsets
    Y = []
    for i in range(0, num_slots):
        Y.append(int((len(slot_sizes[i])/float(total_slots))*len(arc.keys())))
    else:
        Y[num_slots-1] += len(arc.keys()) - sum(Y)

    # Adjusting CAS
    for i in range(0, num_slots):
        CAS[i] -= Y[i]

    # sorting ARC by value
    arc_sorted = {k: v for k, v in sorted(arc.items(), key=lambda item: item[1])}

    print('LENGTH ARC ->')
    print(len(arc_sorted.keys()))
    print('KUI FOR 1 LENGTH ->')
    print(len(kui_idx[1]))

    for (item, price) in arc_sorted.items():
        placed = False
        while not placed:
            if Y[s_type] != 0:
                slots[s_type].append((item,))
                item_placed += 1
                ITEMS_PLACED += 1
                #TOTAL_REVENUE += kui_idx[(item,)][-1]
                Y[s_type] -= 1
                placed = True
            if(Y[s_type] == 0):
                s_type += 1
            if s_type == num_slots:
                break

    #print ('SLOTS')
    #print (slots)

    # Scan kUI Index to fill remaining slots
    h = []
    for i in range(0, len(kui_idx.keys())+1):
        h.append(0)
    stype = 0
    can_place_more = True
    
    while stype < num_slots:
        
        for lv in range(2, len(kui_idx.keys())+1):
            #print('.', end='')
            if can_place_more == False:
                break
            # if the slot type is filled
            if CAS[stype] <= 0:
                can_place_more = False
                break
            # if there is not enough space to place itemset
            if CAS[stype] < lv:
                placed = False
                while not placed:
                    lv -= 1
                    if lv <= 1 or CAS[stype] <= 0:
                        can_place_more = False
                        break
                    if h[lv] >= len(kui_idx[lv]):
                        lv -= 1
                        continue
                    if CAS[stype] >= lv:
                        # if h[lv] >= len(kui_idx[lv]):
                        #     continue
                        # print('lv h[lv]')
                        # print(lv)
                        # print(h[lv])
                        itemset = kui_idx[lv][h[lv]][0]
                        slots[stype].append(itemset)
                        ITEMS_PLACED += len(itemset)
                        SLOT_WISE_REVENUE[stype] += kui_idx[lv][h[lv]][-1]
                        TOTAL_REVENUE += kui_idx[lv][h[lv]][-1] * (1.0 / (stype+1))
                        h[lv] += 1
                        CAS[stype] = CAS[stype] - lv
                        placed = True
                        break
            else:
                if h[lv] >= len(kui_idx[lv]):
                    continue
                itemset = kui_idx[lv][h[lv]][0]
                slots[stype].append(itemset)
                ITEMS_PLACED += len(itemset)
                SLOT_WISE_REVENUE[stype] += kui_idx[lv][h[lv]][-1]
                TOTAL_REVENUE += kui_idx[lv][h[lv]][-1] * (1.0/ (stype+1))
                h[lv] += 1
                CAS[stype] = CAS[stype] - lv
        if can_place_more == False:
            print('THE SLOT TYPES COMPLETED SO CONTINUE')
            stype += 1
            can_place_more = True

    print('ITEMS_PLACED ->')
    print(ITEMS_PLACED)
    print('TOTAL ITEMS ->')
    print(sum([len(k) for k in data_dict.keys()]))
    print('TOTAL_SLOTS ->')
    print(total_slots)
    print('TOTAL_REVENUE ->')
    print(TOTAL_REVENUE)
    print ('SLOT WISE REVENUE ->')
    print (SLOT_WISE_REVENUE)
    return slots