"""
"""


def main():
    
    a = float(input("Starting population, in thousands: "))
    b = float(input("Average daily increase, in percent: "))
    c = int(input("Number of days to multiply: "))
    d = max(len(str(c)), 2)
    print('Day   Approx. Pop') 
    for e in range(c+1):    #each iteration for days, the range object produces the next integer ina sequence
        print(f' {e:>{d},.0f}    {a:10,.3f}') #print days and total population
        a*=(1+(b)/100)      #each iteration for population, the range object produces the next integer ina sequence

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
