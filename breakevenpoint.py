import matplotlib.pyplot as plt


# =========================
# 1. CORE FUNCTIONS
# =========================

def total_cost(cf, cv, v):
    return cf + cv * v


def total_revenue(sp, v):
    return sp * v


def profit(cf, cv, sp, v):
    return total_revenue(sp, v) - total_cost(cf, cv, v)


def break_even_units(cf, cv, sp):
    if sp <= cv:
        raise ValueError("Selling price must be greater than variable cost.")
    return cf / (sp - cv)


def break_even_revenue(bep, sp):
    return bep * sp


# =========================
# 2. INPUT VALIDATION
# =========================

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")


# =========================
# 3. BUSINESS INSIGHT LAYER
# =========================

def business_insight(cf, cv, sp, v):
    pr = profit(cf, cv, sp, v)

    print("\n--- Business Insight ---")

    if sp <= cv:
        print("⚠️ Not viable: no profit per unit.")
    elif pr > 0:
        print("✅ Profitable business.")
    else:
        print("⚠️ Currently operating at a loss.")


# =========================
# 4. OUTPUT FORMAT
# =========================

def show_results(cf, cv, sp, v):
    tc = total_cost(cf, cv, v)
    tr = total_revenue(sp, v)
    pr = profit(cf, cv, sp, v)
    bep = break_even_units(cf, cv, sp)
    ber = break_even_revenue(bep, sp)

    print("\n========== RESULTS ==========")
    print(f"Total Cost        : ${tc:.2f}")
    print(f"Total Revenue     : ${tr:.2f}")
    print(f"Profit            : ${pr:.2f}")
    print(f"Break-Even Units  : {bep:.2f}")
    print(f"Break-Even Revenue: ${ber:.2f}")
    print("=============================\n")

    business_insight(cf, cv, sp, v)


# =========================
# 5. VISUALIZATION
# =========================

def plot_graph(cf, cv, sp, max_v=1000):
    units = list(range(0, max_v, 10))

    costs = [total_cost(cf, cv, v) for v in units]
    revenues = [total_revenue(sp, v) for v in units]

    bep = break_even_units(cf, cv, sp)

    plt.figure(figsize=(10, 6))
    plt.plot(units, costs, label="Total Cost")
    plt.plot(units, revenues, label="Total Revenue")

    plt.axvline(x=bep, linestyle="--", label="Break-Even Point")

    plt.title("Break-Even Analysis")
    plt.xlabel("Units Sold")
    plt.ylabel("Money")
    plt.legend()
    plt.grid(True)

    plt.show()


# =========================
# 6. MAIN MENU
# =========================

def main():
    print("\n================================")
    print("   BREAK-EVEN ANALYSIS TOOL")
    print("================================\n")

    cf = get_float("Fixed Costs (CF): ")
    cv = get_float("Variable Cost (CV): ")
    sp = get_float("Selling Price (SP): ")
    v = get_float("Units Sold (V): ")

    while True:
        print("\nChoose option:")
        print("1 - Show Results")
        print("2 - Show Graph")
        print("3 - Show Both")
        print("0 - Exit")

        choice = input(">> ")

        if choice == "1":
            show_results(cf, cv, sp, v)

        elif choice == "2":
            plot_graph(cf, cv, sp)

        elif choice == "3":
            show_results(cf, cv, sp, v)
            plot_graph(cf, cv, sp)

        elif choice == "0":
            print("Goodbye !")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()