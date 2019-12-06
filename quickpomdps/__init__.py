import os
import subprocess
import sys

from julia import Main

script_dir = os.path.dirname(os.path.realpath(__file__))
Main.include(os.path.join(script_dir, "setup.jl"))

from julia.QuickPOMDPs import *
from julia import POMDPs


def install():
    """
    Install Julia packages required for quickpomdps
    """
    subprocess.check_call(['julia', os.path.join(script_dir, 'install.jl')])
