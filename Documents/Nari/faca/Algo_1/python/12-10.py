from queue import LifoQueue
from queue import Queue

pila = LifoQueue()
print(pila.empy)
pila.put(1)
pila.put(2)
pila.put(3)
print(pila.empty())

cola = Queue()
cola.put(1)


