from itertools import product
from algebra.homomorphism import GroupHom

# 共役
def conjugate(G, g, x):
    return G.multiply(G.multiply(g, x), G.inverse(g))

# 共役写像
def conjugation_map(G, g):
    mapping = {}
    inv_g = G.inverse(g)

    for x in G.elements:
        # φ_g(x) = g x g^{-1}
        mapping[x] = G.multiply(G.multiply(g, x), inv_g)

    return GroupHom(G, G, mapping)

# 交換子[g1, g2] = g1g2g1^(-1)g2^(-1)
def commutator(G, a, b):
    return G.multiply(G.multiply(a, b), G.multiply(G.inverse(a), G.inverse(b)))

# 中心
def center(G):
    return {
        x
        for x in G.elements
        if all(G.multiply(x, y) == G.multiply(y, x) for y in G.elements)
    }

# 交換子部分群[G, G]
def commutator_subgroup(G):
    elems = G.elements
    comms = {commutator(G, a, b) for a, b in product(elems, repeat=2)}
    return comms

def pick_one(G):
    return next(iter(G.elements))
