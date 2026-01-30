"""
===========================================================
EJERCICIO VACUUM AGENT (2x2 con letras A, B, C, D)
Respuestas a los literales A, B y C dentro del mismo código
===========================================================

Grid (2x2):
    A   B
    C   D

Convención:
- Cada casilla puede estar "Clean" o "Dirty".
- El agente (aspiradora) está ubicado en una de las casillas: A, B, C o D.
- El agente percibe únicamente:
  1) Su ubicación (location)
  2) El estado de la casilla donde está (status)
- Con esa información decide una acción.

===========================================================
LITERAL A) Análisis del algoritmo
===========================================================

Tipo de agente:
- Agente reactivo simple (Simple Reflex Agent).

Justificación:
- El agente toma decisiones basándose únicamente en la percepción actual
  (ubicación y estado de la casilla).
- No tiene memoria, no planifica y no mantiene un modelo interno del mundo.

Política de decisión:
1) Si la casilla actual está sucia ("Dirty") → acción "Suck".
2) Si la casilla actual está limpia ("Clean") → el agente se mueve siguiendo
   una regla fija de recorrido.

Separación agente–entorno:
- El agente decide la acción.
- El entorno aplica los efectos de la acción (función de transición de estados).

===========================================================
LITERAL B) Número de estados posibles
===========================================================

Para un grid 2x2 hay 4 casillas: A, B, C y D.

Cada casilla puede estar en dos estados:
- Clean
- Dirty

Estados del mundo (sin incluir la posición del agente):
- 2^4 = 16 estados posibles.

Estados totales (incluyendo la posición del agente):
- El agente puede estar en 4 casillas distintas.
- 4 * 2^4 = 64 estados posibles.

Fórmula general para un grid m x n:
- Sea k = m * n (número de casillas).
- Estados del mundo: 2^k.
- Estados totales (mundo + agente): k * 2^k.

A continuación se incluye una función que calcula estos valores.
"""

def count_states(m, n):
    """
    Calcula los estados posibles para un grid m x n.
    Retorna:
    - estados_mundo: configuraciones de Clean/Dirty.
    - estados_totales: configuraciones incluyendo la posición del agente.
    """
    k = m * n
    estados_mundo = 2 ** k
    estados_totales = k * estados_mundo
    return estados_mundo, estados_totales


# Ejemplo para el caso 2x2 (literal B)
states_world_2x2, states_total_2x2 = count_states(2, 2)

print("LITERAL B (2x2)")
print("Estados del mundo:", states_world_2x2)
print("Estados totales:", states_total_2x2)
print()


"""
===========================================================
LITERAL C) Algoritmo y simulación para grid 2x2 con A, B, C, D
===========================================================

Acciones posibles:
- "Suck"
- "Left", "Right", "Up", "Down"

Estrategia del agente:
- Si la casilla está sucia, la limpia.
- Si está limpia, recorre el grid en un ciclo simple:
  A → B → D → C → A

La simulación mantiene la misma estructura original:
- Una función para el agente.
- Una función de simulación.
- Un ciclo for que representa el paso del tiempo.
"""

def action_vacuum_agent(location, status):
    """
    Agente reactivo simple para el mundo 2x2.
    location: 'A', 'B', 'C' o 'D'
    status: 'Clean' o 'Dirty'
    """

    if status == "Dirty":
        return "Suck"

    if location == "A":
        return "Right"
    elif location == "B":
        return "Down"
    elif location == "D":
        return "Left"
    elif location == "C":
        return "Up"


def simulate_vacuum_agent():
    """
    Simulación del entorno 2x2.
    El entorno aplica los efectos de cada acción decidida por el agente.
    """

    world = {
        "A": "Dirty",
        "B": "Dirty",
        "C": "Dirty",
        "D": "Dirty"
    }

    location = "A"
    actions = []

    for _ in range(10):
        status = world[location]
        action = action_vacuum_agent(location, status)
        actions.append(action)

        if action == "Suck":
            world[location] = "Clean"

        elif action == "Right":
            location = "B"
        elif action == "Down":
            location = "D"
        elif action == "Left":
            location = "C"
        elif action == "Up":
            location = "A"

    return actions, world


# Ejecución final del literal C
actions, final_world = simulate_vacuum_agent()

print("LITERAL C")
print("Acciones realizadas:", actions)
print("Estado final del mundo:", final_world)


"""
===========================================================
Nota adicional
===========================================================

La línea:
    actions, final_world = simulate_vacuum_agent()

funciona porque la función retorna dos valores:
    return actions, world

Python empaqueta estos valores en una tupla y luego los desempaqueta
automáticamente en las variables actions y final_world.
"""