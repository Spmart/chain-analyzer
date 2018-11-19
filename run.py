import analyzer as an
# G = (VT, VN, P, S)
# V* - все, включая пустую цепочку
# V+ - все, исключая пустую цепочку
greet_message = 'Введите грамматику. Пустая цепочка задается как "ЭПС".'
VT_message = 'Введите множество терминальных символов через запятую:'
VN_message = 'Введите множество нетерминальных символов через запятую:'
P_message = 'Введите правила в формате "a>Aa|a" через запятую:'
S_message = 'Введите начальный символ:'

RR_message = 'Это регулярная грамматика, выровненная вправо'
RL_message = 'Это регулярная грамматика, выровненная влево'
CF_message = 'Это контекстно-свободная грамматика'
CD_message = 'Это контекстно-зависимая грамматика'
TZ_message = 'Это грамматика типа 0'

print(greet_message)
VT = input(VT_message).split(',')  # терминалы
VN = input(VN_message).split(',')  # нетерминалы
P = input(P_message).split(',')  # правила
P = an.parse_rules(P)  # преобразовать правила из строки в словарь
# DEBUG
# print(an.is_regular_right(VT, VN, P))
# print(an.is_regular_left(VT, VN, P))
# print(an.is_context_free(VT, VN, P))
# print(an.is_context_depending(VT, VN, P))

if an.is_regular_right(VT, VN, P):
    print(RR_message)
elif an.is_regular_left(VT, VN, P):
    print(RL_message)
elif an.is_context_free(VT, VN, P):
    print(CF_message)
elif an.is_context_depending(VT, VN, P):
    print(CD_message)
else:
    print(TZ_message)
