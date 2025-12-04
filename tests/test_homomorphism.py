import pytest
from groups.cyclic import CyclicGroup, CyclicElement
from groups.dihedral import DihedralGroup, DihedralElement
from algebra.homomorphism import GroupHom
from algebra.ops import *

def test_group_hom_call_and_mapping():
    G = CyclicGroup(4)
    mapping = {x: x for x in G.elements}
    phi = GroupHom(G, G, mapping)

    for x in G.elements:
        assert phi(x) == mapping[x]
        assert phi.mapping[x] == mapping[x]

def test_group_hom_homomorphis_property():
    G = DihedralGroup(5)
    g = pick_one(G)
    mapping = {x: conjugate(G, g, x) for x in G.elements}
    phi = GroupHom(G, G, mapping)

    assert phi.is_homorphism()

def test_group_hom_mono():
    G = DihedralGroup(4)
    g = DihedralElement(2, False, 4, r_gen=G.r_gen, s_gen=G.s_gen)
    mapping = {x: conjugate(G, g, x) for x in G.elements}
    phi = GroupHom(G, G, mapping)

    assert phi.is_mono()

def test_group_hom_equality():
    G = CyclicGroup(4)

    mapping1 = {x: x for x in G.elements}
    mapping2 = {x: x for x in G.elements}
    mapping3 = {x: G.multiply(x, x) for x in G.elements}  # different map

    phi1 = GroupHom(G, G, mapping1)
    phi2 = GroupHom(G, G, mapping2)
    phi3 = GroupHom(G, G, mapping3)

    assert phi1 == phi2
    assert phi1 != phi3
    assert not (phi1 != phi2)

def test_group_hom_hash_and_set_behavior():
    G = CyclicGroup(4)

    mapping1 = {x: x for x in G.elements}
    mapping2 = {x: x for x in G.elements}
    mapping3 = {x: G.multiply(x, x) for x in G.elements}

    phi1 = GroupHom(G, G, mapping1)
    phi2 = GroupHom(G, G, mapping2)
    phi3 = GroupHom(G, G, mapping3)

    S = {phi1, phi2, phi3}

    # phi1 and phi2 are same → eliminated by set
    assert len(S) == 2
    assert phi1 in S
    assert phi3 in S


def test_group_hom_isomorphism_identity():
    G = CyclicGroup(4)
    mapping = {x: x for x in G.elements}  # identity
    phi = GroupHom(G, G, mapping)

    assert phi.is_isomorphism()


def test_group_hom_isomorphism_non_bijective():
    G = CyclicGroup(4)

    # φ(x)=0 constant map → not bijective
    mapping = {x: G.identity for x in G.elements}
    phi = GroupHom(G, G, mapping)

    assert not phi.is_isomorphism()


def test_group_hom_repr_runs():
    """At least ensure repr does not crash."""
    G = CyclicGroup(4)
    mapping = {x: x for x in G.elements}
    phi = GroupHom(G, G, mapping)

    text = repr(phi)
    assert "GroupHom" in text

def test_group_hom_eq_notinstance():
    G1 = CyclicGroup(4)
    mapping1 = {x: G1.identity for x in G1.elements}
    phi1 = GroupHom(G1, G1, mapping1)
    assert phi1 != 123

def test_not_homomorphism():
    G = CyclicGroup(6)
    g = CyclicElement(2, 6, r_gen=G.r_gen)
    mapping = {x: g for x in G.elements}
    phi = GroupHom(G, G, mapping)

    assert not phi.is_homorphism()

def test_image_size():
    G = CyclicGroup(4)
    mapping = {x: x for x in G.elements}  # identity
    phi = GroupHom(G, G, mapping)

    assert phi.image_size() == 4