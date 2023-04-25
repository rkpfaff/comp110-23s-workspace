"""Identifying variables in the scope of the program of variable definition is crucial"""

"""Identifying Scope"""
lauren: str = "a friend"
def stranger() -> None:
    lauren: str = "a horse"
    print(lauren)

#>>> print(lauren)
#a friend
#>>> stranger()
#a horse
#>>> print(lauren)
#a friend

"""Accessing Global Names"""
def global_access() -> None:
    print(lauren)
    
#>>> global_access()
#"a friend"

"""Named Constants and Magic Numbers"""    
def compound(current: float) -> float:
    return current + (current * 0.009)

#float-literal 0.009 is a constant value AKA Magic Number in the program -> makes program more difficult to understand & are more work to change and maintain
#prefer Named Constants which is a global variable whose value is initialized and does not change at runtime (used in all caps w/ underscores)

INTEREST_RATE: float = 0.009

def compound(current: float) -> float:
    return current + (current * INTEREST_RATE)

"""Reassigning a Global Variable"""
lauren: str = "a friend"
def a_forceful_stranger() -> None:
    global lauren
    lauren = "MY HORSE"
    print(lauren)

#>>> print(lauren)
#a friend
#>>> a_forceful_stranger()
#MY HORSE
#>>> print(lauren)
#MY HORSE