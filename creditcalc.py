import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["diff", "annuity"],
                    help="You need to choose only diff of annuity.")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

parameters = [args.type, args.principal, args.periods,
               args.interest, args.payment]
# print(parameters[2])


value = len(parameters)
j = 0
while (j < len(parameters)):
    if(parameters[j] == None):
        value = value -1
        j = j + 1
    else:
        j = j + 1
# print(value)

def check(num):
    if (num != None):
        return (float(num) < 0)
    else:
        return False
# print(check(-5))

if(parameters[0] == "diff" and parameters[4] != None):
    print("IT is diff payment.Incorrect parameters")
elif(parameters[0] == "diff"):
    if(value < 4):
        print("Incorrect parameters1")
    elif(check(parameters[1]) or check(parameters[2]) or check(parameters[3])):
        print("Incorrect parameters11")
    else:
        print("It is diff payment")
        i = float(parameters[3]) / (12 * 100)
        m = 1
        overpayment = 0 - float(parameters[1])
        while(m <= float(parameters[2])):
            d = float(parameters[1]) / float(parameters[2]) + i * (float(parameters[1]) - (float(parameters[1])*(m-1)/float(parameters[2])))
            print("Month {}: payment is {}".format(m,math.ceil(d)))
            overpayment = overpayment + math.ceil(d)
            m = m + 1
        print("Overpayment = {}".format(math.ceil(overpayment)))
elif(parameters[0] == "annuity"):
    if(value < 4):
        print("Incorrect parameters2")
    elif(check(parameters[1]) or check(parameters[2]) or
     check(parameters[3]) or check (parameters[4])):
        print("Incorrect parameters21")
    else:
        # print("It is annuity payment")
        if(parameters[1] == None):
            i = float(parameters[3]) / (12 * 100)
            principal = math.ceil(float(parameters[4]) * (math.pow((1 + i),float(parameters[2])) - 1) / (i * math.pow((1 + i),float(parameters[2]))))
            print("Your annuity payment = {}!".format(principal))
            overpayment = float(parameters[2]) * float(parameters[4]) - principal
            print("Overpayment = {}".format(overpayment))
        elif(parameters[4] == None):
            i = float(parameters[3]) / (12 * 100)
            payment = math.ceil(float(parameters[1]) * i * math.pow((1 + i),float(parameters[2])) / (math.pow((1 + i),float(parameters[2])) - 1))
            print("Your annuity payment = {}!".format(payment))
            overpayment = payment * float(parameters[2]) - float(parameters[1])
            print("Overpayment = {}".format(overpayment))
        elif(parameters[2] == None):
            i = float(parameters[3]) / (12 * 100)
            n = math.ceil (math.log(float(parameters[4])/(float(parameters[4])-i*float(parameters[1])) , (1 + i)))
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
            overpayment = float(parameters[4]) * n - float(parameters[1])
            print("Overpayment = {}".format(overpayment))
else:
    print("Incorrect parameters")
