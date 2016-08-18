from Tkinter import *
import gettext
import logging
import sys
import os




_ = gettext.gettext


class MainWindowApp:
    def __init__(self, log):
        """ Remember cumulative logs, get logger """
        self.log = log
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """ Create and run GUI """
        self.root = root = Tk()
        root.geometry('{}x{}'.format( 400, 100))
        root.title(_('Welcome TO Money Exchange'));

        l1=Label(root, text="Coin Rate :", fg="red",font=("Helvetica", 16)).grid(row=0,column=0)
        l2=Label(root, text="1 coin === 0.0002$", font=("Helvetica", 16))

        b1=Button(root, text=_('Refresh Coin Value'), command=self.getCoinValue, width=30).grid(row=1,)
        b2=Button(root, text=_('View Transaction Details'), command=self.onDatabaseLog, width=30)
        b3=Button(root, text=_('Exit'), command=self.onExit, width=10)



        l2.grid(row=0,column=0)


        b2.grid(row=2,column=0)
        b3.grid(row=3,column=0)


        '''e1 = Entry(root)
        e2 = Entry(root)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)



        Button(root, text=_('Refresh'), command=self.getCoinValue, width=30 ).pack(side=TOP)
        Button(root, text=_('View Transaction Details'), command=self.onDatabaseLog, width=30).pack(side=TOP)
        Button(root, text=_('Exit'), command=self.onExit, width=10).pack(side=TOP)'''

        self.center(root)
        root.mainloop()

    def onExit(self):
        """ Process 'Exit' command """
        # self.root.quit()
        #sys.exit()
        os._exit(0)


    def onDatabaseLog(self):
        """ Process 'View Log' command """
        print "take database recodes"

    def getCoinValue(self):
        """ Process 'Start' command """
        print "get coin values"


    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
