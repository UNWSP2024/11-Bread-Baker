# Name: Ariana Fafach
# Date: 4/15/2026
# Title: Program #1: My Favorite Saying


import tkinter

class MyGUI:
    def __init__(self):

        # Creat GUI window:
        self.window = tkinter.Tk()

        # Name GUI window:
        self.window.title("My Favorite Saying")
        # Write message:
        self.label1 = tkinter.Label(self.window, text = "Only one life shall soon be past,")
        self.label2 = tkinter.Label(self.window, text = "Only what's done for Christ will last,")
        self.label3 = tkinter.Label(self.window, text = "And when I die how glad I shall be,")
        self.label4 = tkinter.Label(self.window, text = "If the lamp of my life has burned out for Thee.")
        self.label5 = tkinter.Label(self.window, text = "~ C.T. Studd")

        # Give one of the labels padding so that everyting fits well on the GUI window:
        self.label1.pack(ipadx = 55)

        # Pack all of the labels
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
    
        tkinter.mainloop()

if __name__ == '__main__':
    
    # Create an instance of MYGUI:
    my_gui = MyGUI()




