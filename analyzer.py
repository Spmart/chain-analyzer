def contains_all(str, set):
    """Проверить, что 'str' содержит все символы из 'set'"""
    return 0 not in [c in str for c in set]


def is_context_depending(VT, VN, P):  # если грамматика относится к типу 1
    """Проверяет, относится ли грамматика к первому типу (КЗ)"""
    left_sides = list(P.keys())  # все левые части правил
    right_sides = list(P.values())  # все правые части правил
    VT_and_VN = ''.join(VT + VN)
    for left_side in left_sides:  # каждую левую часть
        if not contains_all(VT_and_VN, left_side):
            return False
    for right_side in right_sides:  # каждую правую часть
        for item in right_side:  # каждый элемент правой части
            if not contains_all(VT_and_VN, item) and item != 'ЭПС':
                return False
    for key in left_sides:  # проверить, что левые части меньше соответствующих правых
        values = P.get(key)  # получить правую часть по ключу
        for value in values:  # проверить каждое правило
            if len(key) > len(value):
                return False
    return True  # если все проверки пройдены, то это КЗ-грамматика


def is_context_free(VT, VN, P):
    """Проверяет, относится ли грамматика ко второму типу (КС)"""
    left_sides = list(P.keys())  # все левые части правил
    right_sides = list(P.values())  # все правые части правил
    VN_str = ''.join(VN)
    VT_and_VN_str = ''.join(VT + VN)
    for left_side in left_sides:
        if not contains_all(VN_str, left_side):  # проверить левые части правил среди VN
            return False
    for right_side in right_sides:
        for item in right_side:
            if not contains_all(VT_and_VN_str, item) and item != 'ЭПС':
                return False
    return True


def is_regular_right(VT, VN, P):
    """Проверяет, относится ли грамматика к третьему типу (РП)"""
    left_sides = list(P.keys())
    right_sides = list(P.values())
    VT_str = ''.join(VT)
    VN_str = ''.join(VN)
    for left_side in left_sides:
        if not contains_all(VN_str, left_side):
            return False
    for right_side in right_sides:
        for item in right_side:
            if len(item) == 1:  # если длина строки = 1
                if not contains_all(VT_str, item):
                    return False
            elif len(item) == 2:  # если длина строки = 2
                if not contains_all(VT_str, item[0]):  # самый левый символ должен быть в VT
                    return False
                if not contains_all(VN_str, item[1]):  # самый правый символ должен быть в VN
                    return False
            else:  # если в строке больше двух позиций
                return False
    for left_side in left_sides:  # проверить, что терминалы в правилах для нетерминала идентичны
        right_side = list(P.get(left_side))  # получить правую часть для каждого нетерминала
        terminal = ''
        for item in right_side:
            if len(item) == 1:
                if terminal == '':  # если это первая итерация, то записать терминал
                    terminal = item
                if terminal != item:
                    return False
            else:
                if terminal == '':
                    terminal = item[0]
                if terminal != item[0]:
                    return False
    return True


def is_regular_left(VT, VN, P):  # вопиющее неоптимальное дублирование кода
    """Проверяет, относится ли грамматика к третьему типу (РЛ)"""
    left_sides = list(P.keys())
    right_sides = list(P.values())
    VT_str = ''.join(VT)
    VN_str = ''.join(VN)
    for left_side in left_sides:
        if not contains_all(VN_str, left_side):
            return False
    for right_side in right_sides:  # для правой стороны каждого правила
        for item in right_side:
            if len(item) == 1:  # если длина строки = 1
                if not contains_all(VT_str, item):
                    return False
            elif len(item) == 2:  # если длина строки = 2
                if not contains_all(VN_str, item[0]):  # самый левый символ должен быть в VN
                    return False
                if not contains_all(VT_str, item[1]):  # самый правый символ должен быть в VT
                    return False
            else:  # если в строке больше двух позиций
                return False
    for left_side in left_sides:  # проверить, что терминалы в правилах для нетерминала идентичны
        right_side = list(P.get(left_side))  # получить правую часть для каждого нетерминала
        terminal = ''
        for item in right_side:
            if len(item) == 1:
                if terminal == '':  # если это первая итерация, то записать терминал
                    terminal = item
                if terminal != item:
                    return False
            else:
                if terminal == '':
                    terminal = item[1]
                if terminal != item[1]:
                    return False
    return True


def parse_rules(rules):
    """Разбирает строку на составляющие. Возвращает словарь в формате 'лч : [пч, пч, пч]'"""
    rules_dict = dict()
    for rule in rules:
        left_side, right_side = rule.split('>')  # разделить строку на правую и левую часть
        right_side = list(right_side.split('|'))  # отделить каждое правило с правой стороны
        rules_dict[left_side] = right_side
    return rules_dict
