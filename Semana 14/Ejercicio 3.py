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
        def _print(node, level):
            if node is not None:
                indent = "  " * level
                print(f"{indent}- {node.data}")
                _print(node.left, level + 1)
                _print(node.right, level + 1)

        print("Tree Structure:")
        _print(self.root, 0)
        print(f"\nTree Depth: {self.Tree_Depth}")


bonzai = Node("A",Node("B"),Node("C"))
level_bonzai = depth_node(bonzai)
print(level_bonzai)


tree = Binary_Tree(Node("A"))
tree.add_node(Node("B"))
tree.add_node(Node("C"))
tree.add_node(Node("D"))
tree.add_node(Node("E"))

tree.print_structure()






















