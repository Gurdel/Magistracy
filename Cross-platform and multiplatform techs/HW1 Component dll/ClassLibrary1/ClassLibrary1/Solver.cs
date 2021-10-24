using System;

namespace ClassLibrary1
{
    public class Solver
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

        public static void Newton(double x, double e, int template, double[] args)
        {
            Console.WriteLine("\tNewton (tangent) method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return;
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
        }

        public static void Dichotomy(double a, double b, double e, int template, double[] args)
        {
            Console.WriteLine("\tDichotomy method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return;
            }
            FuncDelegate F = ApplyTemplate(template, args);

            if (F(a, args) * F(b, args) > 0)
            {
                Console.WriteLine("Bad interval");
                return;
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
        }

        public static void Secant(double x_2, double x_1, double e, int template, double[] args)
        {
            Console.WriteLine("\tSecant (chord) method");
            if (args.Length < 3)
            {
                Console.WriteLine("Not enough arguments for template");
                return;
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
        }
    
    }
}
