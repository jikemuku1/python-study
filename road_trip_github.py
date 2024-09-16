"""
"""



def main():
    d=float(input("Road trip fuel cost estimator:\n  How far away is your destination (miles)? "))#the distance between your destination and your current position
    p=float(input("  What is the average price of gas (dollars per gallon)? "))
    m=float(input("  What is the fuel efficiency of your vehicle (mpg)? "))
    c=2*d*p/m
    print(f'\nThe fuel cost for this trip is approximately ${int(c)}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
