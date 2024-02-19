using System;
using System.Collections.Generic;
using System.IO;


namespace assignment1_wenpingwang.models
{
    public static class TokTokManager
    {

        private static List<TokTok> TOKTOKS = new List<TokTok>();
        private static string FILENAME = "tiktoks.txt";

        static TokTokManager()
        {

            Initialize();


        }

        public static void Initialize()
        {
            //TOKTOKS.Clear();
            //StreamReader reader = new StreamReader(FILENAME);
            //while(reader != null)
            //    {
            //    string readline = reader.ReadLine();
            //    if (string.IsNullOrEmpty(readline))
            //        break;
            //    TokTok tokTok = TokTok.Parse(readline);
            //    TOKTOKS.Add(tokTok);


            //}

            TOKTOKS.Clear(); // Clear any previous data
            // Adding some sample TokToks
            TOKTOKS.Add(new TokTok("User1", 30, "#dance", Audience.world));
            TOKTOKS.Add(new TokTok("User2", 45, "#comedy", Audience.group));
            TOKTOKS.Add(new TokTok("User3", 20, "#talent", Audience.special));

            //Loading TokToks from file
            if (File.Exists(FILENAME))
            {
                string[] lines = File.ReadAllLines(FILENAME);
                foreach (string line in lines)
                {
                    TokTok tokTok = TokTok.Parse(line);
                    TOKTOKS.Add(tokTok);
                }
            }

        }

        public static void Show()
        {
            foreach (var toktok in TOKTOKS)
            {
                Console.WriteLine(toktok);



            }

        }

        public static void Show(string tag)
        {
            foreach (var tokTok in TOKTOKS)
            {
                if (tokTok.HashTag ==tag)
                {
                    Console.WriteLine(tokTok);
                }
            }
        }

        public static void Show(int length)
        {
            foreach (var tokTok in TOKTOKS)
            {
                if (tokTok.Length > length)
                {
                    Console.WriteLine(tokTok);
                }
            }
        }

        public static void Show(Audience audience)
        {
            foreach (var tokTok in TOKTOKS)
            {
                if (tokTok.Audience == audience)
                {
                    Console.WriteLine(tokTok);
                }
            }
        }





    }
}
