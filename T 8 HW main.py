\Завдання 1 

import heapq
def minimize_cost(cables):
    """
    Знаходить мінімальні загальні витрати на об'єднання мережевих кабелів.
    Аргументи:
    cables (list): Список довжин кабелів.
    Повертає:
    int: Мінімальні загальні витрати на об'єднання кабелів.
    """
    # Ініціалізуємо мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки залишилося більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        combined = first + second
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, combined)
        
        # Додаємо витрати на об'єднання до загальної суми
        total_cost += combined
    
    return total_cost
# Приклад використання
if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    result = minimize_cost(cables)
    print(f"Мінімальні загальні витрати: {result}")  




\Завдання (необовʼязкове) 

import heapq
def merge_k_lists(lists):
    """
    Об'єднує кілька відсортованих списків у один відсортований список.
    Аргументи:
    lists (list of lists): Список відсортованих списків.
    Повертає:
    list: Відсортований список, отриманий шляхом об'єднання всіх вхідних списків.
    """
    min_heap = []
    
    # Додаємо перші елементи всіх списків до купи
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(min_heap, (sorted_list[0], i, 0))
    
    result = []
    
    # Поки купа не порожня
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо є наступний елемент у тому ж списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result
# Приклад використання
if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list) 

