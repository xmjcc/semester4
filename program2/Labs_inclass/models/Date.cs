using System;

namespace Labs_inclass
{
    internal class Date
    {
        private int year;
        private int month;
        private int day;

        public Date( int day=1 ,int month=1,int year=2022 )
        {
            this.year = year;
            this.month = month;
            this.day = day;

        }

        public override string ToString()
        {

            return($"today's date is [MM-DD-YYYY] {month}-{day}-{year}");
        }

        public void Add(int days = 0 )
        {
            Console.WriteLine($"add {days} days");
            this.day =this.day + days;
            Normalize();


        }

        public void Add(int days=0, int months=0)
        {
            Console.WriteLine($"add {days} days and {months} months");
            this.day = this.day + days;
            this.month = this.month+months;

            
            Normalize();
        }


        public void Add(Date other)
        {
            Console.WriteLine($"add {other.day} days and {other.month} months and {other.year} years");

            this.day = this.day + other.day;
            this.month = this.month + other.month;
            this.year = this.year + other.year;
            Normalize();

        }


        private void Normalize()
        {
            Console.WriteLine("the new date is ");

            while (this.month > 12)
            {
                this.year++;
                this.month = this.month - 12;

            }

            int daysInMonth = DateTime.DaysInMonth(year, month);

            while (this.day > daysInMonth)
            {
                this.month++;
                this.day = this.day - daysInMonth;
                while (this.month > 12)
                {
                    this.year++;
                    this.month = this.month - 12;

                }

            }

            return;


        }





        

        
 



    }
}
