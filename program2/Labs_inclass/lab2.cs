using Labs_inclass.models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Labs_inclass
{
    class lab2
    {
        static void Main1(string[] args)
        {
            Car car1 = new Car("Nissan",1997,  20000, true);
            Car car2 = new Car("Ford",2023,  20000);
            Car car3 = new Car( "Tesla",2023, 50000);
            Car car4 = new Car("Ford",1965,  5000, false);
            Console.WriteLine(car1);
            Console.WriteLine(car2);
            Console.WriteLine(car3);
            Console.WriteLine(car4);

        }
    }
}
