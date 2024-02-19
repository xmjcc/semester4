using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace lab6.models
{

    enum SongGenre {
        Unclassified = 0, 
        Pop = 0b1,
        Rock = 0b10,
        Blues = 0b100,
        Country = 0b1_000,
        Metal = 0b10_000,
        Soul = 0b100_000
    }
    internal class Song
    {
        public string Artist { get; private set; }
        public string Title { get; private set; }
        public double Length { get; private set; }
        public SongGenre Genre { get; private set; }

        public Song (string title, string artist, double length, SongGenre Songgenre)
        {
            this.Artist = artist;
            this.Title = title;
            this.Length = length;
            this.Genre = Songgenre;

        }

        public override string ToString()
        {
            // Generate genre string based on combined genres
            List<string> genreStrings = new List<string>();
            foreach (SongGenre genreFlag in Enum.GetValues(typeof(SongGenre)))
            {
                if ((Genre & genreFlag) != 0)
                {
                    genreStrings.Add(genreFlag.ToString());
                }
            }
            string genreString = string.Join(", ", genreStrings);

            return $"{Title} by {Artist} ({genreString}), {Length} min";

        }


    }


   




  


    
}
