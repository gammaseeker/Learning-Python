annual_salary = 120000
portion_saved = .1
total_cost = 1000000
monthly_salary = (annual_salary / 12.0)

portion_down_payment = 0.25 * total_cost

current_savings = 0

returns = (current_savings * 0.4) / 12

overall_savings = returns + (portion_saved * monthly_salary)

months = 0
# Want to exit the loop when there is enough savings for a down payment
while current_savings < portion_down_payment:
    current_savings +=  current_savings * (0.4 / 12)  # Monthly interest
    current_savings += portion_saved  # Monthly savings
    months += 1
print("It will take {} months to save!".format(months))

current_Saving=0
rate=0.04/12

monthly_savings = monthly_salary*0.1 

i=0
while (current_Saving <= portion_down_payment):
    current_Saving = current_Saving+(monthly_savings)*rate + monthly_savings 
    i=i+1
print(i)