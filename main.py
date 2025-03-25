import csv
import random
from check_answer import check_answer

# - highscore system 

#Highscore system shoud be saved to a file fpr each subject in each year group mapped to the name of the player
#highscore ect should be visible before the start and score ect should be visbiel after the quiz
def load_highscores():
    highscores = []
    with open("highscores.csv", newline="") as highscore_file:
        highscore_list = csv.reader(highscore_file)
        for score in highscore_list:
            highscore_loading = {"name": score[0], "year": score[1], "subject": score[2], "high_score": score[3]}
            highscores.append(highscore_loading)

    return highscores

def highscore_appender(name, year_group, subject, score):
    with open("highscores.csv", mode="a", newline="") as highscore_file:
        highscore_editor = csv.writer(highscore_file)
        new_score = [name, year_group, subject, score]
        highscore_editor.writerow(new_score)

        highscores = []
        highscores = load_highscores()
        print(highscores)
        
        return highscores
        

def load_questions():
    questions = [] # list to store the questions
    with open("questions.csv", newline="") as questions_file:
            question_list = csv.reader(questions_file)
            for question in question_list: # for the rows in the csv file
                question_loading = {"year": question[0], "subject": question[1], "question": question[2], "hint": question[3]} # create the loading question // item 0 in the row is the question, item 1 is the answer
                questions.append(question_loading) # append the question to the list of questions

    return questions

def filter_questions(questions, year_group, subject):
    filtered_questions = []
    for questions in questions:
        if questions["year"] == str(year_group) and questions["subject"] == subject:
            filtered_questions.append(questions)

    return filtered_questions

def run_quiz(questions, year_group, subject, name, highscores):
    current_score = 0
    highscore = "You haven't played this one before!"
    subject_questions = filter_questions(questions, year_group, subject)

    for score in highscores:
        if score["name"] == name and score["subject"] == subject and score["year"] == year_group:
            highscore == score["high_score"]

    print("- - - - - - Year " + str(year_group) + " " + subject + " Quiz! - - - - - -")
    print()

    if not type(highscore) == str:
        print("Your highscore for this quiz is: " + highscore)
    else:
        print(highscore)
        
    print()
    print("If you would like a hint, type 'Hint' and press ENTER - these question will only be worth one point - instead of two.")
    print("If you would like to skip the question, type 'Skip' and press ENTER.")
    print("AS THIS QUIZ RELYS ON NETWORK -- PLEASE BE PATIENT WHILE THE ANSWERS ARE FETCHED")
    print()
    for i in range(10):
        hint = False
        failed = False
        current_question = random.choice(subject_questions)
        subject_questions.remove(current_question)
        question_text = current_question["question"]
        question_hint = current_question["hint"]

        print()
        print(f"{i + 1}. {question_text}")
        print()
        user_answer = input("Enter your answer: ")
        while user_answer == "":
            print()
            print("Answer cannot be blank.")
            print()
            user_answer = input("Enter your answer: ")
        
        if user_answer.lower() == "hint":
                print()
                print(f"- - - - - {question_hint} - - - - -")
                print()
                user_answer = input("Enter your answer: ")
                hint = True

        if not user_answer.lower() == "skip":

            attempts = 0
            while attempts < 3:
                try:
                    checked_answer = check_answer(question_text, user_answer)
                    break
                except:
                    attempts += 1
            
            if attempts > 2:
                print()
                print("- - - - Failed to fetch answer - - - -")
                print("You can have the points!")
                print()
                failed = True

                if hint:
                    current_score += 1
                    hint = False
                else:
                    current_score += 2

            if failed == False:
                correct_and_feedback = checked_answer.split("|")
                
                if correct_and_feedback[0] == "0":
                    print()
                    print("Correct!")
                    if hint:
                        current_score += 1
                        hint = False
                    else:
                        current_score += 2
                else:
                    print()
                    print(f"{correct_and_feedback[1]}")


    print()
    if current_score > 9:
        print(f"Well done! you scored {current_score}")
    else:
        print(f"There's always next time... you scored {current_score}")   
    
    if type(highscore) == str:
        highscores = highscore_appender(name, year_group, subject, current_score)

    #elif highscore > current_score: 
        #pass


    #print(highscore)

def subject_selection(year_group):
    subjects = ["Math", "Science", "English", "History", "Geography"]

    print("--- Subject Selection ---")
    print()
    print("Press ENTER to scroll subjects")
    print("Type 'Select' and press ENTER to select the subect")
    print()

    select = ""
    subject = ""
    while select.lower() != "select":
        for i in range(len(subjects)):
            print(subjects[i])
            print()
            select = input()
            if select.lower() == "select":
                subject = subjects[i]
                print()
                break
    

    print(f"Great! You selected year {year_group} {subject}, press ENTER to continue.")
    print("// If you would like to change your subject or year, type 'Change' and press enter.")

    change = input()
    while change.lower() == "change":
        print()
        subject_selection(year_group)
        change = input()
    
    return subject

def get_year_group(prompt):
    while True:
        try: # incase the user enters a string
            year_group = int(input(str(prompt)))
            break
        except ValueError: # if the user enters a string
            print()
            print("Please enter a number.")
            print()


    while year_group < 7 or year_group > 9: # if the year group is not between 7 and 9         
        print()
        print("Please enter a year group between 7 and 9.")
        print()
        year_group = get_year_group("")

    return year_group

def year_group_selection():

    year_group = get_year_group("Please enter your year group: ")
    print()
    print(f"Awesome! Year {year_group} selected, press ENTER to continue.")
    print("// If you would like to change your year group, type 'Change' and press enter.")
    change = input() #continues on enter

    while change.lower() == "change": # if the user wants to change their year group
        year_group = get_year_group("Please enter your year group: ")
        print()
        print(f"Awesome! Year {year_group} selected, press ENTER to continue.")
        print("// If you would like to change your year group, type 'Change' and press enter.")
        print()  
        change = input()
    
    return year_group

def get_name(highscores):
    name = input("Please enter your name: ")
    
    check_again = True #checks if the name is in the highscore file
    while check_again:
        check_again = False
        for score in highscores:
            if name == score["name"]:
                print()
                played_before = input("This name is in use, enter 'Yes' if you have you played before and used this name. ")
                if played_before.lower() == "yes":
                    break

                print()
                name = input("Please enter a different name: ")
                check_again = True

    while name == "":
        print()
        name = input("Name cannot be blank. Please enter your name: ")

    print()
    print(f"Hello {name}! Press ENTER to continue.")
    print("Type 'Change' and press ENTER to change your name.")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")  
    return name

def name_selection(highscores):
    print()
    name = get_name(highscores)
    change = input()

    while change.lower() == "change":
        print()
        name = get_name()
        print()
        change = input()

    return name

def main():
    playing = True
    print()
    print("- - - - - - - - - - - - - - - - - -")
    print("Welcome to the Years 7-9 General Knowledge Quiz!")
    print("- - - - - - - - - - - - - - - - - -")

    questions = load_questions()
    highscores = load_highscores()
    name = name_selection(highscores)

    while playing:
        year_group = year_group_selection()
        subject = subject_selection(year_group)
        run_quiz(questions, year_group, subject, name, highscores)
        print()
        playing = input("Would you like to play again? // if so enter 'Yes' ")
        print()
        if playing.lower() != "yes":
            playing = False

    print()
    print("- - - - - - - - - - - - -")
    print(f"Thanks for playing {name}!")
        
main()