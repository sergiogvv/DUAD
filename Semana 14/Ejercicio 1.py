# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        if self.head:
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data, end=" -> ") 
                current_node = current_node.next
            print(current_node.data)
        else:
            print("Estructura de datos vacía")

    def push(self, new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node
        print(f'\nPUSH: {new_node.data}')

    def pop(self):
        if self.head:
          print(f'\nPOP: {self.head.data}')
          self.head = self.head.next
        else:
          print("Estructura de datos vacía")


print("Init stack")
first_node = Node("Hola")
my_stack = Stack(first_node)
my_stack.print_structure() 

second_node = Node("Mundo")
my_stack.push(second_node)
my_stack.print_structure()

third_node = Node("3er nodo")
my_stack.push(third_node)
my_stack.print_structure()

my_stack.pop()
my_stack.print_structure()

my_stack.pop()
my_stack.print_structure()

my_stack.pop()
my_stack.print_structure()