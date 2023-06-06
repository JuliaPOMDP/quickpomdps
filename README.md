[![test](https://github.com/JuliaPOMDP/quickpomdps/actions/workflows/ci.yml/badge.svg)](https://github.com/JuliaPOMDP/quickpomdps/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JuliaPOMDP/quickpomdps/branch/master/graph/badge.svg?token=MCbhOtnJBj)](https://codecov.io/gh/JuliaPOMDP/quickpomdps)
[![Gitter](https://badges.gitter.im/JuliaPOMDP/Lobby.svg)](https://gitter.im/JuliaPOMDP/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Slack](https://img.shields.io/badge/Chat%20on%20Slack-with%20%23pomdp--bridged-ff69b4)](https://julialang.org/slack/)

# quickpomdps - python

`quickpomdps` is a package to quickly define [[PO]MDPs](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process) in Python.
You can use any of the solvers in [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl) ecosystem, directly in Python.

A hybrid continuous-discrete light-dark problem definition (taken from [`examples/lightdark.py`](examples/lightdark.py) looks like this:
```python
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
```

## Installation

```bash
pip install quickpomdps
```
`quickpomdps` uses the [pyjulia package](https://github.com/JuliaPy/pyjulia) which requires julia to be installed. We recommend using [juliaup](https://github.com/JuliaLang/juliaup) for this purpose.

Upon invocation of `import quickpomds` in Python, all Julia dependencies will be installed if they are not already present.
Please note that, by default, the Julia dependencies are added to the *global* environment.
If you want to install these dependencies to a local environment instead, export the `JULIA_PROJECT` with the desired path as documented [here](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_PROJECT).


## Development

This package uses [python-poetry](https://python-poetry.org/) for dependency
management. Thus, it may be installed via one of the may [ways supported by poetry](https://python-poetry.org/docs/cli/#add), for example,
```bash
git clone https://github.com/JuliaPOMDP/quickpomdps
cd quickpomdps
poetry install
poetry run python examples/lightdark.py
```

## Usage

See [`examples/`](examples/) and [`tests/`](tests/). Documentation can be found at the [QuickPOMDPs.jl](https://github.com/JuliaPOMDP/QuickPOMDPs.jl) and [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl/blob/master/README.md) packages.

## Help

If you need help, please ask on the [POMDPs.jl discussions page](https://github.com/JuliaPOMDP/POMDPs.jl/discussions)!
