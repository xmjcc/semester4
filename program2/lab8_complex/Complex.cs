using System;

namespace lab8_complex
{
    public class Complex
    {

        public int Real { get;}
        public int Imaginary { get;}

        // Argument property (computed property)
        public double Argument { get=>Math.Atan(this.Imaginary/this.Real);}

        // Modulus property (computed property)
        public double Modulus { get=>Math.Sqrt(Math.Pow(this.Real,2) + Math.Pow(this.Imaginary,2));}
        // Zero property (factory property)
        public static Complex Zero => new Complex(0, 0);

        public Complex(int real, int imaginary)
        {
            this.Real = real;
            this.Imaginary = imaginary;
        }

        public override string ToString()
        {
            string sign = (Imaginary<0) ? "" : "+" ;
            string sreal = (Real > 0) ? (" " + Real) : Convert.ToString(Real);
          
            return $"{sreal}{sign}{Imaginary}i";
        }

        public static Complex operator +(Complex lhs, Complex rhs) 
        { 
            int real = lhs.Real + rhs.Real;
            int imaginary = lhs.Imaginary + rhs.Imaginary;  
            return new Complex(real, imaginary);
        }

        public static Complex operator -(Complex lhs, Complex rhs)
        {
            int real = lhs.Real - rhs.Real;
            int imaginary = lhs.Imaginary - rhs.Imaginary;
            return new Complex(real, imaginary);
        }

        public static Complex operator -(Complex a)
        {
            int real = -a.Real;
            int imaginary = -a.Imaginary;
            return new Complex(real, imaginary);
        }

        public static Complex operator *(Complex lhs, Complex rhs)
        {
            int a = lhs.Real;
            int b = lhs.Imaginary;
            int c = rhs.Real;
            int d = rhs.Imaginary;
            int real = a*c - b*d;
            int imaginary = a*d+b*c;
            return new Complex(real, imaginary);
        }

        public static bool operator ==(Complex lhs, Complex rhs)
        {

            return (lhs.Real == rhs.Real && lhs.Imaginary == rhs.Imaginary);

        }
        public static bool operator !=(Complex lhs, Complex rhs)
        {

            return (lhs.Real != rhs.Real || lhs.Imaginary != rhs.Imaginary);

        }





    }
}
