# Rock-Paper-and-Scissors

## Instalation and starting
1. At first you must install [Python](https://www.python.org/downloads/)
2. For this program you need installed [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html) library 
3. To start program you need to open folder with program file("[cd](https://en.wikipedia.org/wiki/Cd_(command))" command) in [cmd](https://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/) tab, than you need to type "python file_name.py"
* For old version you need rating.txt file in same directory as program code


## How program works
1. At first user input his name
2. Program checks if user name is in rating.csv file 
if not it creates row with user name + score(0)
3. Program prints Hello + user name, and commands available in game
4. User must prints one of the availeble comands:
* "!rating" program prints user name + user rating
* "!exit"  program deletes old rating.csv file and creates new uppdated file, print bye and break the game loop.
* "!leaderboard" program will show first 3 users sorted by score
* "Rock","Paper" or "Scissors" program will compare computer choise with user input
and print "Well played,computer chose" + computer choise + "and failed" if user won,
* "Sorry but computer chose" + computer choise if user lost
or "There is a Draw" + "(" + computer chose + ")" if there is a Draw
and program will add +50 points to user rating if there is a Draw,
or +100 points if user won.
