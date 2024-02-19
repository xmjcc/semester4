using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace wk6
{
    internal class Program
    {
        class ClassA
        {
            public ClassA() { Console.WriteLine("ClassA"); }
        }

        class ClassB : ClassA
        {
            public ClassB(string s = "Default") { Console.WriteLine("ClassB" + s); }

        }

        class ClassC : ClassB
        {
            public ClassC() : base("newstring") { Console.WriteLine("ClassC"); }

        }


        static void Main(string[] args)
        {
           ClassC obj = new ClassC();
            Console.WriteLine(obj);
        }



    }

}
    

