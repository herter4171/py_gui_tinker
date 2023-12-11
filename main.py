import wx

#from db_wrapper import db_wrapper
from window import window

from ecr_fetcher import EcrFetcher
ecr_fetcher = EcrFetcher()

#db_wrap = db_wrapper()
#print("TABLE NAMES")
#[print(x) for x in db_wrap.table_names]

#print("\nMATERIAL_NAMES")
#[print(x) for x in db_wrap.material_names]

app = wx.App()
window(None, 'ECR Image Lookup GUI', ecr_fetcher)
app.MainLoop()