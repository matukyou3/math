import pytest
from groups.cyclic import CyclicGroup, CyclicElement
from groups.dihedral import DihedralGroup, DihedralElement
from algebra.homomorphism import GroupHom
from algebra.ops import *
from algebra.theory import *

def test_inn_returns_set():
    G = CyclicGroup(5)
    I = Inn(G)
    assert isinstance(I, set)
    assert all(isinstance(phi, GroupHom) for phi in I)


def test_inn_cyclic_trivial():
    G = CyclicGroup(9)
    I = Inn(G)
    # アーベル群 → 内自己同型は恒等写像のみ
    assert len(I) == 1
    phi = next(iter(I))
    for x in G.elements:
        assert phi(x) == x


def test_inn_size_matches_G_mod_center():
    """
    一般論: |Inn(G)| = |G| / |Z(G)|
    """
    for G in [CyclicGroup(6), DihedralGroup(5), DihedralGroup(8)]:
        Z = center(G)                 # ★ ops.center(G)
        I = Inn(G)
        assert len(I) == len(G.elements) // len(Z)



# Euler φ(n)
def phi(n):
    result = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def test_auto_returns_set():
    G = CyclicGroup(6)
    A = Auto(G)
    assert isinstance(A, set)
    assert all(isinstance(a, GroupHom) for a in A)


def test_auto_cyclic_size():
    for n in [1, 2, 3, 4, 5, 6, 8, 9]:
        G = CyclicGroup(n)
        A = Auto(G)
        assert len(A) == phi(n)


def test_auto_dihedral_size():
    for n in [3, 4, 5, 6, 8]:
        G = DihedralGroup(n)
        A = Auto(G)
        assert len(A) == n * phi(n)


def test_auto_all_are_isomorphisms():
    G = DihedralGroup(6)
    A = Auto(G)
    for phi in A:
        assert phi.is_isomorphism()
