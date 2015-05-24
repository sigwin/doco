#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mod.cli import Client


def _main():
    c = Client()
    c.setup_socket()
    c.sendcmd("doco")
    c.close_socket()

if __name__ == "__main__":
    _main()
