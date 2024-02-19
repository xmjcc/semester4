
using System;
using System.IO;
using Person_test.models;
using System.Collections.Generic;


namespace Person_test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //string currentDirectory = Directory.GetCurrentDirectory();
            //Console.WriteLine("Current Directory: " + currentDirectory);

            TextReader reader = new StreamReader("person.txt");

            List<Person> persons = new List<Person>();


            string line = reader.ReadLine();
            //Console.WriteLine(line);


            while (line != null)
            {
                string[] values = line.Split('\t');
                string name = values[0];
                double weight = Convert.ToDouble(values[1]);
                int age = Convert.ToInt32(values[2]);
                bool isMarried = Convert.ToBoolean(values[3]);
                persons.Add(new Person(name, age, weight, isMarried));
                line = reader.ReadLine();
                
            }


            reader.Close();

            foreach (Person person in persons)
            {
                Console.WriteLine($"Name: {person.Name}, Weight: {person.Weight}, Age: {person.Age}, isMarried: {person.IsMarried}");
            }


        }
    }
}
