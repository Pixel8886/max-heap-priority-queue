class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        size = len(self._heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < size and self._heap[left_child] < self._heap[smallest]:
                smallest = left_child
            if right_child < size and self._heap[right_child] < self._heap[smallest]:
                smallest = right_child

            if smallest == index:
                break

            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            index = smallest

    def insert(self, priority, value):
        entry = (-priority, self._counter, value)
        self._counter += 1
        self._heap.append(entry)
        self._sift_up(len(self._heap) - 1)

    def extract_max(self):
        if not self._heap:
            raise IndexError("Очередь пуста")
        max_entry = self._heap[0]
        last_entry = self._heap.pop()
        if self._heap:
            self._heap[0] = last_entry
            self._sift_down(0)
        return max_entry[2]

    def peek_max(self):
        if not self._heap:
            raise IndexError("Очередь пуста")
        return self._heap[0][2]

    def change_priority(self, old_value, new_priority):
        for i, entry in enumerate(self._heap):
            if entry[2] == old_value:
                new_entry = (-new_priority, entry[1], entry[2])
                self._heap[i] = new_entry
                self._sift_up(i)
                self._sift_down(i)
                return True
        return False

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0


def run_tests():
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50)

    pq = PriorityQueue()
    pq.insert(10, "Задача A")
    pq.insert(5, "Задача B")
    pq.insert(20, "Задача C")
    assert pq.peek_max() == "Задача C"
    print("Тест 1 (Вставка и peek_max): Пройден")

    assert pq.extract_max() == "Задача C"
    assert pq.peek_max() == "Задача A"
    print("Тест 2 (Извлечение максимума): Пройден")

    pq2 = PriorityQueue()
    pq2.insert(5, "Первый")
    pq2.insert(5, "Второй")
    pq2.insert(5, "Третий")
    assert pq2.extract_max() == "Первый"
    assert pq2.extract_max() == "Второй"
    print("Тест 3 (FIFO при равных приоритетах): Пройден")

    pq3 = PriorityQueue()
    pq3.insert(10, "A")
    pq3.insert(20, "B")
    pq3.insert(30, "C")
    pq3.change_priority("A", 100)
    assert pq3.peek_max() == "A"
    print("Тест 4 (Изменение приоритета): Пройден")

    pq4 = PriorityQueue()
    try:
        pq4.extract_max()
        assert False
    except IndexError:
        print("Тест 5 (Обработка пустой очереди): Пройден")

    print("=" * 50)
    print("ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()