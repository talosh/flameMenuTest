import os
from sgtk.platform.qt import QtGui

from pprint import pprint

class menuAction(object):
    def __init__(self):
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.mbox = QtGui.QMessageBox()
    
    def __getattr__(self, name):
        def method(*args, **kwargs):
            self.mbox.setText(name)
            self.mbox.exec_()
        return method

    def build_menu(self, number_of_menu_itmes):
        menu = {'name': self.name, 'actions': []}
        for i in xrange(1, number_of_menu_itmes+1):
            menu['actions'].append({
                'name': 'Menu Item ' + str(i),
                'execute': getattr(self, self.name + '_menu_item_' + str(i))
            })
        return menu

app = menuAction()

def get_media_panel_custom_ui_actions():
    return app.build_menu(100)
    