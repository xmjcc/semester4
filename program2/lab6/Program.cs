using lab6.models;
using System;
using System.Collections.Generic;
using System.IO;

namespace lab6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ////To test the constructor and the ToString method
            Song newsong = new Song("Baby", "Justin Bebier", 3.35, SongGenre.Pop);
            Console.WriteLine(newsong);

            //This is first time that you are using the bitwise or. It is used to specify a combination of genres
            Console.WriteLine(new Song("The Promise", "Chris Cornell", 4.26, SongGenre.Pop | SongGenre.Country));

            Library.LoadSongs("Lab_06_songs4.txt");     //Class methods are invoke with the class name
            Console.WriteLine("\n\nAll songs");
            Library.DisplaySongs();

            SongGenre genre = SongGenre.Rock;
            Console.WriteLine($"\n\n{genre} songs");
            Library.DisplaySongs(genre);

            string artist = "Bob Dylan";
            Console.WriteLine($"\n\nSongs by {artist}");
            Library.DisplaySongs(artist);

            Console.WriteLine("find the songs longer than, please type in minutes:");
            double length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine($"\n\nSongs more than {length}mins");
            Library.DisplaySongs(length);



        }

        public static class Library
        {

            private static List<Song> songs = new List<Song>();


            public static void LoadSongs(string fileName)
            {
                songs.Clear();

                StreamReader reader = new StreamReader(fileName);
                while (reader != null)
                {
                    string title = reader.ReadLine();
                    if (string.IsNullOrEmpty(title))
                        break;

                    string artist = reader.ReadLine();
                    double length = Convert.ToDouble(reader.ReadLine());
                    SongGenre genre = (SongGenre)Enum.Parse(typeof(SongGenre), reader.ReadLine());


                    Song newsong = new Song(title, artist, length, genre);
                    songs.Add(newsong);


                    //Console.WriteLine(title);
                    //Console.WriteLine(artist);
                    //Console.WriteLine(length);
                    //Console.WriteLine(genre);

                }

            }


            public static void DisplaySongs()
            {
                foreach (var song in songs)
                {

                    Console.WriteLine(song);
                }

            }

            public static void DisplaySongs(double longerthan)
            {
                foreach (var song in songs)
                {
                    if (song.Length > longerthan)
                    {
                        Console.WriteLine(song);

                    }


                }



            }

            public static void DisplaySongs(SongGenre genre)
            {
                foreach (var song in songs)
                {
                    if (song.Genre.HasFlag(genre))
                        Console.WriteLine(song);

                }

            }


            public static void DisplaySongs(string artist)
            {
                foreach (var song in songs)
                {
                    if (song.Artist == artist)
                        Console.WriteLine(song);
                }
            }

        }




    }
}
