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

import os

# See terminal_lib.Window.py for more details about how this class works
class TerminalWindow(Window):
    __gtype_name__ = "TerminalWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(TerminalWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutTerminalDialog
        self.PreferencesDialog = PreferencesTerminalDialog

        # Code for other initialization actions should be added here.
        net_status = "KO :("
        net_address = "Desconocida"
        try:
            import netifaces
            address = netifaces.ifaddresses('eth0') 
            net_address = address[2][0]['addr']
            net_status = "OK"
        except:
            print "No hemos podido acceder a la conf de red"
        self.ui.label_net_status.set_text("Estado de la RED: %s \nDirección IP:%s"%(net_status,net_address))
    #Señales
    def button_connect_clicked_cb(self,widget):
        print "Ha hecho click en conectar"
        print os.system('/usr/local/bin/rdesktop')
    def button_reboot_clicked_cb(self,widget):
        print "Ha hecho click en reiniciar"
        print os.system('/sbin/shutdown -r now')
        
