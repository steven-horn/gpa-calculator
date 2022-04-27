from gui import *

def main():
    """
    screen that shows upon boot
    """
    window = Tk()

    widgets = Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
