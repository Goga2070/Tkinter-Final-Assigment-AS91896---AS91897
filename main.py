from tkinter import *
from tkcalendar import *
import base64, zlib
import tempfile
from tkinter import messagebox
import tkinter.font as tkfont

#Making a transparent window icon instead of a feather
ICON = zlib.decompress(
    base64.b64decode(
        "eJxjYGAEQgEBBiDJwZDBy"
        "sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="
    )
)
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)

# Creating window for program
root = Tk()
#Icon bitmap sets the feather to whatever file I want it to be , in this case its transparent
root.iconbitmap(default=ICON_PATH)
root.minsize(height=120, width=170)
root.title("Main Menu")
canvas = Canvas(root)


# Making the program look better with rounded corners
def round_rectangle_border(x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius,
        y1,
        x1 + radius,
        y1,
        x2 - radius,
        y1,
        x2 - radius,
        y1,
        x2,
        y1,
        x2,
        y1 + radius,
        x2,
        y1 + radius,
        x2,
        y2 - radius,
        x2,
        y2 - radius,
        x2,
        y2,
        x2 - radius,
        y2,
        x2 - radius,
        y2,
        x1 + radius,
        y2,
        x1 + radius,
        y2,
        x1,
        y2,
        x1,
        y2 - radius,
        x1,
        y2 - radius,
        x1,
        y1 + radius,
        x1,
        y1 + radius,
        x1,
        y1,
    ]

    return canvas.create_polygon(points, **kwargs, smooth=True)


my_rectangle = round_rectangle_border(50, 50, 150, 100, radius=20, fill="blue")


# Creating the main menu
def Menu():
    # Making record keeper page
    def recordpage():
        root.minsize(height=200, width=170)

        # Making everything global to be used on the back function
        global customer_name_label
        global item_hired_label
        global item_quantity_label
        global reciept_num_label
        global customer_name_input
        global item_quantity_input
        global reciept_num_input
        global item_hired_input
        global enterbutton
        global datalist

        # Labels for the input boxes
        customer_name_label = Label(root, text="Customer Name")
        customer_name_label.grid(column=1, row=2)
        item_hired_label = Label(root, text="Hired Item")
        item_hired_label.grid(column=2, row=2)
        item_quantity_label = Label(root, text="Item Quantity")
        item_quantity_label.grid(column=3, row=2)
        reciept_num_label = Label(root, text="Reciept Number")
        reciept_num_label.grid(column=4, row=2)

        # Input boxes
        customer_name_input = Entry(root)
        customer_name_input.grid(column=1, row=3)
        item_hired_input = Entry(root)
        item_hired_input.grid(column=2, row=3)
        item_quantity_input = Entry(root)
        item_quantity_input.grid(column=3, row=3)
        reciept_num_input = Entry(root)
        reciept_num_input.grid(column=4, row=3)

        # Empty record list
        datalist = []

        # Adding enter button to accept the values enetered
        def enter():
            # Checks if item quantity inputted is a number
            try:
                item_quantity_input_interger = int(item_quantity_input.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter number!")

            # Then checks if item quantity inputted is a number within 500 otherwise becomes invalid
            if item_quantity_input_interger > 500:
                messagebox.showerror("Error", "Please enter a number within 500!")
                item_quantity_input_interger = " "

            # Making all future values into global to be used in dictionary creation
            datalist.append(
                [
                    customer_name_input.get(),
                    item_hired_input.get(),
                    item_quantity_input_interger.get(),
                    reciept_num_input.get(),
                ]
            )
            update_record()

        enterbutton = Button(root, text="Enter", command=enter)
        enterbutton.grid(column=1, row=5)

        # Destorying previous page elemnts
        menubutton_1.destroy()
        menubutton_2.destroy()
        label_name.destroy()

        # Adding back button for record keeping page
        global button_2
        button_2 = Button(
            root, text="<--Menu", width="7", command=back, activebackground="red"
        )
        button_2.grid(column=1, row=1, sticky=W)

    # Making Record Viewing page
    def viewrecordspage():
        root.minsize(height=200, width=170)
        label_name.destroy()
        menubutton_1.destroy()
        menubutton_2.destroy()

        global delete
        global update_record

        def delete():
            del datalist[int(select.curseselection()[0])]
            update_record()
        
        def update_record():
            select.delete(0, END)
            for n,p,a in datalist:
                select.insert(END, n)

        scroll_bar = Scrollbar(root, orient=VERTICAL)
        select = Listbox(root, yscrollcommand=scroll_bar.set, height=100, width=160)
        scroll_bar.configure(command=select.yview)
        # scroll_bar.grid(column=4, fill=Y)
        # select.place(x=200,y=260)

        # Making everything global to be used on the back function
        global customer_name_label
        global item_hired_label
        global item_quantity_label
        global reciept_num_label

        # Labels for the grid boxes
        customer_name_label = Label(root, text="Customer Name")
        customer_name_label.grid(column=1, row=2)
        item_hired_label = Label(root, text="Hired Item")
        item_hired_label.grid(column=2, row=2)
        item_quantity_label = Label(root, text="Item Quantity")
        item_quantity_label.grid(column=3, row=2)
        reciept_num_label = Label(root, text="Reciept Number")
        reciept_num_label.grid(column=4, row=2)

        # Making each variable unique to place into grid boxes

        # Adding back button for record viewing page
        global button_2
        button_2 = Button(
            root, text="<--Menu", width="7", command=back, activebackground="red"
        )
        button_2.grid(column=1, row=1, sticky=W)

        # Making a back button that can be used on all pages.

    def back():
        root.minsize(height=200, width=170)
        root.title("Party Hire Store Record Keeper")
        Menu()

        # removing the back button
        button_2.destroy()

        # Removing the other assests,  buttons and labels
        customer_name_label.destroy()
        item_hired_label.destroy()
        enterbutton.destroy()
        item_quantity_label.destroy()
        reciept_num_label.destroy()
        customer_name_input.destroy()
        item_hired_input.destroy()
        item_quantity_input.destroy()
        reciept_num_input.destroy()

    # Labeling the main menu
    label_name = Label(
        root, text="Party Hire Store Record Keeper", font=(25), padx=8, pady=5
    )
    label_name.grid(column=2, row=1)

    # Making buttons to seperate
    menubutton_1 = Button(
        root, text="Add a Record", command=recordpage, activebackground="white"
    )
    menubutton_1.grid(column=2, row=2)
    menubutton_2 = Button(
        root, text="View Records", command=viewrecordspage, activebackground="white"
    )
    menubutton_2.grid(column=2, row=3)


Menu()
root.mainloop()
