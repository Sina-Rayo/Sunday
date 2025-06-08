import os , time , sys
import Realization , Response
import pyttsx3
from tkinter import *
from playsound import playsound
import argparse
import queue
import sounddevice as sd
import vosk
import json


banner = """
  ________   __     __ ___    __ ________     __  ____  ____  
 /  ______\ |  |   |  |   \  |  |   ___  \   /  \|_  _||_  _| 
|  |_____   |  |   |  |  \ \ |  |  |   \  \ / /\ \ \ \  / /   
 \_____  \  |  |   |  |  |\ \|  |  |    |  / /__\ \ \ \/ /    
 ______|  | |  \___/  |  | \ \  |  |___/  / /    \ \ |  |_    
\________/   \_______/|__|  \___|________/___|  |___\_____|   
"""

#### Info ####
curpath = os.getcwd()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

#### functions ####
def know_command(txt):
    global is_listening
    is_listening = False
    tag = Realization.realize(txt)
    if tag == "Not Exist Err" or tag == None:
        not_exist()
    # elif(tag== "write"):
    #     inp.delete('1.0' , 'end')
    #     Buttons.pack()
    else:
        res = Response.get_func(tag)
        if(res == "Not in path err"):
            func_not_exist()
        else:
            listen_after = res[len(res)-1]
            res = res[:-1]
            Response.do(res)
            if(listen_after == '0'):
                hide_win()
            else:
                # playsound(f"{curpath}\Stuff\Listening.mp3") 
                listen_again()
        

def Get_Command():
    txt = Recognize_voice()
    print('\n'*5)

    if(txt == ''):
        hide_win()
        return None
    know_command(txt)

def speak(text):
    engine.say(text)
    print("Sunday :  " + text + '\n\n')
    engine.runAndWait()

# def question(q):
#     speak(q)
#     txt = Recognize_voice()
#     print('\n'*5)
#     ans = Realization.realize(txt)
    
#     if(ans == "write" or ans == "Not Exist Err"):
#         ans = input("you :  ")
#     return ans


def START():
    print('\n' + '-' * 100 + '\n'*10)
    Starting()
    root.deiconify()
    playsound(f"{curpath}\Stuff\Listening.mp3") 

    inp.delete('1.0' , 'end')
    Buttons.pack_forget()
    msg_s.set(' ')
    root.update()
    print(banner + '\n'*6)
    # Speech.speak("Listening")
    Get_Command()



############################# USER INTERFACE ###############################
############################################################################
def dummy_func():
    return None

root = Tk()

######### Setting #########
root.title("SUNDAY")
w = 600
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
xx = (ws/3) 
yy = (hs/1024)

root.geometry('%dx%d+%d+%d' % (w, h, xx, yy))
root.configure(bg="black")
root.resizable(width=False , height=False)
root.protocol("WM_DELETE_WINDOW", dummy_func)

######### Variables #########
msg_s = StringVar()
ent_txt = StringVar(value='')
is_editing = False
is_listening = False
is_adding = False
mtm = 0
tm_names = ['dark' , 'light']

theme = {
    'dark' : {
        'main_bg' : 'black',
        'eyes' : '\\Stuff\SunDayDark.png',
        'msg' : 'red',
        'text_bg' : 'black',
        'text_fg' : 'white',
        'button_bg' : 'black',
        'buttons' : ['light blue' , 'green' , 'red' , 'yellow'],
        'short_cuts' : 'gray'
    },
    'light' : {
        'main_bg' : 'light yellow',
        'eyes' : '\\Stuff\SunDayLight.png',
        'msg' : 'dark blue',
        'text_bg' : 'light yellow',
        'text_fg' : 'black',
        'button_bg' : 'light yellow',
        'buttons' : ['green' , 'purple' , 'red' , 'blue'],
        'short_cuts' : 'pink'
    }
}

######### Functions #########

def onKeyPress(event):
    global is_editing , is_listening
    
    if event.char == '\r' :
        if start_win.winfo_exists():
            start_all()
        # elif func_frame.winfo_ismapped():
        #     add_sen(inp.get('1.0' , 'end') , func_entry.get())
        elif is_editing:
            is_editing = False
            editf(inp.get('1.0' , 'end'))

    if Buttons.winfo_ismapped():
        if event.char == '\x01' and (not is_editing) and (not is_listening):
            add_sen_st()
            # func_entry.focus()
        elif event.char == '\x05':
           editsh()
        elif event.char == '\x0c':
            listen_again()
        elif event.char == '\x1b':
            hide_win()
        elif event.keycode == 84:
            change_tm()

def onMousePress(event):
    if event.widget == inp:
        is_editing = True

def show_msg(m):
    msg_s.set(m)

def editsh():
    global is_editing
    is_editing = True
    inp.focus()


def editf(txt):
    know_command(txt)


def make_tag(txt):
    with open('Data\Tags.json' , 'r') as jfile:
        s_list = json.load(jfile)
    jfile.close()

    txtl = txt.split()
    tag = ""
    for i in txtl:
        tag += i[0]

    # lf = 0
    # rf = len(s_list)-1
    # cf = int((lf + rf) / 2)
    # while(lf < rf):
    #     if(txt < s_list[cf]): 
    #         rf = cf-1
    #     else:
    #         lf = cf+1
    #     cf = int((lf + rf) / 2)
    # while(s_list[cf] == tag):
    #     try:
    #         num = int(tag[len(tag)-1])
    #         num +=1
    #         tag.pop()
    #         tag += str(num)
    #     except:
    #         tag += '1'
    #     cf += 1

    while(tag in s_list):
        tag += '*'

    s_list.append(tag)
    s_list.sort()
    with open('Data\Tags.json' , 'w') as jfile:
        add_list = json.dumps(s_list)
        jfile.write(add_list)
    return tag

def add_sen(txt , func):
    if str(msg_s.get()) == "Didn't Get you":
        tag = make_tag(txt)
        Realization.make_sentense(txt , Checkbutton3.get())
        Realization.add_tag(txt , tag)
    else:
        tag = Realization.realize(txt)

    Response.add_function(tag, func , Checkbutton2.get() , Checkbutton1.get())

    entr.delete('1.0' , END)
    hide_win()

def add_sen_st():
    is_editing = False
    add_win.deiconify()
    # func_frame.pack()

def not_exist():
    msg_s.set("Didn't Get you")
    Buttons.pack()
    root.update()
    speak("Didn't Get you")
    
def func_not_exist():
    msg_s.set("Not related to the conversation")
    Buttons.pack()
    root.update()
    speak("what?")

def hide_win():
    Buttons.pack_forget()
    # func_frame.pack_forget()
    add_win.withdraw()
    root.withdraw()
    START()

def listen_again():
    global is_listening
    is_listening = True
    is_editing = False
    Get_Command()

def edit_txt(txt):
    inp.delete('1.0' , 'end')
    inp.insert(INSERT , txt)
def start_all():
    start_win.destroy()
    START()


def change_tm():
    global mtm , engine
    engine.setProperty('voice', voices[(len(voices)-1)*((mtm+1)%2)].id)
    mtm += 1
    if(mtm > 1):
        mtm = 0

    t_dic = theme[tm_names[mtm]]


    img3 = PhotoImage(file= f"{curpath}{t_dic['eyes']}")
    
    root.configure(bg=t_dic['main_bg'])
    limg.configure(image = img3 , bg=t_dic['main_bg'])
    limg.image = img3
    msg.configure(bg = t_dic['main_bg'] , fg = t_dic['msg'])
    inp.configure(bg = t_dic['text_bg'] , fg=t_dic['text_fg'])
    Buttons.configure(bg=t_dic['main_bg'])
    Labels.configure(bg = t_dic['main_bg'])
    b = 0
    for btn in [btn1 , btn2 , btn3 , btn4]:
        btn.configure(bg=t_dic['button_bg'] , fg = t_dic['buttons'][b])
        b += 1
    b=0
    for lbl in [lbl1 , lbl2 , lbl3 , lbl4 , lbl5]:
        lbl.configure(bg=t_dic['main_bg'] , fg = t_dic['short_cuts'])
        b += 1
    f1.configure(bg=t_dic['main_bg'])
    add_win.configure(bg=t_dic['main_bg'])
    lbel2.configure(bg = t_dic['main_bg'] , fg=t_dic['msg'])
    entr.configure(bg=t_dic['text_bg'] , fg=t_dic['text_fg'])

    for But in [Button1 , Button2 , Button3]:
        But.configure(bg = t_dic['button_bg'] , fg=t_dic['buttons'][3])
    btn122.configure(bg =t_dic['button_bg'] , fg=t_dic['buttons'][0])
    

######### Elements #########

img = PhotoImage(file=f'{curpath}\Stuff\SunDayDark.png')
limg = Label(root , image=img , bg='black')
limg.pack(side='top')
# limg.place(x=50 , y=0)


# Main Window

msg = Label(root , textvariable=msg_s , bg='black' , fg='red' , font='Arial 16')
msg.pack(pady=8)

inp = Text(root ,bg='black' , fg='white' , insertbackground='light green',height=5 , width=40 , font ='Arial 18')
# inp.place(x=25 , y = 300)
inp.pack(pady=20)


Buttons = Frame(root , width=480 , height=120, bg='black')
# Buttons.place(x=50 , y=350)
# Buttons.pack()
# Buttons.pack_forget()

btn1 = Button(Buttons , text='Edit and Run' ,activebackground='gray' , bg='black' 
,command=lambda: editf(inp.get('1.0' , 'end')) ,fg='light blue' ,width=10, height=1 , font='Arial 14')
btn1.place(x=120 , y=0)

btn2 = Button(Buttons , text='Add' ,activebackground='gray' , bg='black' 
,command=lambda: add_sen_st() ,fg='green' ,width=10, height=1 , font='Arial 14')
btn2.place(x=0 , y=0)

btn3 = Button(Buttons , text='Close' ,activebackground='gray' , bg='black' ,command=lambda: hide_win() ,
 fg='red' ,width=10, height=1 , font='Arial 14')
btn3.place(x=360 , y=0)

btn4 = Button(Buttons , text='Listen' ,activebackground='gray' , bg='black' ,command=lambda: listen_again() ,
 fg='yellow' ,width=10, height=1 , font='Arial 14')
btn4.place(x=240 , y=0)

Labels = Frame(Buttons , width=480 , height=30, bg='black')
Labels.place(x=0 , y=50)

lbl1 = Label(Labels , text='ctrl + E'  , bg='black' ,fg='gray' ,width=10, height=1 , font='Arial 14')
lbl1.place(x=120 , y=0)

lbl2 = Label(Labels , text='ctrl + A'  , bg='black' ,fg='gray' ,width=10, height=1 , font='Arial 14')
lbl2.place(x=0 , y=0)

lbl3 = Label(Labels , text='Esc'  , bg='black' ,fg='gray' ,width=10, height=1 , font='Arial 14')
lbl3.place(x=360 , y=0)

lbl4 = Label(Labels , text='ctrl + L'  , bg='black' ,fg='gray' ,width=10, height=1 , font='Arial 14')
lbl4.place(x=240 , y=0)

theme_btn = Button(root , text='theme' , bg='light green' , fg='black' , width=8 , height=1
 , font='Arial 8' , command=lambda : change_tm())
theme_btn.place(x= 0 , y = 470)

lbl5 = Label(root , text='ctrl + T'  , bg='black' ,fg='gray' ,width=8, height=1 , font='Arial 8')
lbl5.place(x=60 , y=470)

# func_frame = Frame(root , width=100 , bg='black')
# func_frame.pack(pady=2)

# func_str = Label(func_frame , text='Enter Function : ', bg='black' , fg="pink" , font='Arial 14')
# func_str.pack(side='left')


# func_btn = Button(func_frame ,command= lambda: add_sen(inp.get('1.0' , 'end') , func_entry.get())
#  , text='ADD' , width=5 , height=1 , bg='black' , fg="light green" , font='Arial 14')
# func_btn.pack(side='right' , padx=10)

# func_entry = Entry(func_frame , width=20 , bg='black' , fg="yellow" , font='Arial 14')
# func_entry.pack(side='right')

# func_frame.pack_forget()
# btn4 = Button(root , text='show msg' , command=lambda: add_sen())
# btn4.place(x=10 , y=10)
# btn5 = Button(root , text='hide' , command=lambda: hide_win())
# btn5.place(x=80 , y=10)
# btn6 = Button(root , text='btn_hide' , command=lambda: btn_hide())
# btn6.place(x=120 , y=10)


root.bind('<KeyPress>', onKeyPress)
root.bind('<Button-1>', onMousePress)

root.withdraw()

img2 = PhotoImage(file=f'{curpath}\Stuff\SunDay2.png')
# Start Window
start_win = Toplevel()
start_win.title("SUNDAY")
start_win.geometry('%dx%d+%d+%d' % (400, 300, xx, yy))
start_win.configure(bg="black")
start_win.resizable(width=False , height=False)
start_win.protocol("WM_DELETE_WINDOW", dummy_func)
limg2 = Label(start_win , image=img2)
limg2.pack(side='top')

btn322 = Button(start_win , text='START' ,activebackground='white' , bg='black' ,command=lambda: start_all() ,
 fg='yellow' ,width=100, height=50 , font='Arial 80')
btn322.pack(side='bottom')


#  ADD WINDOW

add_win = Toplevel()
add_win.title("ADD Function")
add_win.geometry('500x500')
add_win.configure(bg="black")
add_win.resizable(width=False , height=True)
add_win.protocol("WM_DELETE_WINDOW", dummy_func)

# --------------------------------------------------------------

# lbel1 = Label(add_win , text="sentence : " + str(inp.get('1.0' , 'end')) , font='Arial 24' , bg='black' , fg='red')
# lbel1.pack(pady=20)
# lbl2 = Label(f1 , text="example " , font='Arial 24' , bg='black' , fg='light green')
# lbl2.pack(side='right')

f1 = Frame(add_win , width=800 , height=2 , bg='black')
f1.pack()
lbel2 = Label(f1 , text="function :  " , font='Arial 24' , bg='black' , fg='light green')
lbel2.pack(side='left')
entr = Text(f1 ,bg='black' , fg='light green' , insertbackground='red',height=3 , width=40 , font ='Arial 18')
entr.pack(side='right' , padx=5)


Checkbutton1 = BooleanVar()
Button1 = Checkbutton(add_win, text = "listen after", variable = Checkbutton1, activebackground='gray',
 onvalue = 1, offvalue = 0,height = 2, width = 10 , bg='black' , fg='yellow' , font='Arial 24' ,
  selectcolor='light green', indicatoron=False)
Button1.pack()

Checkbutton2 = BooleanVar()
Button2 = Checkbutton(add_win, text = "Add Here", variable = Checkbutton2, activebackground='gray',
 onvalue = 1, offvalue = 0,height = 2, width = 10 , bg='black' , fg='yellow' , font='Arial 24' ,
  selectcolor='light green', indicatoron=False)
Button2.pack()

Checkbutton3 = BooleanVar()
Button3 = Checkbutton(add_win, text = "Variable", variable = Checkbutton3, activebackground='gray',
 onvalue = 1, offvalue = 0,height = 2, width = 10 , bg='black' , fg='yellow' , font='Arial 24' ,
  selectcolor='light green', indicatoron=False)
Button3.pack()

btn122 = Button(add_win , text='ADD' ,activebackground='gray' , bg='black' 
,command=lambda: add_sen(inp.get('1.0' , 'end') , entr.get('1.0' , 'end')) ,fg='light blue' ,width=10, height=1 , font='Arial 40')
btn122.pack()


add_win.withdraw()

############################# Recognizer ###################################
############################################################################



q = queue.Queue()


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)

try:
    if args.model is None:
        args.model = "model"
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])

    model = vosk.Model(args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))


def Recognize_voice():
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device, dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, args.samplerate)
        qe = ""
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = rec.Result()
                te_txt = json.loads(res)["text"]
                sys.stdout.write("\r " + te_txt)
                sys.stdout.flush()
                edit_txt(te_txt)
                root.update()
                return te_txt
            else:
                te = rec.PartialResult()
                if not te == qe:
                    te_txt = json.loads(te)["partial"]
                    sys.stdout.write("\r" + te_txt)
                    sys.stdout.flush()
                    edit_txt(te_txt)
                    root.update()
                qe = te

            if dump_fn is not None:
                dump_fn.write(data)


def Starting():
    with sd.RawInputStream(samplerate=args.samplerate, blocksize=8000, device=args.device, dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = rec.Result()
            else:
                txt = rec.PartialResult()
                if "sunday" in txt:
                    return txt


            if dump_fn is not None:
                dump_fn.write(data)





start_win.bind('<KeyPress>', onKeyPress)
root.mainloop()

# Update() 
# while(True):
    # START()