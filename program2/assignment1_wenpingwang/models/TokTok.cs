using System;

namespace assignment1_wenpingwang.models
{
    public class TokTok
    {
        private int _id = 0;
        public string Originator { get; }
        public double Length { get;}
        public string HashTag { get; }
        public Audience Audience { get; }
        public string Id { get; }

        public TokTok(string originator, double length, string hashtag, Audience audience)
        {
            this.Originator = originator;
            this.Length = length;
            this.HashTag = hashtag;
            this.Audience = audience;
            _id++;
            this.Id = _id.ToString();

        }


        private TokTok(string id, string originator, double length, Audience audience,string hashtag)
        {
            this.Originator = originator;
            this.Length = length;
            this.HashTag = hashtag;
            this.Audience = audience;
            this.Id = id;

        }

        public override string ToString()
        {
            return $"ID:{Id}, Originator:{Originator}, Length: {Length}, Audience: {Audience},  Hashtag: {HashTag}";
        }

        public static TokTok Parse(string line)
        {
            string[] parts = line.Split('\t');
            string id = parts[0];
            string originator = parts[1];
           
            int length = int.Parse(parts[2]);
            Audience audience = (Audience)Enum.Parse(typeof(Audience), parts[3]);
            string hashtag = parts[4];
           

            return new TokTok(id, originator, length,audience, hashtag);

        }






    }
}
