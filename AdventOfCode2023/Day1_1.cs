using System.Text;

namespace AdventOfCode2023
{
    public static class Day1_1
    {
        public static void Execute()
        {
            String line;
            try
            {
            StreamReader sr = new StreamReader("C:\\Users\\DSU\\OneDrive - Dakota State University\\Desktop\\repositories\\AdventOfCode2023\\AdventOfCode2023\\Day1.txt");

                line = sr.ReadLine();
                List<string> lines = new List<string>();

                while (line != null)
                {
                    //Console.WriteLine(line);
                    lines.Add(line);
                    line = sr.ReadLine();
                }
                sr.Close();
                int sumOfCalibrationValues = 0;
                
                for ( int i = 0; i < lines.Count; i++)
                {
                    List<int> allNumbersInLine = new List<int>();
                    foreach (char character in lines[i])
                    {
                        if (Char.IsDigit(character))
                        {
                            allNumbersInLine.Add((int)Char.GetNumericValue(character));
                        }
                    }
                    int calibrationValue = Int32.Parse(string.Join("", allNumbersInLine[0], allNumbersInLine[allNumbersInLine.Count - 1]));
                    //Console.WriteLine(calibrationValue);
                    sumOfCalibrationValues += calibrationValue;
                }
                Console.WriteLine(sumOfCalibrationValues);

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
