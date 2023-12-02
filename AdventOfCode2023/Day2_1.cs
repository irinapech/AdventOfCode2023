using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2023
{
    public static class Day2_1
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
                    // Console.WriteLine(line);
                    games.Add(line);
                    line = sr.ReadLine();
                }
                sr.Close();

                int numberOfRedCubes = 12;
                int numberOfGreenCubes = 13;
                int numberOfBlueCubes = 14;

                //# go through each line (separated by line)
                //# go through each allCubesDrawn (separated by ;)
                //# go through each cube (separated by ,)
                //#if out of possible range - allCubesDrawn the flag to false
                //#if the flag is still true (aka the game is possible) - add its ID to the sum

                int sumOfIDsOfPossibleGames = 0;

                for (int i = 0; i < games.Count; i++)
                {
                    bool isGamePossible = true;
                    
                    string allCubesDrawn = games[i].Split(":", StringSplitOptions.RemoveEmptyEntries)[1];
                    string[] sets = allCubesDrawn.Split(";", StringSplitOptions.RemoveEmptyEntries);
                    foreach (string set in sets)
                    {
                        string[] cubes = set.Trim().Split(",", StringSplitOptions.RemoveEmptyEntries);
                        foreach (string cube in cubes)
                        {
                            int number = Convert.ToInt32(cube.Trim().Split(" ", StringSplitOptions.RemoveEmptyEntries)[0]);
                            string color = cube.Trim().Split(" ", StringSplitOptions.RemoveEmptyEntries)[1];
                            if (color == "red" &&  number > numberOfRedCubes
                                || color == "green" && number > numberOfGreenCubes
                                || color == "blue" && number > numberOfBlueCubes)
                            {
                                isGamePossible = false;
                            }
                        }
                    }
                    if (isGamePossible)
                    {
                        sumOfIDsOfPossibleGames += i + 1;
                    }
                }
                Console.WriteLine("Sum of IDs of possible games: " + sumOfIDsOfPossibleGames);
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
