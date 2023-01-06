import math
print("Enter the loan principal:")
s = float(input())
print('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:''')
answer = input()
if(answer == "m"):
    print("Enter the monthly payment:")
    answer_m = float(input())
    month = math.ceil( s / answer_m)
    if (month == 1):
        print("It will take 1 month to repay the loan")
    else:
        print("It will take ", month," months to repay the loan")
elif(answer == "p"):
    print("Enter the number of months:")
    answer_p = float(input())
    payment = math.ceil( s / answer_p)
    lastpayment = s - (answer_p - 1) * payment
    if (payment == lastpayment):
        print("Your monthly payment = ", payment)
    else:
        print("Your monthly payment = ", payment, " and the last payment = " , lastpayment, ".")

