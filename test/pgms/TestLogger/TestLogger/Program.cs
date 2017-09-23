using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TestLogger
{
    public class Program
    {
        private static void Main(string[] args)
        {
            for (int i = 0; i < 10; ++i)
            {
                Console.WriteLine($"Testing {i}");
                Thread.Sleep(1000);
            }
        }
    }
}
