using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace wk5_exer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Time t1 = new Time(11200);
            Time t2 = new Time(11100);
            Time t3 = t1 - t2;
            bool equalornot = t1== t2;
            Console.WriteLine(t1);
            Console.WriteLine(t2);
            Console.WriteLine(t3);
            Console.WriteLine(equalornot);

        }
    }
}
