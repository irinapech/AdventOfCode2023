namespace AdventOfCode2023
{
    public static class Day1_2
    {
        public static void Execute()
        {
            String line;
            try
            {
                StreamReader sr = new StreamReader("../Day1.txt");

                line = sr.ReadLine();
                List<string> lines = new List<string>();

                while (line != null)
                {
                    //Console.WriteLine(line);
                    lines.Add(line);
                    line = sr.ReadLine();
                }
                sr.Close();

                Dictionary<string, int> digits = new Dictionary<string, int>();
                digits.Add("one", 1);
                digits.Add("two", 2);
                digits.Add("three", 3);
                digits.Add("four", 4);
                digits.Add("five", 5);
                digits.Add("six", 6);
                digits.Add("seven", 7);
                digits.Add("eight", 8);
                digits.Add("nine", 9);

                int numberOfLettersInOne_Two_Six = 3;
                int numberOfLettersInFour_Five_Nine = 4;
                int numberOfLettersInThree_Seven_Eight = 5;

                int sumOfCalibrationValues = 0;

                for (int i = 0; i < lines.Count; i++)
                {
                    List<int> allNumbersInLine = new List<int>();
                    for (int j = 0; j < lines[i].Length; j++)
                    {
                        if (lines[i].Length - j >= numberOfLettersInOne_Two_Six && digits.ContainsKey(lines[i].Substring(j, numberOfLettersInOne_Two_Six)))
                        {
                            allNumbersInLine.Add(digits[lines[i].Substring(j, numberOfLettersInOne_Two_Six)]);
                        }
                        else if (lines[i].Length - j >= numberOfLettersInFour_Five_Nine && digits.ContainsKey(lines[i].Substring(j, numberOfLettersInFour_Five_Nine)))
                        {
                            allNumbersInLine.Add(digits[lines[i].Substring(j, numberOfLettersInFour_Five_Nine)]);
                        }
                        else if (lines[i].Length - j >= numberOfLettersInThree_Seven_Eight && digits.ContainsKey(lines[i].Substring(j, numberOfLettersInThree_Seven_Eight)))
                        {
                            allNumbersInLine.Add(digits[lines[i].Substring(j, numberOfLettersInThree_Seven_Eight)]);
                        }
                        else if (Char.IsDigit(lines[i][j]))
                        {
                            allNumbersInLine.Add((int)Char.GetNumericValue(lines[i][j]));
                        }
                    }
                    int calibrationValue = Int32.Parse(string.Join("", allNumbersInLine[0], allNumbersInLine[allNumbersInLine.Count - 1]));
                    // Console.WriteLine(calibrationValue);
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
