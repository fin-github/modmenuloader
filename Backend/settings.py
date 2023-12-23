from Backend.classes import *
from Backend.mods import *

class Settingsclass():
    def get_settings(self):
        return (
            # USE HERE!!!!!!!!!
            ModInfo(i=0, name="Example Name", desc="This is the description!", active=False, enable_func=null_func, disable_func=null_func),
            ModInfo(i=1, name="Example Name 2", desc="This is the description! 2", active=False, enable_func=null_func), # disable_func isnt required
            ModInfo(i=2, name="No Title", desc="Sets the CMD window title to nothing.", active=False, enable_func=Mods.notitle)
        )

Settings = Settingsclass()
