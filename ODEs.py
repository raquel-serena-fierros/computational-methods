def f(x, y):
    return ((y-x))
 
def rk4(x0, y0, x, h):
    
    n = (int)((x - x0)/h)
    y = y0

    print('---------------------------')   
    print('*********** RK4 ***********')
    print('---------------------------')
    
    for i in range(1, n + 1):
 
        #rk4 computation
        k1 = h * f(x0, y)
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x0 + h, y + k3)
        
        # Update next value of y for rk4
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
        print(y)
        print('---------------------------')
    return y
    

def rk3(x0, y0, x, h): 

    n = (int)((x - x0)/h)
    y = y0

    print('\n')   
    print('\n')   
    print('*********** RK3 ***********')
    print('---------------------------')
    for i in range(1, n + 1):

        #rk3 computation
        k1 = h * f(x0, y)
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x0 + h, y-k1 + 2.0 * k2)
        
        # Update next value of y for rk4
        y = y + (1.0 / 6.0)*(k1 + 4 * k2 + k3)

        # Update next value of x
        x0 = x0 + h
        data = y
        
        print(y)
        print('---------------------------')
    return y
 

def euler(x0,y0,x,h):
    print('\n')   
    print('\n')   
    print('*********** EULER ***********')
    print('---------------------------')
 
    n = (int)((x - x0)/h)
    
    for i in range(n+1):
        
        c = f(x0, y0)
        yn = y0 + h * c
        
        print(y0)
        y0 = yn
        x0 = x0+h
        print('---------------------------')  


print('Enter initial point for x0:')
x0 = float(input('x0 = '))
print('Enter initial point for y0:')
y = float(input('y0 = '))

print('Find y(?): ')
x = float(input('y(?) = '))

print('Enter height')
h = float(input('h = '))

#k4(x0, y, x, h)
#rk3(x0, y, x, h)
euler(x0, y, x, h)
 
