using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace wk4_excercise
{
    internal class Distance
    {

        const double MILES_TO_KM = 1.61;
    
        private double _miles;
        public double Km
        {
            get {return _miles*MILES_TO_KM;}
            set {_miles = value/MILES_TO_KM;}

        }

        public double Mile
        {
            get { return _miles;}
            set {_miles = value;}   
        }
    }
}
