"""Return vs Print"""

def foo(x: int)-> int:
    print(f"{x} is my favorite number")
    return x

y: int = foo(7)
print(y)

def foo(x:int) -> bool:
    return True
    
def foo(x: int, y:int )-> str:
    return "hello"

y: int = foo(7,10)
print(y)