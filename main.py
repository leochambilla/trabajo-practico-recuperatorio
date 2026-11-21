
import sys
import consultar_clima


def main():
    ruta = sys.argv[1]
    estacion = sys.argv[2]

    # Cargar las observaciones válidas del JSON.
    observaciones = consultar_clima.cargar_observaciones(ruta)

    print(f"Observaciones válidas: {len(observaciones)}")
    print()

    # Filtrar las observaciones de la estación elegida.
    de_la_estacion = consultar_clima.filtrar_por_estacion(observaciones, estacion)
    horas = consultar_clima.hora_humedad(de_la_estacion)
    # Calcular el resumen de temperaturas.
    resumen = consultar_clima.resumir_temperaturas(de_la_estacion) 
    minima = resumen["minima"]
    maxima = resumen["maxima"]

    print(estacion)
    print(f"Observaciones: {resumen['cantidad']}")
    print(f"horas de humedad alta:  {horas}")
    print(f"Temperatura mínima: {minima.temperatura} °C "f"a las {minima.hora} h ")
    print(f"Temperatura máxima: {maxima.temperatura} °C "f"a las {maxima.hora} h")
    print(f"Temperatura promedio: {resumen['promedio']} °C")
    print()

    # Mostrar todas las observaciones de la estación.
    for observacion in de_la_estacion:
        print(observacion.mostrar_observacion())


main()
