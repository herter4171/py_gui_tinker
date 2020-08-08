import wx

from db_wrapper import db_wrapper
from window import window

db_wrap = db_wrapper()
#print("TABLE NAMES")
#[print(x) for x in db_wrap.table_names]

#print("\nMATERIAL_NAMES")
#[print(x) for x in db_wrap.material_names]

test_data = db_wrap.get_table_data_raw('Steel_Thermal_Conductivity')
app = wx.App()
window(None, 'Material Properties GUI', db_wrap)
app.MainLoop()