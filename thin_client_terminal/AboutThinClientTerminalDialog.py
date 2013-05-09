# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gtk

from thin_client_terminal.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('thin-client-terminal')

class AboutThinClientTerminalDialog(gtk.AboutDialog):
    __gtype_name__ = "AboutThinClientTerminalDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AboutThinClientTerminalDialog object.
        """
        builder = get_builder('AboutThinClientTerminalDialog')
        new_object = builder.get_object("about_thin_client_terminal_dialog")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initalizing should be called after parsing the ui definition
        and creating a AboutThinClientTerminalDialog object with it in order to
        finish initializing the start of the new AboutThinClientTerminalDialog
        instance.
        
        Put your initialization code in here and leave __init__ undefined.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)

        # Code for other initialization actions should be added here.


if __name__ == "__main__":
    dialog = AboutThinClientTerminalDialog()
    dialog.show()
    gtk.main()
