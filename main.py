import csv

#idea - general knowledge year 7-10 quiz on all general subjects // 
# you can select your year group and the subject you want to be quizzed on

def load_questions():
    questions = [] # list to store the questions
    with open("questions.csv", newline="") as questions_file:
            question_list = csv.reader(questions_file)
            for question in question_list: # for the rows in the csv file
                question_loading = {"year": question[0], "subject": question[1], "question": question[2], "answer": question[3], "hint": question[4]} # create the loading question // item 0 in the row is the question, item 1 is the answer
                questions.append(question_loading) # append the question to the list of questions

    return questions


def run_quiz():
    pass

def topic_selection_page():
    topics = ["Maths", "Science", "English", "History", "Geography", "Art", "Music", "Languages", "Technology", "General Knowledge"]
    print("Press ENTER to scroll topics")
    print("Type 'Start' and press ENTER to select the topic")
    print()
    select = ""
    topic = ""
    while select.lower() != "start":
        for i in range(len(topics)):
            print(topics[i])
            select = input()
            if select.lower() == "start":
                topic = topics[i]
                print()
                break

    print(f"Great! You selected {topic} press ENTER to continue.")
    print("// If you would like to change your topic, type 'Change' and press enter.")


def get_year_group(prompt):
    while True:
        try: # incase the user enters a string
            print()
            year_group = int(input(str(prompt)))
            return(year_group)
        except ValueError: # if the user enters a string
            print()
            print("Please enter a number.")

def check_year_group(year_group):
    year_group = year_group
    while year_group < 7 or year_group > 10: # if the year group is not between 7 and 10
        print()
        print("Please enter a year group between 7 and 10.")
        year_group = get_year_group("")
    return year_group

def year_group_selection():
    year_group = get_year_group("Please enter your year group: ")
    year_group = check_year_group(year_group)

    print()
    print(f"Awesome! Year {year_group} selected, press ENTER to continue.")
    print("// If you would like to change your year group, type 'Change' and press enter.")
    print()
    
def welcome_page():
    print() #first set of text
    print("- - - - - - - - - - - - - - - - - -")
    print("Welcome to the Years 7-10 General Knowledge Quiz!")
    print("- - - - - - - - - - - - - - - - - -")

    year_group_selection()

    change = input() #continues on enter
    while change.lower() == "change": # if the user wants to change their year group
        year_group_selection()
        change = input()

    else:
        topic_selection_page() # if the user doesn't want to change their year group continue to the topic selection page

def main():
    load_questions()
    welcome_page()

main()