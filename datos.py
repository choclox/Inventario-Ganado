from ejemplos import ganado
from datetime import date
import pandas as pd


class manejo_datos:
    def __init__(self,ganado):
        self.len = len(ganado)
        self._values = pd.DataFrame(ganado)
        self.ids = self._values["id"]
        self.Edad()
        self.cantidades()
        self.Promedios()
        self.filtros(["-Seleccionar-" for x in range(9) ])
        """"id": 1, "Marca": "M001", "Nacimiento": "2018-05-12", "Sexo": "Hembra", "Peso": 450, "Raza": "Holstein", "Estado_Salud": "Saludable", "Condicion_Corporal": "Adecuado", "Corral": 3"""
    
    def convertir_a_int(self, diccionario):
        return {str(k): int(v) for k, v in diccionario.items()}

    def cantidades(self):
        self.marcas = self.convertir_a_int(dict(self._values["Marca"].value_counts()))
        self.sexos = self.convertir_a_int(dict(self._values["Sexo"].value_counts()))
        self.razas = self.convertir_a_int(dict(self._values["Raza"].value_counts()))
        self.salud = self.convertir_a_int(dict(self._values["Estado_Salud"].value_counts()))
        self.condicion = self.convertir_a_int(dict(self._values["Condicion_Corporal"].value_counts()))
        self.corrales = self.convertir_a_int(dict(self._values["Corral"].value_counts()))
        self.edades = self.convertir_a_int(dict(self._values["Edad"].value_counts()))
        
    def muestra(self):
        
        dato = ["Animales","Machos","Hembras","Peso Promedio","P. Medio Machos","P. Medio Hembras","Saludables","Heridos","Enfermos"]
        cantidades = [self.len,self.sexos["Macho"],self.sexos["Hembra"],self.peso_promedio,self.pesoP_machos,self.pesoP_hembras,self.salud["Saludable"],self.salud["Herido"],self.salud["Enfermo"]]
        cantidades = [int(valor) for valor in cantidades]
        return dato , cantidades
        #return self.len + list(self.sexos.items()) + self.peso_promedio + self.pesoP_machos + self.pesoP_hembras + list(self.salud.items())

    def Promedios(self):
       self.peso_promedio = self._values["Peso"].mean()
       self.edad_promedio = self.edadesdf["Edad"].mean()
       self.pesoP_machos = self._values["Peso"][self._values["Sexo"]=="Macho"].mean()
       self.pesoP_hembras = self._values["Peso"][self._values["Sexo"]=="Hembra"].mean()

    def Edad(self):
        edades = []
        for fecha in self._values["Nacimiento"]:
            fecha_nacimiento = date.fromisoformat(fecha)
            edad = date.today() - fecha_nacimiento
            edades.append(edad.days // 365)
        self.edadesdf = pd.DataFrame(zip(self.ids,edades))
        self.edadesdf.columns = ["id","Edad"]
        self._values = self._values.merge(self.edadesdf,on="id")
        columnas_ordenadas = ["id", "Marca", "Edad", "Nacimiento", "Sexo", "Peso", "Raza", "Estado_Salud", "Condicion_Corporal", "Corral"]
        self._values = self._values[columnas_ordenadas]

    def filtros(self,lista_filtros):
        for index,filtro in enumerate(lista_filtros):
            if filtro == "-Seleccionar-" or filtro == "":
                lista_filtros[index] = None
        marca,peso,edad,año,raza,sexo,salud,Ccorporal,corral = lista_filtros
        self._values_filtrados = self._values
        # Filtra por marca si está definido
        if marca != None:
            print(f"Filtrando por Marca: {marca}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Marca"].str.startswith(marca)]
            print(f"Después del filtro de Marca: {self._values_filtrados.shape}")

        if peso != None:
            if "-" in str(peso):
                menor, mayor = str(peso).split("-")
                print(f"Filtrando por Peso: entre {menor} y {mayor}")
                self._values_filtrados = self._values_filtrados[
                    (self._values_filtrados["Peso"] >= int(menor)) & 
                    (self._values_filtrados["Peso"] <= int(mayor))
                ]
            print(f"Después del filtro de Peso: {self._values_filtrados.shape}")

        if edad != None:
            print(f"Filtrando por Edad: {edad}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Edad"] == int(edad)]
            print(f"Después del filtro de Edad: {self._values_filtrados.shape}")

        if año != None:
            print(f"Filtrando por Año: {año}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Nacimiento"].str.startswith(año)]
            print(f"Después del filtro de Año: {self._values_filtrados.shape}")

        if raza != None:
            print(f"Filtrando por Raza: {raza}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Raza"] == raza]
            print(f"Después del filtro de Raza: {self._values_filtrados.shape}")

        if sexo != None:
            print(f"Filtrando por Sexo: {sexo}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Sexo"] == sexo]

        if salud != None:
            print(f"Filtrando por Sexo: {salud}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Estado_Salud"] == salud]
            
        if Ccorporal != None:
            print(f"Filtrando por Sexo: {Ccorporal}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Condicion_Corporal"] == Ccorporal]
        
        if corral != None:
            print(f"Filtrando por Sexo: {corral}")
            self._values_filtrados = self._values_filtrados[self._values_filtrados["Corral"] == int(corral)]
        
        return self._values_filtrados.to_dict(orient="records")

    
    @property
    def values(self):
        return self._values.to_dict(orient="records")
    
    @property
    def values_filtrados(self):
        return self._values_filtrados.to_dict(orient="records")
    
    @property
    def keys(self):
        return self._values.columns
    
    
    
if __name__ == "__main__":
        
    """values = tuple(zip(*(animal.values() for animal in ganado)))
    print(values[0])"""
    
    manejo = manejo_datos(ganado)
    print(manejo.marcas)  # {'M001': 1, 'M002': 1, 'M003': 1}
    print(manejo.sexos)   # {'Hembra': 2, 'Macho': 1}
    print(manejo.razas)   # {'Holstein': 2, 'Angus': 1}
    print(manejo.salud)   # {'Saludable': 2, 'Enfermo': 1}
    print(manejo.condicion)  # {'Adecuado': 2, 'Regular': 1}
    print(manejo.corrales)   # {3: 2, 4: 1}
    print(manejo.edades)
    print(manejo.values)
    print(manejo.values_filtrados)
    lista_filtros= ["", "-Seleccionar-", "-Seleccionar-", "-Seleccionar-", "-Seleccionar-","-Seleccionar-", "-Seleccionar-", "-Seleccionar-","-Seleccionar-"]
    print(manejo.filtros(lista_filtros))
    print(list(manejo.sexos.keys()))
    print(manejo.muestra())
    