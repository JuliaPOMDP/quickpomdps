# quickpomdps - python

[![Build Status](https://travis-ci.org/JuliaPOMDP/quickpomdps.svg?branch=master)](https://travis-ci.org/JuliaPOMDP/quickpomdps)

[![Gitter](https://badges.gitter.im/JuliaPOMDP/Lobby.svg)](https://gitter.im/JuliaPOMDP/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Slack](https://img.shields.io/badge/Chat%20on%20Slack-with%20%23pomdp--bridged-ff69b4)](https://slackinvite.julialang.org)

`quickpomdps` is a package to quickly define [[PO]MDPs](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process) in Python.
You can use any of the solvers in [POMDPs.jl](https://github.com/JuliaPOMDP/POMDPs.jl) ecosystem, directly in Python.

## Installation

To install `quickpomdps`, use `pip`:

```bash
pip install quickpomdps
```

Using `quickpomdps` requires that Julia is installed and in the `PATH` along with `POMDPs.jl` and `PyCall.jl`.
To install Julia, download a generic binary from [the JuliaLang site](https://julialang.org/downloads/) and add it to your `PATH`.
To install basic Julia packages required for `quickpomdps`, open a Python interpreter and run:

```python
>>> import quickpomdps
>>> quickpomdps.install()
```

## Usage

See [`examples/`](examples/).
