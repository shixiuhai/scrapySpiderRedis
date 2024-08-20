from enum import Enum

class WarnType(Enum):
    def __new__(cls, type:int, name:str, message:str):
        # Create a new instance of the enum
        obj = object.__new__(cls)
        # obj._value_ = type
        obj.display_type=type
        obj.display_name = name  
        obj.display_message = message 
        return obj

    SEX = (1, "色情", "色情描述")
    FIRE = (2, "火焰", "火焰描述")

    
    @property
    def name(self):
        # Override the name property to return the custom display name
        return self.display_name
    
    @property
    def type(self):
        # Override the value property to return the type value
        return self.display_type
    
    @property
    def message(self):
        # Override the message property to return the message
        return self.display_message

    @classmethod
    def get_type(cls, name):
        for warnTypeItem in cls:
            if warnTypeItem.name == name:
                return warnTypeItem.type  # 返回type值
            
print(WarnType.FIRE.name)
print(WarnType.FIRE.type)
print(WarnType.FIRE.message)
print(WarnType.get_type("火焰"))



class WarnTypeTwo(Enum):
    def __new__(cls, type:int, name:str):
        # Create a new instance of the enum
        obj = object.__new__(cls)
        # obj._value_ = type
        obj.display_type=type
        obj.display_name = name  
        return obj

    SEX = (1, "色情")
    FIRE = (2, "火焰")

    
    @property
    def name(self):
        # Override the name property to return the custom display name
        return self.display_name
    
    @property
    def type(self):
        # Override the value property to return the type value
        return self.display_type
    

    @classmethod
    def get_type(cls, name):
        for warnTypeItem in cls:
            if warnTypeItem.name == name:
                return warnTypeItem.type  # 返回type值
            
print(WarnTypeTwo.FIRE.name)
print(WarnTypeTwo.get_type(WarnTypeTwo.FIRE.name))
            
