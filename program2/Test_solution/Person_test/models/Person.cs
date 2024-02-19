using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Person_test.models
{
    class Person
    {

        public string Name { get;}
        public int Age { get;}
        public double Weight { get;}
        public bool IsMarried { get;}

        public Person (string name, int age, double weight, bool isMarried = true)
        {
            this.Name = name;
            this.Age = age;
            this.Weight = weight;
            this.IsMarried = isMarried;

        }
    }
}
