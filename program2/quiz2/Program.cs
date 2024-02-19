using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace quiz2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Car car1 = new Car();
            Car car2 = new Car();
            car1.Model = "Toyota";
            car2.Model = "Honda";
            Car car3 = car1;
            car3.Model = "Tesla";

            Console.WriteLine("Car1: " + car1.Model);
            Console.WriteLine("Car2: " + car2.Model);
            Console.WriteLine("Car3: " + car3.Model);
        }
    }
}
