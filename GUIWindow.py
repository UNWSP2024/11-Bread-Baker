# Name: Ariana Fafach
# Date: 4/15/2026
# Title: Program #2: GUI Window

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create window:
        self.window = tkinter.Tk()
        # Name window:
        self.window.title("Info")

        # Create information button:
        self.my_button = tkinter.Button(self.window, text = 'Click here to see information', command = self.show_information, relief = 'raised')

        # Pad information button:
        self.my_button.pack(padx = 20, pady = 5)

        # Create quit button:
        self.quit_button = tkinter.Button(self.window, text = "Quit",command = self.window.destroy, relief = 'raised')

        # Pad quit button:
        self.quit_button.pack(padx = 20, pady = 5)

        # Pack both buttons:
        self.my_button.pack()
        self.quit_button.pack()
        
        # Enter the mainloop:
        self.window.mainloop()


    def show_information(self):

        # Show information:
        tkinter.messagebox.showinfo('Information', '''
Ariana Fafach 
12345 somewhere drive 
NowhereVille MN 54321''')
        

if __name__ == '__main__':

    # Creat an instance of MyGUI:
    my_gui = MyGUI()
