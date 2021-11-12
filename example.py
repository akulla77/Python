import math

def sign(num):
    return f'{num}' if num <= 0 else f'+{num}'

def check_int(s):
    if  not s:
        return False
    elif s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def enter_digit():
        s=input()
        while (not check_int(s)):
            print('ENTER DIGIT!!!')
            s=input()
        return s


print("Enter a ")
a = float(enter_digit())
print("Enter b ")
b = float(enter_digit())
print("Enter c ")
c = float(enter_digit())



print(f'{a}x^2{sign(b)}x{sign(c)}=0')

d=b**2-4*a*c
print("d =",d)
try:
    if d > 0:
        x1=(-b+math.sqrt(d)/ (2*a))
        x2=(-b-math.sqrt(d)/ (2*a))
        print ("x1 = ",x1,"x2 = ",x2)
    elif d == 0:
        x=-b/(2*a)
        print("x =",x)
    else:
        print("No roots, because d<0")
except Exception as e:
    print("Unhandled exception! ",e)


