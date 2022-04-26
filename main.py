from gui import *

def main():
    """
    screen that shows upon boot
    """
    window = Tk()
    #window.geometry('500x500')
    #window.resizable(False, False)

    widgets = Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
