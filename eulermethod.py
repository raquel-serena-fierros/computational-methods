import math

def f(x,y):
    return y-(x**2)+1
    
def f1(x):
    return ((x+1)**2)-.5*math.exp( x )

def euler(x0,y0,b,n):
    h = (b-x0)/n
    print('-----------------------------------------------------------------------')    
    print('ti\t        wi\t       yi=y(ti)\t       |(yi-wi)|\t|(yi-wi)/yi|*100')
    print('-----------------------------------------------------------------------')
    for i in range(n+1):
        exact =  f1(x0)
        c = f(x0, y0)
        yn = y0 + h * c
        relerror = abs((exact - y0) / exact) * 100
        error = abs((exact - y0))
        print('%.6f\t%.6f\t%0.6f\t%0.6f\t%.6f'% (x0,y0,exact,error, relerror) )
        print('-----------------------------------------------------------------------')
        y0 = yn
        x0 = x0+h

print('Enter initial point for t:')
x0 = float(input('a = '))
y0 = float(input('y initial point = '))

print('Enter end point for t: ')
b = float(input('b = '))

print('Enter number of steps:')
num = int(input('N = '))

euler(x0,y0,b,num)
