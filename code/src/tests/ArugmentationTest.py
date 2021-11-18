from logics.NaturalTableauxSolver import NaturalTableauxSolver

premises = [
    "I study math or I study nothing", # P or Q
    "If I study math, I study nothing" # P -> Q
]

conclusion = "I study nothing"

nts = NaturalTableauxSolver(premises, conclusion)

nts.solve()

print(nts.solver.closing_arguments)

# nts.solver.solve_tree
