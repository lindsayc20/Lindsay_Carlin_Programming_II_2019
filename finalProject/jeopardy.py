from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
import requests
import random
import sys
from html2text import html2text

Window.size = (600, 400)

categories = [str(x) for x in range(9, 33)]
chosen_categories = []
master_question_list = []
master_answer_list = []
master_incorrect_list = []
answer_choices = []
money = 0
welcome_image = Image(source='jeopardylogo.png')


for i in range(6):
    url = "https://opentdb.com/api.php?amount=5&category=" + random.choice(categories) + "&type=multiple"
    try:
        page = requests.get(url)
        data = page.text
        data = data[data.find("[{"):-1]  # only grab the question list to simplify it  (if this doesn't work, just pull it from the dictionary)
        questions = eval(data)  # evaluate the string as python code
    except Exception as e:
        print("Error found:", e)
        sys.exit()

    category = questions[0].get('category')
    chosen_categories.append(category)
    question_list = [x.get('question').strip() for x in questions]
    answers = [x.get('correct_answer').strip() for x in questions]
    incorrect = [list(x.get('incorrect_answers')) for x in questions]

    for i in range(len(question_list)):
        question_list[i] = html2text(question_list[i]).strip().strip()
        answers[i] = html2text(answers[i]).strip()
    incorrect_ = incorrect[:]
    for i in range(len(incorrect_)):
        incorrect[i] = [html2text(x).strip().strip() for x in incorrect_[i]]
    # print(incorrect)

    master_question_list.append(question_list)
    master_answer_list.append(answers)
    master_incorrect_list.append(incorrect)
    for i in range(len(incorrect)):
        incorrect0 = incorrect[i][0]
        incorrect1 = incorrect[i][1]
        incorrect2 = incorrect[i][2]
        correct_choice = answers[i]
        # print(incorrect0, incorrect1, incorrect2, correct_choice)
        answer_choices.append([incorrect0, incorrect1, incorrect2, correct_choice]) # skips 5 6th)
new_answer_choices = [answer_choices[0:5], answer_choices[5:10], answer_choices[10:15], answer_choices[15:20], answer_choices[20:25], answer_choices[25:30]]

# print(master_question_list)
# print(master_answer_list)
# print(master_incorrect_list)
# print(answer_choices)
# print(new_answer_choices)
# print(len(answer_choices))
# print(len(new_answer_choices))

'''
for i in range(len(question_list)):
    print(end="\n\n")
    print(category)
    print(question_list[i].strip())
        # print("Correct", answers[i])
        # print("Incorrect", incorrect[i])

for i in range(len(master_question_list)):
    for j in range(5):
        print(master_question_list[i][j])
        print(master_answer_list[i][j])
        print(master_incorrect_list[i][j])
        print(new_answer_choices[i][j])
'''

 # print(len(master_question_list))
class ScreenManagement(ScreenManager):
    master_question_list = master_question_list
    chosen_categories = chosen_categories
    correct_choice = correct_choice
    money = 0
    def build(self):
        return JeopardyLayout()
    def get_amount(self, row):
        self.amount = (row + 1) * 200
        return self.amount
    def get_question(self, column, row):
        self.question = master_question_list[column][row]
    def shuffle_choices(self, column, row):
        self.choices = new_answer_choices[column][row]
        # print(self.choices)
        # print(column)
        # print(master_answer_list[column])
        random.shuffle(self.choices)
        self.choice0 = self.choices[0]
        self.choice1 = self.choices[1]
        self.choice2 = self.choices[2]
        self.choice3 = self.choices[3]
        return self.choice0, self.choice1, self.choice2, self.choice3, column
    def get_column(self, column):
        self.col = column
        return self.col
    def get_choice(self, choice):
        self.choice = self.choices[choice]
        # print(self.choices)
        # print(master_answer_list)
        # print(self.choices)
        if self.choice in master_answer_list[self.col]:
            self.right_choice = True
        # print(self.choice, self.right_choice)
        return self.right_choice
    def get_incorrect(self, column, row):
        self.incorrect0 = master_incorrect_list[column][row][0]
        self.incorrect1 = master_incorrect_list[column][row][1]
        self.incorrect2 = master_incorrect_list[column][row][2]
        self.incorrect = [self.incorrect0, self.incorrect1, self.incorrect2]
        return self.incorrect0, self.incorrect1, self.incorrect2
    def get_answer(self, column, row):
        self.answer = master_answer_list[column][row]
        return self.answer
    # def score_change(self):

class JeopardyLayout(BoxLayout):
    pass

class fullImage(Image):
    pass

class WelcomeScreen(Screen):
    layout = BoxLayout()
    welcome_image = fullImage()

class CategoryScreen(Screen):
    layout = BoxLayout()
    for i in range(6):
        chosen_categories = chosen_categories
        master_question_list = master_question_list

class QuestionScreen(Screen):
    layout = BoxLayout()
    for i in range(6):
        question_list = question_list
        chosen_categories = chosen_categories
        master_question_list = master_question_list

class AnswerScreen(Screen):
    layout = BoxLayout()

class JeopardyApp(App):
    def build(self):
        return ScreenManagement()

if __name__=="__main__":
    app = JeopardyApp()
    app.run()

# need score change