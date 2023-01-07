import math
print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
answer = input()
if(answer == "n"):
    print("Enter the loan principal:")
    loan = float(input())
    print("Enter the monthly payment:")
    payment = float(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    n = math.ceil (math.log(payment/(payment-i*loan) , (1 + i)))
    years = n // 12
    months = n % 12
    if (years == 0):
        if (months == 1):
            print("It will take 1 month to repay this loan!")
        elif (months > 1):
            print("It will take {} months to repay this loan!".format(months))
    elif (years == 1):
        if (months == 1):
            print("It will take 1 year and 1 month to repay this loan!")
        elif (months > 1):
            print("It will take 1 year and {} months to repay this loan!".format(months))
        elif (months == 0):
            print("It will take 1 year to repay this loan!")
    elif (years > 1):
        if (months == 1):
            print("It will take {} years and 1 month to repay this loan!".format(years))
        elif (months > 1):
            print("It will take {} years and {} months to repay this loan!".format(years, months))
        elif (months == 0):
            print("It will take {} years to repay this loan!".format(years))
elif(answer == "a"):
    print("Enter the loan principal:")
    loan = float(input())
    print("Enter the number of periods:")
    periods = float(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    a_payment = loan * i * math.pow((1 + i),periods) / (math.pow((1 + i),periods) - 1)
    print("Your monthly payment = {}!".format(math.ceil(a_payment)))
elif(answer == "p"):
    print("Enter the annuity payment:")
    payment = float(input())
    print("Enter the number of periods:")
    periods = float(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    loan = payment * (math.pow((1 + i),periods) - 1) / (i * math.pow((1 + i),periods))
    print("Your loan principal = {}!".format(loan))


