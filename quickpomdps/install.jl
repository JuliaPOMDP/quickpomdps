using Pkg

Pkg.add("POMDPs")
POMDPs.add_registry()
Pkg.add("QuickPOMDPs")
Pkg.add("QMDP")
Pkg.add("POMDPSimulators")
Pkg.add("POMDPPolicies")


using QuickPOMDPs
using PyCall

