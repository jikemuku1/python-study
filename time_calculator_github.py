"""
"""


def main():
    a=float(input("Please enter a time in seconds: "))
    b=((a-(a%3600)%60)%3600)/60
    c=(a%3600)%60
    d=(a%(3600*24)-((a%(3600*24)%3600)-(((a%(3600*24))%3600)%60)))/3600
    e=((a%(3600*24)%3600)-(((a%(3600*24))%3600)%60))/60
    f=((a%(3600*24))%3600)%60
    if a<60:#when the seconds is smaller than 60s
        print(f'  {int(a)} seconds is less than one minute.')
    elif a==60:#when the seconds is 60s
        print(f'  {int(a)} seconds equals {int(a/60)} minute(s).')
    elif a>60 and a<1000:#when the seconds is larger than 60s and smaller than 1000s
        print(f'  {int(a)} seconds equals {int(a/60)} minute(s), and {int(a%60)} second(s).')
    elif a>=1000 and a<3600:#when the seconds is larger than 1000s and smaller than 3600s
        print(f'{int(a):7,.0f} seconds equals {int(a/60)} minute(s), and {int(a%60)} second(s).')
    elif a==3600 :
        print(f'{int(a):7,.0f} seconds equals {int(a/3600)} hour(s).')
    elif a>3600 and a<10000 and b==0 and c!=0:
        print(f'{int(a):7,.0f} seconds equals {int(a/3600)} hour(s), and {int(c)} second(s).')
    elif a>3600 and a<10000 and b!=0 and c==0:
        print(f'{int(a):7,.0f} seconds equals {int(a/3600)} hour(s), and {int(b)} minute(s).')
    elif a>3600 and a<10000 and b!=0 and c!=0:
        print(f'{int(a):7,.0f} seconds equals {int(a/3600)} hour(s), {int(b)} minute(s), and {int(c)} second(s).')
    elif a>=10000 and a<86400 and b==0 and c!=0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600)} hour(s), and {int(c)} second(s).')#a-int(a/3600)-int((a%3600)*3600/60),(a%3600)%60
    elif a>=10000 and a<86400 and b!=0 and c==0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600)} hour(s), and {int(b)} minute(s).')
    elif a>=10000 and a<86400 and b!=0 and c!=0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600)} hour(s), {int(b)} minute(s), and {int(c)} second(s).')
    elif a==86400:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600/24)} day(s).')
    elif a>86400 and a<99999 and d!=0 and e!=0 and f!=0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600/24)} day(s), {int(d)} hour(s), {int(e)} minute(s), and {int(f)} second(s).')
    elif a>86400 and a<99999 and d==0 and e!=0 and f!=0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600/24)} day(s), {int(e)} minute(s), and {int(f)} second(s).')
    elif a>86400 and a<99999 and d!=0 and e==0 and f!=0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600/24)} day(s), {int(d)} hour(s), and {int(f)} second(s).')
    elif a>86400 and a<99999 and d!=0 and e!=0 and f==0:
        print(f'{int(a):8,.0f} seconds equals {int(a/3600/24)} day(s), {int(d)} hour(s), and {int(e)} minute(s).')
    else:
        print(f'{int(a):9,.0f} seconds equals {int(a/3600/24)} day(s), {int(d)} hour(s), {int(e)} minute(s), and {int(f)} second(s).')#((a%(3600*24))%3600)%60


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
