from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, lpSum, value
import matplotlib.pyplot as plt
import numpy as np

model = LpProblem("Factory_Production_Optimization", LpMaximize)

x = LpVariable("Product_A", lowBound=0, cat="Continuous")
y = LpVariable("Product_B", lowBound=0, cat="Continuous")


model += 50 * x + 40 * y, "Total_Profit"

model += 2 * x + 1 * y <= 100, "Machine_1_Capacity"

model += 1 * x + 2 * y <= 80, "Machine_2_Capacity"

model.solve()

print(f"Status: {LpStatus[model.status]}")
print(f"Optimal units of Product A to produce: {x.varValue}")
print(f"Optimal units of Product B to produce: {y.varValue}")
print(f"Maximum Profit: ₹{value(model.objective)}")


x_vals = np.linspace(0, 80, 200)
y1 = (100 - 2 * x_vals)         
y2 = (80 - 1 * x_vals) / 2      

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y1, label="Machine 1 Constraint (2x + y ≤ 100)")
plt.plot(x_vals, y2, label="Machine 2 Constraint (x + 2y ≤ 80)")
plt.xlim((0, 60))
plt.ylim((0, 60))

y_limit = np.minimum(y1, y2)
plt.fill_between(x_vals, 0, y_limit, where=(y_limit >= 0), color='lightblue', alpha=0.5)

plt.plot(x.varValue, y.varValue, 'ro', label="Optimal Solution")
plt.text(x.varValue+1, y.varValue+1, f"({x.varValue:.1f}, {y.varValue:.1f})", fontsize=10)

plt.title("Feasible Region and Optimal Solution")
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.legend()
plt.grid(True)
plt.show()
