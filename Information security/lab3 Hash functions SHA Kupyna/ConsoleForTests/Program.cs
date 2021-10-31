using crypto_lab_3;
using crypto_lab_3.Kupyna;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

namespace ConsoleForTests
{
    class Program
    {
        static public void FindCollision(IHashFunc hashFunc, int nonce, string proof, Random random)
        {
            byte[] inp = new byte[nonce];
            string hash;
            //HashSet<string> foundHashes = new HashSet<string>();
            ulong iterationsCounter = 0;

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();

            while (true)
            {
                iterationsCounter++;
                RandomizeByteArr(inp, random);

                hash = Encoding.ASCII.GetString(hashFunc.CalcHash(inp));
                //foundHashes.Add(hash);

                if (hash.StartsWith(proof))
                    break;
            }

            stopwatch.Stop();

            Console.WriteLine($"Found in {iterationsCounter} iterations \n Time spent {stopwatch.ElapsedMilliseconds} ms");
        }

        static public void RandomizeByteArr(byte[] inp, Random random)
        {
            for (int i = 0; i < inp.Length; ++i)
                inp[i] = (byte)random.Next(255);
        }

        static void Main(string[] args)
        {
            Random random = new Random();

            IHashFunc kupyna = new Kupyna();
            IHashFunc sha256Func = new SHA256();

            string proof = "";
            int nonce = 55;

            for (int i = 0; i < 5; i++)
            {
                proof += "0";
                Console.WriteLine($"\t\tProof = {proof}");


                Console.WriteLine("SHA256");
                FindCollision(sha256Func, nonce, proof, random);
                Console.WriteLine();

                Console.WriteLine("Kupyna");
                FindCollision(kupyna, nonce, proof, random);
                Console.WriteLine();
            }
        }
    }
}
