using System;

namespace lab8_complex
{
    internal class Program
    {
        static void Main(string[] args)
        {


            Complex c0 = new Complex(-2, 3);
            Complex c1 = new Complex(-2, 3);
            Complex c2 = new Complex(1, -2);

            Console.WriteLine($"{c0}");
            Console.WriteLine(c1);
            Console.WriteLine(c2);
            Console.WriteLine($"{c1} + {c2} = {c1 + c2}");
            Console.WriteLine($"{c1} - {c2} = {c1 - c2}");
            Complex c3 = c1 + c2;

            Console.WriteLine($"{c3} in polar form is {c3.Modulus:f2} is ({c3.Argument:f2})");

            Console.WriteLine($"{c0} {(c0 == c1 ? "=" : "!=")} {c1}");
            Console.WriteLine($"{c0} {(c0 == c2 ? "=" : "!=")} {c2}");
            Complex c4 = c1 * c2;
            Console.WriteLine($"{c1}*{c2} is {c4}");
            Console.WriteLine($"-({c1}) is {-c1}");
            



        }
    }
}
