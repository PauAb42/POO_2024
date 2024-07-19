class Usuario:
    def __init__ (self, nombre, direccion, tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel
    
    def info_usuario(self):
        print(f"El usuario es: {self.getNombre()}, su dirección es {self.getDireccion()} y su teléfono es: {self.getTel()}")

    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getTel(self):
        return self.tel
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def setDireccion(self, direccion):
        self.direccion=direccion

    def setTel(self, tel):
        self.tel=tel

class Cliente (Usuario):
    def __init__ (self, nombre, direccion, tel, num_cliente):
        super().__init__(nombre,direccion,tel)
        self.__num_cliente=num_cliente

    def info_usuario(self):
        print(f"El usuario #{self.getNum_cliente()} es el cliente {self.getNombre()}, su direccion es {self.getDireccion()} y su teléfono es: {self.getTel()}")

    def getNum_cliente(self):
        return self.__num_cliente
    
    def setNum_cliente(self, num_cliente):
        self.__num_cliente=num_cliente
    
class Empleado (Usuario):
    def __init__ (self, nombre, direccion, tel, num_empleado, salario, tipo):
        super().__init__(nombre, direccion, tel)
        self._salario=salario
        self._num_empleado=num_empleado
        self._tipo=tipo

    def info_usuario(self):
        print(f"El empleado #{self.getNum_empleado()} se llama: {self.getNombre()} y la direccion es {self.getDireccion()} y el telefono es: {self.getTel()}, tiene un salario de {self.getSalario()} y es de tipo {self.getTipo()}")
    
    def getNum_empleado(self):
        return self._num_empleado

    def getSalario(self):
        return self._salario

    def getTipo(self):
        return self._tipo
    
    def setSalario(self, salario):
        self._salario=salario

    def setNum_empleado(self, num_empleado):
        self._num_empleado=num_empleado

    def setTipo(self, tipo):
        self._tipo=tipo