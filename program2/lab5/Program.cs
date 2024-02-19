using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab5
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Pet cat1 = new Pet("cat", 4, "British");
            Pet cat2 = new Pet("dog", 2, "American");
            Pet cat3 = new Pet("barby", 8, "Africa");
            Pet cat4 = new Pet("lionpet", 7, "Asia");

            cat1.SetOwner("benjamin");
            cat2.SetOwner("Joe Biden");
            cat3.SetOwner("Franky");
            cat4.SetOwner("Xi Jingping");

            cat1.Train(true);
            cat2.Train(true);
            cat3.Train(false);
            cat4.Train(true);

            //Console.WriteLine(cat1);

            List<Pet> PetList = new List<Pet>();
            PetList.Add(cat1);
            PetList.Add(cat2);
            PetList.Add(cat3);
            PetList.Add(cat4);

            foreach (Pet p in PetList)
            {
                Console.WriteLine(p);
            }

            Console.WriteLine("\n Please enter the owner's name");
            string ownerName =Console.ReadLine();
            ownerName = ownerName.ToLower();

            foreach (Pet pet in PetList)
            {
                string owner = pet.Owner.ToLower();

                if (owner == ownerName)
                {
                    Console.WriteLine(pet.ToString());
                }


            }

        }
    }
}
