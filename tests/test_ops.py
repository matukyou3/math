import pytest
from groups.cyclic import CyclicGroup, CyclicElement
from groups.dihedral import DihedralGroup, DihedralElement
from algebra.ops import *

# 中心がGの部分集合であること
@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_center(G):
    Z = center(G)
    assert Z.issubset(G.elements)

# 共役
@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_conjugate(G):
    for x in G.elements:
        for y in G.elements:
            assert conjugate(G, x, y) in G.elements


@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_conjugation_map(G):
    g = pick_one(G)
    phi = conjugation_map(G, g)
    for x in G.elements:
        assert phi(x) == conjugate(G, g, x)

@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_commutator(G):
    for x in G.elements:
        for y in G.elements:
            assert commutator(G, x, y) in G.elements

@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_commutator_subgroup(G):
    assert commutator_subgroup(G).issubset(G.elements)


@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_commutator_subgroup_identity(G):
    H = commutator_subgroup(G)
    assert G.identity in H

@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_commutator_subgroup_closed(G):
    H = commutator_subgroup(G)
    for x in H:
        for y in H:
            assert G.multiply(x, y) in H


@pytest.mark.parametrize("G", [CyclicGroup(9), DihedralGroup(8)])
def test_commutator_subgroup_inverse_closed(G):
    H = commutator_subgroup(G)
    for h in H:
        assert G.inverse(h) in H

