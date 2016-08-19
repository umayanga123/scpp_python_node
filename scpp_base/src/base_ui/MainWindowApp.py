from Tkinter import *
import gettext
import logging
import sys
import os

from PIL import ImageTk,Image

from base_ui import ViewLog

_ = gettext.gettext


class MainWindowApp:
    def __init__(self, log):
        """ Remember cumulative logs, get logger """
        self.log = log
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """ Create and run GUI """
        self.root = root = Tk()
        self.root.columnconfigure(0, weight=1)  #center component
        #self.root.config(bg='Thistle')
        root.geometry('{}x{}'.format( 350, 500))
        root.resizable(width=False, height=False)
        root.title(_('Welcome Money Exchange'))

        path = "img/b.png"
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))


        self.topBar = Frame(self.root, border=1, relief=GROOVE )
        self.topBar.grid(row=0, column=0, columnspan=2,sticky=E+W +N +S)
        self.topBar.columnconfigure(0, weight=1)

        l0=Label(self.topBar, image=img).grid(row=1, column=0,columnspan=2, sticky=N , padx=5, pady=20)
        l1=Label(self.topBar, text="Coin Rate :", fg="red",font=("Helvetica", 16)).grid(row=1,column=0,sticky=W +S,pady=5,padx=5)
        l2=Label(self.topBar, text="1 coin === 0.0002$", font=("Helvetica", 16))

        b1=Button(self.root, text=_('Refresh Coin Value'), command=self.getCoinValue, width=30 ,background='green').grid(row=1,column=0,pady=5,padx=5)

        b2=Button(self.root, text=_('View Transaction Details'), command=self.onDatabaseLog, width=30)
        b3=Button(self.root, text=_('View Log File'), command=self.onViewLog, width=30)
        b4=Button(self.root, text=_('Exit'), command=self.onExit, width=10,background='red')



        l2.grid(row=1,column=0,sticky=E+S,pady=5,padx=5)
        b2.grid(row=3,column=0,pady=5,padx=5)
        b3.grid(row=4, column=0,pady=5,padx=5)
        b4.grid(row=5,column=0,pady=5,padx=5)


        self.center(root)
        root.mainloop()

    def onExit(self):
        """ Process 'Exit' command """
        os._exit(0)


    def onDatabaseLog(self):
        """ Process 'View DB enrties' command """
        print "take database recodes"

    def getCoinValue(self):
        """ Process 'Start' command """
        print "get coin values"

    def onViewLog(self):
        """ Process 'View Log' command """
        ViewLog.ViewLog(self.root, self.log)


    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
