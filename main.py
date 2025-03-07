import csv
questions = []
with open("questions.csv", newline="") as questions:
        question_reader = csv.reader(questions)
        for question in question_reader:
            print(question)

def main():
    pass