from enum import Enum

class Resultados(Enum):
    TAREA_AGREGADA = 1
    TAREA_YA_EXISTE = 2
    TAREA_COMPLETADA = 3
    TAREA_YA_COMPLETADA = 4
    TAREA_QUITADA = 5
    TAREA_NO_ENCONTRADA = 6
    NUMERO_INVALIDO = 7
    NINGUNA_TAREA = 8
    NINGUNA_ENTRADA = 9
    OPCION_INVALIDA = 10