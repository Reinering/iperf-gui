# -*- coding: utf-8 -*-



import sys, datetime
import getopt
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from iperf_client import MainWindow
import logging.handlers
import os
# from pycrunch_trace.client.api import trace


version = "v1.0.0"
computer_digits = "32位"
package_time = ""



def log():

    if not os.path.exists("log/"):
        os.mkdir('log/')
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    LOG_FILE = "log/" + now + '.log'
    logger = logging.getLogger("myapp")
    hdlr = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*10240, backupCount=400)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=LOG_FILE,
                        filemode='a+')
    logger.addHandler(hdlr)
    logger.setLevel(0)
    return logger


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

# @trace()
def main(argv=None):
    if argv is None:
        argv = sys.argv
    logger = log()
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            app = QApplication(sys.argv)
            pic = "pic/logo.jpg"
            existPic = os.path.exists(pic)
            if existPic:
                splash = QSplashScreen(QPixmap(pic))
                splash.show()
            ui = MainWindow()
            ui.show()
            if existPic:
                splash.finish(ui)
            sys.exit(app.exec_())
        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2



if __name__ == "__main__":
    sys.exit(main())
