class GroupHom:
    def __init__(self, G, H, mapping):
        self.G = G
        self.H = H
        self.mapping = mapping

    def __call__(self, x):
        return self.mapping[x]
    
    def __repr__(self):
        pairs = ", ".join(f"{repr(k)} -> {repr(v)}" for k, v in self.mapping.items())
        return f"GroupHom({{{pairs}}})"
    
    def __eq__(self, other):
        if not isinstance(other, GroupHom):
            return False
        return all(self(x) == other(x) for x in self.H.elements)

    def __hash__(self):
        return hash(tuple((x, self(x)) for x in self.H.elements))

    
    def is_homorphism(self):
        """φ(xy)=φ(x)φ(y)"""
        for x in self.G.elements:
            for y in self.G.elements:
                left = self(self.G.multiply(x, y))
                right = self.H.multiply(self(x), self(y))
                if left != right:
                    return False
        return True
    
    @property
    def image(self):
        return {self(g) for g in self.G.elements}
    
    def is_mono(self):
        ker = {x for x in self.G.elements if self(x) == self.H.identity}
        return ker == {self.G.identity}
    
    def is_epi(self):
        return self.image == set(self.H.elements)
    
    def image_size(self):
        return len(self.image)

    def is_isomorphism(self):
        return self.is_homorphism and self.is_epi()


