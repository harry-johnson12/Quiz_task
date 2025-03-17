import csv

#idea - general knowledge year 7-9 quiz on all general subjects // 
# you can select your year group and the subject you want to be quizzed on

#NEXT TO DO: restructure so functions are called in main()  

# - generate questions, 20x question for each subject for each year group (7-9)
# maths - science - english - history - geography - art - music - technology - general knowledge

# - run quiz function // including hints, score system, timer, highscore system

#Highscore system shoud be saved to a file fpr each subject in each year group mapped to the name of the player
#highscore ect should be visible before the start and score ect should be visbiel after the quiz

def load_questions():
    questions = [] # list to store the questions
    with open("questions.csv", newline="") as questions_file:
            question_list = csv.reader(questions_file)
            for question in question_list: # for the rows in the csv file
                question_loading = {"year": question[0], "subject": question[1], "question": question[2], "answer": question[3], "hint": question[4]} # create the loading question // item 0 in the row is the question, item 1 is the answer
                questions.append(question_loading) # append the question to the list of questions

    return questions

def filter_questions(questions, year_group, subject):
    filtered_questions = []
    for questions in questions:
        if questions["year"] == str(year_group) and questions["subject"] == subject:
            filtered_questions.append(questions)

    return filtered_questions

def run_quiz(questions, year_group, subject, name):
    subject_questions = filter_questions(questions, year_group, subject)
    for question in subject_questions: #just printing the questions for now
        print(question["question"])

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
            #print()
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
    print()  
    change = input() #continues on enter

    while change.lower() == "change": # if the user wants to change their year group
        year_group = get_year_group("Please enter your year group: ")
        print()
        print(f"Awesome! Year {year_group} selected, press ENTER to continue.")
        print("// If you would like to change your year group, type 'Change' and press enter.")
        print()  
        change = input()
    
    return year_group

def get_name():
    name = input("Please enter your name: ")
    while name == "":
        print()
        name = input("Name cannot be blank. Please enter your name: ")
    print()
    print(f"Hello {name}! Press ENTER to continue.")
    print("Type 'Change' and press ENTER to change your name.")
    return name

def name_selection():
    print()
    name = get_name()
    print()
    change = input()

    while change.lower() == "change":
        name = get_name()
        print()
        change = input()

    return name

def main():

    print()
    print("- - - - - - - - - - - - - - - - - -")
    print("Welcome to the Years 7-10 General Knowledge Quiz!")
    print("- - - - - - - - - - - - - - - - - -")

    questions = load_questions()
    name = name_selection()
    year_group = year_group_selection()
    subject = subject_selection(year_group)
    run_quiz(questions, year_group, subject, name)

main()
