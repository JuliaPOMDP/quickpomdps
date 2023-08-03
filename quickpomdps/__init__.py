import os

import julia

def install_julia_dependencies():
    """
    Install Julia packages required for quickpomdps
    """
    from julia import Pkg

    Pkg.add(["PyCall","QuickPOMDPs"])

try:
    from julia import QuickPOMDPs
except Exception as ex:
    print('Could not load QuickPOMDPs Julia package.')
    print('Caught the following exception:')
    print(ex)
    if isinstance(ex, julia.core.UnsupportedPythonError):
        print('Running julia.install()')
        julia.install()
    print('Running quickpomdps.install_julia_dependencies()')
    install_julia_dependencies()
    print('done!')

script_dir = os.path.dirname(os.path.realpath(__file__))
julia.Main.include(os.path.join(script_dir, "setup.jl"))
from julia.QuickPOMDPs import (
    DiscreteExplicitPOMDP,
    DiscreteExplicitMDP,
    QuickMDP,
    QuickPOMDP,
    MissingQuickArgument,
)
