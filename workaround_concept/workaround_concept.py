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
                'execute': getattr(self, 'menu_item_' + str(i))
            })
        return menu
    
    def dummy(self, *args, **kwargs):
        self.mbox.setText('Dummy')
        self.mbox.exec_()

app = menuAction()

def get_media_panel_custom_ui_actions():
    original_menu = app.build_menu(400)
    modified_menu = dict(original_menu)
    action_names = []
    action_methods = []
    for action in original_menu['actions']:
        action_names.append(action['name'])
        action_methods.append(action['execute'])

    modified_menu['actions'] = []
    for i in xrange(len(action_names) + 164):
        if i < 164:
            modified_menu['actions'].append({
                'name': 'Dummy ' + str(i),
                'isVisible': False,
                'execute': action_methods[i]
                })
        elif i in range(164, len(action_names)):
            modified_menu['actions'].append({
                'name': action_names[i-164],
                'execute': action_methods[i]
                })
        else:
            modified_menu['actions'].append({
                'name': action_names[i-164],
                'execute': app.dummy
                })

    return modified_menu