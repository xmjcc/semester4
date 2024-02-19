using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab5
{
    internal class Pet
    {


        public string Name { get; set; }
        public string Owner { get; set; }
        public int Age { get; set; }
        public string Description { get; set; }
        public bool IsHouseTrain {get; set; }

        public Pet (string name, int age, string description)
        {
            this.Name = name;
            this.Age = age;
            this.Description = description;
            this.Owner = "no one";
            this.IsHouseTrain = false;

        }


        public override string ToString()
        {
            string recordString = IsHouseTrain ? "house trained" : "not house trained";
            return $"{Name} {Description}  's owner is - {Owner} is {recordString}";
        }

        public void SetOwner(string newowner)
        {
            this.Owner = newowner;

        }

        public void Train(bool isHouseTrain)
        {
            this.IsHouseTrain =isHouseTrain;

        }

    }
}
