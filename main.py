from algebra.ops import center
from algebra.theory import  Inn
from groups.dihedral import DihedralGroup

G = DihedralGroup(4)
for g in G.elements:
    print(g)

print(center(G))
print(len(Inn(G)))