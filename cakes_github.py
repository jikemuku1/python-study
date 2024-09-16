"""
"""


def main():
    a=int(input('Enter the number of layers: '))
    # b=a+5
    for b in range(1,a+1):
        for c in range(a-b):
            print(' ', end='')
        print('[', end='')
        for c in range(2 * b - 1):
            print('*', end='')
        print(']')   
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
