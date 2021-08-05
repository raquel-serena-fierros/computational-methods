from pprint import pprint

def gauss_seidel(a, x ,b):
    n = len(a)                   
    for j in range(0, n):        
        d = b[j]                  
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]    
        x[j] = d / a[j][j]        
    return x                
n = 4                             
a = []                            
b = []       

# Diagonally dominant 
print("***With Diagonally-dominant form:***\n")
x = [0, 0, 0,0]                        
a = [[10,1,-2,2],[2,-8,1,-3],[4,-1,7,2],[4,3,1,-9]]
b = [3,-15,19,-22]
count = 0;
print("count:", count)
pprint(x)

for i in range(0, 25):            
    x = gauss_seidel(a, x, b)
    count = i+1;
    print("count:", count)
    pprint(x)

# Not diagonally dominant 
print("\n\n\n***Without Diagonally-dominant form:***\n")
x = [0, 0, 0,0]                        
a = [[2,-8,1,-3],[10,1,-2,2],[4,3,1,-9],[4,-1,7,2]]
b = [-15,3,-22,19]
count = 0;
print("count:", count)
pprint(x)

for i in range(0, 25):            
    x = gauss_seidel(a, x, b)
    count = i+1;
    print("count:", count)
    pprint(x)