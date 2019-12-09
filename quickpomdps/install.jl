using Pkg

Pkg.add("PyCall")
Pkg.add("POMDPs")
Pkg.add("QuickPOMDPs")
Pkg.add("POMDPSimulators")
Pkg.add("POMDPPolicies")

using POMDPs
POMDPs.add_registry()
Pkg.add("QMDP")

using QuickPOMDPs
using PyCall

