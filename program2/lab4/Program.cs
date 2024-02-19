using lab4.models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace lab4
{
    internal class Program
    {
        static void Main(string[] args)
        {
        // Creating a Medal instance
        Medal goldMedal = new Medal("Narendra", "Boxing", MedalColor.Gold, 2012, true);

            // Using the ToString() method to print the information
            Console.WriteLine(goldMedal.ToString());
        }



    }


}



    




