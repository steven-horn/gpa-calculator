from tkinter import *
from functions import *


class Gui:
    def __init__(self, window):
        """Initial screen and all widgets. Most of the widgets are initially hidden from the user with pack_forget()"""
        self.__class_one_grade = 0
        self.__class_two_grade = 0
        self.__class_three_grade = 0
        self.__class_four_grade = 0
        self.__class_five_grade = 0
        self.__number_of_classes = 1

        self.window = window
        self.window.geometry('500x800')
        self.window.resizable(False, False)
        self.window.title('GPA Calculator')

        self.frame_top = Frame(self.window)
        self.welcome_label = Label(self.frame_top, text='Welcome to GPA Calculator!')
        self.welcome_label.pack()
        self.frame_top.pack()

        self.frame_one = Frame(self.window)
        self.class_label = Label(self.frame_one, width=10, text='Class')
        self.grade_label = Label(self.frame_one, width=8, text='Percent Grade')
        self.letter_label = Label(self.frame_one, width=10, text='Letter Grade')
        self.class_label.pack(side='left')
        self.grade_label.pack(side='left', padx=50)
        self.letter_label.pack(side='right')
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.class_one_entry = Entry(self.frame_two)
        self.class_one_label = Label(self.frame_two)
        self.percent_one_entry = Entry(self.frame_two)
        self.percent_one_label = Label(self.frame_two)
        self.letter_one_label = Label(self.frame_two)
        self.submit_one_button = Button(self.frame_two, text='Submit', command=self.finish_one)
        self.class_one_entry.pack(side='left')
        self.class_one_label.pack_forget()
        self.percent_one_entry.pack(side='left')
        self.percent_one_label.pack_forget()
        self.submit_one_button.pack(side='right')
        self.letter_one_label.pack(side='right')
        self.frame_two.pack_forget()

        self.frame_three = Frame(self.window)
        self.class_two_entry = Entry(self.frame_three)
        self.class_two_label = Label(self.frame_three)
        self.percent_two_entry = Entry(self.frame_three)
        self.percent_two_label = Label(self.frame_three)
        self.letter_two_label = Label(self.frame_three)
        self.submit_two_button = Button(self.frame_three, text='Submit', command=self.finish_two)
        self.class_two_entry.pack(side='left')
        self.class_two_label.pack_forget()
        self.percent_two_entry.pack(side='left')
        self.percent_two_label.pack_forget()
        self.submit_two_button.pack(side='right')
        self.letter_two_label.pack(side='right')
        self.frame_three.pack_forget()

        self.frame_four = Frame(self.window)
        self.class_three_entry = Entry(self.frame_four)
        self.class_three_label = Label(self.frame_four)
        self.percent_three_entry = Entry(self.frame_four)
        self.percent_three_label = Label(self.frame_four)
        self.letter_three_label = Label(self.frame_four)
        self.submit_three_button = Button(self.frame_four, text='Submit', command=self.finish_three)
        self.class_three_entry.pack(side='left')
        self.class_three_label.pack_forget()
        self.percent_three_entry.pack(side='left')
        self.percent_three_label.pack_forget()
        self.submit_three_button.pack(side='right')
        self.letter_three_label.pack(side='right')
        self.frame_four.pack_forget()

        self.frame_five = Frame(self.window)
        self.class_four_entry = Entry(self.frame_five)
        self.class_four_label = Label(self.frame_five)
        self.percent_four_entry = Entry(self.frame_five)
        self.percent_four_label = Label(self.frame_five)
        self.letter_four_label = Label(self.frame_five)
        self.submit_four_button = Button(self.frame_five, text='Submit', command=self.finish_four)
        self.class_four_entry.pack(side='left')
        self.class_four_label.pack_forget()
        self.percent_four_entry.pack(side='left')
        self.percent_four_label.pack_forget()
        self.submit_four_button.pack(side='right')
        self.letter_four_label.pack(side='right')
        self.frame_five.pack_forget()

        self.frame_six = Frame(self.window)
        self.class_five_entry = Entry(self.frame_six)
        self.class_five_label = Label(self.frame_six)
        self.percent_five_entry = Entry(self.frame_six)
        self.percent_five_label = Label(self.frame_six)
        self.letter_five_label = Label(self.frame_six)
        self.submit_five_button = Button(self.frame_six, text='Submit', command=self.finish_five)
        self.class_five_entry.pack(side='left')
        self.class_five_label.pack_forget()
        self.percent_five_entry.pack(side='left')
        self.percent_five_label.pack_forget()
        self.submit_five_button.pack(side='right')
        self.letter_five_label.pack(side='right')
        self.frame_six.pack_forget()

        self.frame_bottom = Frame(self.window)
        self.add_button = Button(self.frame_bottom, text='Add Class', command=self.add_class)
        self.calculate_button = Button(self.frame_bottom, text='Calculate GPA', command=self.gpa_calculator)
        self.gpa_label = Label(self.frame_bottom, text='Average GPA')
        self.add_button.pack(side='left')
        self.calculate_button.pack(side='left')
        self.gpa_label.pack(side='right')
        self.frame_bottom.pack()

        self.frame_error = Frame(self.window)
        self.error_label = Label(self.frame_error, text='Please input a number between 0 - 100', fg='red', relief='raised', font=('arial', 12))
        self.error_label.pack()
        self.frame_error.pack_forget()

    def add_class(self):
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
        self.frame_bottom.pack_forget()
        self.frame_two.pack()

    def finish_one(self):
        x = self.class_one_entry.get()
        y = self.percent_one_entry.get()
        self.__class_one_grade = letter_grade(y)
        if self.__class_one_grade is False:
            self.frame_error.pack()
        else:
            self.class_one_label.config(text=x)
            self.percent_one_label.config(text=y)
            self.class_one_entry.destroy()
            self.percent_one_entry.destroy()
            self.class_one_label.pack(side='left')
            self.percent_one_label.pack(side='left')
            self.letter_one_label.config(text=self.__class_one_grade)
            self.__class_one_grade = conversion(self.__class_one_grade)
            self.submit_one_button.destroy()
            self.frame_error.pack_forget()
            self.frame_bottom.pack()

    def two_classes(self):
        """Screen when we have created two grade books"""
        self.frame_bottom.pack_forget()
        self.frame_three.pack()

    def finish_two(self):
        x = self.class_two_entry.get()
        y = self.percent_two_entry.get()
        self.__class_two_grade = letter_grade(y)
        if self.__class_two_grade is False:
            self.frame_error.pack()
        else:
            self.class_two_label.config(text=x)
            self.percent_two_label.config(text=y)
            self.class_two_entry.destroy()
            self.percent_two_entry.destroy()
            self.class_two_label.pack(side='left')
            self.percent_two_label.pack(side='left')
            self.letter_two_label.config(text=self.__class_two_grade)
            self.__class_two_grade = conversion(self.__class_two_grade)
            self.submit_two_button.destroy()
            self.frame_error.pack_forget()
            self.frame_bottom.pack()

    def three_classes(self):
        """Screen when we have created three grade books"""
        self.frame_bottom.pack_forget()
        self.frame_four.pack()

    def finish_three(self):
        x = self.class_three_entry.get()
        y = self.percent_three_entry.get()
        self.__class_three_grade = letter_grade(y)
        if self.__class_three_grade is False:
            self.frame_error.pack()
        else:
            self.class_three_label.config(text=x)
            self.percent_three_label.config(text=y)
            self.class_three_entry.destroy()
            self.percent_three_entry.destroy()
            self.class_three_label.pack(side='left')
            self.percent_three_label.pack(side='left')
            self.letter_three_label.config(text=self.__class_three_grade)
            self.__class_three_grade = conversion(self.__class_three_grade)
            self.frame_error.pack_forget()
            self.submit_three_button.destroy()
            self.frame_bottom.pack()

    def four_classes(self):
        """Screen when we have created four grade books"""
        self.frame_bottom.pack_forget()
        self.frame_five.pack()

    def finish_four(self):
        x = self.class_four_entry.get()
        y = self.percent_four_entry.get()
        self.__class_four_grade = letter_grade(y)
        if self.__class_four_grade is False:
            self.frame_error.pack()
        else:
            self.class_four_label.config(text=x)
            self.percent_four_label.config(text=y)
            self.class_four_entry.destroy()
            self.percent_four_entry.destroy()
            self.class_four_label.pack(side='left')
            self.percent_four_label.pack(side='left')
            self.letter_four_label.config(text=self.__class_four_grade)
            self.__class_four_grade = conversion(self.__class_four_grade)
            self.frame_error.pack_forget()
            self.submit_four_button.destroy()
            self.frame_bottom.pack()

    def five_classes(self):
        """Screen when we have created four grade books"""
        self.frame_bottom.pack_forget()
        self.frame_six.pack()

    def finish_five(self):
        x = self.class_five_entry.get()
        y = self.percent_five_entry.get()
        self.__class_five_grade = letter_grade(y)
        if self.__class_five_grade is False:
            self.frame_error.pack()
        else:
            self.class_five_label.config(text=x)
            self.percent_five_label.config(text=y)
            self.class_five_entry.destroy()
            self.percent_five_entry.destroy()
            self.class_five_label.pack(side='left')
            self.percent_five_label.pack(side='left')
            self.letter_five_label.config(text=self.__class_five_grade)
            self.__class_five_grade = conversion(self.__class_five_grade)
            self.frame_error.pack_forget()
            self.submit_five_button.destroy()
            self.add_button.destroy()
            self.frame_bottom.pack()

    def gpa_calculator(self):
        if self.__number_of_classes == 2:
            self.gpa_label.config(text=f'GPA Average: {self.__class_one_grade}')
        elif self.__number_of_classes == 3:
            gpa = average(self.__class_one_grade, self.__class_two_grade)
            self.gpa_label.config(text=f'GPA Average: {gpa}')
        elif self.__number_of_classes == 4:
            gpa = average(self.__class_one_grade, self.__class_two_grade, self.__class_three_grade)
            self.gpa_label.config(text=f'GPA Average: {gpa}')
        elif self.__number_of_classes == 5:
            gpa = average(self.__class_one_grade, self.__class_two_grade, self.__class_three_grade, self.__class_four_grade)
            self.gpa_label.config(text=f'GPA Average: {gpa}')
        else:
            gpa = average(self.__class_one_grade, self.__class_two_grade, self.__class_three_grade, self.__class_four_grade, self.__class_five_grade)
            self.gpa_label.config(text=f'GPA Average: {gpa}')
