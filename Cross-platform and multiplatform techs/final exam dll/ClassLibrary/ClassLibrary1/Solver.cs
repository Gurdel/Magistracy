using System;
using System.Globalization;
using System.IO;

namespace ClassLibrary1
{
    public class Solver
    {
        private static string allSymbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхїфівапролджєяґчсмитьбюЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯҐЧСМИТЬБЮёъыэЁЪЭЫ1234567890`:;~!@#$%^&*()_+-=[]{}\\.\',\"<>/?|₴'№ \n\r\t";
        private static int dictLength = allSymbols.Length;

        public static char cipher(char ch, int key)
        {
            key %= dictLength;

            if (!allSymbols.Contains(ch))
            {
                return ch;
            }

            char res = allSymbols[(allSymbols.IndexOf(ch) + key + dictLength) % dictLength];
            return res;
        }


        public static string Encrypt(string input, int key)
        {
            key %= dictLength;
            string output = string.Empty;

            foreach (char ch in input)
                output += cipher(ch, key);

            return output;
        }

        public static string Decrypt(string input, int key)
        {
            key %= dictLength;
            return Encrypt(input, -key);
        }


        public static void Main()
        {
            Console.WriteLine("Type a string to encrypt: ");
            string UserString = Console.ReadLine();
            Console.WriteLine("\n");

            Console.Write("Enter your Key:\t");
            int key = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("\n");


            Console.WriteLine("Encrypted Data");
            string cipherText = Encrypt(UserString, key);
            Console.WriteLine(cipherText);
            Console.Write("\n");

            Console.WriteLine("Decrypted Data:");
            string plainText = Decrypt(cipherText, key);
            Console.WriteLine(plainText);
            Console.Write("\n");
        }
    }
}
