\* The Whiskas Problem *\
Minimize
Total_Cost_of_Ingredients_per_can: 0.008 Ingr_Beef + 0.013 Ingr_Chicken
 + 0.001 Ingr_Gel + 0.01 Ingr_Mutton + 0.002 Ingr_Rice + 0.005 Ingr_Wheat
Subject To
FatRequirement: 0.1 Ingr_Beef + 0.08 Ingr_Chicken + 0.11 Ingr_Mutton
 + 0.01 Ingr_Rice + 0.01 Ingr_Wheat >= 6
FibreRequirement: 0.005 Ingr_Beef + 0.001 Ingr_Chicken + 0.003 Ingr_Mutton
 + 0.1 Ingr_Rice + 0.15 Ingr_Wheat <= 2
PercentagesSum: Ingr_Beef + Ingr_Chicken + Ingr_Gel + Ingr_Mutton + Ingr_Rice
 + Ingr_Wheat = 100
ProteinRequirement: 0.2 Ingr_Beef + 0.1 Ingr_Chicken + 0.15 Ingr_Mutton
 + 0.04 Ingr_Wheat >= 8
SaltRequirement: 0.005 Ingr_Beef + 0.002 Ingr_Chicken + 0.007 Ingr_Mutton
 + 0.002 Ingr_Rice + 0.008 Ingr_Wheat <= 0.4
End
