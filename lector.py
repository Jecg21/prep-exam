def calcular_promedio(notas):
    """Calcula el promedio aritmético de una lista de notas numéricas.

    Argumentos:
    notas (list): Lista de enteros o flotantes con las calificaciones.

    Retorna:
    float: El promedio ponderado de las notas de la lista.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
