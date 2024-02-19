using assignment1_wenpingwang.models;
using System;

namespace assignment1_wenpingwang
{
    internal class Program
    {
        static void Main(string[] args)
        {
            TokTokManager.Initialize(); // Initialize TokTokManager
                                        // Test TokTokManager methods
            Console.WriteLine("All TokToks:");
            TokTokManager.Show();
            Console.WriteLine("\nTokToks with hashtag #dance:");
            TokTokManager.Show("#dance");
            Console.WriteLine("\nTokToks longer than 30 seconds:");
            TokTokManager.Show(30);
            Console.WriteLine("\nTokToks with audience 'Special':");
            TokTokManager.Show(Audience.special);
        }
    }
}
