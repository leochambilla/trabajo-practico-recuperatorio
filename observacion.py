class Observacion_Clase:

    def __init__(self, estacion, hora, temperatura, humedad, velocidad_viento ,presion ):
        self.estacion = estacion

        self.presion = presion
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.velocidad_viento = velocidad_viento

        if estacion == "":
            raise ValueError("La estación no puede estar vacía")

        if hora < 0 or hora > 23:
            raise ValueError("La hora está fuera de rango")

        if temperatura is None:
            raise ValueError("Falta la temperatura")

        if humedad is None:
            raise ValueError("Falta la humedad")

        if humedad < 0 or humedad > 100:
            raise ValueError("La humedad no cumple los límites")

        if velocidad_viento is None:
            raise ValueError("Falta la velocidad del viento")

        if velocidad_viento < 0:
            raise ValueError("La velocidad del viento no puede ser negativa")

    def es_de_estacion(self, estacion):
        return self.estacion == estacion

    def intensidad_viento(self):
        if self.velocidad_viento < 2:
            return "calma"
        elif self.velocidad_viento < 20:
            return "leve"
        elif self.velocidad_viento < 40:
            return "moderado"
        else:
            return "fuerte"
        
    def mostrar_observacion(self):
        return (f"{self.estacion} | {self.hora} h | {self.temperatura} °C | {self.humedad} % | {self.velocidad_viento}km/h ({self.intensidad_viento()})")

    