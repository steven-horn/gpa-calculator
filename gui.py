from tkinter import *
from functions import *


class Gui:
    def __init__(self, window):
        """Initial screen and all widgets. Most of the widgets are initially hidden from the user with pack_forget()"""
        self.grades_list_one = []
        self.grades_list_two = []
        self.grades_list_three = []
        self.grades_list_four = []
        self.grades_list_five = []

        self.__number_of_classes = 1
        self.window = window
        self.window.geometry('500x800')
        self.window.resizable(False, False)
        self.window.title('Class Grade Book')

        self.frame_top = Frame(self.window)
        self.welcome_label = Label(self.frame_top, text='Welcome to your grade book!')
        self.welcome_label.pack()
        self.frame_top.pack()

        self.frame_one_class = Frame(self.window)
        self.class_one_label = Label(self.frame_one_class, width=10, text='Calculus')
        self.grade_one_label = Label(self.frame_one_class, width=5, text='Grade: ')
        self.add_one_entry = Entry(self.frame_one_class)
        self.class_one_button = Button(self.frame_one_class, width=10, text='Add grade', command=self.class_one_grades)
        self.class_one_label.pack(side='left')
        self.grade_one_label.pack(side='left', padx=50)
        self.class_one_button.pack(side='right')
        self.add_one_entry.pack(side='right', padx=2)
        self.frame_one_class.pack_forget()

        self.frame_one_scores = Frame(self.window)
        self.one_labelframe = LabelFrame(self.frame_one_scores, text='Current Scores')
        self.one_label = Label(self.one_labelframe, width=30, wraplength=300, text='')
        self.one_delete_entry = Entry(self.frame_one_scores)
        self.one_delete_button = Button(self.frame_one_scores, width=10, text='Delete')
        self.one_labelframe.pack(side='left')
        self.one_label.pack()
        self.one_delete_entry.pack(side='left')
        self.one_delete_button.pack(side='right')
        self.frame_one_scores.pack_forget()

        self.frame_two_class = Frame(self.window)
        self.class_two_label = Label(self.frame_two_class, width=10, text='Temp')
        self.grade_two_label = Label(self.frame_two_class, width=5, text='Temp')
        self.add_two_entry = Entry(self.frame_two_class)
        self.class_two_button = Button(self.frame_two_class, width=10, text='Add grade', command=self.class_two_grades)
        self.class_two_label.pack(side='left')
        self.grade_two_label.pack(side='left', padx=50)
        self.class_two_button.pack(side='right')
        self.add_two_entry.pack(side='right', padx=2)
        self.frame_two_class.pack_forget()

        self.frame_two_scores = Frame(self.window)
        self.two_labelframe = LabelFrame(self.frame_two_scores, text='Current Scores')
        self.two_label = Label(self.two_labelframe, width=30, wraplength=300, text='')
        self.two_delete_entry = Entry(self.frame_two_scores)
        self.two_delete_button = Button(self.frame_two_scores, width=10, text='Delete')
        self.two_labelframe.pack(side='left')
        self.two_label.pack()
        self.two_delete_entry.pack(side='left')
        self.two_delete_button.pack(side='right')
        self.frame_two_scores.pack_forget()

        self.frame_three_class = Frame(self.window)
        self.class_three_label = Label(self.frame_three_class, width=10, text='Temp')
        self.grade_three_label = Label(self.frame_three_class, width=5, text='Temp')
        self.add_three_entry = Entry(self.frame_three_class)
        self.class_three_button = Button(self.frame_three_class, width=10, text='Add grade', command=self.class_three_grades)
        self.class_three_label.pack(side='left')
        self.grade_three_label.pack(side='left', padx=50)
        self.class_three_button.pack(side='right')
        self.add_three_entry.pack(side='right', padx=2)
        self.frame_three_class.pack_forget()

        self.frame_three_scores = Frame(self.window)
        self.three_labelframe = LabelFrame(self.frame_three_scores, text='Current Scores')
        self.three_label = Label(self.three_labelframe, width=30, wraplength=300, text='')
        self.three_delete_entry = Entry(self.frame_three_scores)
        self.three_delete_button = Button(self.frame_three_scores, width=10, text='Delete')
        self.three_labelframe.pack(side='left')
        self.three_label.pack()
        self.three_delete_entry.pack(side='left')
        self.three_delete_button.pack(side='right')
        self.frame_three_scores.pack_forget()

        self.frame_four_class = Frame(self.window)
        self.class_four_label = Label(self.frame_four_class, width=10, text='Temp')
        self.grade_four_label = Label(self.frame_four_class, width=5, text='Temp')
        self.add_four_entry = Entry(self.frame_four_class)
        self.class_four_button = Button(self.frame_four_class, width=10, text='Add grade', command=self.class_four_grades)
        self.class_four_label.pack(side='left')
        self.grade_four_label.pack(side='left', padx=50)
        self.class_four_button.pack(side='right')
        self.add_four_entry.pack(side='right', padx=2)
        self.frame_four_class.pack_forget()

        self.frame_four_scores = Frame(self.window)
        self.four_labelframe = LabelFrame(self.frame_four_scores, text='Current Scores')
        self.four_label = Label(self.four_labelframe, width=30, wraplength=300, text='')
        self.four_delete_entry = Entry(self.frame_four_scores)
        self.four_delete_button = Button(self.frame_four_scores, width=10, text='Delete')
        self.four_labelframe.pack(side='left')
        self.four_label.pack()
        self.four_delete_entry.pack(side='left')
        self.four_delete_button.pack(side='right')
        self.frame_four_scores.pack_forget()

        self.frame_five_class = Frame(self.window)
        self.class_five_label = Label(self.frame_five_class, width=10, text='Temp')
        self.grade_five_label = Label(self.frame_five_class, width=5, text='Temp')
        self.add_five_entry = Entry(self.frame_five_class)
        self.class_five_button = Button(self.frame_five_class, width=10, text='Add grade', command=self.class_five_grades)
        self.class_five_label.pack(side='left')
        self.grade_five_label.pack(side='left', padx=50)
        self.class_five_button.pack(side='right')
        self.add_five_entry.pack(side='right', padx=2)
        self.frame_five_class.pack_forget()

        self.frame_five_scores = Frame(self.window)
        self.five_labelframe = LabelFrame(self.frame_five_scores, text='Current Scores')
        self.five_label = Label(self.five_labelframe, width=30, wraplength=300, text='')
        self.five_delete_entry = Entry(self.frame_five_scores)
        self.five_delete_button = Button(self.frame_five_scores, width=10, text='Delete')
        self.five_labelframe.pack(side='left')
        self.five_label.pack()
        self.five_delete_entry.pack(side='left')
        self.five_delete_button.pack(side='right')
        self.frame_five_scores.pack_forget()

        self.frame_add_button = Frame(self.window)
        self.class_entry = Entry(self.frame_add_button)
        self.button_add_class = Button(self.frame_add_button, text='Add Class', command=self.clicked)
        self.class_entry.pack(side='left', padx=10)
        self.button_add_class.pack(side='right', padx=10)
        self.frame_add_button.pack()

        self.frame_error = Frame(self.window)
        self.error_label = Label(self.frame_error, text='Please input a number between 0 - 120', fg='red', relief='raised', font=('arial', 12))
        self.error_label.pack()
        self.frame_error.pack_forget()

    def clicked(self):
        """Function to set the screen"""
        if self.__number_of_classes == 1:
            self.one_class()
            self.__number_of_classes += 1
        elif self.__number_of_classes == 2:
            self.two_classes()
            self.__number_of_classes += 1
        elif self.__number_of_classes == 3:
            self.three_classes()
            self.__number_of_classes += 1
        elif self.__number_of_classes == 4:
            self.four_classes()
            self.__number_of_classes += 1
        else:
            self.five_classes()

    def one_class(self):
        """Screen when we have created only one grade book"""
        self.frame_add_button.pack_forget()
        self.frame_one_class.pack()
        self.frame_one_scores.pack()
        self.frame_add_button.pack()

    def two_classes(self):
        """Screen when we have created two grade books"""
        self.frame_add_button.pack_forget()
        self.frame_two_class.pack()
        self.frame_two_scores.pack()
        self.frame_add_button.pack()

    def three_classes(self):
        """Screen when we have created three grade books"""
        self.frame_add_button.pack_forget()
        self.frame_three_class.pack()
        self.frame_three_scores.pack()
        self.frame_add_button.pack()

    def four_classes(self):
        """Screen when we have created four grade books"""
        self.frame_add_button.pack_forget()
        self.frame_four_class.pack()
        self.frame_four_scores.pack()
        self.frame_add_button.pack()

    def five_classes(self):
        """Screen when we have created four grade books"""
        self.frame_add_button.destroy()
        self.frame_five_class.pack()
        self.frame_five_scores.pack()

    def class_one_grades(self):
        """Function to get grades from user input. Store them into a list and update label"""
        grade = self.add_one_entry.get()
        x = valid_score(grade)
        if x is False:
            self.frame_error.pack()
        else:
            self.grades_list_one.append(grade)
        text = ",".join(self.grades_list_one)
        self.one_label.config(text=f'{text}')
        self.add_one_entry.delete(0, END)

    def class_two_grades(self):
        """Function to get grades from user input. Store them into a list and update label"""
        grade = self.add_two_entry.get()
        x = valid_score(grade)
        if x is False:
            self.frame_error.pack()
        else:
            self.grades_list_two.append(grade)
        text = ",".join(self.grades_list_two)
        self.two_label.config(text=f'{text}')
        self.add_two_entry.delete(0, END)

    def class_three_grades(self):
        """Function to get grades from user input. Store them into a list and update label"""
        grade = self.add_three_entry.get()
        x = valid_score(grade)
        if x is False:
            self.frame_error.pack()
        else:
            self.grades_list_three.append(grade)
        text = ",".join(self.grades_list_three)
        self.three_label.config(text=f'{text}')
        self.add_three_entry.delete(0, END)

    def class_four_grades(self):
        """Function to get grades from user input. Store them into a list and update label"""
        grade = self.add_four_entry.get()
        x = valid_score(grade)
        if x is False:
            self.frame_error.pack()
        else:
            self.grades_list_four.append(grade)
        text = ",".join(self.grades_list_four)
        self.four_label.config(text=f'{text}')
        self.add_four_entry.delete(0, END)

    def class_five_grades(self):
        """Function to get grades from user input. Store them into a list and update label"""
        grade = self.add_five_entry.get()
        x = valid_score(grade)
        if x is False:
            self.frame_error.pack()
        else:
            self.grades_list_five.append(grade)
        text = ",".join(self.grades_list_five)
        self.five_label.config(text=f'{text}')
        self.add_five_entry.delete(0, END)
