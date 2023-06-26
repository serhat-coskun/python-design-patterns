from abc import abstractmethod, ABC
from typing import Any



class CommonInterface(ABC):
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
    

class Core(CommonInterface):
    
    def execute(self, value: Any)-> Any:
        print("Core: processing...")
        return value

class LoggingDecorator(CommonInterface):
    
    def __init__(self, object: CommonInterface) -> None:
        self._wrappe = object
    
    def execute(self, value: Any)-> Any:
        val = self._wrappe.execute(value)
        print(f"Executed execute({value}) returned {val}")
        return val



class CachingDecorator(CommonInterface):
    
    def __init__(self, object: CommonInterface) -> None:
        self._wrappe = object
        self._cache = dict()
    
    def execute(self, value: Any)-> Any:
        val = None
        if value in self._cache:
            val =  self._cache[value]
            print(f"Cache hit execute({value})")

        else:
            val = self._wrappe.execute(value)
            self._cache[value] = val
            print(f"Cache miss execute({value})")
   
        return val
    


obj = Core()

print("Undecorated form!")
obj.execute(1)

print("Decorated with logging decorator!")
obj = LoggingDecorator(obj)
obj.execute(1)
obj.execute(2)


print("Also decorated with cache decorator!")
obj = CachingDecorator(obj)
obj.execute(1)
obj.execute(2)
obj.execute(1)

