import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Funkcje przynależności dochodu
def low_income(x): return np.maximum(0, np.minimum(1, (3000 - x) / 2000))
def medium_income(x): return np.maximum(0, np.minimum((x - 2000) / 2000, (6000 - x) / 2000))
def high_income(x): return np.maximum(0, np.minimum(1, (x - 5000) / 2000))

# Funkcje przynależności zadłużenia
def low_debt(x): return np.maximum(0, np.minimum(1, (5000 - x) / 3000))
def high_debt(x): return np.maximum(0, np.minimum(1, (x - 3000) / 3000))

# T-norms
def t_norm_min(a, b): return np.minimum(a, b)
def t_norm_product(a, b): return a * b
def t_norm_lukasiewicz(a, b): return np.maximum(0, a + b - 1)

# T-conorms
def t_conorm_max(a, b): return np.maximum(a, b)
def t_conorm_probabilistic_sum(a, b): return a + b - a * b
def t_conorm_lukasiewicz(a, b): return np.minimum(1, a + b)

# Ocena reguł
def evaluate_rules(income_val, debt_val, tnorm, tconorm):
    low_i = low_income(income_val)
    med_i = medium_income(income_val)
    high_i = high_income(income_val)

    low_d = low_debt(debt_val)
    high_d = high_debt(debt_val)

    r1 = tnorm(high_i, low_d)
    r2 = tnorm(med_i, low_d)
    r3 = tconorm(low_i, high_d)

    credit_yes = tconorm(r1, r2)
    credit_no = r3

    return {"TAK": credit_yes, "NIE": credit_no}

# Przykładowe dane
examples = [
    {"income": 4500, "debt": 2500},
    {"income": 2000, "debt": 5500},
    {"income": 2632, "debt": 3938},
    {"income": 5571, "debt": 3775},

]

tnorms = {
    "min": t_norm_min,
    "product": t_norm_product,
    "lukasiewicz": t_norm_lukasiewicz
}

tconorms = {
    "max": t_conorm_max,
    "prob_sum": t_conorm_probabilistic_sum,
    "lukasiewicz": t_conorm_lukasiewicz
}

results = []
for i, ex in enumerate(examples):
    for tnorm_name, tnorm_func in tnorms.items():
        for tconorm_name, tconorm_func in tconorms.items():
            outcome = evaluate_rules(ex["income"], ex["debt"], tnorm_func, tconorm_func)
            results.append({
                "Przykład": f"Przykład {i+1}",
                "Dochód": ex["income"],
                "Dług": ex["debt"],
                "T-norma": tnorm_name,
                "T-konorma": tconorm_name,
                "TAK": round(outcome["TAK"], 3),
                "NIE": round(outcome["NIE"], 3),
                "Decyzja": "TAK" if outcome["TAK"] > outcome["NIE"] else "NIE"
            })

df_results = pd.DataFrame(results)
print(df_results)
# Wizualizacja funkcji przynależności
x_income = np.linspace(0, 10000, 200)
x_debt = np.linspace(0, 10000, 200)

income_memberships = {
    "Low Income": low_income(x_income),
    "Medium Income": medium_income(x_income),
    "High Income": high_income(x_income)
}

debt_memberships = {
    "Low Debt": low_debt(x_debt),
    "High Debt": high_debt(x_debt)
}

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

for label, y in income_memberships.items():
    axs[0].plot(x_income, y, label=label)
axs[0].set_title("Funkcje przynależności - Dochód")
axs[0].set_xlabel("Dochód")
axs[0].set_ylabel("Stopień przynależności")
axs[0].legend()
axs[0].grid(True)

for label, y in debt_memberships.items():
    axs[1].plot(x_debt, y, label=label)
axs[1].set_title("Funkcje przynależności - Dług")
axs[1].set_xlabel("Dług")
axs[1].set_ylabel("Stopień przynależności")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()