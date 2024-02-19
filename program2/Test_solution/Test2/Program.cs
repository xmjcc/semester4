using System;
using System.ComponentModel;
using System.IO;
using System.Runtime.CompilerServices;
using System.Xml;

namespace Test2
{
    internal class Program
    {

        
        static void Main(string[] args)
        {

            //TextWriter writer = new StreamWriter("TextFile1.txt");
            //writer.Write("Nykribet");
            //writer.WriteLine("\n Nykribet2222");

            //File.WriteAllText("TextFile1.txt", "how are you");

            TextReader reader = new StreamReader("TextFile1.txt");
            string line = reader.ReadLine();
            Console.WriteLine(reader.ReadLine());

            line = reader.ReadLine();

            while(line != null)
            {
                Console.WriteLine(line);
                line = reader.ReadLine();

            }


            reader.Close();


            //string currentDirectory = Directory.GetCurrentDirectory();
            //Console.WriteLine("Current Directory: " + currentDirectory);

            //for (int i = 1; i <= 12; i++)
            //{
            //    writer.WriteLine($"{i,6} x 15 = {i * 15}");     //Do more writing, 6 is the position of i
            //}

            //writer.Close();


        }
    }
}
