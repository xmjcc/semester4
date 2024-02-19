using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Labs_inclass
{
    internal class Car
    {
        private int year;
        private string model;
        private bool isDrivable;
        private double price;
        private string drivable;
        public Car(string model, int year, double price, bool isDrivable = true)
        {
            this.year = year;
            this.model = model;
            this.price = price;
            this.isDrivable = isDrivable;

        }

        public override string ToString()
        {
            if (this.isDrivable == true)
            { drivable = "is drivable"; }
            else
            {
                drivable = "is not drivable";
            }
            return $"{year} {model} {drivable} and the price is {price}";
        }


    }
}
