# - Поиск в ширину вычисляет кратчайший путь в невзвешенном графе.
# - Алгоритм Дейкстры вычисляет кратчайший путь во взвешенном графе.
# - Алгоритм Дейкстры работает только в том случае, если все веса поло­жительны.
# - При наличии отрицательных весов используйте алгоритм Беллмана­ Форда.
from PIL import Image
myImage = Image.open('algorithms/dijcstra.png');
# myImage.show()  # чтобы посмотреть условие, убери шарп в начале строки 

# Для реализации этого примера понадобятся три хеш - таблицы.
# ГРАФ(GRAPH)  стоимости(COSTS)  РОДИТЕЛИ(PARENTS)
# Хеш-таблицы стоимостей и родителей будут обновляться по ходу работы
# алгоритма. Сначала необходимо реализовать граф.

graph = {}
graph['start'] = {}             # описываем хэш таблицу графа
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# Стоимость узла определяет, сколько времени потребу­ется для перехода
#  к этому узлу от начального узла. Вы
# знаете, что переход от начального узла к узлу В занимает
# 2 минуты . Вы знаете, что для перехода к узлу А требует­
# ся 6 минут (хотя, возможно, вы найдете более быстрый
# путь). Вы не знаете, сколько времени потребуется для достижения 
# конечно­го узла. Если стоимость еще неизвестна, она считается бесконечной.

infinity = float('inf')         # определяем бесконечность
costs = {}                      # описываем хэш таблицу стоииости
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}                    # создаем хэш таблицу родителей
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []                  # массив для отслеживания обраб. элем.

def find_lowest_cost_node(costs):       #
    lowest_cost = float('inf')          #
    lowest_cost_node = None             #
    for node in costs:                  # перебираем все узлы
        cost = costs[node]              #
        if cost < lowest_cost and node not in processed:    
            lowest_cost = cost          # если это узел с наим. стоимостью
            lowest_cost_node = node     # из уже виденных и он еще не был обработан, то
    return lowest_cost_node             # он назначается новым улом с наименьшей стоимостью

def find_lowest_cost(graph):
    node = find_lowest_cost_node(costs)     # находим узел с наим. значением
    while node is not None:                 # если обработаны все узлы, цикл завершен
        cost = costs[node]                  #
        neighbors = graph[node]             #
        for n in neighbors.keys():          # перебираем всех соседей тек. узла
            new_cost = cost + neighbors[n]  # 
            if costs[n] > new_cost:         # если к соседу можно добраться быстрее
                costs[n] = new_cost         # через тек. узел, обновляем стоимость узла
                parents[n] = node           # этот узел становится новым родителем для соседа
        processed.append(node)              # узел помечается как обработанный
        node = find_lowest_cost_node(costs) # найти след. узел для обработки и повт. цикл
    return print(f'Кратчайший путь займет {cost} минут')    

find_lowest_cost(graph)