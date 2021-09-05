import os

import julia
julia.install()
from julia import Main

script_dir = os.path.dirname(os.path.realpath(__file__))
try:
    Main.include(os.path.join(script_dir, "setup.jl"))
    from julia.QuickPOMDPs import (DiscreteExplicitPOMDP,
                                   DiscreteExplicitMDP,
                                   QuickMDP,
                                   QuickPOMDP,
                                   MissingQuickArgument)

except Exception as e:
    print(e)

    print("!" * 10)
    print("Try running quickpomdps.install() first!")
    print("!" * 10)


def install():
    """
    Install Julia packages required for quickpomdps
    """
    from julia import Pkg
    Pkg.add("POMDPs")
    Pkg.add("POMDPSimulators")
    Pkg.add("POMDPPolicies")
    Pkg.add("QuickPOMDPs")
