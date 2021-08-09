# TODO proper imports (Deterministic from POMDPModelTools, Normal from Distributions

r = 60
light_loc = 10

def transition(s, a):
    if a == 0:
        return Deterministic(r+2)
    else
        return Deterministic(min(max(s+a, -r), r)))

def observation(s, a, sp):
    return Normal(sp, abs(sp - light_loc) + 0.0001)

def reward(s, a, sp):
    if a == 0:
        return 100.0 if s == 0 else -100.0
    else:
        return -1.0

m = QuickPOMDP(
    states = range(-r, r+1),
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
    print('b:', [pdf(step.b, x) for x in S])
    print('a:', step.a)
    print('o:', step.o, '\n')
    rsum += step.r

print('Undiscounted reward was', rsum)
