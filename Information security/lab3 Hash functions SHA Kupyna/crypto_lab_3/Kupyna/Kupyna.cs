using System;
using System.Collections.Generic;
using System.Text;

namespace crypto_lab_3.Kupyna
{
    public class Kupyna : IHashFunc
    {
        byte[] IV = new byte[64]
        {
            0x40, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0
        };

        public byte[] CalcHash(byte[] message)
        {
            byte[] paddedmessage = MessagePreprocessHelper.GetPaddedMessage512(message);

            byte[][] blocks = MessagePreprocessHelper.SplitMessage512(paddedmessage);

            byte[] resultBlockOperation = processBlockOperation(blocks);

            return resultBlockOperation;
        }


        private byte[] processBlockOperation(byte[][] messageByBlocks)
        {
            byte[] h = IV;
            for (int i = 0; i < messageByBlocks.Length; i++)
            {
                byte[] messageForTPlusCircle = XOR(messageByBlocks[i], h);

                byte[] messageForTPlus = messageByBlocks[i];

                byte[] messageAfterTPlusCircle = TPCircle.generateMessageAfterTPlusCircle(messageForTPlusCircle);

                byte[] messageAfterTPlus = TPlus.generateMessageAfterTPlus(messageForTPlus);

                h = lastBlockOperation(messageAfterTPlusCircle, messageAfterTPlus, h);
            }

            byte[] messageAfterFinalOperation = finalOperation(h);

            byte[] cutMessage = cutTo256Bit(messageAfterFinalOperation);

            return cutMessage;
        }

        private byte[] lastBlockOperation(byte[] messageAfterTPlusCircle, byte[] messageAfterTPlus, byte[] h_prev)
        {
            byte[] xorInputParameters = XOR(messageAfterTPlusCircle, messageAfterTPlus);

            return XOR(xorInputParameters, h_prev);
        }

        private byte[] finalOperation(byte[] messageAfterLastBlockOperation)
        {
            byte[] messageForXOR = messageAfterLastBlockOperation;

            byte[] messageAfterTPlusCircle = TPCircle.generateMessageAfterTPlusCircle(messageAfterLastBlockOperation);

            return XOR(messageForXOR, messageAfterTPlusCircle);
        }

        private byte[] cutTo256Bit(byte[] messageAfterFinalOperation)
        {
            byte[] message256Bit = new byte[32];

            for (int i = 0; i < 32; i++)
            {
                message256Bit[i] = messageAfterFinalOperation[32 + i];
            }

            return message256Bit;
        }

        public static byte[] XOR(byte[] firstArray, byte[] secondArray)
        {
            byte[] thirdArray = new byte[firstArray.Length];
            for (int i = 0; i < firstArray.Length; i++)
            {
                thirdArray[i] = (byte)(firstArray[i] ^ secondArray[i]);
            }
            return thirdArray;
        }
    }
}
