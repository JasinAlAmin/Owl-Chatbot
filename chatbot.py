from tkinter import *
from tkinter import.scrolledtext import ScrolledTest
from tkinter import import messagebox, filledialog 
import wolfalpha 
import threading


class Pyhobot:
  def __int__(self.root):
    self.root =root
    self.font=('arial',12)
    self.background_color ='#7e7a79'
    self.text_color= '#ffffff'
if __name__ = "__main__";
  root = Tk()
  root.title("Owl-Chatbot")
  root.gemetry("500X520")
  root.resizable(0.0)
  Pybot(root)
  root.mainloop()
  
menybar = Menu(self.root)
option_meny.add_command(label="clear chat",command=self.clear_chat)
option_meny.add_command(label="Save chat",command=self.save_chat)
option_meny.add_separator()
option_meny.add_command(label="Exit",command=self.root.quit)
option.add_casade(label="Option",menu=option_menu)
menubar.root.config.menubar)

self.text_area = ScrolledTest(self.root.front=self.front,bg=self.background_color,fg=self.text_color)
self.text_area.place(x=10,y=10,width=480,hight=440)

frame = frame(self.root,bg=self.background_color)
frame.place(x=10,y=460,width=480,hight=50)

self.entry_box = Entry(frame,font=('arial',14))
self.entry_box.grid(row=10,column=0,pady=0,pady5)
self.send_button = Button(frame,text ='Send',command=self.human_input)
self.send_button.grid(row=0,column=1,pady=9,padx=5)


def human_input(self):4
  input = self.entry_box.get()
  if input:
    self.text_area.insert(END,"human:" + input)
    self.entry_box.delete(0,END)
    self.call_bot(input)
    
def bot_output(self,input):
  appid = "Random text""
  client = wolframalpha API KEY(appid)
  res = client.query(input)
  answer = next(res.results).text
  if answer:
    self.text_area.insert(END,"\OwlBotchatt:" + answer  +'\n')
    
def call_bot(self,input):
  x  = threading.Thread(target=self.bot_output,args=(input,))
  x.start()

def save_chat(self):
  filname = filedialig.asksaveasfile()
  if filename:
    with open (filename,"w") as f:
      f.write(self.text_area.get(0.0,END))
def clear_chatt():
  if messagebox.askyesno("OwlBotchatt says","Are you sure"):
    self.text_area.delete(0.0,END)
  
  

