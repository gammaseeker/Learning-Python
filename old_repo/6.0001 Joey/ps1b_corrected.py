def main():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
    total_cost = float(input("Enter the cost of your dream home:"))
    semi_annual_raise = float(input("Enter raise:"))

    # Test case
    # annual_salary = 120000
    # portion_saved = .1
    # total_cost = 1000000
    
    portion_down_payment = 0.25 * total_cost
    current_savings = 0.0
    r = 0.04
    monthly_salary = annual_salary/12.0
    months = 0

    while(current_savings <= portion_down_payment):
        months += 1
        if(months % 6 == 0):
            annual_salary = annual_salary * (1 + semi_annual_raise)
        current_savings += current_savings * r / 12 + annual_salary/12 * portion_saved
        

    print("Enter your annual salary: ", annual_salary)
    print("Enter the percent of your salary to save, as a decimal: ", portion_saved)
    print("Enter the cost of your dream home:", total_cost)
    print("Number of months:", months)

main()