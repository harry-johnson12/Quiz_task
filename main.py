import csv

#idea - general knowledge year 7-9 quiz on all general subjects // 
# you can select your year group and the subject you want to be quizzed on

#NEXT TO DO: - generate questions, - run quiz function // including hints, score system, timer, highscore system
#Highscore system shoud be saved to a file fpr each subject in each year group
#highscore ect should be visible before the start and score ect should be visbiel after the quiz

def load_questions():
    questions = [] # list to store the questions
    with open("questions.csv", newline="") as questions_file:
            question_list = csv.reader(questions_file)
            for question in question_list: # for the rows in the csv file
                question_loading = {"year": question[0], "subject": question[1], "question": question[2], "answer": question[3], "hint": question[4]} # create the loading question // item 0 in the row is the question, item 1 is the answer
                questions.append(question_loading) # append the question to the list of questions

    return questions

def run_quiz():
    print("RUN QUIZ PLACEHOLDER")

def subject_selection_page():
    subjects = ["Maths", "Science", "English", "History", "Geography", "Art", "Music", "Technology", "General Knowledge"]

    print("--- Subject Selection ---")
    print()
    print("Press ENTER to scroll subjects")
    print("Type 'Select' and press ENTER to select the subect")
    print("Type 'Back' and press ENTER to change your year group")
    print()

    select = ""
    subject = ""
    while select.lower() != "select":
        for i in range(len(subjects)):
            print(subjects[i])
            print()
            select = input()
            if select.lower() == "back":
                year_group_selection()
                break
            if select.lower() == "select":
                subject = subjects[i]
                print()
                break

    print(f"Great! You selected {subject}, press ENTER to continue.")
    print("// If you would like to change your subject, type 'Change' and press enter.")

    print()
    change = input()
    while change.lower() == "change":
        print()
        subject_selection_page()
        change = input()
    
    run_quiz()

def get_year_group(prompt):
    while True:
        try: # incase the user enters a string
            print()
            year_group = int(input(str(prompt)))
            break
        except ValueError: # if the user enters a string
            print()
            print("Please enter a number.")

    while year_group < 7 or year_group > 9: # if the year group is not between 7 and 9
        print()
        print("Please enter a year group between 7 and 9.")
        year_group = get_year_group("")

    return year_group

def year_group_selection():
    year_group = get_year_group("Please enter your year group: ")

    print()
    print(f"Awesome! Year {year_group} selected, press ENTER to continue.")
    print("// If you would like to change your year group, type 'Change' and press enter.")
    print()  

    change = input() #continues on enter
    while change.lower() == "change": # if the user wants to change their year group
        year_group_selection()
        change = input()

    subject_selection_page()

def welcome_page():
    print() #first set of text
    print("- - - - - - - - - - - - - - - - - -")
    print("Welcome to the Years 7-10 General Knowledge Quiz!")
    print("- - - - - - - - - - - - - - - - - -")

    year_group_selection()

def main():
    #load_questions()
    welcome_page()

main()