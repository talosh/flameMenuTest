# flameMenuTest
scripts to test potential "over 164 items" python custom actions menu bug in Autodesk Flame 2020

There seem to be a bug in Autodesk Flame 2020.1 and 2020.2: when a total number of items in 
custom menu actions is over 164 wrong bound method is called. The correct method comes further down in
menu and is bound to wrong menu action. 
There might be a possible workaround with loading custom actions through the wrapper and adding bogus non-visible 
menu items
