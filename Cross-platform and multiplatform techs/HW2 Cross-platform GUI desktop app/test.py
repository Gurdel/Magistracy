import solver as Solver

print(*Solver.Newton(0, 0.0001, 1, [3.0, 1.0, 1.0 ]), sep='\n')
print(*Solver.Dichotomy(-1, 1, 0.0001, 1, [3.0, 1.0, 1.0 ]), sep='\n')
print(*Solver.Secant(-2, -1, 0.0001, 1, [3.0, 1.0, 1.0 ]), sep='\n')

print(*Solver.Newton(0, 0.0001, 2, [3.0, 4.0, -5.0]), sep='\n')
print(*Solver.Dichotomy(-2, 2, 0.0001, 2, [3.0, 4.0, -5.0]), sep='\n')
print(*Solver.Secant(0, 0.5, 0.0001, 2, [3.0, 4.0, -5.0]), sep='\n')

print(*Solver.Newton(0, 0.0001, 3, [2.0, 2.0, -9.0]), sep='\n')
print(*Solver.Dichotomy(-2, 2, 0.0001, 3, [2.0, 2.0, -9.0]), sep='\n')
print(*Solver.Secant(0, 0.5, 0.0001, 3, [2.0, 2.0, -9.0]), sep='\n')

print(Solver.Help(), sep='\n')