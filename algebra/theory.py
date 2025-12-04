from algebra.ops import conjugation_map
from algebra.homomorphism import GroupHom
from itertools import product


def Inn(G):
    return {conjugation_map(G, g) for g in G.elements}

def Auto(G):
    autos = set()
    gens = G.generators
    elems = list(G.elements)

    # 生成元の像の候補（全体 G.elements）
    candidates = [elems] * len(gens)

    # 生成元の像の全組合せを列挙
    for images in product(*candidates):
        gen_map = dict(zip(gens, images))

        # 生成元から全元への mapping を作成
        mapping = {}
        for x in elems:
            # x を生成元の積で表す（Group に表現メソッドが必要）
            # ここでは x.word で [g1, g2, ...] のリストと仮定
            val = G.identity
            for g in x.word:  # word = gens の積で表した表現
                val = G.multiply(val, gen_map[g])
            mapping[x] = val

        phi = GroupHom(G, G, mapping)

        if phi.is_isomorphism():
            autos.add(phi)
    return autos
