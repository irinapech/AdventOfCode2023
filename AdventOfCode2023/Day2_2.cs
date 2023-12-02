using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2023
{
    public static class Day2_2
    {
        public static void Execute()
        {
            String line;
            try
            {
                StreamReader sr = new StreamReader("../Day2.txt");

                line = sr.ReadLine();

                List<string> games = new List<string>();

                while (line != null)
                {
                    games.Add(line);
                    line = sr.ReadLine();
                }
                sr.Close();

                int sumOfPowers = 0;

                //# go through each line (separated by line)
                //# go through each allCubesDrawn (separated by ;)
                //# go through each cube (separated by ,)
                //#if out of possible range - allCubesDrawn the flag to false
                //#if the flag is still true (aka the game is possible) - add its ID to the sum

                for (int i = 0; i < games.Count; i++)
                {
                    int numberOfMaxRed = 0;
                    int numberOfMaxGreen = 0;
                    int numberOfMaxBlue = 0;
                    
                    string allCubesDrawn = games[i].Split(":", StringSplitOptions.RemoveEmptyEntries)[1];
                    string[] sets = allCubesDrawn.Split(";", StringSplitOptions.RemoveEmptyEntries);
                    foreach (string set in sets)
                    {
                        string[] cubes = set.Trim().Split(",", StringSplitOptions.RemoveEmptyEntries);
                        foreach (string cube in cubes)
                        {
                            int number = Convert.ToInt32(cube.Trim().Split(" ", StringSplitOptions.RemoveEmptyEntries)[0]);
                            string color = cube.Trim().Split(" ", StringSplitOptions.RemoveEmptyEntries)[1];
                            if (color == "red" && number > numberOfMaxRed)
                            {
                                numberOfMaxRed = number;
                            }
                            if (color == "green" && number > numberOfMaxGreen)
                            {
                                numberOfMaxGreen = number;
                            }
                            if (color == "blue" && number > numberOfMaxBlue)
                            {
                                numberOfMaxBlue = number;
                            }
                        }
                    }
                    int powerOfSet = numberOfMaxRed * numberOfMaxGreen * numberOfMaxBlue;
                    sumOfPowers += powerOfSet;
                }
                Console.WriteLine("Sum of powers: " + sumOfPowers);
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
            finally
            {
                Console.WriteLine("Executing finally block.");
            }
        }
    }
}
