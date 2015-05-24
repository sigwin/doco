# -*- coding: utf-8 -*-

import netifaces
import sys
import socket
import os

if os.path.exists("util.py"):
    from util import *
else:
    from mod.util import *
CONFIG = os.path.abspath(os.path.dirname(__file__))+"/../config.json"
import logging
logger = logging.getLogger(__name__)


class Server:
    def __init__(self):
        self.SETTING = get_config(CONFIG)
        self.buf = 8192
        logger.info("server setup.")

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(['', self.SETTING['port']])
        sock.bind(('', self.SETTING['port']))
        try:
            while True:
                msg, address = sock.recvfrom(8192)
                logger.info(("%s, %s") % (msg.decode('utf-8'), address))
                rev = self._cmd(msg.decode('utf-8'))
                sock.sendto(rev.encode('utf-8'), address)
        finally:
            sock.close()

    def _get_iface(self):
        try:
            iface_data = netifaces.ifaddresses(self.SETTING['interface'])
            ip = iface_data.get(netifaces.AF_INET)[0]
            host = os.uname()[1]
        except Exception:
            import sys
            print("Error: not found iface data")
            sys.exit(-1)
        return {"ip": ip['addr'], "host": host}

    def _cmd(self, cmd):
        iface = self._get_iface()
        return "%s\t\t%s" % (iface['host'], iface['ip'])


if __name__ == '__main__':
    f = Server()
    f.start()
