using System;

namespace ClassLibrary1
{
    class Solver
    {
        public static double F(double x)
        {
            return (3.0 * x + Math.Cos(x) + 1.0);
        }
        public static double F1(double x)
        {
            return (3.0 - Math.Sin(x));
        }

        static void Newton()
        {
            double x = 0;
            double e = 0.0001;
            double f = F(x);
            double f1 = F1(x);
            int i = 0;
            Console.WriteLine($"{i}) \t x = {x.ToString("F" + 10)} ; \t f = {f.ToString("F" + 10)} ;");
            while (Math.Abs(f) > e)
            {
                x = x - (f / f1);

                f = F(x);
                f1 = F1(x);
                ++i;
                Console.WriteLine($"{i}) \t x = {x.ToString("F" + 10)} ; \t f = {f.ToString("F" + 10)} ;");
            }
        }

        static void Dichotomy()
        {
            double a = -1;
            double b = 1;
            double x = 0;
            double e = 0.0001;
            double f = F(x);
            int i = 0;
            Console.WriteLine($"{i}) \t a = {a.ToString("F" + 10)} ;\t b = {b.ToString("F" + 10)} ;\t x = {x.ToString("F" + 10)} ; \t f = {f.ToString("F" + 10)} ;");
            while (Math.Abs(f) > e)
            {
                if (Math.Sign(F(a)) == Math.Sign(F(x)))
                    a = x;
                if (Math.Sign(F(b)) == Math.Sign(F(x)))
                    b = x;

                x = (a + b) / 2;
                f = F(x);
                ++i;
                Console.WriteLine($"{i}) \t a = {a.ToString("F" + 10)} ;\t b = {b.ToString("F" + 10)} ;\t x = {x.ToString("F" + 10)} ; \t f = {f.ToString("F" + 10)} ;");
            }
        }
    }
}
