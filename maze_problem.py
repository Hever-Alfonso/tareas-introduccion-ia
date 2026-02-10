# ============================================================
# Maze_problem.ipynb (CÓDIGO BASE DEL PROFESOR)
# NO MODIFICADO: solo con comentarios/pistas resaltadas
# ============================================================

import heapq  # El módulo heapq implementa colas de prioridad (heaps)


class Node:
    def __init__(self, position, parent=None, path_cost=0):  # TODO (PROF): AGREGAR ACTION
        # position: la coordenada (x, y) o (fila, columna) del robot en el maze
        self.position = position

        # parent: referencia al nodo anterior (sirve para reconstruir el camino)
        self.parent = parent

        # path_cost: costo acumulado hasta llegar a este nodo
        self.path_cost = path_cost

        # TODO (PROF): AGREGAR ACTION
        # Te falta guardar la acción tomada para llegar a este nodo:
        # por ejemplo: "UP", "DOWN", "LEFT", "RIGHT"
        # Esto permite luego "trackear" movimientos al reconstruir el camino.

    def __lt__(self, other):
        # Esto define cómo se comparan dos nodos en el heap.
        # Actualmente compara por path_cost.
        return self.path_cost < other.path_cost


class Problem:
    # TODO (PROF): DEFINA la Class problem como lo considere necesario,
    # puede basarse del ejemplo de Bucharest.
    #
    # Esta clase debería (según el enunciado) representar la estructura del problema:
    # - state (la posición del robot)
    # - actions(state)
    # - result(state, action)
    # - action_cost(state, action, next_state)
    #
    # En el código base AÚN NO ESTÁ DEFINIDA.
    pass


def find_exit(maze):
    start = (1, 1)  # Posición inicial basado en la documentación suministrada
    end = (1, 6)    # Posición de la salida basado en la documentación suministrada

    # TODO (PROF): DEFINA el conjunto de actions posibles
    # Pista del enunciado: (Up, Down, Right, Left) NO diagonales.
    # Normalmente se define algo como:
    # actions = { (delta_x, delta_y): "NOMBRE_ACCION" } o similar.

    problem = Problem()  # TODO (PROF): COMPLETE LA DEFINICIÓN DEL OBJETO
    # También: ADAPTELO EN LOS PUNTOS QUE LO REQUIERAN.

    def manhatan_distance(pos, goal):
        # Heurística Manhattan: distancia usando movimiento horizontal/vertical
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def get_neighbors(pos):
        # TODO (PROF): ESTA FUNCIÓN DEBERIA AJUSTARSE PARA HACER TRACKING DE MOVIMIENTOS
        # (Up, Down, Right, Left)
        #
        # En el código actual, solo devuelve posiciones vecinas, pero no registra
        # cuál acción llevó a cada vecino.
        neighbors = []
        for move in [x for x in problem.actions.keys()]:
            # Nota: esto asume que problem.actions existe y es un diccionario
            # donde las llaves son movimientos (dx, dy) o similares.
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if maze[neighbor[0]][neighbor[1]] != "#":
                # Si el vecino NO es pared, lo agrega
                # (Aquí el notebook original tiene un problema de indentación / duplicación)
                neighbors.append(neighbor)
              neighbors.append(neighbor)  # <- esta línea está tal cual en el original (ojo: indentación)
        return neighbors

    start_node = Node(start, path_cost=0)

    # OJO: aquí se usa "goal" pero arriba se definió "end".
    # En el notebook original aparece así.
    frontier = [(manhatan_distance(start, goal), start_node)]

    heapq.heapify(frontier)  # Convierte frontier en una cola de prioridad (heap)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)

        # OJO: aquí también se usa "goal" (no definido arriba en el original)
        if node.position == goal:
            return reconstruct_path(node)

        for neighbor in get_neighbors(node.position):
            new_cost = node.path_cost + 1  # costo uniforme de 1 por movimiento (según enunciado)

            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, path_cost=new_cost)

                # aquí se usa "end" (sí existe arriba)
                heapq.heappush(frontier, (manhatan_distance(neighbor, end), reached[neighbor]))

    return None  # No se encontró salida


def reconstruct_path(node):
    # TODO (PROF): AJUSTAR PARA QUE, ADEMÁS DE POSICIONES, MUESTRE ACCIONES TOMADAS
    #
    # Actualmente reconstruye solo lista de posiciones usando "parent".
    # Para acciones necesitas que Node guarde "action" (ver TODO en Node).
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    path.reverse()
    return path


# ============================================================
# Ejecución (tal cual venía en el notebook)
# ============================================================

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", "#", " ", "#", " ", "E", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

path = find_exit(maze)
if path:
    print("Ruta encontrada:", path)
else:
    print("No se encontró una ruta a la salida.")