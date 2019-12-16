import os
import subprocess
import sys

from julia import Main

script_dir = os.path.dirname(os.path.realpath(__file__))
try:
    Main.include(os.path.join(script_dir, "setup.jl"))
    from julia.QuickPOMDPs import (DiscreteExplicitPOMDP,
                                   DiscreteExplicitMDP,
                                   QuickMDP,
                                   QuickPOMDP,
                                   MissingQuickArgument)
    from julia import POMDPs

except Exception as e:
    print(e)

    print("!" * 10)
    print("Try running quickpomdps.install() first!")
    print("!" * 10)


def install():
    """
    Install Julia packages required for quickpomdps
    """
    subprocess.check_call(['julia', os.path.join(script_dir, 'install.jl')])
