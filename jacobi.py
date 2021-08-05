from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A,b,N=35,x=None):
    if x is None:
        x = zeros(len(A[0]))
    D = diag(A)
    R = A - diagflat(D)
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x
    
 
initial = array([0,0,0,0])

#diagonally dominant arrays 
A_diagdom = array([[10,1,-2,2],[2,-8,1,-3],[4,-1,7,2],[4,3,1,-9]])
b_diagdom = array([3,-15,19,-22])

# non diagonally dominant arrays 
A = array([[2,-8,1,-3],[10,1,-2,2],[4,3,1,-9],[4,-1,7,2]])
b = array([-15,3,-22,19])

solution1 = jacobi(A_diagdom, b_diagdom, N=35, x= initial)
print("***Diagonally-dominant form:***")
print("A:")
pprint(A_diagdom)
print("b:")
pprint(b_diagdom)
print("Solution x:")
pprint(solution1)

print("\n")
solution2 = jacobi(A, b, N=25, x= initial)
print("***Without Diagonally-dominant form:***")
print("A:")
pprint(A)
print("b:")
pprint(b)
print("Solution x:")
pprint(solution2)
