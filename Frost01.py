from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.title('Frost ver 0.1')
root.iconbitmap(r'C:\Users\Urban\Documents\PythonMapa\Frost\Frostico.ico')

#creates left side menu frame
left_side_menu_frame = Frame(root, width=150, height=420, bg = "deep sky blue")

#creates working canvas for frost elements workspace
working_canvas = Canvas(root, width= 800, height = 500, bg = "ghost white") 

left_side_menu_frame.grid(row=1, column=1)
working_canvas.grid(row=1, column=2)

#creates main menu menubar
def hello():
    print ("hello!")

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)


####################################
button_clear_canvas = Button(left_side_menu_frame, text = "Clear canvas", relief = "ridge", borderwidth = 1)
button_clear_canvas.pack(padx = 40, pady = 20, side = "bottom")


def mouse_click(event):
    print(event.x, event.y)
	
	
root.bind('<Button-1>', mouse_click)
root.mainloop()