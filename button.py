from tkinter import *
import webbrowser
def click():
    url = 'https://www.youtube.com/watch?v=awbSwt4quKk'
    webbrowser.open(url)

window=Tk()
window.geometry('500x500')

button=Button(window,
              text='Click',command=click,
              font=('Comic Sans',50)
              )
button.pack()











window.mainloop()