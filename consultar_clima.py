
import json
from observacion import Observacion_Clase


def cargar_observaciones(ruta):
    lista_observaciones = []

    with open(ruta, "r") as archivo:
        registros = json.load(archivo)

    for registro in registros:
        try:
            nueva_observacion = Observacion_Clase(
                registro["estacion"],
                registro["hora"],
                registro["temperatura"],
                registro["humedad"],
                registro["velocidad_viento"],
                registro["presion"]
            )
        except ValueError:
            continue

        lista_observaciones.append(nueva_observacion)

    return lista_observaciones

def filtrar_por_estacion(lista_observaciones, estacion):
    resultado = []

    for dato in lista_observaciones:
        if dato.es_de_estacion(estacion):
            resultado.append(dato)

    return resultado



def resumir_temperaturas(lista_observaciones):
    cantidad = len(lista_observaciones)

    minima = None
    maxima = None

    suma = 0

    for dato in lista_observaciones:
        suma = suma + dato.temperatura
    
        if minima is None:
            minima = dato
        elif dato.temperatura < minima.temperatura:
            minima = dato


        if maxima is None:
            maxima = dato
        elif dato.temperatura > maxima.temperatura:
            maxima = dato

    promedio = suma / cantidad

    return {
        "cantidad": cantidad,
        "minima": minima,
        "maxima": maxima,
        "promedio": promedio
    }
