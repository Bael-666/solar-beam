# Import PuLP modeler functions
from pulp import *

def main(whiska):
    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("The Whiskas Problem", LpMinimize)
    # A dictionary called 'ingredient_vars' is created to contain the referenced Variables
    ingredient_vars = LpVariable.dicts("Ingr",whiska,0)
    # The objective function is added to 'prob' first
    prob += lpSum([i.cost*ingredient_vars[i] for i in whiska]), "Total Cost of Ingredients per can"
    # The five constraints are added to 'prob'
    prob += lpSum([ingredient_vars[i] for i in whiska]) == 100, "PercentagesSum"
    prob += lpSum([i.prot * ingredient_vars[i] for i in whiska]) >= 8.0, "ProteinRequirement"
    prob += lpSum([i.fat * ingredient_vars[i] for i in whiska]) >= 6.0, "FatRequirement"
    prob += lpSum([i.fibre * ingredient_vars[i] for i in whiska]) <= 2.0, "FibreRequirement"
    prob += lpSum([i.salt * ingredient_vars[i] for i in whiska]) <= 0.4, "SaltRequirement"
    # The problem data is written to an .lp file
    prob.writeLP("WhiskasModel.lp")
    # The problem is solved using PuLP's choice of Solver
    prob.solve()
    return prob