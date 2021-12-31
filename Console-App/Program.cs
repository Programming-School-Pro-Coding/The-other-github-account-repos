using System;
using System.Text.RegularExpressions;
namespace ConsoleApp10
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write("Enter Text : ");
                string x = Console.ReadLine();
                string justNumbers = Regex.Replace(x, "[A-Za-z ]", string.Empty);
                string justString = Regex.Replace(x, @"[\d-]", string.Empty);
                Console.WriteLine("Here is the number of characters : " + justString.Length);
                Console.WriteLine("here number of digits : " + justNumbers.Length);
                string capitalLetters = Regex.Replace(x, "[^A-Z]", string.Empty);
                Console.WriteLine("here numbers if capital letters : " + capitalLetters.Length + " he : " + "[" + capitalLetters + "]");
                string chars = Regex.Replace(x, "[^!,%,@,!,?,&]", string.Empty);
                Console.WriteLine("chars from text : " + chars.Length);
                // long word


                String string1 = x;
                String word = "", small = "", large = "";
                String[] words = new String[100];
                int length = 0;

                string1 = string1 + " ";

                for (int i = 0; i < string1.Length; i++)
                {
                    if (string1[i] != ' ')
                    {
                        word = word + string1[i];
                    }
                    else
                    {
                        words[length] = word;
                        length++;
                        word = "";
                    }
                }

                small = large = words[0];

                for (int k = 0; k < length; k++)
                {

                    if (small.Length > words[k].Length)
                        small = words[k];

                    if (large.Length < words[k].Length)
                        large = words[k];
                }

                Console.WriteLine("Smallest word: " + small);
                Console.WriteLine("Largest word: " + large);
                Console.ReadKey();
            }

        }
    }
}
