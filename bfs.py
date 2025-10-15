from collections import deque
from typing import List
from typing import Dict
from typing import Set
from typing import Tuple

Ciudad = str
Grafo = Dict[Ciudad, List[Tuple[Ciudad, int]]]


def BFS(G,origen, destino):
    
    if origen not in G or destino not in G:
        return None
    
    visitado: Set [Ciudad] = set ([origen])
    pred: Dict[Ciudad, Ciudad] = {origen: None}
    Q = deque([origen])
    
    while Q:
        u = Q.popleft()
        if u == destino:
            break
        for v, _ in G[u]:
            if v not in visitado:
                visitado.add(v)
                pred[v] = u
                Q.append(v)

    if destino not in pred:
        return None

    # reconstruir
    camino: List [Ciudad] = []
    actual: Ciudad = destino
    while actual is not None:
        camino.append(actual)
        actual = pred[actual]
    camino.reverse()
    return camino


# ---------- (2) Factor horario ----------
def factor_horario(minutos: int) -> float:
    minutos = minutos % (24*60)
    if 0 <= minutos < 6*60:
        return 1.0
    if 6 * 60 <= minutos <16*60:
        return 2.0
    return 1.5
   
def siguiente_cambio (minutos : int) -> int:
    md = minutos % (24*60)
    dia_base = minutos - md
    bordes = [6 * 60, 16 * 60, 24 * 60]
    for b in bordes:
        if md < b:
            return dia_base + b
    return dia_base + 24 * 60 

def tiempo_tramo_respetando_horario(inicio: int, duracion_base: int) -> int:
    tiempo_real = 0
    tiempo_base_consumido = 0
    t = inicio
    
    while tiempo_base_consumido < duracion_base:
        factor = factor_horario(t)
        # Avanzamos 1 minuto real
        tiempo_real += 1
        t += 1
        # El tiempo base que consumimos depende del factor
        tiempo_base_consumido += 1.0 / factor
    
    return tiempo_real




def tiempo_total(g: Grafo, camino: List[Ciudad], inicio_min: int) -> Tuple[float, int]: 
    tiempo_total_real = 0.0
    tiempo_actual = inicio_min    
    for u, v in zip(camino, camino[1:]):
       
        peso_base = next(peso for vecino, peso in g[u] if vecino == v)
        factor = factor_horario(tiempo_actual)
        
        tiempo_tramo = peso_base * factor
        
        tiempo_total_real += tiempo_tramo
        tiempo_actual += int(tiempo_tramo)
        
    return tiempo_total_real, tiempo_actual


def add_edge(g: Grafo, u: Ciudad, v: Ciudad, peso: int):
   
    g.setdefault(u, []).append((v, peso))
    g.setdefault(v, []).append((u, peso))

# ---------- Grafo () ----------
def grafo_rumania_completo() -> Grafo:
    g: Grafo = {}
    ciudades = [
        "Oradea", "Zerind", "Sibiu", "Arad", "Rimnicu Vilcea", "Fagaras", 
        "Timisoara", "Pitesti", "Bucharest", "Lugoj", "Mehadia", "Drobeta", 
        "Craiova", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"
    ]
    
    add_edge(g, "Oradea", "Zerind", 71)
    add_edge(g, "Oradea", "Sibiu", 151)
    add_edge(g, "Zerind", "Arad", 75)
    add_edge(g, "Sibiu", "Arad", 140)
    add_edge(g, "Sibiu", "Rimnicu Vilcea", 80)
    add_edge(g, "Sibiu", "Fagaras", 99)
    add_edge(g, "Arad", "Timisoara", 118)
    add_edge(g, "Rimnicu Vilcea", "Pitesti", 97)
    add_edge(g, "Fagaras", "Bucharest", 211)
    add_edge(g, "Timisoara", "Lugoj", 111)
    add_edge(g, "Lugoj", "Mehadia", 70)
    add_edge(g, "Mehadia", "Drobeta", 75)
    add_edge(g, "Drobeta", "Craiova", 120)
    add_edge(g, "Rimnicu Vilcea", "Craiova", 146)
    add_edge(g, "Craiova", "Pitesti", 138)
    add_edge(g, "Pitesti", "Bucharest", 101)
    add_edge(g, "Bucharest", "Giurgiu", 90)
    add_edge(g, "Bucharest", "Urziceni", 85)
    add_edge(g, "Urziceni", "Hirsova", 98)
    add_edge(g, "Hirsova", "Eforie", 86)
    add_edge(g, "Urziceni", "Vaslui", 142)
    add_edge(g, "Vaslui", "Iasi", 92)
    add_edge(g, "Iasi", "Neamt", 87)
    return g


# ---------- Pruebas rápidas () ----------
if __name__ == "__main__":
    g = grafo_rumania_completo()
    path = BFS(g, "Giurgiu", "Urziceni")
    print("Camino (BFS, aristas):", path)

    # Ejemplo del enunciado:
    # Viaje a las 5:00 → primera franja (factor 1.0) para Giurgiu→Bucharest,
    # luego cruza 6:00 y la segunda tiene factor 2.0.
    inicio_5am = 5 * 60
    if path:
        print("Tiempo total iniciando 5:00:", tiempo_total(g, path, inicio_5am), "min")

    # Mismo viaje iniciando 4:00 (ambos tramos antes de 6:00 si el primer tramo termina a tiempo):
    inicio_4am = 4 * 60
    if path:
        print("Tiempo total iniciando 4:00:", tiempo_total(g, path, inicio_4am), "min")

    

