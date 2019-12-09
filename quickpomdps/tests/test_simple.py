import quickpomdps

def test_basics():
    def T(s, a, sp):
        return s == sp

    def Z(a, sp, o):
        return 0.1

    def R(s, a):
        return -1.0

    S = ['l', 'r']
    A = ['l', 'r']
    O = ['l', 'r']
    γ = 0.95
    prob = quickpomdps.DiscreteExplicitPOMDP(S, A, O, T, Z, R, γ)
