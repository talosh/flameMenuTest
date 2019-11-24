# flameMenuTest
A set of python scripts to test potential "over 164 items" python custom actions menu bug in Autodesk Flame 2020

There seem to be a bug in Autodesk Flame 2020.1 and 2020.2 when total number of items in 
custom menu is over 164. It resets index of methonds list and on menu item 165 the first method is called and so on.
There is possible workaround with loading custom actions through the wrapper and shifting names against actions by 
adding bogus non-visible menu items (see workaround_concept folder)
