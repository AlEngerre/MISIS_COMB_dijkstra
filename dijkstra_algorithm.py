import heapq

def dijkstra(graph, start):
    # Проверка на наличие отрицательных весов
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if weight < 0:
                raise ValueError("Алгоритм Дейкстры не поддерживает графы с отрицательными весами рёбер.")

    # Инициализация
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Очередь с приоритетами (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропуск если расстояние уже не актуально
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
