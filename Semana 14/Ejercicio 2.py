# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Double_Ended_Queue:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head = head
        self.tail = head

    def print_structure(self):
        if self.head:
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data, end=" -> ") 
                current_node = current_node.next
            print(current_node.data)
        else:
            print("Estructura de datos vacía")

    def _Tail(self,current_node):
        #recorrer estructura hacia la izquierda y asignar tail
        while current_node.next is not None:
            current_node = current_node.next
        self.tail = current_node


    def push_left(self, new_node):
        #agregar nodo al inicio
        current_node = self.head
        self.head = new_node
        self.head.next = current_node
        print(f'\nPUSH LEFT: {new_node.data}')


    def push_right(self, new_node):
        #recorrer estructura hacia la izquierda
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        #agregar nodo al final y asignar tail
        current_node.next = new_node
        self.tail = new_node
        print(f'\nPUSH RIGHT: {new_node.data}')

    def pop_left(self):
        #quitar nodo al inicio
        if self.head:
            print(f'\nPOP LEFT: {self.head.data}')
            self.head = self.head.next
            
            if self.head is not None: #si la estructura no esta vacia...
                self._Tail(self.head)
            else:
                self.tail = None # no hay tail si la estructura ya esta vacia
        else:
            print("Estructura de datos vacía")

    def pop_right(self):
        if self.head: #si la estructura no esta vacia...
            #...recorrer estructura hacia la izquierda 
            current_node = self.head
            if self.head.next is not None:
                while current_node.next is not self.tail:
                    current_node = current_node.next
                #quitar nodo al final y asginar tail
                print(f'\nPOP RIGHT: {current_node.next.data}')
                self.tail = current_node
                current_node.next = None
            else:
                print(f'\nPOP RIGHT: {current_node.data}')
                self.head = None # no hay head si la estructura ya esta vacia
        else:
            print("Estructura de datos vacía")


print("Init Double Ended Queue")
first_node = Node("Hola")
my_dbl_ended_q = Double_Ended_Queue(first_node)
my_dbl_ended_q.print_structure() 

second_node = Node("Mundo")
my_dbl_ended_q.push_right(second_node)
my_dbl_ended_q.print_structure()

third_node = Node("!")
my_dbl_ended_q.push_right(third_node)
my_dbl_ended_q.print_structure()

pre_first_node = Node("¡")
my_dbl_ended_q.push_left(pre_first_node)
my_dbl_ended_q.print_structure()

my_dbl_ended_q.pop_right()
my_dbl_ended_q.print_structure()

my_dbl_ended_q.pop_left()
my_dbl_ended_q.print_structure()

my_dbl_ended_q.pop_left()
my_dbl_ended_q.print_structure()

my_dbl_ended_q.pop_right()
my_dbl_ended_q.print_structure()
