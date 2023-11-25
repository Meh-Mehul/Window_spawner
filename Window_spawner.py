# window tester for future uses

from tkinter import *

root0 = Tk()
root0.geometry("600x600+750+300")

label0 = Label(root0, text="     ").grid(row=0, column=0)
label1 = Label(root0, text=" Welcome to window size tester by Mehul")
label1.grid(row= 1, column= 0)
label1.configure(font=('Arial', 13, 'bold'))

label2 = Label( root0, text= "                      Enter dimesions:", font=('Arial', 13, 'bold')).grid(row= 2,column=0)


label3 = Label( root0, text= "                     Enter X dimesion:", font=('Arial', 13)).grid(row= 3,column=0)

label4 = Label( root0, text= "                     Enter Y dimesion:", font=('Arial', 13)).grid(row= 4,column=0)




EntryX = Entry( root0, width= 15, borderwidth=5)
EntryX.grid(row=3, column=1)


EntryY = Entry( root0, width= 15, borderwidth=5)
EntryY.grid(row=4, column=1)

label5 = Label( root0, text= "                      Enter location", font=('Arial', 13, 'bold')).grid(row= 5,column=0)


label6 = Label( root0, text= "                     Enter X location:", font=('Arial', 13)).grid(row= 6,column=0)

label7 = Label( root0, text= "                     Enter Y location:", font=('Arial', 13)).grid(row= 7,column=0)




Entryx = Entry( root0, width= 15, borderwidth=5)
Entryx.grid(row=6, column=1)


Entryy = Entry( root0, width= 15, borderwidth=5)
Entryy.grid(row=7, column=1)




def the_click():
	SizeX = EntryX.get()
	SizeY = EntryY.get()
	Sizex = Entryx.get()
	Sizey = Entryy.get()
	rooti = Tk()
	size_str = f'{SizeX}x{SizeY}+{Sizex}+{Sizey}'
	rooti.geometry(size_str)
	def endlifetime():
		rooti.destroy()
	rooti.after(3000,endlifetime)
	rooti.mainloop()
The_Button = Button(root0, text= "Spawn Test Window", font= ('Arial', 12, 'bold'), padx=5,pady=5, command=the_click).grid( row=22,column=1)
























root0.mainloop()