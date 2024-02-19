using Labs_inclass.models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Labs_inclass
{
    class lab3
    {
        static void Main(string[] args)
        {
            Date date1 = new Date(23, 01, 2011);
            Console.WriteLine(date1);
            date1.Add(12);
            Console.WriteLine(date1);

            date1.Add(1, 2);
            Console.WriteLine(date1);

            date1.Add(new Date(1, 1, 1000));
            Console.WriteLine(date1);



        }
    }
}
