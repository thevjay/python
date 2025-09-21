class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala Blend class"

class C(A):
    label = "C: Herbal Blend class"

class D(C,B):
    # label = "D: Special Blend class"
    pass

cup = D()
print(cup.label)
print(D.__mro__)

# C: Herbal Blend class
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>) 