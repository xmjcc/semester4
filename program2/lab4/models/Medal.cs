using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab4.models
{
    public enum MedalColor
    {
        Bronze,
        Silver,
        Gold
    }

    internal class Medal
    {

        // Properties
        public string Name { get; }
        public string TheEvent { get; }
        public MedalColor Color { get; }
        public int Year { get; }
        public bool IsRecord { get; }

        // Constructor
        public Medal(string name, string theEvent, MedalColor color, int year, bool isRecord)
        {
            this.Name = name;
            this.TheEvent = theEvent;
            this.Color = color;
            this.Year = year;
            this.IsRecord = isRecord;
        }

        // ToString() method
        public override string ToString()
        {
            string recordString = IsRecord ? "(R)" : "";
            return $"{Year} - {TheEvent}{recordString} {Name}({Color})";
        }


    }
}
