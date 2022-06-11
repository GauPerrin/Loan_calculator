import argparse
import math
import sys

print("What kind of loan do have?")
print(
    """type "d" for differentiated payment,
type "a" for annuity payment,
type "zero" for 0 percent loan:
"""
)
kind = input()

if kind == "zero":
    print("Enter the loan principal:")
    choice = int(input())
    print("What do you want to calculate?")
    print(
        """type "m" for number of monthly payments,
     type "p" for the monthly payment:"""
    )
    type = input()
    if type == "p":
        print("Enter the number of months:")
        months = int(input())
        payment = math.ceil(choice / months)
        last_payment = choice - (months - 1) * payment
        print(
            "Your monthly payment = "
            + str(payment)
            + " and the last payment = "
            + str(last_payment)
            + "."
        )
    elif type == "m":
        print("Enter the monthly payment:")
        pay = int(input())
        time_left = math.ceil(choice / pay)
        if time_left == 1:
            print("It will take " + str(time_left) + " month to repay the loan")
        else:
            print("It will take " + str(time_left) + " months to repay the loan")
# ne pas oublier les str() pour mettre des chiffres dans un string de print

elif kind == "a":
    print("What do you want to calculate ?")
    print(
        """type "n" for number of monthly payments,
     type "a" for annuity monthly payment amount,
     type "p" for loan principal:"""
    )
    choice = input()
    if choice == "n":
        print("Enter the loan principal:")
        principal = int(input())
        print("Enter the monthly payment:")
        mpay = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        i = (interest / 100) / 12
        month = math.log(mpay / (mpay - i * principal), (1 + i))
        month = math.ceil(month)
        year = month / 12
        # so as only to get the integer
        months = math.floor((year - math.floor(year)) * 12)
        years = month // 12

        print(
            "It will take "
            + str(years)
            + " years and "
            + str(months)
            + " months to repay this loan!"
        )

    elif choice == "a":
        print("Enter the loan principal:")
        principal = int(input())
        print("Enter the number of periods:")
        periods = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        i = (interest / 100) / 12
        annuity = math.ceil(
            principal * (i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)
        )
        # this assumes payments are made monthly
        print("Your monthly payment = " + str(annuity) + "!")

    elif choice == "p":
        print("Enter the annuity payment:")
        annuity = float(input())
        print("Enter the number of periods:")
        periods = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        i = (interest / 100) / 12
        principal = annuity / ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
        print("Your loan principal = " + str(principal) + "!")

    else:
        print("Please enter correctly 'n' , 'p' or 'a'")

elif kind == "d":
    print("Enter loan principal: ")
    p = int(input())
    print("Enter the number of periods (in months)")
    n = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = (interest / 100) / 12
    sum = 0
    for h in range(n):
        d = (p / n) + i * (p - (p * h) / n)
        d = math.ceil(d)
        # rounding up the output
        sum = sum + d
        print("Month " + str(h + 1) + " payment is " + str(d))
    print("\n")
    print("Overpayment = " + str(sum - p))

else:
    print("You must have misstyped your loan type")
