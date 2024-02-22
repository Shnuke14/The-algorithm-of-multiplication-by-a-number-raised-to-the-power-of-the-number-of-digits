def multiply(n):
  n = str(n)
  ## Фильтрация на "+" и "-"
  digits = len(''.join(filter(lambda x: x not in ['+', '-'], n)))
  return int(n) * (5 ** digits)

## Начальное число
n = 10

## Степень числа 5, которая зависит от количества цифр в числе
digits = 0

## Вывод ответа
multiply(n)