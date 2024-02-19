using Labs_inclass.models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Labs_inclass
{
    class Program2
    {
        static void Main1(string[] args)
        {
            Console.WriteLine("Hello World");
            Person me = new Person();
            me.FirstName = "Luiz";
            me.LastName = "Benjamin";
            me.DateOfBirth = new DateTime(1985, 07, 15);
            Console.WriteLine(me.FirstName+" "+me.LastName);


        }
    }
}
