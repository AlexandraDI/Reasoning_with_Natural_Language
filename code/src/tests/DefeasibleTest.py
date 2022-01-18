from logics.DefeasibleTableauxSolver import DefeasibleTableauxSolver
from logics.NaturalTableauxSolver import NaturalTableauxSolver

premises = [
    # "I study math or I study physics",  # P or Q
    # "Normally I do not study physics",  # ! Q,
    # "I study physics",
    # # "Normally If I study physics then I study math",
    # "Normally if I study math then I study statistics",  #  P -_-_> R
    # "Normally if I study statistics then I enjoy myself",  # R -_-_> S
    "Usually it is not raining",
    "when it is cloudy then it is raining",
    "it is cloudy"
]

conclusion = "it is raining"

nts = DefeasibleTableauxSolver(premises, conclusion, True)

proof = nts.solve()
print(nts.contradiction_in_information)
print(proof)
print(nts.defeated_defeasible_expressions)
print(nts.is_contradiction_resolved())
# print(nts.defeated_defeasible_expressions[0].support)

print([ str(i) for i in nts.expressions])

print([ str(i) for i in nts.solver.closing_arguments])
# print(nts.contradiction_in_information)

print(nts.solver.closing_arguments)

# print(nts.get_dot_graph())

# nts.solver.solve_tree.save_pdf("image_3.pdf","pdf")
# #
# nts = NaturalTableauxSolver(premises, conclusion)
# proof = nts.solve()
# print(nts.solver.closing_arguments)
# nts.solver.solve_tree.save_pdf("image_temp.pdf","pdf")
# print(proof)
# print([str(i) for i in nts.expressions])
# print([str(i) for i in nts.solver.closing_arguments])
# print(nts.solver.closing_arguments)

# nts.solver.solve_tree.save_pdf("image_3.pdf", "pdf")
