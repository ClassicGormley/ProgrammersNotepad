import sys
import os
from time import time
from pynput.keyboard import Key, Controller

v = sys.version

if "2.7" in v:
    import Tkinter as tkinter
    from Tkinter import *
    import tkFileDialog as filedialog
    import tkMessgeBox as messagebox
elif "3.6" in v or "3.7" in v:
    import tkinter as tkinter
    from tkinter import *


class KeyboardNotepad:
    root = Tk()

    # default window width and height
    thisWidth = 800
    thisHeight = 800
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)

    #keyboard = Controller()

    # Add scrollbar
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self, **kwargs):

        # Set the window text
        self.root.title("Untitled - Programmer's Keyboard Notepad")

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # For left-align
        left = (screen_width / 2) - (self.thisWidth / 2)

        # For right-align
        top = (screen_height / 2) - (self.thisHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' %
                           (self.thisWidth, self.thisHeight, left, top))

        # To make the text area auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls

        self.thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.thisFileMenu.add_command(label="New", command=self.new_file)

        # To open an already existing file
        self.thisFileMenu.add_command(label="Open", command=self.open_file)

        # To save current file
        self.thisFileMenu.add_command(label="Save", command=self.save_file)

        # To create a line in the dialog
        self.thisFileMenu.add_separator()

        # To terminate
        self.thisFileMenu.add_command(
            label="Exit", command=self.quit_application)
        self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)

        # To give a feature of cut
        self.thisEditMenu.add_command(label="Cut", command=self.cut)

        # To give a feature of copy
        self.thisEditMenu.add_command(label="Copy", command=self.copy)

        # To give a feature of paste
        self.thisEditMenu.add_command(label="Paste", command=self.paste)

        # To give a feature of editing
        self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)

        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

        # Bind functions to text box
        self.root.bind("<KeyPress>", self.key_pressed)
        self.root.bind("<KeyRelease>", self.key_released)

    # Add functionality
    def quit_application(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.root.destroy()

    def open_file(self):

        self.file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("text files", "*.txt"), ("all files", "*.*")))

        if self.file == "":
            # no file to open
            self.file = None
        else:
            # try to open the file
            # set the window title
            self.root.title(os.path.basename(self.file) +
                            " - Programmer's Keyboard Notepad")
            self.thisTextArea.delete(1.0, END)

            file = open(self.file, 'r')

            self.thisTextArea.insert(1.0, file.read())

            file.close()

    def new_file(self):
        self.root.title("Untitled - Programmer's Keyboard Notepad")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def save_file(self):

        if self.file is None:
            # save as new file

            self.file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                                     filetypes=[("All Files", "*,*"), ("Text Documents", "*.txt")])
            if self.file == "":
                self.file = None
            else:

                # try to save the file
                file = open(self.file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()
                # change the window title
                self.root.title(os.path.basename(self.file) +
                                " - Programmer's Keyboard Notepad")

        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):
        # run main application
        self.root.mainloop()

    # Lomnpress substitution
    start_time = 0
    end_time = 0

    def key_pressed(self, event):
        global start_time
        start_time = time()
        print(event.char)

    def key_released(self, event):
        global start_time, end_time
        keyboard = Controller()
        end_time = time()

        if end_time - start_time > 0.2:
            if event.char == 'w':
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.shift)
                keyboard.press('[')
                keyboard.release('[')
                keyboard.release(Key.shift)
            elif event.char == 'o':
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.shift)
                keyboard.press(']')
                keyboard.release(']')
                keyboard.release(Key.shift)
            elif event.char == 'e':
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press('[')
                keyboard.release('[')
            elif event.char == 'i':
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(']')
                keyboard.release(']')
 #           elif event.char == 'v':
 #               keyboard.press(Key.backspace)
 #               keyboard.release(Key.backspace)
 #               keyboard.press(Key.shift)
 #               keyboard.press('9')
 #               keyboard.release('9')
 #               keyboard.release(Key.shift)
 #           elif event.char == 'n':
 #               keyboard.press(Key.backspace)
 #               keyboard.release(Key.backspace)
 #               keyboard.press(Key.shift)
 #               keyboard.press('0')
 #               keyboard.release('0')
 #               keyboard.release(Key.shift)


# Run main application
notepad = KeyboardNotepad(width=600, height=400)
notepad.run()
