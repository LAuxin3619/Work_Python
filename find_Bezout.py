a = int(input('>'))
b = int(input('>'))
(s_1, s_2, t_1, t_2, q) = [1, 0, 0, 1, 0]
while a % b != 0:
    while a > b:
        a -= b
        q += 1
    tmp = a
    a = b
    b = tmp
    tmp = s_2
    s_2 = s_1 - tmp * q
    s_1 = tmp
    tmp = t_2
    t_2 = t_1 - tmp * q
    t_1 = tmp
    q = 0
print(f'{s_2} {t_2}')
