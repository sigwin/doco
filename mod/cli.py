# -*- coding: utf-8 -*-
from socket import *
import os

if os.path.exists("util.py"):
    from util import *
else:
    from mod.util import *
CONFIG = os.path.abspath(os.path.dirname(__file__))+"/../config.json"


class Client:
    def __init__(self):
        self.SETTING = get_config(CONFIG)
        self.buf = 8192
        try:
            host = os.uname()[1]
        except Exception:
            import sys
            print("Error: not found iface data")
            sys.exit(-1)

    def setup_socket(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.sock.bind(('', 0))

    def sendcmd(self, cmd=""):
        self.sock.sendto(cmd.encode('utf-8'),
                         ('255.255.255.255', self.SETTING['port']))
        self.sock.settimeout(1)
        while True:
            try:
                msg, address = self.sock.recvfrom(self.buf)
                print(msg.decode('utf-8'))
            except timeout:
                break
            except Exception as e:
                import sys
                print(e)
                sys.exit(-1)

    def close_socket(self):
        self.sock.close()
