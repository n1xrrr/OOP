#Графы
#u - ребро | v - вершина     
#add_edge(u, v) — для добавления рёбер. X
#display() — для отображения графа. X
#dfs(start) — для выполнения поиска в глубину и вывода посещённых вершин.
#bfs(start) — для выполнения поиска в ширину и вывода посещённых вершин.
# https://evileg.com/ru/post/512/ - bfs 
# https://habr.com/ru/companies/otus/articles/660725/ - dfs 
# https://www.youtube.com/watch?v=VehB3eglQMQ&t - graph 

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs(start):
        ...
        
    def bfs(graph, root):
        ...
              
    def dfs(self, start):
        """Запускает поиск в глубину с заданной вершины start."""
        visited = set()
        stack = [start]  # Используем список как стек

        while stack:
            vertex = stack.pop()  # Извлекаем последний элемент из стека
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                # Добавляем соседей в стек
                for neighbour in self.graph.get(vertex, []):
                    if neighbour not in visited:
                        stack.append(neighbour)

    def bfs(self, start):
        """Запускает поиск в ширину с заданной вершины start."""
        visited = set()
        queue = [start]  # Используем список как очередь
        visited.add(start)

        while queue:
            vertex = queue.pop(0)  # Извлекаем первый элемент из очереди
            print(vertex, end=' ')
            for neighbour in self.graph.get(vertex, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)  # Добавляем в конец очереди
