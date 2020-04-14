# Rock-Paper-and-Scissors
That is my first GitHub project, and it might work like:
1. At first user input his name
2. Program checks if user name is in rating.txt(rating.csv in second version) file 
if not it creates line with user name + score(0)
(rating.txt file must not contain blank lines and it must be in the same directory as code)
3. Program prints Hello + user name, and commands available in game
4. User must prints one of the availeble comands, and if user print:
⋅⋅* "!rating" program prints user name + user rating
⋅⋅* "!exit" program will delete line with previous user name and score,close file, print bye and break the game loop.
⋅⋅* "Rock","Paper" or "Scissors" program will compare computer choise with user input
and print "Well played,computer chose" + computer choise + "and failed" if user won,
⋅⋅* "Sorry but computer chose" + computer choise if user lost
or "There is a Draw" + "(" + computer chose + ")" if there is a Draw
and program will add +50 points to user rating if there is a Draw,
or +100 points if user won.
