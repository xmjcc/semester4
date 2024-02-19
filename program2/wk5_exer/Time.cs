using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace wk5_exer
{
    internal class Time
    {
        private int ticks;

        public int Seconds { get => ticks % 60; }
        public int Minutes { get => ticks / 60 % 60; }
        public int Hours { get => ticks / 3600; }

        public Time(int ticks)
        {
            this.ticks = ticks;

        }

        public static Time operator +(Time lhs, Time rhs) => new Time(lhs.ticks + rhs.ticks);

        public static Time operator -(Time lhs, Time rhs) => new Time(lhs.ticks - rhs.ticks);
        //{return new Time(lhs.ticks+rhs.ticks);}

        public static bool operator ==(Time lhs, Time rhs) { return (lhs.ticks == rhs.ticks); }
        public static bool operator !=(Time lhs, Time rhs) { return (lhs.ticks != rhs.ticks); }
        public override string ToString()
        {
            return $"the time is {Hours} hours: {Minutes} minutes:  {Seconds} seconds:";
        }


    }
}
