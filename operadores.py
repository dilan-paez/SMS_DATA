import requests, json
from pymongo import MongoClient

# Clase para capturar y limpiar datos
class capture:

    proveedor_2 = []  # Lista para almacenar proveedores

    def __init__(self):
        self.dataJson = []  # Inicializa la lista de datos en formato JSON

    # Método para capturar datos de la API
    def captura(self):
        datos = requests.get('https://www.datos.gov.co/resource/m5pi-7cau.json')  # Solicita los datos de la API
        self.dataJson = datos.json()  # Convierte la respuesta en JSON

    # Método para limpiar los datos
    def limpieza(self):
        for ind in range(len(self.dataJson)):
            jsonClean = {
                "Year": "",  # Inicializa el año
                "Quarter": "",  # Inicializa el trimestre
                "Provider": "",  # Inicializa el proveedor
                "Income": ""  # Inicializa los ingresos
            }
            # Mapea el proveedor original a uno limpio
            if self.dataJson[ind]['proveedor'] == "ALMACENES EXITO INVERSIONES S.A.S.":
                jsonClean['Provider'] = "MOVIL EXITO"
            elif self.dataJson[ind]['proveedor'] == "AVANTEL S.A.S":
                jsonClean['Provider'] = "WOM"
            elif self.dataJson[ind]['proveedor'] == "VIRGIN MOBILE COLOMBIA S.A.S.":
                jsonClean['Provider'] = "VIRGIN MOBILE"
            elif self.dataJson[ind]['proveedor'] == "SUMA MOVIL S.A.S.":
                jsonClean['Provider'] = "SUMA MOVIL"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA MOVIL  S.A ESP":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "LOGISTICA FLASH COLOMBIA S.A.S":
                jsonClean['Provider'] = "FLASH"
            elif self.dataJson[ind]['proveedor'] == "COMUNICACION CELULAR S A COMCEL S A":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP":
                jsonClean['Provider'] = "ETB"
            elif self.dataJson[ind]['proveedor'] == "SETROC MOBILE GROUP SAS":
                jsonClean['Provider'] = "SETROC"
            elif self.dataJson[ind]['proveedor'] == "PARTNERS TELECOM COLOMBIA SAS":
                jsonClean['Provider'] = "PARTNERS"
            elif self.dataJson[ind]['proveedor'] == "LIWA SAS ESP":
                jsonClean['Provider'] = "LIWA"
            elif self.dataJson[ind]['proveedor'] == "LOV TELECOMUNICACIONES SAS":
                jsonClean['Provider'] = "LOV"
            elif self.dataJson[ind]['proveedor'] == "UFF MOVIL SAS":
                jsonClean['Provider'] = "UFF"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA TELECOMUNICACIONES S.A. E.S.P.":
                jsonClean['Provider'] = "MOVISTAR"

            # Asigna el año y el trimestre de los datos originales
            jsonClean['Year'] = self.dataJson[ind]['anno']
            jsonClean['Quarter'] = self.dataJson[ind]['trimestre']
            jsonClean['Income'] = self.dataJson[ind]['ingresos_por_mensajes']
            print(jsonClean)  # Imprime el JSON limpio

    # Método para guardar datos en MongoDB
    def savedata(self, jsonClean):
        self.collection.insert_one(jsonClean)  # Inserta el documento en la colección
        print(f"Datos guardados en MongoDB: {jsonClean}")  # Mensaje de confirmación

    # Método de prueba
    def impresion(self):
        print("hello")  # Imprime un saludo






































































































































































































prueba=capture()
prueba.captura()
prueba.limpieza()