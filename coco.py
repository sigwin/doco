#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mod.app import srvApp
from mod.runner import AppDaemonRunner


def _main():
    app = srvApp()
    daemon_runner = AppDaemonRunner(app)
    if not app.foreground:
        daemon_runner.do_action()
    else:
        app.run()

if __name__ == "__main__":
    _main()
