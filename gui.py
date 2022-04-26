from tkinter import *


class Gui:
    def __init__(self, window):
        """Initial screen"""
        self.__number_of_classes = 1
        self.window = window
        self.window.geometry('300x100')
        self.window.resizable(False, False)
        self.window.title('Class Grade Book')

        self.frame_top = Frame(self.window)
        self.welcome_label = Label(self.frame_top, text='Welcome to your grade book!')
        self.welcome_label.pack()
        self.frame_top.pack()

        self.frame_second = Frame(self.window)
        self.class_entry = Entry(self.frame_second)
        self.button_add_class = Button(self.frame_second, text='Add Class', command=self.clicked)
        self.class_entry.pack(side='left', padx=10)
        self.button_add_class.pack(side='right', padx=10)
        self.frame_second.pack()

    def clicked(self):
        """Function to set the screen"""
        if self.__number_of_classes == 1:
            self.one_class()
            self.__number_of_classes += 1
            self.frame_second.destroy()
            self.button_add_class.destroy()
            self.class_entry.destroy()
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
        self.window.geometry('900x900')

        self.frame_class_one = Frame(self.window)
        self.class_one_label = Label(self.frame_class_one, text='TEMPORARY')
        self.class_one_grade_label = Label(self.frame_class_one, text='TEMPORARY')
        #self.add_grade_entry = Entry(self.frame_class_one)
        self.add_grade_button = Button(self.frame_class_one, text='Add grade')

        self.class_one_label.pack(side='left', padx=10)
        self.class_one_grade_label.pack(side='left')
        #self.add_grade_entry.pack(side='left', padx=30)
        self.add_grade_button.pack(side='right', padx=10)
        self.frame_class_one.pack()

    def two_classes(self):
        """Screen when we have created two grade books"""
        self.window.geometry('300x200')

    def three_classes(self):
        """Screen when we have created three grade books"""
        self.window.geometry('300x300')

    def four_classes(self):
        """Screen when we have created four grade books"""
        self.window.geometry('400x400')
