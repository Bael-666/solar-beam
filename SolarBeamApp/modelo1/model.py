# Import PuLP modeler functions
from pulp import *

def main(rutas, fabricas, tiendas):
    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("Ruta de transporte", LpMinimize)
    # A dictionary called 'ingredient_vars' is created to contain the referenced Variables
    rutas_vars = LpVariable.dicts("Rutas", rutas, lowBound = 0, cat = LpInteger)
    # The objective function is added to 'prob' first
    prob += lpSum([i.costo*rutas_vars[i] for i in rutas]), "Costo de envio"
    # The five constraints are added to 'prob'
    for i in fabricas:
        prob += lpSum([rutas_vars[j] for j in rutas 
                                        if i.id == j.fabric_id]) <= i.produccion, "Prod_%s"%i
    for i in tiendas:
        prob += lpSum([rutas_vars[j] for j in rutas 
                                        if i.id == j.tiend_id]) >= i.demand, "Deman_%s"%i
    # The problem is solved using PuLP's choice of Solver
    prob.solve()
    return prob