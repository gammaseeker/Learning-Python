semiAnnualRaise = 0.07
rAnnual = 0.04
r = rAnnual/12
homeCost = 1000000
downPaymentPercent = 0.25
downPayment = downPaymentPercent * homeCost
savings = 0
monthLimit = 36
savingsRate = 0.50

# Counters
monthCounter = 0
stepCounter = 1

# Range
min = 0
max = 10000

# Request the user's starting salary
currentSalary = int(input("Enter your current salary: "))

# Save this to a separate variable so it can be reset later, when rerunning the bisection method.
presentSalary = currentSalary

# Function to run the bisection method with a lower and upper limit
def computeRate(lower, upper):

    global savings, currentSalary, monthCounter, max, min, stepCounter, savingsRate


# As long as the amount in Savings is less than the down payment (25% on 1MM = $250,000), do this:

    while (savings < downPayment):
        savingsRate = ((upper+lower)/2)/10000
        monthlySalary = currentSalary/12
        monthlyReturn = savings * r
        monthlyContribution = monthlySalary * savingsRate
        savings = savings + monthlyContribution + monthlyReturn
        monthCounter += 1
        if (monthCounter % 6 == 0):
            currentSalary = currentSalary + (currentSalary*semiAnnualRaise)


    if (monthCounter > monthLimit):
        monthCounter = 0
        savings = 0
        currentSalary = presentSalary
        stepCounter += 1
        min = savingsRate*10000
        computeRate(min, max)

    elif (monthCounter < monthLimit):


        monthCounter = 0

        savings = 0

        currentSalary = presentSalary

        stepCounter += 1

        max = savingsRate * 10000

        computeRate(min, max)

    elif savings > downPayment + 100:
        monthCounter = 0
        savings = 0
        currentSalary = presentSalary
        stepCounter += 1
        max = (savingsRate * 10000)-1
        computeRate(min, max)

    elif savings < downPayment - 100:

        monthCounter = 0

        savings = 0

        currentSalary = presentSalary

        stepCounter += 1

        max = (savingsRate * 10000)+1

        computeRate(min, max)
# Do the bisection method & post the results.

computeRate(min, max)

print("Rate:", savingsRate)

print("Savings:", savings)

print("Months:", monthCounter)

print("Iterations:", stepCounter)

