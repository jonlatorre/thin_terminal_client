# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('terminal')

from terminal_lib import Window
from terminal.AboutTerminalDialog import AboutTerminalDialog
from terminal.PreferencesTerminalDialog import PreferencesTerminalDialog

# See terminal_lib.Window.py for more details about how this class works
class TerminalWindow(Window):
    __gtype_name__ = "TerminalWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(TerminalWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutTerminalDialog
        self.PreferencesDialog = PreferencesTerminalDialog

        # Code for other initialization actions should be added here.

