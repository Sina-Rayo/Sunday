from tkinter import *
import os , json , Realization

root = Tk()
curpath = os.getcwd()

######### Setting #########
root.title("SUNDAY")
w = 720
h = 950
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
xx = (ws/3) 
yy = (hs/1024)

root.geometry('%dx%d+%d+%d' % (w, h, xx, yy))
root.configure(bg="black")


######### Variables #########
msg_s = StringVar(value='')
func_show = StringVar(value='')
btn_list = []
ch_list = []
entry_row = 1
entry_col = 2
ch_col = 1
ch_row = 1

######### Functions #########

def get_children(indx):
    with open("Data\Trie.json" , 'r') as jfile:
        dic = json.load(jfile)
        node = dic[indx]
        nodes = []

        for nd in node["children"]:
            nodes.append((dic[nd]["ind"] , dic[nd]["tag"]))
            
    jfile.close()
    return nodes

def del_btn(txt , indx):
    global entry_row , entry_col
    for btn in reversed(btn_list):
        tt = btn['text'].split()[1]
        ss = btn['text'].split()[0]
        btn.destroy()
        btn_list.pop()
        new_msg = msg_s.get().rsplit(' ' ,1)[0]
        msg_s.set(new_msg)

        entry_col -= 1
        if(entry_col == 0):
            entry_col = 4
            entry_row -= 1

        if int(tt) == indx:
            break
    add_button(txt, indx)
    msg_s.set(msg_s.get().replace('Root' , ''))

def add_child(chd):
    global ch_col, ch_row
    btn2 = Button(children_box , text=chd[1] ,activebackground='gray' , bg='black' 
    ,command= lambda: add_button(chd[1], chd[0]) ,fg='white' ,width=15, height=1 , font='Arial 14')
        
    btn2.grid(row=ch_row , column=ch_col , pady=3 , padx=2)
    ch_list.append(btn2)
    ch_col += 1
    if(ch_col == 5):
        ch_col = 1
        ch_row += 1


def add_button(txt , indx):
    global entry_row , entry_col
    btn = Button(Buttons , text=txt + " " + str(indx) ,activebackground='gray' , bg='black' 
    , command=lambda: del_btn(txt , indx) ,fg='white' ,width=15, height=1 , font='Arial 14' , name=str(indx))

    btn.grid(row=entry_row , column=entry_col , pady=5 , padx=2)
    btn_list.append(btn)
    entry_col += 1
    if(entry_col == 5):
        entry_col = 1
        entry_row += 1
    
    msg_s.set(msg_s.get() + " " + txt)
    func_show.set('Current Tag : ' + str(Realization.realize(msg_s.get())))

    for ch in reversed(ch_list):
        ch.destroy()
        ch_list.pop()

    global ch_col, ch_row
    ch_col = 1
    ch_row = 1
    for child in get_children(indx):
        add_child(child)

def add_func(txt , func):
    Realization.add_function(txt , func)
    func_show.set('Current Tag : ' + func)

######### Elements #########

img = PhotoImage(file=f'{curpath}\Stuff\SunDay.png')
limg = Label(root , image=img)
limg.pack(side='top')


cur_sen = Label(root , textvariable=msg_s , bg='black' , fg='red' , font='Arial 14')
cur_sen.pack(pady=8)


Buttons = Listbox(root , width=480 , height=20, bg='black')
Buttons.pack(pady=8)

children_box = Listbox(root , width=480 , height=10, bg='black')
children_box.pack(pady=8)

func_frame = Frame(root , width=60 , bg='black')
func_frame.pack(pady=30)

func_str = Label(func_frame , text='Enter Tag : ', bg='black' , fg="pink" , font='Arial 24')
func_str.pack(side='left' ,padx=20)

func_entry = Entry(func_frame , width=20 , bg='black' , fg="yellow" , font='Arial 24')
func_entry.pack(side='right',pady=5)

func_btn = Button(root ,command= lambda: add_func(msg_s.get() ,func_entry.get()) , text='ADD' , width=10 , height=2 
, bg='black' , fg="light green" , font='Arial 30')
func_btn.pack(pady=20)


cur_func_str = Label(root , textvariable=func_show
, bg='black' , fg="Green" , font='Arial 24')
cur_func_str.pack(pady=10)


add_button("Root", 0)
msg_s.set(msg_s.get().replace('Root' , ''))

root.mainloop()

