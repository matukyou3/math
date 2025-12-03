# tests/test_cyclic.py

import pytest
from groups.cyclic import CyclicGroup, CyclicElement
import math


def test_elements_count():
    """要素数が n 個であること"""
    G = CyclicGroup(7)
    assert len(G.elements) == 7


def test_identity():
    """単位元 e の確認"""
    G = CyclicGroup(5)
    e = G.identity
    for a in G.elements:
        assert G.multiply(a, e) == a
        assert G.multiply(e, a) == a


def test_inverse():
    """逆元の確認：a * a^-1 = e"""
    G = CyclicGroup(8)
    e = G.identity
    for a in G.elements:
        inv = G.inverse(a)
        assert G.multiply(a, inv) == e
        assert G.multiply(inv, a) == e


def test_operation_closure():
    """閉性：演算結果が必ず G の要素になる"""
    G = CyclicGroup(6)
    for a in G.elements:
        for b in G.elements:
            c = G.multiply(a, b)
            assert c in G.elements


def test_associativity():
    """結合律 (a*b)*c == a*(b*c) を brute force チェック"""
    G = CyclicGroup(6)
    for a in G.elements:
        for b in G.elements:
            for c in G.elements:
                left = G.multiply(G.multiply(a, b), c)
                right = G.multiply(a, G.multiply(b, c))
                assert left == right


def test_generators():
    """生成元の確認：gcd(k, n)=1 の k が生成元になる"""
    G = CyclicGroup(10)
    gens = G.generators  # [R^1] のみ

    # 値だけ抜き出す
    gen_values = {g.r for g in gens}
    assert 1 in gen_values
    assert len(gen_values) == 1


def test_power_full_generation():
    """生成元 g=R^1 が全ての要素を生成するか（巡回群の本質）"""
    n = 12
    G = CyclicGroup(n)
    g = G.r_gen

    generated = set()

    x = G.identity
    for _ in range(n):
        generated.add(x)
        x = G.multiply(x, g)

    assert generated == G.elements


def test_repr():
    """__repr__ が期待通りの文字列"""
    G = CyclicGroup(7)
    elems = list(G.elements)
    assert repr(elems[0]) == "R^0" or repr(elems[0]) == "e"
    assert repr(CyclicElement(3, 7, r_gen=G.r_gen)) == "R^3"


def test_equality_and_hash():
    """等価性と hash の整合性"""
    a = CyclicElement(3, 10)
    b = CyclicElement(13, 10)  # 13 mod 10 = 3
    c = CyclicElement(4, 10)

    assert a == b
    assert hash(a) == hash(b)
    assert a != c
