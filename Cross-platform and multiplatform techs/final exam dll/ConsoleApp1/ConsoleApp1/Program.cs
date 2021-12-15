using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Test output");
            var encr = ClassLibrary1.Solver.Encrypt("Maksym Шевченко", 8);
            Console.WriteLine(encr);
            var decr = ClassLibrary1.Solver.Decrypt(encr, 8);
            Console.WriteLine(decr);


            Console.WriteLine("\n\n");
            ClassLibrary1.Solver.Main();
        }
    }
}
