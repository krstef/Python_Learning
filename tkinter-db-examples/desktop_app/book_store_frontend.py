from tkinter import *
import book_store_backend as back

window = Tk()
window.wm_title("Book Store app")
# Presenter part
#Helper func - bind method expects event argument
def get_selected_row(event):
    try:
        global selected
        #take first param from the list - index number
        index = listbox.curselection()[0]
        #from the listbox get the index
        selected = listbox.get(index)
        #show selected data in entries
        e1.delete(0, END)
        e1.insert(END, selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[2])
        e3.delete(0, END)
        e3.insert(END, selected[3])
        e4.delete(0, END)
        e4.insert(END, selected[4])
    except IndexError:
        pass

def view_all():
    listbox.delete(0, END)
    for row in back.view():
        listbox.insert(END, row)

def search():
    listbox.delete(0, END)
    #get the string object from StringVar
    for row in back.search(title_text.get(), author_text.get(), year_text.get(),\
     isbn_text.get()):
        listbox.insert(END, row)

def insert():
    back.insert(title_text.get(), author_text.get(), year_text.get(),\
     isbn_text.get())
    listbox.delete(0,END)
    listbox.insert(END, (title_text.get(), author_text.get(), year_text.get()))

def delete():
    back.delete(selected[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def update():
    back.update(selected[0], title_text.get(), author_text.get(), \
    year_text.get(), isbn_text.get())

# View part
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row =0, column = 1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row =1, column = 1)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row =0, column = 3)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row =1, column = 3)

listbox = Listbox(window, height=10, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column = 2, rowspan=6)

# apply scrollbar to listbox
listbox.configure(yscrollcommand=scroll.set)
scroll.configure(command = listbox.yview)
#bind selcted data to the method
listbox.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=15, command= view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=15, command = search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=15, command = insert)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=15, command = update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=15, command = delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=15, command = window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
