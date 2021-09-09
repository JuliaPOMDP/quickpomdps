import os


import julia
from julia.api import Julia
jl = Julia(compiled_modules=False)

julia.install()
from julia import Main


def install_julia_dependencies():
    """
    Install Julia packages required for quickpomdps
    """
    from julia import Pkg

    Pkg.add("POMDPs")
    Pkg.add("POMDPSimulators")
    Pkg.add("POMDPPolicies")
    Pkg.add("QuickPOMDPs")


install_julia_dependencies()

script_dir = os.path.dirname(os.path.realpath(__file__))
Main.include(os.path.join(script_dir, "setup.jl"))
from julia.QuickPOMDPs import (
    DiscreteExplicitPOMDP,
    DiscreteExplicitMDP,
    QuickMDP,
    QuickPOMDP,
    MissingQuickArgument,
)
