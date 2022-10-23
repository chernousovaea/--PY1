src = not False and True or False and not True

# result = True and True or False and False # избавились от отрицания
# result = True or False # избавились от логического "И"
# result = True # избавились от логического "ИЛИ"
# TODO расписать упрощение выражения

result = True  # TODO подставить результат выражения

print(src == result)
