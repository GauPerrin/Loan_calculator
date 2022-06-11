import argparse
import math
import sys

# to check the number of argument <5
# You provide 4 arguments and one is unknown and will be computed with the 4 other
parser = argparse.ArgumentParser(description="This program is a credit calculator.")
parser.add_argument(
    "--type",
    choices=["diff", "annuity"],
    help="You need to choose only one kind of loan from the list",
)

parser.add_argument(
    "--payment",
    type=float,
    help="Enter the monthly payment ",
)
parser.add_argument(
    "--principal",
    type=float,
    help="Enter the amount of your principal",
)

parser.add_argument(
    "--periods",
    type=int,
    help="Enter the length in month until full repayment",
)

parser.add_argument(
    "--interest",
    type=float,
    help="Enter the loan interest percentage ",
)
# the only


# 5 argument
# cannot run with less than 4 argument for bot annuity and differentiated payment

if len(sys.argv) != 5:
    # remenber that sys.argv gives a list with the program name first so +1
    print("You need to enter 4 arguments")
    quit()
    # stops the program there if there is more or less arguments than 4


args = parser.parse_args()


if args.interest is not None:
    i = ((args.interest) / 100) / 12
else:
    print("Interest is required for each calculation")
    quit()


if args.type == "diff":
    sum = 0
    p = args.principal
    n = args.periods
    for h in range(n):
        d = (p / n) + i * (p - (p * h) / n)
        d = math.ceil(d)
        # rounding up the output
        sum = sum + d
        print("Month " + str(h + 1) + " payment is " + str(d))
    print("\n")
    print("Overpayment = " + str(sum - p))

elif args.type == "annuity":

    if args.payment is None:
        p = args.principal
        n = args.periods

        a = math.ceil(p * (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
        sum = int((n * a) - p)
        print("Your annuity payment = " + str(a) + "!")
        print("Overpayement = " + str(sum))

    elif args.principal is None:
        n = args.periods
        a = args.payment
        p = math.floor(a / ((i * (1 + i) ** n) / (((1 + i) ** n) - 1)))
        sum = int((n * a) - p)

        print("Your loan principal = " + str(p) + "!")
        print("Overpayment = " + str(sum))

    elif args.periods is None:
        a = args.payment
        p = args.principal
        n = math.log(a / (a - i * p), (1 + i))

        n = math.ceil(n)
        y = n / 12
        # so as only to get the integer
        n1 = math.floor((y - math.floor(y)) * 12)
        years = n // 12
        sum = int((n * a) - p)

        print(
            "It will take "
            + str(years)
            + " years and "
            + str(n1)
            + " months to repay this loan!"
        )
        print("Overpayment = " + str(sum))
