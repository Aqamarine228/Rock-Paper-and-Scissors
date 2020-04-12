import random
import os
import pandas as pd


class GAME:

    # start method
    def __init__(self):
        name = input("Enter your name: ")
        self.name = name
        print("Hello,", name)
        print(
            "Plese input bellow one of the comands: \
             Rock, Paper, Scissors, !leaderboard(if you want to see frirst 3 leaders sorted by rating), \
             !rating(if you want to see a score) or !exit(if you want to exit from the program and save the result)")

    # function that cheks if file rating.csv exists, and cheks for user name index
    def start(self):
        # if file rating.csv exists
        if os.path.exists("rating.csv"):
            # df is rating.csv DataFrame
            df = pd.read_csv("rating.csv")
            # cheks for user name index in Names column
            index = df[df["Names"] == self.name].index.values
            # if user name doesn't in DataFrame than index is blank list
            if len(index) == 0:
                # creates new row with user name and rating, concatenates it with DataFrame
                df = df.append({"Names": self.name, "Rating": 0}, ignore_index=True)
                # delets Unnamed column
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                # removes old version of rating.csv file
                os.remove("rating.csv")
                # creates uppdated rating.csv file
                df.to_csv("rating.csv")
                # cheks for user name index
                realindex = df[df["Names"] == self.name].index.values
                return realindex, df
            else:
                # if user name in DataFrame
                realindex = index
                return realindex, df
        # if rating.csv doesn't exist
        else:
            # creates new row with user name and rating
            df = pd.DataFrame({"Names": [self.name], "Rating": [0]})
            # delets Unnamed column
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            # creates new rating.csv file
            df.to_csv("rating.csv")
            # checks for name index in Names column
            realindex = df[df["Names"] == self.name].index.values
            return realindex, df

    # function with game loop
    def game(self, realindex, df):
        while True:
            # dictioanry with win combinations
            windict = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Rock"}
            user = input("Please chose and input: > ")
            choice = ["Rock", "Scissors", "Paper"]
            # points for draw and win
            draw = 50
            win = 100
            # computer chose random element from choice list
            computer = random.choice(choice)
            try:
                # ratting comand
                if user == "!rating":
                    # prints user rating
                    print("Your rating:", df["Rating"].loc[realindex].values[0])
                # checks if user choiced same as computer
                elif user == computer:
                    print("There is a draw", "(" + computer + ")")
                    # adds 50 points if there is a draw(causes warning[SettingWithCopyWarning], please help, if anyone can solve it)
                    df["Rating"].loc[realindex] += draw
                # exit command
                elif user == "!exit":
                    # delets old rating.csv file
                    os.remove("rating.csv")
                    # delets Unnamed column
                    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                    # creates new uppdated rating.csv file
                    df.to_csv("rating.csv")
                    print("Bye!")
                    break
                elif user == "!leaderboard":
                    # makes copy of columns Names and Rating from DataFrame
                    users = df.copy(["Names", "Rating"])
                    # sort copied DataFrame by Rating
                    users = users.sort_values(by="Rating", ascending=False)
                    # delets unnamed column
                    users = users.loc[:, ~users.columns.str.contains('^Unnamed')]
                    print(users.head(3))
                # checks if user won
                elif user != computer and windict[user] == computer:
                    print("Well done computer chose", computer, "and failed")
                    # add +100 points to the score if the user won(causes warning[SettingWithCopyWarning], please help, if anyone can solve it)
                    df["Rating"].loc[realindex] += win
                # checks if user lost
                elif user != computer and windict[user] != computer:
                    print("Sorry computer chose", computer)
            # it prints the messege if if user doesn't input something from the comands
            except KeyError:
                print("You should input Rock,Paper,Scissors,!leaderboard,!rating or !exit")


whole_game = GAME()
realindex, df = whole_game.start()
whole_game.game(realindex, df)
