using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab7
{
    internal class Program
    {


        static void Main(string[] args)
        {
            // Create a list to store the objects
            List<Time> times = new List<Time>()
        {
            new Time(9, 35),
            new Time(18, 5),
            new Time(20, 500),
            new Time(10),
            new Time()
        };

            // Display all the objects with the initial format (Hour12)
            TimeFormat format = TimeFormat.Hour12;
            Console.WriteLine($"\nTime format is {format}");
            foreach (Time t in times)
            {
                Console.WriteLine(t);
            }

            // Change the format of the output to Mil
            format = TimeFormat.Mil;
            Console.WriteLine($"\nSetting time format to {format}");
            Time.SetFormat(format);
            // Again display all the objects
            foreach (Time t in times)
            {
                Console.WriteLine(t);
            }

            // Change the format of the output to Hour24
            format = TimeFormat.Hour24;
            Console.WriteLine($"\nSetting time format to {format}");
            Time.SetFormat(format);
            foreach (Time t in times)
            {
                Console.WriteLine(t);
            }


        }


        public enum TimeFormat
        {
            Mil,
            Hour12,
            Hour24
        }

        public class Time
        {
            private int hour;
            private int minute;
            private static TimeFormat TIME_FORMAT = TimeFormat.Hour12;

            public int Hour
            {
                get { return hour; }
            }

            public int Minute
            {
                get { return minute; }
            }

            public Time(int hours = 0, int minutes = 0)
            {
                if (hours >= 0 && hours <= 24)
                    hour = hours;
                else
                    hour = 0;

                if (minutes >= 0 && minutes < 60)
                    minute = minutes;
                else
                    minute = 0;
            }

            public override string ToString()
            {
                switch (TIME_FORMAT)
                {
                    case TimeFormat.Mil:
                        return $"{hour:D2}{minute:D2}";
                    case TimeFormat.Hour12:
                        string amPm = (hour < 12) ? "AM" : "PM";
                        int hour12 = (hour == 0 || hour == 12) ? 12 : hour % 12;
                        return $"{hour12:D2}:{minute:D2} {amPm}";
                    case TimeFormat.Hour24:
                        return $"{hour:D2}:{minute:D2}";
                    default:
                        return $"{hour:D2}:{minute:D2}";
                }
            }

            public static void SetFormat(TimeFormat timeFormat)
            {
                TIME_FORMAT = timeFormat;
            }
        }





    }
}
