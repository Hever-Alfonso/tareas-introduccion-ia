# --- CÓDIGO ORIGINAL VS MODIFICADO ---

def decidir_accion(entorno):
    # Lógica original
    if entorno == "amenaza":
        return "Defender"      # Acción ante peligro
    elif entorno == "recurso":
        return "Recolectar"    # Acción de beneficio
    
    # Lógica agregada (Modificación)
    elif entorno == "obstaculo":
        return "Saltar"        # NUEVO: Evita un bloqueo
    elif entorno == "tienda":
        return "Comprar"       # NUEVO: Intercambio de recursos
    
    # Acción por defecto
    else:
        return "Explorar"      # Busca nuevos entornos

# --- ENTRADA POR TERMINAL Y PRUEBA ---

# Solicita al usuario que ingrese un valor por terminal
dato_ingresado = input("Ingresa el tipo de entorno (amenaza, recurso, obstaculo, tienda): ").lower()

# Ejecuta la función y muestra el resultado
resultado = decidir_accion(dato_ingresado)
print(f"El agente ha decidido: {resultado}")

"""
PREGUNTAS DE LA ACTIVIDAD:

1. ¿Qué tan flexible es este agente?
Es rígido (basado en reglas). Solo entiende opciones exactas; 
si escribes algo parecido pero no igual, no sabe qué hacer.

2. ¿Cómo podrían hacerlo más sofisticado?
Integrando un sistema de recompensas (Aprendizaje por Refuerzo) 
o permitiendo que procese múltiples entradas (ej. entorno + nivel de energía).
"""