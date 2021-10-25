using System;
using System.Globalization;
using System.IO;

namespace ConsoleForTesting
{
    class Program
    {
        public static void Help()
        {
            string text = @"
                Library for solving equations by numerical methods

                Equations templates:
                    1. a*x + b*cos(x) + c
                    2. a*x^2 + b*x + c
                    3. a*x * exp(b*x) + c

                Methods:
                    1. Newton (tangent) method
                    2. Dichotomy method
                    3. Secant (chord) method

Common function parameters:
    e: accuracy
    template: number of equation template
    args: list of equation parameters [a, b, c]
Newton(double x, double e, int template, double[] args)
    x: init value
Dichotomy(double a, double b, double e, int template, double[] args)
    a: left value of the interval in which the solution is located
    b: right value of the interval in which the solution is located
Secant(double x_2, double x_1, double e, int template, double[] args)
    x_1: previous value of x (Xn-1)
    x_2: previous value of x_1 (Xn-2)
 ";
            Console.WriteLine(text);
        }

        delegate double FuncDelegate(double x, double[] args);
        private static double template_1(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            var c = args[2];
            return (a * x + b * Math.Cos(x) + c);
        }
        private static double template_1_derivate(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            return (a - b * Math.Sin(x));
        }
        private static double template_2(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            var c = args[2];
            return (a * x * x + b * x + c);
        }
        private static double template_2_derivate(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            return (2 * a * x + b);
        }
        private static double template_3(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            var c = args[2];
            return (a * x * Math.Exp(b * x) + c);
        }
        private static double template_3_derivate(double x, double[] args)
        {
            var a = args[0];
            var b = args[1];
            return (a * Math.Exp(b * x) + a * b * x * Math.Exp(b * x));
        }

        static FuncDelegate ApplyTemplate(int template, double[] args)
        {
            FuncDelegate F = template_1; //default template
            switch (template)
            {
                case 1:
                    Console.WriteLine($"{args[0]}x + {args[1]}cos(x) + {args[2]}\n");
                    break;
                case 2:
                    F = template_2;
                    Console.WriteLine($"{args[0]}x^2 + {args[1]}x + {args[2]}\n");
                    break;
                case 3:
                    F = template_3;
                    Console.WriteLine($"{args[0]}x * exp({args[1]}x) + {args[2]}\n");
                    break;
                default:
                    Console.WriteLine("Applied default template");
                    Console.WriteLine($"{args[0]}x + {args[1]}cos(x) + {args[2]}\n");
                    break;
            }
            return F;
        }

        static FuncDelegate GetDerivate(int template)
        {
            FuncDelegate F = template_1_derivate; //default template derivate
            switch (template)
            {
                case 1:
                    break;
                case 2:
                    F = template_2_derivate;
                    break;
                case 3:
                    F = template_3_derivate;
                    break;
                default:
                    break;
            }
            return F;
        }

        public static double[] Newton(double x, double e, int template, double[] args)
        {
            Console.WriteLine("\tNewton (tangent) method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return new double[] { 0, 0, 0};
            }
            FuncDelegate F = ApplyTemplate(template, args);
            FuncDelegate F_derivate = GetDerivate(template);

            double f = F(x, args);
            double f1 = F_derivate(x, args);
            int i = 0;
            Console.WriteLine($"{i}) \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
            while (Math.Abs(f) > e)
            {
                x = x - (f / f1);

                f = F(x, args);
                f1 = F_derivate(x, args);
                ++i;
                Console.WriteLine($"{i}) \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
            }
            Console.WriteLine("\n");
            return new double[] { i, x, f};
        }

        public static double[] Dichotomy(double a, double b, double e, int template, double[] args)
        {
            Console.WriteLine("\tDichotomy method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return new double[] { 0, 0, 0 };
            }
            FuncDelegate F = ApplyTemplate(template, args);

            if (F(a, args) * F(b, args) > 0)
            {
                Console.WriteLine("Bad interval");
                return new double[] { 0, 0, 0 };
            }

            double x = (a + b) / 2;
            double f = F(x, args);
            int i = 0;
            Console.WriteLine($"{i}) \t a = {a.ToString("F" + 10)} \t b = {b.ToString("F" + 10)} \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
            while (Math.Abs(f) > e)
            {
                if (Math.Sign(F(a, args)) == Math.Sign(F(x, args)))
                    a = x;
                if (Math.Sign(F(b, args)) == Math.Sign(F(x, args)))
                    b = x;

                x = (a + b) / 2;
                f = F(x, args);
                ++i;
                Console.WriteLine($"{i}) \t a = {a.ToString("F" + 10)} \t b = {b.ToString("F" + 10)} \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
            }
            Console.WriteLine("\n");
            return new double[] { i, x, f };
        }

        public static double[] Secant(double x_2, double x_1, double e, int template, double[] args)
        {
            Console.WriteLine("\tSecant (chord) method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return new double[] { 0, 0, 0 };
            }
            FuncDelegate F = ApplyTemplate(template, args);

            double x = x_1;
            double f = F(x, args);
            int i = 0;
            Console.WriteLine($"{i}) \t x-2 = {x_2.ToString("F" + 10)} \t x-1 = {x_1.ToString("F" + 10)} \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
            while (Math.Abs(f) > e)
            {
                x = x_1 - F(x_1, args) * ((x_1 - x_2) / (F(x_1, args) - F(x_2, args)));

                f = F(x, args);
                ++i;
                Console.WriteLine($"{i}) \t x-2 = {x_2.ToString("F" + 10)} \t x-1 = {x_1.ToString("F" + 10)} \t x = {x.ToString("F" + 10)}  \t f = {f.ToString("F" + 10)} ");
                x_2 = x_1;
                x_1 = x;
            }
            Console.WriteLine("\n");
            return new double[] { i, x, f };
        }
        public static void ProcessFiles(string input, string output)
        {
            Console.WriteLine($"Processing input file {input}");
            try
            {
                StreamReader sr = new StreamReader(input);
                StreamWriter sw = new StreamWriter(output);


                string line = sr.ReadLine();
                while (line != null)
                {
                    string[] a = line.Trim().Replace('.', ',').Split(' ');
                    double[] res = { };
                    string method = a[0];
                    switch (method)
                    {
                        case "Newton":
                            res = Newton(Double.Parse(a[1]), Double.Parse(a[2]), Int32.Parse(a[3]), new double[] { Double.Parse(a[4]), Double.Parse(a[5]), Double.Parse(a[6])});                            
                            break;
                        case "Dichotomy":
                            res = Dichotomy(Double.Parse(a[1]), Double.Parse(a[2]), Double.Parse(a[3]), Int32.Parse(a[4]), new double[] { Double.Parse(a[5]), Double.Parse(a[6]), Double.Parse(a[7]) });
                            break;
                        case "Secant":
                            res = Secant(Double.Parse(a[1]), Double.Parse(a[2]), Double.Parse(a[3]), Int32.Parse(a[4]), new double[] { Double.Parse(a[5]), Double.Parse(a[6]), Double.Parse(a[7]) });
                            break;
                        default:
                            sw.WriteLine($"Incorrect method {method}");
                            break;
                    }
                    sw.WriteLine($"iteration: {res[0]}\tx = {res[1].ToString("N10", CultureInfo.InvariantCulture)}\tF(x) = {res[2].ToString("N10", CultureInfo.InvariantCulture)}\tmethod: {method}");
                    line = sr.ReadLine();
                }

                sr.Close();
                sw.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
            finally
            {
                Console.WriteLine($"Processing completed. The results are written to {output}");
            }
        }

        static void Main(string[] args)
        {
            Newton(0, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });
            Dichotomy(-1, 1, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });
            Secant(-2, -1, 0.0001, 1, new double[] { 3.0, 1.0, 1.0 });

            Newton(0, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });
            Dichotomy(-2, 2, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });
            Secant(0, 0.5, 0.0001, 2, new double[] { 3.0, 4.0, -5.0 });

            Newton(0, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });
            Dichotomy(-2, 2, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });
            Secant(0, 0.5, 0.0001, 3, new double[] { 2.0, 2.0, -9.0 });

            Help();
            ProcessFiles("C:\\Users\\maksy\\input.txt", "C:\\Users\\maksy\\output.txt");
        }
    }
}
