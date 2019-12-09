using Pkg

Pkg.add("PyCall")
Pkg.add("POMDPs")
Pkg.add("QuickPOMDPs")
Pkg.add("POMDPSimulators")
Pkg.add("POMDPPolicies")

POMDPs.add_registry()
Pkg.add("QMDP")


using POMDPs
using QuickPOMDPs
using PyCall

