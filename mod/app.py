# -*- coding: utf-8 -*-
import time
import sys
import signal
import os

from mod.srv import Server

import logging
logger = logging.getLogger(__name__)


class srvApp:
    def __init__(self):
        self.app_name = 'srvApp'
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '/tmp/%s_%s.pid' % (self.app_name, os.geteuid())
        self.pidfile_timeout = 5
        self.log_file = '/tmp/%s_%s.log' % (self.app_name, os.geteuid())
        self.foreground = False

    def output(self, message):
        if not self.foreground:
            logger.info(message)
        else:
            print(message)

    def run(self):
        if not self.foreground:
            logging.basicConfig(level=logging.NOTSET,
                                format='%(asctime)s %(levelname)s %(message)s',
                                filename=self.log_file,
                                filemode='a')

        f = Server()
        f.start()
        self.output("server start.")
        while True:
            time.sleep(1)
