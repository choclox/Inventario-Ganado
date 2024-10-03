class ganado():
    def __init__(self,id_animal=None,raza:str =None,fecha_ingreso=None,fecha_salida=None,peso=None,sexo=None,marca=None,numero=None):
        self._id_animal = id_animal
        self._numero = numero
        self._marca = marca
        self._raza = raza
        self._peso = peso
        self._sexo = sexo
        self._fecha_ingreso = fecha_ingreso 
        self._fecha_salida = fecha_salida
    
    @property
    def id_animal(self):
        return self._id_animal
    
    @id_animal.setter
    def id_animal(self,id_animal):
        self._id_animal = id_animal
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self,numero):
        self._numero = numero
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    
    @property
    def raza(self):
        return self._raza
    
    @raza.setter
    def raza(self,raza):
        self._raza = raza
    
    @property
    def peso(self):
        return self._peso
    
    @numero.setter
    def peso(self,peso):
        self._peso = peso
        
    @property
    def sexo(self):
        return self._sexo
    
    @numero.setter
    def sexo(self,sexo):
        self._sexo = sexo