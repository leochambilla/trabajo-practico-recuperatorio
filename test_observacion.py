from observacion import Observacion_Clase


def test_crear_observacion():
    observacion = Observacion_Clase(
        "AEROPARQUE AERO",
        8,
        12.5,
        80,
        10
    )

    assert observacion.estacion == "AEROPARQUE AERO"
    assert observacion.hora == 8
    assert observacion.temperatura == 12.5
import pytest
from observacion import Observacion_Clase


def test_crear_observacion():
    observacion = Observacion_Clase("AEROPARQUE AERO",8,12.5,80,10)

    assert observacion.estacion == "AEROPARQUE AERO"
    assert observacion.hora == 8
    assert observacion.temperatura == 12.5


def test_hora_invalida():
    with pytest.raises(ValueError):
        Observacion_Clase("AEROPARQUE AERO", 25, 12.5, 80, 10)