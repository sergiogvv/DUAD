from abc import ABC, abstractmethod

class Material(): # Cualquier objeto que se almacena en bodega es un material 
    status = "GOOD"
    def __init__(self,sap_code):
        self.sap_code = sap_code
    def scrap(self):
        self.status = "SCRAP"
    def print_properties(self):
        properties = {}
        properties['CODE'] = self.sap_code
        properties['STATUS'] = self.status
        print(properties)

class Machine(): #Maquina utilizada
    def __init__(self, machine_type):
        self.machine_type = machine_type
        

class Builder(): # Persona que fabrica un material en el proceso
    def __init__(self,builder_id):
        self.builder_id = builder_id


class Product(Material,Builder): #Producto final que consite de un material crudo, la persona que lo fabrica yla maquina utilizada. Hereda de Material, Builder y Machine
    def __init__(self, material, builder, machine):
        Material.__init__(self,material.sap_code)
        self.sap_code = self.sap_code.replace("R","P")
        Builder.__init__(self, builder.builder_id)
        self.sap_code += str(self.builder_id)
        Machine.__init__(self, machine.machine_type)
        self.sap_code += str(self.machine_type)

def warehouse_status(warehouse):
    print('A continuacion se muestran los bienes almacenados y su respectivo estado')
    for item in warehouse:
        item.print_properties()

# objetos que representan los recursos durante un turno dado en el proceso
operator_01 = Builder('168')
operator_02 = Builder('082')
press_a_01 = Machine("AU")
press_a_02 = Machine("MA")
raw_material_01 = Material("R255")
raw_material_02 = Material("R696")
raw_material_03 = Material("R343")

# productos terminados
finished_product_01 = Product(raw_material_01,operator_01, press_a_01)
finished_product_02 = Product(raw_material_02,operator_02,press_a_02)

#almecenamiento en bodega de materiales
warehouse_01 = [raw_material_01,raw_material_02,raw_material_03, finished_product_01, finished_product_02]

# revision de inventario
warehouse_status(warehouse_01)

