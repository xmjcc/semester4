using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace wk4_excercise
{
    internal class Program
    {
        static void Main(string[] args)
        {


            Distance d1 = new Distance();
            d1.Mile = 1;
            Console.WriteLine(d1.Km);
            d1.Km = 2;
            Console.WriteLine(d1.Mile);


        }
    }
}
