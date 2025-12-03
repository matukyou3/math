from algebra import FiniteGroup, GroupElement

# r：回転
# R^n=e

class CyclicElement(GroupElement):
    def __init__(self, r=0, n=1, r_gen=None):
        self.r = r % n
        self.n = n
        self.r_gen = r_gen

        self.word = [self.r_gen]*self.r

        

    def __repr__(self):
        return f"R^{self.r}"
    
    def __eq__(self, other):
        return (
            isinstance(other, CyclicElement) and
            self.r == other.r and
            self.n == other.n
        )
    
    def __hash__(self):
        return hash((self.r, self.n))
    
class CyclicGroup(FiniteGroup):
    # 群構造定義
    def __init__(self, n):
        self.n = n
        self.r_gen = CyclicElement(1, n)

        elems = [CyclicElement(k, n, r_gen=self.r_gen) for k in range(n)]
        self._elements = set(elems)
    
    # 生成元
    @property
    def generators(self):
        return [self.r_gen]
    
    # 群演算定義
    def multiply(self, a, b):
        n = self.n
        # (R^a)(R^b) = R^(a+b)
        return CyclicElement(a.r + b.r, n, r_gen=self.r_gen)
    
    # 単位元
    @property
    def identity(self):
        return CyclicElement(0, self.n, r_gen=self.r_gen)
    

    # 逆元
    def inverse(self, a):
        n = self.n
        return CyclicElement(-a.r, n, r_gen=self.r_gen)
    
    @property
    def elements(self):
        return self._elements
