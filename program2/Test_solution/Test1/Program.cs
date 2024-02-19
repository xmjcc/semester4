using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Test1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Assume initial date components
            int year = 2023;
            int month = 13; // February
            int day = 35; // Day more than 30

            // Normalize the date
           // DateTime originalDate = new DateTime(year, month, day);
            //DateTime normalizedDate = NormalizeDate(originalDate);
            
            

            while (month > 12)
            {
                year++;
                month = month - 12;

            }

            int daysInMonth = DateTime.DaysInMonth(year, month);

            while (day > daysInMonth) 
            {
                month++;
                day = day - daysInMonth;
            }


            DateTime newDate = new DateTime(year, month, day);
            Console.WriteLine(newDate.ToString());

            
        }

       
    }


       
}
