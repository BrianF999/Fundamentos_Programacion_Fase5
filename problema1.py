# =================================================================
# Evaluación Final POA - Fase 5
# Problema 1: Nivel de compromiso de sesiones de clientes
# =================================================================

# Módulo (Función) para calcular la clasificación de compromiso
def clasificar_compromiso(duracion, clics):
    """
    Evalúa el nivel de compromiso basado en la duración en segundos y la cantidad de clics.
    """
    # Lógica de Negocio: Clasificar como "Alto" (si Duración > 180s y Clics > 8)
    if duracion > 180 and clics > 8:
        return "Alto"
    # Lógica de Negocio: Clasificar como "Bajo" (si Duración < 60s o Clics < 3)
    elif duracion < 60 or clics < 3:
        return "Bajo"
    # Lógica de Negocio: Clasificar como "Medio" en todos los demás casos
    else:
        return "Medio"

def main():
    # Datos Iniciales: Una matriz con al menos 5 filas de datos
    # Formato: [ID Cliente, Duración (segundos), Eventos Clics]
    sesiones_clientes = [
        [101, 200, 10],  # Cumple >180s y >8 clics -> Alto
        [102, 45, 5],    # Cumple <60s -> Bajo
        [103, 120, 5],   # No cumple extremos -> Medio
        [104, 300, 2],   # Cumple <3 clics -> Bajo
        [105, 190, 9]    # Cumple >180s y >8 clics -> Alto
    ]

    print("========================================")
    print(" INFORME DE COMPROMISO DE CLIENTES")
    print("========================================")
    print(f"{'ID Cliente':<15} | {'Clasificación Final'}")
    print("-" * 40)

    # Recorrer la matriz para generar el informe
    for sesion in sesiones_clientes:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamado a la función para obtener la clasificación
        clasificacion = clasificar_compromiso(duracion, clics)
        
        # Salida: Generar un informe listando el ID del cliente y su clasificación final
        print(f"{id_cliente:<15} | {clasificacion}")
        
    print("========================================")
    
    # -----------------------------------------------------------------
    # LÍNEA AGREGADA: Esta función congela la consola de Windows
    # para evitar que se cierre automáticamente al terminar el programa.
    # -----------------------------------------------------------------
    input("\nPresiona la tecla ENTER para cerrar el informe...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()