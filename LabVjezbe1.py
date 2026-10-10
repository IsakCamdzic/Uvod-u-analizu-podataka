def total_consumption(list):
    total = 0
    for value in list:
        total = total + value
    return total

def average_consumption(list):
    total = total_consumption(list)
    average = total / len(list)
    return average

def total_cost(list):
    total = total_consumption(list)
    cost = total * 0.15
    return cost

def main():
    monthly_consumption = [320, 300, 280, 350, 420]

    print("Electricity Consumption Report")
    print("------------------------------")
    print(f"Total consumption: {total_consumption(monthly_consumption)} kWh")
    print(f"Average consumption: {average_consumption(monthly_consumption)} kWh")
    print(f"Total cost: {total_cost(monthly_consumption)} EUR")

if __name__ == "__main__":
    main()