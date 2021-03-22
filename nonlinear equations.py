from sympy import *

import numpy as zeros
# приближенное решение моё (-0.8, -0.5)
# приближённое решение Кости (0.668, 0.256) и (0, 0)
import math
# кароч сказали, что именно эти символы будут переменными в уравнениях
x1 = Symbol('x1')
x2 = Symbol('x2')
# записали уравнения (уже выраженные)
#-----------------------------------------------------пользовательский ввод------------------------------------------------------------------

#мои
alpha = sqrt(1-x2**2)               #(1+x1**2)*x2              sqrt(x1/x2-1)
beta = (1+x1**2)*x2
# вводим свои функции(мои)
f1 = x1/(1+x2**2)-x2
f2 = x1**2 + x2**2 -1
#Костя
#f1 = x1**2 + x2**2 - 2*x2
#f2 = x2 - 0.5*ln(x1+1)
#пример
#f1 = x2*(x1-1)-1
#f2 = x1**2 - x2**2 - 1
# вводим свои значения(мои)
def_x1 = str(-0.8)
def_x2 = str(-0.5)
#Костя
#def_x1 = str(0.65)
#def_x2 = str(0.25)
#пример
#def_x1 = str(1.5)
#def_x2 = str(1.5)

#-----------------------------------------------------------------------------------------------------------------------

# нашли производные
ax1 = diff(alpha, x1, 1)
ax2 = diff(alpha, x2, 1)
bx1 = diff(beta, x1, 1)
bx2 = diff(beta, x2, 1)

derivs=[[ax1, ax2], [bx1, bx2]]
for_norma = [[1,1],[1,1]]
for i in range(len(derivs)):
    for j in range(len(derivs[i])):
        derivs[i][j] = str(derivs[i][j]).replace("x1", def_x1)
        derivs[i][j] = derivs[i][j].replace("x2", def_x2)
        print("derivs[", i, "][", j, "]: ", derivs[i][j])
        for_norma[i][j] = eval(derivs[i][j])
        print("for norma[", i, "][", j, "]: ", for_norma[i][j])

cube_norma = max(abs(float(for_norma[0][0]))+abs(float(for_norma[0][1])), abs(float(for_norma[1][0]))+abs(float(for_norma[1][1])))
octa_norma = max(abs(float(for_norma[0][0]))+abs(float(for_norma[1][0])), abs(float(for_norma[0][1]))+abs(float(for_norma[1][1])))

print("ax1: ", ax1)
print("ax2: ", ax2)
print("bx1: ", bx1)
print("bx2: ", bx2)
print ("cube: ", cube_norma)
print ("oct: ", octa_norma)

# по прикольчику выходим, если норма и в этом случае меньше нужного числа
if cube_norma>1 and octa_norma>1:
    import sys
    sys.exit(0)

proizv = [[eval(str(diff(f1, x1, 1)).replace("x1", def_x1).replace("x2", def_x2)),     eval(str(diff(f2, x1, 1)).replace("x1", def_x1).replace("x2", def_x2)) ],
          [eval(str(diff(f1, x2, 1)).replace("x2", def_x2).replace("x1", def_x1)),     eval(str(diff(f2, x2, 1)).replace("x2", def_x2).replace("x1", def_x1))]]

print("proizvodniye v tochke: ",proizv)
import numpy
lamb12 = numpy.array([[proizv[0][0], proizv[0][1]],[proizv[1][0], proizv[1][1]]])
lamb1_free = [-1, 0]

lamb2_free = [0, -1]
lambdas11_12 = numpy.linalg.solve(lamb12, lamb1_free)
lambdas21_22 = numpy.linalg.solve(lamb12, lamb2_free)

lambdas = [[lambdas11_12[0],lambdas11_12[1]],[lambdas21_22[0],lambdas21_22[1]]]
print("lambdas11_12_21_22: ",lambdas)

X_mass = [float(def_x1), float(def_x2)]
X_mass_next = [0,0]
check = 0
# проверка на неравенство нулю определителя лямбд
if lambdas[0][0]*lambdas[1][1]-lambdas[0][1]*lambdas[1][0]:
    for i in range(1000):
        X_mass_next[0] = X_mass[0]\
                         + lambdas[0][0]*float(eval(str(f1).replace("x1", str(X_mass[0])).replace("x2", str(X_mass[1])))) + \
                         lambdas[0][1]* float(eval(str(f2).replace("x1", str(X_mass[0])).replace("x2", str(X_mass[1]))))
        X_mass_next[1] = X_mass[1] + lambdas[1][0] * float(eval(str(f1).replace("x1", str(X_mass[0])).replace("x2", str(X_mass[1])))) + \
                         lambdas[1][1] * float(eval(str(f2).replace("x1", str(X_mass[0])).replace("x2", str(X_mass[1]))))
        X_diff_max = max(abs(X_mass_next[1])-abs(X_mass[1]),abs(X_mass_next[0])-abs(X_mass[0]))
        check+=1
        if X_diff_max<0.0001:
            break
        X_mass[0]=X_mass_next[0]
        X_mass[1]=X_mass_next[1]
        print("x1", X_mass_next[0],"x2", X_mass_next[1])
print("X-es: ", X_mass_next)
print("iters: ", check)
print('X_diff_max',X_diff_max)