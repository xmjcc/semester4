using System;
using System.Collections.Generic;

namespace lab9
{
    internal class Program
    {
        //define abstract class Shape
        public abstract class Shape 
        {
            public string Name { get; private set; }
            public abstract double Area { get;  } //define abstract property Area, which will ensure the derived class will have a property of Area
           
               

            public Shape(string name)
            {
                this.Name = name;

            }

            //To String method
            public override string ToString()
            {
                return $"the shape is {Name} and the area is {Area}"; 

            }
        }

        //derived class Square
        public class Square : Shape
        {
            public double Length { get; protected set; }
            public override double Area => Math.Round(Length * Length,2);

            public Square (string name, double length): base(name)
            {
                this.Length = length;

            }



        }

        //derived class Circle
        public class Circle : Square
        {
            public override double Area => Math.Round(Math.PI* Length*Length,2);

            public Circle (string name, double length): base(name,length)
            {

            }


        }

        //derived class Rectangle
        public class Rectangle : Shape
        {
            public double Width { get; protected set; }
            public double Height { get; protected set; }


            public override double Area { get { return Width * Height; } }

            public Rectangle(string name, double width, double height) : base(name)
            {
                this.Width = width;
                this.Height = height;

            }
        }


        //derived class Ellipse
        public class Ellipse : Rectangle
            {
                public override double Area => Math.Round(Math.PI*Width * Height,2);

                public Ellipse(string name, double width, double height):base(name, width, height)
                {

                }

            }

        public class Triangle : Rectangle
            {
                public override double Area => Width * Height*0.5;

                public Triangle(string name, double width, double height) : base(name, width, height)
                {

                }

            }     

        public class Diamond : Rectangle    
          {
             public override double Area => Width * Height * 0.5;

                public Diamond (string name, double width, double height) : base(name, width, height)
                {

                }

          }       



            static void Main(string[] args)
        {
            List<Shape> shapes = new List<Shape>(); //create a list of shapes

            shapes.Add(new Square("s1", 2));
            shapes.Add(new Rectangle("r1", 2, 3));
            shapes.Add(new Circle("c1", 2));
            shapes.Add(new Triangle("t1", 4, 6));
            shapes.Add(new Ellipse("e1", 2, 3));
            shapes.Add(new Diamond("d1", 2, 3));

            shapes.Add(new Square("s2", 5));
            shapes.Add(new Rectangle("r2", 5, 4));
            shapes.Add(new Circle("c2", 1));
            shapes.Add(new Triangle("t2", 7, 8));

            foreach (var s in shapes)
            {
                Console.WriteLine(s);
            }



        }
    }
}
