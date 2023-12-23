def null_func():
    return
class ModInfo():
    def __init__(self, i, name:str, desc:str, active:bool, enable_func:object, disable_func:object=null_func):
        self.i=i
        self.name = name
        self.desc = desc
        self.active = active
        self.enable_func = enable_func
        self.disable_func = disable_func
