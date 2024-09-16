"""
"""


def main():
    a=int(input("How many packages will be purchased: "))
    f=a*880
    b=(a-0.1*a)*880
    c=float((a-0.15*a)*880)
    d=(a-0.3*a)*880
    e=(a-0.42*a)*880
    if a<0:#the first case for leap year
        print(f'  Invalid Input!')
    elif a>=0 and a<4:#the first case for leap year
        print(f'  No discount applied.\n  The total price to purchase {a} packages is ${f:6,.2f}.')
    elif a>=4 and a<40:#the first case for leap year
        print(f'  10% discount applied.\n  The total price to purchase {a} packages is ${b:8,.2f}.')
    
    elif a>=40 and a<200:#the second case for leap year
        print(f'  15% discount applied.\n  The total price to purchase {a} packages is ${c:8,.2f}.')
    elif a>=200 and a<1000:#the second case for leap year
        print(f'  30% discount applied.\n  The total price to purchase {a} packages is ${d:8,.2f}.')
    else:
        print(f'  42% discount applied.\n  The total price to purchase {a} packages is ${e:8,.2f}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
