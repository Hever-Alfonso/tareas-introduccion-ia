"""
AQUÍ VA EL ENUNCIADO COMPLETO DEL WORD (PEGADO COMO COMENTARIO MULTILÍNEA)
Pégalo completo tal como te lo dieron en el documento.
"""

import heapq  # Cola de prioridad
import math   # Para sqrt en distancia euclidiana


# ============================================================
# CÓDIGO ORIGINAL DEL PROFESOR (NO SE MODIFICA)
# Lo dejamos comentado para mantener la integridad del código base.
# ============================================================

# (Aquí puedes pegar el código original si tu profesor exige verlo completo en el archivo)


# ============================================================
# SOLUCIÓN FUNCIONAL BASADA EN LA GUÍA (BestFirstSearch.ipynb)
# ============================================================

class Node:
    """
    Nodo de búsqueda (como en el ejemplo del profe).

    state      -> posición del robot (fila, columna)
    parent     -> nodo anterior (para reconstruir el camino)
    action     -> acción tomada para llegar aquí (UP/DOWN/LEFT/RIGHT)
    path_cost  -> costo acumulado desde el inicio
    """

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        # Comparación simple (el heap realmente usa la prioridad f)
        return self.path_cost < other.path_cost


class Problem:
    """
    Estructura del problema (como Bucharest).

    initial: estado inicial
    goal: meta
    actions(state): acciones válidas desde state
    result(state, action): nuevo estado
    action_cost(state, action, next_state): costo del movimiento
    is_goal(state): True si state es meta
    """

    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.result = result
        self.action_cost = action_cost
        self.is_goal = is_goal


def expand(problem, node):
    """
    Genera hijos del nodo (igual que el ejemplo del profe).
    """
    s = node.state
    for action in problem.actions(s):
        s_prime = problem.result(s, action)
        new_cost = node.path_cost + problem.action_cost(s, action, s_prime)
        yield Node(state=s_prime, parent=node, action=action, path_cost=new_cost)


def best_first_search(problem, f):
    """
    Best-First Search genérico (estructura del ejemplo del profe).
    Nosotros usaremos f = g + h para comportarse como A*.
    """
    start_node = Node(state=problem.initial)

    frontier = [(f(start_node), start_node)]  # (prioridad, nodo)
    heapq.heapify(frontier)

    reached = {problem.initial: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)

        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (f(child), child))

    return None


# ------------------------------------------------------------
# Funciones del MAZE
# ------------------------------------------------------------

def find_start_and_goal(maze):
    """
    Busca "S" y "E" en el maze.
    """
    start = None
    goal = None

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                goal = (r, c)

    return start, goal


def manhattan_distance(a, b):
    """
    Distancia Manhattan: buena para movimientos ortogonales.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_distance(a, b):
    """
    Distancia Euclidiana: línea recta.
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def reconstruct_path(node):
    """
    Reconstruye posiciones y acciones desde la meta hasta el inicio.
    """
    positions = []
    actions = []

    current = node
    while current is not None:
        positions.append(current.state)
        if current.action is not None:
            actions.append(current.action)
        current = current.parent

    positions.reverse()
    actions.reverse()
    return positions, actions


def find_exit(maze, heuristic_type="manhattan"):
    """
    Resuelve el laberinto usando best_first_search con f = g + h.
    """
    start, goal = find_start_and_goal(maze)
    if start is None or goal is None:
        return None

    # Movimientos permitidos (sin diagonales)
    moves = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
    }

    def actions(state):
        """
        Devuelve acciones válidas desde state.
        """
        r, c = state
        possible = []

        # Recorremos el diccionario moves:
        # name = "UP", "DOWN", ...
        # (dr, dc) = (-1,0), (1,0), ...
        for name, (dr, dc) in moves.items():
            nr, nc = r + dr, c + dc

            # Validar límites
            if nr < 0 or nr >= len(maze) or nc < 0 or nc >= len(maze[0]):
                continue

            # Validar pared
            if maze[nr][nc] == "#":
                continue

            possible.append(name)

        return possible

    def result(state, action):
        """
        Aplica la acción y devuelve el nuevo estado.
        """
        r, c = state
        dr, dc = moves[action]
        return (r + dr, c + dc)

    def action_cost(state, action, next_state):
        """
        Según el enunciado: todas las acciones cuestan 1.
        """
        return 1

    def is_goal(state):
        """
        True si llegamos a la salida.
        """
        return state == goal

    def h(state):
        """
        Heurística: Manhattan o Euclidiana.
        """
        if heuristic_type == "euclidean":
            return euclidean_distance(state, goal)
        return manhattan_distance(state, goal)

    def f(node):
        """
        f(n) = g(n) + h(n)
        g(n) = node.path_cost
        """
        return node.path_cost + h(node.state)

    problem = Problem(
        initial=start,
        goal=goal,
        actions=actions,
        result=result,
        action_cost=action_cost,
        is_goal=is_goal
    )

    solution_node = best_first_search(problem, f)
    if solution_node is None:
        return None

    return reconstruct_path(solution_node)


# ============================================================
# Prueba rápida
# ============================================================

if __name__ == "__main__":
    maze = [
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "S", "#", " ", "#", " ", "E", "#"],
        ["#", " ", " ", " ", "#", " ", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"]
    ]

    result_data = find_exit(maze, heuristic_type="manhattan")

    if result_data is None:
        print("No se encontró una ruta a la salida.")
    else:
        positions, actions_taken = result_data
        print("Ruta encontrada (posiciones):", positions)
        print("Acciones tomadas:", actions_taken)