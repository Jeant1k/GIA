# ПОКА нашлось (133) ИЛИ нашлось (881)

#   ЕСЛИ нашлось (133)

#     ТО заменить (133, 81)

#       ИНАЧЕ заменить (881, 13)

S = '8' * 99 + '1'
while '133' in S or '881' in S:
    if '133' in S:
        S = S.replace('133', '81', 1)
    else:
        S = S.replace('881', '13', 1)
print(S)
