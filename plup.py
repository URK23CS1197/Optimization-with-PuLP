import pulp


model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)


A = pulp.LpVariable('Product_A', lowBound=0, cat='Integer')
B = pulp.LpVariable('Product_B', lowBound=0, cat='Integer')


model += 20 * A + 30 * B, "Total Profit"


model += 4 * A + 6 * B <= 240, "Labor Constraint"
model += 2 * A + 1 * B <= 100, "Material Constraint"

model.solve()


print("Status:", pulp.LpStatus[model.status])
print(f"Produce {A.varValue} units of Product A")
print(f"Produce {B.varValue} units of Product B")
print(f"Maximum Profit: ₹{pulp.value(model.objective)}")
