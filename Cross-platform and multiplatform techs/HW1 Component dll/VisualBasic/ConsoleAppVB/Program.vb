Imports System

Module Program
    Sub Main(args As String())
        ClassLibrary1.Solver.Newton(0, 0.0001, 1, New Double() {3.0, 1.0, 1.0})
        ClassLibrary1.Solver.Dichotomy(-1, 1, 0.0001, 1, New Double() {3.0, 1.0, 1.0})
        ClassLibrary1.Solver.Secant(-2, -1, 0.0001, 1, New Double() {3.0, 1.0, 1.0})

        ClassLibrary1.Solver.Newton(0, 0.0001, 2, New Double() {3.0, 4.0, -5.0})
        ClassLibrary1.Solver.Dichotomy(-2, 2, 0.0001, 2, New Double() {3.0, 4.0, -5.0})
        ClassLibrary1.Solver.Secant(0, 0.5, 0.0001, 2, New Double() {3.0, 4.0, -5.0})

        ClassLibrary1.Solver.Newton(0, 0.0001, 3, New Double() {2.0, 2.0, -9.0})
        ClassLibrary1.Solver.Dichotomy(-2, 2, 0.0001, 3, New Double() {2.0, 2.0, -9.0})
        ClassLibrary1.Solver.Secant(0, 0.5, 0.0001, 3, New Double() {2.0, 2.0, -9.0})

        ClassLibrary1.Solver.Help()
        ClassLibrary1.Solver.ProcessFiles("C:\\Users\\maksy\\input.txt", "output.txt")
    End Sub
End Module
