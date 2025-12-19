import pulp


def main():
    

    model = pulp.LpProblem("Optimization_Production", pulp.LpMaximize)

    # Змінні: кількість виробленого Лимонаду (lemonade) та Фруктового соку (juice)
    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    # Цільова функція: максимізація загальної кількості продуктів
    model += lemonade + juice, "Total_Products"

    # Обмеження ресурсів
    model += 2 * lemonade + juice <= 100, "Water_Constraint"
    model += lemonade <= 50, "Sugar_Constraint"
    model += lemonade <= 30, "Lemon_Juice_Constraint"
    model += 2 * juice <= 40, "Fruit_Puree_Constraint"

    model.solve()

    # Вивід результатів
    print("Status:", pulp.LpStatus[model.status])
    print("Optimal production plan:")
    print(f" Lemonade: {lemonade.varValue} units")
    print(f" Fruit juice: {juice.varValue} units")
    print("Maximum total products:", pulp.value(model.objective))


if __name__ == "__main__":
    main()