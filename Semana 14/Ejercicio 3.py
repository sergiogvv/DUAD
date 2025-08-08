# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

def depth_node(node):
    if node is None:
        return 0
    return 1 + max(depth_node(node.left), depth_node(node.right))


class Node: #nodo tipo subarbol
    data: str
    left: "Node"
    right: "Node"
    

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Binary_Tree:
    root: Node
    level = 0

    def __init__(self, root_node):
        self.root = root_node

    @property
    def Tree_Depth(self):
        return depth_node(self.root)


    def add_node(self, new_node):
        self._insert_evenly(self.root, new_node)

    def _insert_evenly(self, current_node, new_node):
        if current_node.left is None:
            current_node.left = new_node
        elif current_node.right is None:
            current_node.right = new_node
        else:
            if depth_node(current_node.left) <= depth_node(current_node.right): #si rama izquierda es menos profunda igual entonces...
                self._insert_evenly(current_node.left, new_node) #insertar nodo en rama izquierda
            else:
                self._insert_evenly(current_node.right, new_node) #sino insertar nodo en rama derecha


    def print_structure(self):
        print("Tree Structure:")
        self._print_subtree(self.root)
        print(f"\nTree Depth: {self.Tree_Depth}")

        
    def _print_subtree(self, node, pre_char="", is_right=True):
            if node is not None:
                connector = "└── "
                print(pre_char + connector + node.data)
                if is_right:
                    new_pre_char = pre_char + "│   "
                else:
                    new_pre_char = pre_char + "    "
                self._print_subtree(node.right, new_pre_char, True) #nodos derechos se imprimen abajo
                self._print_subtree(node.left, new_pre_char, False) #nodos izquierdos se imprimien arriba




bonzai = Node("A",Node("B"),Node("C"))
level_bonzai = depth_node(bonzai)
print(level_bonzai)
print()


tree = Binary_Tree(Node("A"))
tree.add_node(Node("B"))
tree.add_node(Node("C"))
tree.add_node(Node("D"))
tree.add_node(Node("E"))
tree.add_node(Node("F"))
tree.add_node(Node("G"))
tree.add_node(Node("H"))
# tree.add_node(Node("I"))
# tree.add_node(Node("I"))

tree.print_structure()






















