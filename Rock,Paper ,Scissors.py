import random
import os


#function that gets score for name in rating.txt file 
def get_score_for_name(path_to_file, name,score_out):
    with open(path_to_file) as file_handler:
        for name_ in file_handler:
            name_list = name_.split()
            if name_list[0] == name:
                score_out.append(name_list[1])
        file_handler.close()
    return score_out

#function that checks or create(if name is not in a file) score and name in rating.txt file
def check(path_to_file, name,score_out,namezr):
    with open(path_to_file,"r+") as f:
        filev = f.read()
        if name in filev:
            get_score_for_name(path_to_file,name,score_out)
        else:   
            f.write(namezr)
            score_out.append("0")
        f.close()

#function that deletes line in rating.txt file
def delete_line_by_full_match(original_file, line_to_delete):
    is_skipped = False
    dummy_file = original_file + '.bak'
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        for line in read_obj:
            line_to_match = line
            if line[-1] == '\n':
                line_to_match = line[:-1]
            if line_to_match != line_to_delete:
                write_obj.write(line)
            else:
                is_skipped = True
        read_obj.close()

    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)

#function with game loop
def game(scoredef,filename,scorestrer,name):
    while 5:
        #dictioanry with win combinations       
        windict = {"Rock":"Scissors", "Paper":"Rock", "Scissors":"Rock"}
        user = input("Please chose and input: > ")
        choice = ["Rock", "Scissors", "Paper"]
        #computer chose random element from choice list
        computer = random.choice(choice)
        try:
            #ratting comand
            if user == "!rating":
                #prints user rating
                print("Your rating:",scoredef)
            #checks if user choiced same as computer
            elif user == computer:
                print("There is a draw","(" + computer + ")")
                #adds 50 points if there is a draw
                scoredef += 50
            #exit command
            elif user == "!exit":
                print("Bye!")
                someintstr = 0
                scorestrnow = str(scoredef)
                namenow = name + " " + scorestrnow + "\n"
                namebefore = name + " " + scorestr
                #deletes previous user name and score from rating.txt
                delete_line_by_full_match(filename,namebefore)
                #writes new user name and score in rating.txt 
                with open(filename,"a") as f:
                    f.write(namenow)
                    f.close()
                break
            #checks if user won
            elif user != computer and windict[user] == computer:
                print("Well done computer chose",computer, "and failed")
                #add +100 points to the score if the user won
                scoredef += 100
            #checks if user lost
            elif user != computer and windict[user] != computer:
                print("Sorry computer chose",computer)
        #it prints the messege if if user doesn't input something from the comands
        except KeyError:
            print("You should input Rock,Paper,Scissors,!rating or !exit")


name = input("Enter your name: ")
namez = name + " "+ "0" + "\n"
lister =[]
print("Hello,",name)
print("Plese input bellow one of the comands: Rock, Paper,Scissors, !rating(if you want to see a score) or !exit(if you want to exit from the program and save the result)")
check(".\\rating.txt",name,lister,namez)
#make string from list
scorestr = "".join(lister)
#changing type from string to init
score = int(scorestr)
game(score,".\\rating.txt",scorestr,name)
