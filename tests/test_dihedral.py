# tests/test_cyclic.py

import pytest
from groups.dihedral import DihedralGroup, DihedralElement
import math


def test_elements_count():
    """要素数が 2n 個であること"""
    G = DihedralGroup(7)
    assert len(G.elements) == 14


def test_identity():
    """単位元 e の確認"""
    G = DihedralGroup(5)
    e = G.identity
    for a in G.elements:
        assert G.multiply(a, e) == a
        assert G.multiply(e, a) == a


def test_inverse():
    """逆元の確認：a * a^-1 = e"""
    G = DihedralGroup(8)
    e = G.identity
    for a in G.elements:
        inv = G.inverse(a)
        assert G.multiply(a, inv) == e
        assert G.multiply(inv, a) == e


def test_operation_closure():
    """閉性：演算結果が必ず G の要素になる"""
    G = DihedralGroup(6)
    for a in G.elements:
        for b in G.elements:
            c = G.multiply(a, b)
            assert c in G.elements


def test_associativity():
    """結合律 (a*b)*c == a*(b*c) を brute force チェック"""
    G = DihedralGroup(6)
    for a in G.elements:
        for b in G.elements:
            for c in G.elements:
                left = G.multiply(G.multiply(a, b), c)
                right = G.multiply(a, G.multiply(b, c))
                assert left == right


def test_generators():
    """生成元のR,Sで生成される"""
    G = DihedralGroup(10)
    gens = set(G.generators)
    assert G.r_gen in gens
    assert G.s_gen in gens
    assert len(gens) == 2


def test_reflection_id():
    G = DihedralGroup(7)
    s = G.s_gen
    assert G.multiply(s, s) == G.identity


def test_gen_identity():
    """SRS = R^(-1)"""
    G = DihedralGroup(8)
    r = G.r_gen
    s = G.s_gen

    lhs = G.multiply(s, G.multiply(r, G.inverse(s)))
    rhs = G.inverse(r)

    assert lhs == rhs


def test_generaters_all_elements():
    G = DihedralGroup(10)
    r = G.r_gen
    s = G.s_gen

    generated = set()
    queue = [G.identity]

    while queue:
        x = queue.pop()
        if x not in generated:
            generated.add(x)
            queue.append(G.multiply(x, r))
            queue.append(G.multiply(x, s))

    assert generated == G.elements

def test_repr():
    """__repr__ が期待通りの文字列"""
    G = DihedralGroup(7)
    assert repr(DihedralElement(0, False, 7)) == "R^0"
    assert repr(DihedralElement(3, True, 7, r_gen=G.r_gen, s_gen=G.s_gen)) == "S·R^3"


def test_equality_and_hash():
    """等価性と hash の整合性"""
    a = DihedralElement(3, True, 10)
    b = DihedralElement(13, True, 10) 
    c = DihedralElement(3, False, 10)

    assert a == b
    assert hash(a) == hash(b)
    assert a != c
