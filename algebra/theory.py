from algebra.ops import conjugation_map

def Inn(G):
    inn_list = []
    for g in G.elements:
        mapping = conjugation_map(G, g)
        if not any(mapping == m for m in inn_list):
            inn_list.append(mapping)
    return inn_list

