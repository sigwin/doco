# -*- coding: utf-8 -*-
"""
/usr/local/lib/python3.4/dist-packages/daemon/runner.py
try:
    self.daemon_context.stdout = open(app.stdout_path, 'w+t')
except ValueError:
    self.daemon_context.stdout = open(app.stdout_path, 'w+b', buffering=0)
try:
    self.daemon_context.stderr = open(
        app.stderr_path, 'w+t', buffering=0)
except ValueError:
    self.daemon_context.stderr = open(
        app.stderr_path, 'w+b', buffering=0)
"""

import sys
from daemon import runner


class AppDaemonRunner(runner.DaemonRunner):
    def __init__(self, app):
        self._app = app
        self.detach_process = True
        runner.DaemonRunner.__init__(self, app)

    def parse_args(self, argv=None):
        import getopt

        try:
            opts, args = getopt.getopt(sys.argv[1:],
                                       'skrf',
                                       ['start', 'kill', 'foreground'])
        except getopt.GetoptError:
            print((sys.exc_info()))
            print('getopt error...')
            sys.exit(2)

        self.action = ''
        for opt, arg in opts:
            if opt in ('-s'):
                self.action = 'start'

            elif opt in ('-k'):
                self.action = 'stop'

            elif opt in ('-r'):
                self.action = 'restart'

            elif opt in ('-f', '--foreground'):
                self.detach_process = False
                self._app.stdout_path = '/dev/tty'
                self._app.stderr_path = '/dev/tty'
                self._app.foreground = True

            else:
                print('show usage')
                sys.exit(2)

        if not self.action:
            print(sys.argv[0] + ' -s|-k|-r\n-s\tstart\n-k\tstop\n-r\trestart')
            sys.exit(1)

    def do_action(self):
        try:
            runner.DaemonRunner.do_action(self)
        except runner.DaemonRunnerStopFailureError as e:
            print(e)
