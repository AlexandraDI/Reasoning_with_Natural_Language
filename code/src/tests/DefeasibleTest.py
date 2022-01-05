from logics.DefeasibleTableauxSolver import DefeasibleTableauxSolver
from logics.NaturalTableauxSolver import NaturalTableauxSolver

premises = [
    "I study math or I study physics",  # P or Q
    "Normally I do not study physics",  # ! Q
    "Normally if I study math then I study statistics",  #  P -_-_> R
    "Normally if I study statistics then I enjoy myself",  # R -_-_> S
]

conclusion = "I enjoy myself"

nts = DefeasibleTableauxSolver(premises, conclusion)

proof = nts.solve()
print(proof)
print([str(i) for i in nts.expressions])

print([str(i) for i in nts.solver.closing_arguments])

print(nts.solver.closing_arguments)

nts.solver.solve_tree.save_pdf("image_3.pdf", "pdf")

# nts.solver.solve_tree
