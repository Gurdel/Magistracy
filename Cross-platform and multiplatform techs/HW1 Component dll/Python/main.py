import clr
clr.AddReference('ClassLibrary1')
from ClassLibrary1 import Solver


Solver.Newton(0, 0.0001, 1, [3.0, 1.0, 1.0 ])
Solver.Dichotomy(-1, 1, 0.0001, 1, [3.0, 1.0, 1.0 ])
Solver.Secant(-2, -1, 0.0001, 1, [3.0, 1.0, 1.0 ])

Solver.Newton(0, 0.0001, 2, [3.0, 4.0, -5.0])
Solver.Dichotomy(-2, 2, 0.0001, 2, [3.0, 4.0, -5.0])
Solver.Secant(0, 0.5, 0.0001, 2, [3.0, 4.0, -5.0])

Solver.Newton(0, 0.0001, 3, [2.0, 2.0, -9.0])
Solver.Dichotomy(-2, 2, 0.0001, 3, [2.0, 2.0, -9.0])
Solver.Secant(0, 0.5, 0.0001, 3, [2.0, 2.0, -9.0])

Solver.Help()