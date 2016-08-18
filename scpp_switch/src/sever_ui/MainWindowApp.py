import Tkinter
import logging
import ViewLog
import ThreadsConnector
import ActionWindow
import start_application
import gettext
import sys

_ = gettext.gettext


class MainWindowApp:
    def __init__(self, log):
        """ Remember cumulative logs, get logger """
        self.log = log
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """ Create and run GUI """
        self.root = root = Tkinter.Tk()
        root.title(_('Long Operation Demo'));
        Tkinter.Button(root, text=_('Start'), command=self.onStart, width=10).pack(side=Tkinter.LEFT)
        Tkinter.Button(root, text=_('View Log'), command=self.onViewLog, width=10).pack(side=Tkinter.LEFT)
        Tkinter.Button(root, text=_('Exit'), command=self.onExit, width=10).pack(side=Tkinter.LEFT)
        self.center(root)
        root.mainloop()

    def onExit(self):
        """ Process 'Exit' command """
        # self.root.quit()
        sys.exit()

    def onViewLog(self):
        """ Process 'View Log' command """
        ViewLog.ViewLog(self.root, self.log)

    def onStart(self):
        """ Process 'Start' command """
        self.logger.info(_('start module'))
        conn = ThreadsConnector.ThreadsConnector()
        wnd = ActionWindow.ActionWindow(self.root, _('Switch dashbord'), _('Switch logs view'))
        conn.runInGui(wnd, conn, None, start_application.calc, 'calc')

    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
