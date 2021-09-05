[![test](https://github.com/JuliaPOMDP/quickpomdps/actions/workflows/ci.yml/badge.svg)](https://github.com/JuliaPOMDP/quickpomdps/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JuliaPOMDP/quickpomdps/branch/master/graph/badge.svg?token=MCbhOtnJBj)](https://codecov.io/gh/JuliaPOMDP/quickpomdps)
[![Gitter](https://badges.gitter.im/JuliaPOMDP/Lobby.svg)](https://gitter.im/JuliaPOMDP/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Slack](https://img.shields.io/badge/Chat%20on%20Slack-with%20%23pomdp--bridged-ff69b4)](https://julialang.org/slack/)

# quickpomdps - python

`quickpomdps` is a package to quickly define [[PO]MDPs](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process) in Python.
You can use any of the solvers in [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl) ecosystem, directly in Python.

## Installation

This package uses [python-poetry](https://python-poetry.org/) for dependency
management. Beyond that, it is also registered in the PyPI package index. Thus,
installation may happen either via `pip`

```bash
pip install quickpomdps
```

or via one of the may [ways supported by poetry](https://python-poetry.org/docs/cli/#add).

Using `quickpomdps` requires that Julia is installed and in the `PATH`.
To install Julia, download a generic binary from [the JuliaLang site](https://julialang.org/downloads/) and add it to your `PATH`.
To install basic Julia packages required for `quickpomdps`, open a Python interpreter and run:

```python
>>> import quickpomdps
>>> quickpomdps.install()
```

Please note that these commands will install the Julia dependencies in your *global* environment by default. If you want to install these dependencies to a local environment instead, export the `JULIA_PROJECT` with the desired path as documented [here](https://docs.julialang.org/en/v1/manual/environment-variables/#JULIA_PROJECT).

## Usage

See [`examples/`](examples/).
