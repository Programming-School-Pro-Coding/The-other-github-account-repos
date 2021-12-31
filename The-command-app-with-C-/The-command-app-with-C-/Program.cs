using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Console_APP
{
    internal class Program
    {
        static void Main(string[] args)
        {
            {
                Console.Title = "computer console";
                string cmd;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.Beep();
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine("******************************************************************");
                Console.WriteLine("******************************************************************");
                Console.WriteLine("Welcome to the Works Shortcut application.\nThe application was programmed by Ali Zedan, For help type `help`");
                Console.WriteLine("******************************************************************");
                Console.WriteLine("******************************************************************");
                Console.WriteLine("Please Enter the {help} to show the command");

                if (Console.CapsLock)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("********");
                    Console.ForegroundColor = ConsoleColor.Red;

                    Console.WriteLine("You must turn off Caps Lock\nAll commands are in lowercase");

                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("\n********");
                }
                Console.ForegroundColor = ConsoleColor.Green;
                do
                {
                    cmd = Console.ReadLine();
                    if (cmd == "gl")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to google! \n");
                        Process.Start("https://www.google.com");
                        Console.ForegroundColor = ConsoleColor.Green;
                    }
                    else if (cmd == "gl")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to google! \n");
                        Process.Start("https://www.google.com");
                        Console.ForegroundColor = ConsoleColor.Green;
                    }
                    else if (cmd == "help")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("Order List, order: what he doing \n gl : Move To Google \n yt : Move To Youtube \n date : today's date \n time : time now \n sd : turn off the pc \n insta : Move To instagram \n fc : Move To Facebook \n wt : Move To whatsapp \n exit : exit the app");
                        Console.ForegroundColor = ConsoleColor.Green;
                    }
                    else if (cmd == "yt")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to youtube! \n");
                        Process.Start("https://www.youtube.com");
                        Console.ForegroundColor = ConsoleColor.Green;

                    }
                    else if (cmd == "date")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        string date;
                        date = DateTime.Today.ToString().Replace("0:00:00", " ");
                        Console.WriteLine(date);
                        Console.ForegroundColor = ConsoleColor.Green;

                    }
                    else if (cmd == "time")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        string time;
                        time = DateTime.UtcNow.ToString("T");
                        Console.WriteLine(time);
                        Console.ForegroundColor = ConsoleColor.Green;







                        string str = "hello ";
                        char ch = str[3];
                        Console.WriteLine(ch);















                    }
                    else if (cmd == "sd")
                    {
                        string shf;
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Are you sure you want to turn off your device?[yes/no]");
                        Console.ForegroundColor = ConsoleColor.Green;
                        shf = Console.ReadLine();
                        if (shf == "yes")
                        {
                            var psi = new ProcessStartInfo("shutdown", "/s /t 0");
                            psi.CreateNoWindow = true;
                            psi.UseShellExecute = false;
                            Process.Start(psi);
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Yellow;
                            Console.WriteLine("shutdown has been skipped");
                            Console.ForegroundColor = ConsoleColor.Green;
                        }
                    }
                    else if (cmd == "insta")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to instagram! \n");
                        Process.Start("https://www.instagram.com/");
                        Console.ForegroundColor = ConsoleColor.Green;

                    }
                    else if (cmd == "fc")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to facebook! \n");
                        Process.Start("https://www.facebook.com/");
                        Console.ForegroundColor = ConsoleColor.Green;

                    }
                    else if (cmd == "wt")
                    {
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Moved to WhatsApp! \n");
                        Console.ForegroundColor = ConsoleColor.Green;
                        Process.Start("https://web.whatsapp.com/");
                        Console.ForegroundColor = ConsoleColor.Green;
                    }
                    else if (cmd == "exit")
                    {
                        string shr;
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("[System] Are you sure you want to exit the application? [yes/no]");
                        Console.ForegroundColor = ConsoleColor.Green;
                        shr = Console.ReadLine();
                        if (shr == "yes")
                        {
                            Environment.Exit(0);
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Yellow;
                            Console.WriteLine("[System] The application has been closed! \n");
                            Console.ForegroundColor = ConsoleColor.Green;
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Red;

                        Console.WriteLine("[Waring] Type something right to find out the commands, type 'help'!!");
                        Console.ForegroundColor = ConsoleColor.Green;
                    }
                } while (true);




            }
        }
    }
 
}
