using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            ClassLibrary1.Solver.Newton(0, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });
            ClassLibrary1.Solver.Dichotomy(-1, 1, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });
            ClassLibrary1.Solver.Secant(-2, -1, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });

            ClassLibrary1.Solver.Newton(0, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });
            ClassLibrary1.Solver.Dichotomy(-2, 2, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });
            ClassLibrary1.Solver.Secant(0, 0.5, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });

            ClassLibrary1.Solver.Newton(0, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });
            ClassLibrary1.Solver.Dichotomy(-2, 2, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });
            ClassLibrary1.Solver.Secant(0, 0.5, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });

            ClassLibrary1.Solver.Help();
            ClassLibrary1.Solver.ProcessFiles("C:\\Users\\maksy\\input.txt", "C:\\Users\\maksy\\output.txt");
        }
    }
}
