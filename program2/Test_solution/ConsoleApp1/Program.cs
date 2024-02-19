using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
     
        enum MaritalStatus { Single = 6, Married = 2, Separated, Divorced, Widowed };
        enum CarOptions
        {
            None = 0x00,
            SunRoof = 0x01,
            Spoiler = 0x02,
            FogLights = 0x04,
            TintedWindows = 0x08,
            Hydraulics = 0x16
        };
        enum MovieGenre { None, Action, Romance, Documentary, Adult, Sci_Fi, Religious };
        enum Days { Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thu = 5, Fri = 6, Sat =7 };



        static void Main(string[] args)
        {

            //int x = (int) Days.Sun;
            ////Console.WriteLine(x);


            //Days d = (Days)3;
            //Console.WriteLine(d.GetType());
            ////d = (Days) Enum.Parse(typeof(Days), "Mon");
            //Console.WriteLine(Enum.Parse(typeof(Days), "Mon"));

            //Console.WriteLine(d+2);
            //int status = (int)MovieGenre.Action;
            //Console.WriteLine(status);

            Console.Write("Enter a day of the week: ");
            int response = Convert.ToInt32(Console.ReadLine());
            Days day = (Days)response;
            Console.WriteLine(Days.Sat);
            if (day == Days.Sat || day == Days.Sun)
            {
                Console.WriteLine($"{day} is a Home day");
            }
            else
            {
                Console.WriteLine($"{day} is a Work day");
            }




        }
    }
}
