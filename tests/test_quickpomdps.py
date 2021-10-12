from quickpomdps import DiscreteExplicitPOMDP, QuickPOMDP

from julia import Pkg
Pkg.add(["POMDPs", "POMDPSimulators", "POMDPPolicies", "POMDPModelTools", "Distributions", "QMDP"])

from julia.QuickPOMDPs import preprocess
from julia import Main
from julia.Main import applicable, Val, Symbol, Float64

from julia.POMDPs import solve, pdf
from julia.QMDP import QMDPSolver
from julia.POMDPSimulators import stepthrough
from julia.POMDPPolicies import alphavectors
# for lightdark
from julia.POMDPModelTools import Uniform, Deterministic
from julia.Distributions import Normal

def test_basics():
    def T(s, a, sp):
        return s == sp

    def Z(a, sp, o):
        return 0.5

    def R(s, a):
        return -1.0

    S = ['l', 'r']
    A = ['l', 'r']
    O = ['l', 'r']
    discount = 0.95
    prob = DiscreteExplicitPOMDP(S, A, O, T, Z, R, discount)

def test_reward():
    r = True
    def reward(s, a, sp=1, *args): s**2
    jlrew = preprocess(Main.eval('Val(:reward)'), reward)
    assert applicable(jlrew, 1, 2)
    assert applicable(jlrew, 1, 2, 3)
    assert applicable(jlrew, 1, 2, 3, 4)
    assert not applicable(jlrew, 1)

# Tiger POMDP from Kaelbling et al. 98 (http://www.sciencedirect.com/science/article/pii/S000437029800023X)
def test_tiger():

    S = ['left', 'right']
    A = ['left', 'right', 'listen']
    O = ['left', 'right']
    discount = 0.95

    def T(s, a, sp):
        if a == 'listen':
            return s == sp
        else: # a door is opened
            return 0.5 #reset

    def Z(a, sp, o):
        if a == 'listen':
            if o == sp:
                return 0.85
            else:
                return 0.15
        else:
            return 0.5

    def R(s, a):
        if a == 'listen':
            return -1.0
        elif s == a: # the tiger was found
            return -100.0
        else: # the tiger was escaped
            return 10.0

    m = DiscreteExplicitPOMDP(S,A,O,T,Z,R,discount)

    solver = QMDPSolver()
    policy = solve(solver, m)

    print('alpha vectors:')
    for v in alphavectors(policy):
        print(v)

    print()

    rsum = 0.0
    for step in stepthrough(m, policy, max_steps=10):
        print('s:', step.s)
        print('b:', [pdf(step.b, x) for x in S])
        print('a:', step.a)
        print('o:', step.o, '\n')
        rsum += step.r

    print('Undiscounted reward was', rsum)

def test_lightdark():
    r = 60
    light_loc = 10

    def transition(s, a):
        if a == 0:
            return Deterministic(r+1)
        else:
            return Deterministic(min(max(s+a, -r), r))

    def observation(s, a, sp):
        return Normal(sp, abs(sp - light_loc) + 0.0001)

    def reward(s, a, sp):
        if a == 0:
            return 100.0 if s == 0 else -100.0
        else:
            return -1.0

    m = QuickPOMDP(
        states = range(-r, r+2),
        actions = [-10, -1, 0, 1, 10],
        discount = 0.95,
        isterminal = lambda s: s < -r or s > r,
        obstype = Float64,
        transition = transition,
        observation = observation,
        reward = reward,
        initialstate = Uniform(range(-r//2, r//2+1))
    )

    solver = QMDPSolver()
    policy = solve(solver, m)

    print('alpha vectors:')
    for v in alphavectors(policy):
        print(v)

    print()

    rsum = 0.0
    for step in stepthrough(m, policy, max_steps=10):
        print('s:', step.s)
        print('a:', step.a)
        print('o:', step.o, '\n')
        rsum += step.r

    print('Undiscounted reward was', rsum)
