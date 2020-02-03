from __future__ import division


def calculate_nodes_in_projection(patterns, ch_dict=None):
    if ch_dict is None:
        raise ValueError
    nodes_in_proj = set()

    for item in patterns:
        path = set(ch_dict[item.replace(' ', '_')])
        # print  [node.value for node in path]
        nodes_in_proj = nodes_in_proj | path
    return len(nodes_in_proj)


def calculate_drank(patterns, ch_dict=None, ch_height=None):
    if ch_dict is None or ch_height is None:
        raise ValueError

    num_node_in_proj = calculate_nodes_in_projection(patterns, ch_dict=ch_dict)
    num_item_in_pat = len(patterns)
    h = ch_height

    try:
        drank = (num_node_in_proj - (num_item_in_pat + h - 1)) / (
            (h-1)*(num_item_in_pat -1))
    except ZeroDivisionError as e:
        drank = "NOT PROCESSED"

    return drank


def get_dranks(freq_patterns, item_path_dict):
    ch_height = 0
    for item in item_path_dict.keys():
        if len(item_path_dict[item]) > ch_height:
            ch_height = len(item_path_dict[item])

    # print("concept hierarchy height")
    # print (ch_height)
    dranks = {}
    idx = 0
    for patterns in freq_patterns:
        # print("processing pattern %s", ' '.join(patterns), '\n')
        try:
            # calculate drank
            dranks[patterns] = calculate_drank(patterns, ch_dict=item_path_dict, ch_height=ch_height)
        except KeyboardInterrupt:
            dranks[patterns] = "SKIPPED"
        idx += 1

    return dranks
