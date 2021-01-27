# 1.0.0
# 2021.1.27
# text edit
# python 3.7.8
# fww
import tkinter
import Settings
root = tkinter.Tk()
root.title("Text edit")
text1 = tkinter.Text(root)
text1.pack()
menu_first = tkinter.Menu(root)
menu1 = tkinter.Menu(menu_first,tearoff=0)
menu_first.add_cascade(label='File', menu=menu1)
menu1.add_command(label='Exit', command=root.quit) # 用tkinter里面自带的quit()函数
# second
menu2 = tkinter.Menu(menu_first,tearoff=0)
menu_first.add_cascade(label="Edit",menu=menu2)
def upper():
	x = text1.get("0.0","end")
	x = x.upper()
	text1.delete("1.0","end")
	text1.insert("end",x)
def lower():
	x = text1.get("0.0","end")
	x = x.lower()
	text1.delete("1.0","end")
	text1.insert("end",x)
def settings():
	Settings.main()
menu2.add_command(label="Upper",command=upper)
menu2.add_command(label="Lower",command=lower)
menu3 = tkinter.Menu(menu_first,tearoff=0)
menu_first.add_cascade(label="Settings",menu=menu3)
menu3.add_command(label="Settings",command=settings)
root.config(menu=menu_first)

root.mainloop()