# Основные концепции связанного списка
# Каждый элемент связанного списка называется узлом ,
# и каждый узел имеет два разных поля:
# - DATA содержат значение, которое должно быть сохранено в узле.
# - NEXT содержит ссылку на следующий узел в списке.
# Первый узел называется head, и он используется в качестве отправной
# точки для любой итерации по списку. Последний узел должен иметь next 
# ссылку, указывающую None на конец списка.
# collections.deque Используется почти всегда для работы со стеком или
# с очередью. Но также можно реализовать связанный список вручную.

# создаем класс для представления связанног списка:



class LinkedList:
    def __init__(self):
        self.head = None

# __repr__это специальный метод, используемый для представления 
# объектов класса в виде строки. __repr__вызывается repr() встроенной
#  функцией. Вы можете определить собственное строковое 
# представление объектов вашего класса, используя __repr__метод.
    def __repr__(self):                 
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)   

# метод проходит по списку и дает каждый узел. Самое важное, 
# что нужно помнить об этом __iter__, это то, что вам нужно всегда 
# проверять, что текущий node не является None. Когда это условие
# равно True, это означает, что вы достигли конца своего связанного списка.
# После получения текущего узла вы хотите перейти к следующему узлу в списке.
# Вот почему вы добавляете node = node.next
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
 
 # Вставка нового узла в начало списка, вероятно, является самой простой
 # вставкой, поскольку вам не нужно проходить весь список, чтобы сделать это.
 # Все дело в создании нового узла и указании на head него списка.
 # вы устанавливаете self.headссылку nextна новый узел, чтобы новый узел 
 # указывал на старый self.head. После этого вам нужно указать, 
 # что новым head в списке является вставленный узел.   
    def add_first(self, node):
        node.next = self.head
        self.head = node

# Вставка нового узла в конец списка заставляет вас сначала пройти весь 
# связанный список и добавить новый узел, когда вы дойдете до конца. Вы не
# можете просто добавить в конец, как в обычном списке, потому что в 
# связанном списке вы не знаете, какой узел является последним.
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

# Вставка между двумя узлами добавляет еще один уровень сложности к и без
# того сложным вставкам связанного списка, потому что есть два разных 
# подхода, которые вы можете использовать:
# - Вставка после существующего узла
# - Вставка перед существующим узлом
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None: 
            raise Exception("List is empty")
        if self.head.data == target_node_data: 
            return self.add_first(new_node)
        prev_node = self.head
        for node in self: 
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data) 

# Чтобы удалить узел из связанного списка, вам сначала
# нужно просмотреть список, пока не найдете узел, который хотите
# удалить. Как только вы найдете цель, вы хотите связать ее предыдущий
#  и следующий узлы. Это повторное связывание удаляет целевой узел из списка.
# Это означает, что вам нужно отслеживать предыдущий узел по мере 
# перемещения по списку. 
    def remove_node(self, target_node_data):
        if self.head is None: 
            raise Exception("List is empty")
        if self.head.data == target_node_data: 
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self: 
            if node.data == target_node_data:
                previous_node.next = node.next
                return
        previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data) 

# создаем класс для представления каждого узла:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data



llist = LinkedList()
first_node = Node("a")
llist.head = first_node
print(llist)
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
llist.add_before("a", Node("aaaa"))
llist.remove_node("a")
print(llist)
for node in llist:
    print(node)
