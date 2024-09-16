"""
"""


def main():
    P=float(input("Enter the following parameters.\n  The initial deposit? "))# the initial deposit of your account
    r=float(input("  The annual interest rate in percent? "))# the annual interest rate in percent
    t=float(input("  The number of years the account earn interest? "))# the number of years the account earn interest
    n=float(input("  The number of times interest is compounded each year: "))
    FV=P*((1+r/100/n)**(t*n))
    print(f'The balance of this account will be ${FV:10,.2f} after {float(t):.1f} years.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
