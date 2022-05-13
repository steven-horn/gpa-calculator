from tkinter import *
from functions import *


class Gui:
    def __init__(self, window):
        """Initial screen, all widgets, and variables for use within the GUI. Each portion is split by frame in the
        init except for the first two which is the variables and the window properties. Each frame is invisible until
        it has been called by its corresponding function except for the top frame which is always visible and
        the bottom frame which is visible at the beginning."""
        self.__class_grades = []
        self.max_classes = 10

        self.window = window
        self.window.geometry('500x300')
        self.window.resizable(False, False)
        self.window.title('GPA Calculator')

        self.frame_top = Frame(self.window)
        self.welcome_label = Label(self.frame_top, text='Welcome to GPA Calculator!')
        self.welcome_label.pack()
        self.frame_top.pack()

        self.frame_header = Frame(self.window)
        self.class_label = Label(self.frame_header, width=10, text='Class')
        self.grade_label = Label(self.frame_header, width=10, text='Percent Grade')
        self.letter_label = Label(self.frame_header, width=10, text='Letter Grade')
        self.class_label.pack(side='left')
        self.grade_label.pack(side='left', padx=70)
        self.letter_label.pack(side='right')
        self.frame_header.pack()

        self.frame_entry = Frame(self.window)
        self.class_entry = Entry(self.frame_entry, width=25)
        self.percent_entry = Entry(self.frame_entry, width=25)
        self.submit_button = Button(self.frame_entry, text='Submit', command=self.finish)
        self.window.bind('<Return>', self.finish)
        self.class_entry.pack(side='left')
        self.percent_entry.pack(side='left')
        self.submit_button.pack(side='right', padx=15)
        self.frame_entry.pack_forget()

        self.frame_bottom = Frame(self.window)
        self.add_button = Button(self.frame_bottom, text='Add Class', command=self.add_class)
        self.calculate_button = Button(self.frame_bottom, text='Calculate GPA', command=self.gpa_calculator)
        self.gpa_label = Label(self.frame_bottom, text='Average GPA: ')
        self.add_button.pack(side='left', padx=55)
        self.calculate_button.pack(side='left')
        self.gpa_label.pack(side='right', padx=50)
        self.frame_bottom.pack()

        self.frame_error = Frame(self.window)
        self.error_label = Label(self.frame_error, text='Please input a number between 0 - 100', fg='red',
                                 relief='raised', font=('arial', 12))
        self.error_label.pack()
        self.frame_error.pack_forget()

    def add_class(self):
        """Function to determine the frame that is made visible after smashing the add class button."""
        self.frame_entry.pack()
        self.frame_bottom.pack_forget()

    def finish(self, _=None):
        x = self.class_entry.get()
        y = self.percent_entry.get()
        z = letter_grade(y)
        if z is False:
            self.frame_error.pack()
        else:
            self.__class_grades.append(conversion(z))
            new_frame = Frame(self.window)
            new_class_label = Label(new_frame, text=x, width=30)
            new_percent_label = Label(new_frame, text=y, width=10)
            new_letter_label = Label(new_frame, text=z)
            new_class_label.pack(side='left')
            new_percent_label.pack(side='left')
            new_letter_label.pack(side='left', padx=100)
            new_frame.pack()
            self.frame_bottom.pack()
            self.class_entry.delete(0, END)
            self.percent_entry.delete(0, END)
            self.class_entry.focus_force()
            self.frame_entry.pack_forget()
            self.frame_error.pack_forget()
            if len(self.__class_grades) == self.max_classes:
                self.add_button.destroy()

    def gpa_calculator(self):
        gpa = average(*self.__class_grades)
        self.gpa_label.config(text=f'GPA Average: {gpa}')
