#Задача:
#Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
#при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

# Напишите функцию-генератор all_variants(text).
def all_variants(text):

    # Опишите логику работы внутри функции all_variants
    for x in range(len(text)):
        for y in range(len(text)-x):
            yield text[y:y+x+1]

#Вызовите функцию all_variants и выполните итерации.
a = all_variants("abc")
for i in a:
    print(i)








