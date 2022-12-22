#                      ДОМАШНЕЕ ЗАДАНИЕ К СЕМИНАРУ 2

# ЗАДАЧА № 1. Напишите программу, которая принимает на вход вещественное число 
#             и показывает сумму его цифр.

# number = input('Enter a real number: ')
# number1 = number.replace(',', '')
# number2 = number1.replace('.', '')
# stroka = list(number2)
# result = 0             

# for i in stroka:
#     i = int(i)         
#     result += i

# print(f'The sum of the digits of the number {number} is equal to {result}')

# ЗАДАЧА № 2. Напишите программу, которая принимает на вход число N 
#             и выдает набор произведений чисел от 1 до N.

# number = int(input('Enter an integer: '))
# list = [i * 1 for i in range(1, number + 1)]
# print(list)           

# result = 1                
# resultNum = []
# for j in list:
#     result *= j
#     resultNum.append(result)

# print(f'A set of works from 1  to {number} = {resultNum} ')    

# Задача № 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
#             и выведите на экран их сумму.

# number = int(input('Enter the number: '))
# rez = dict()
# summ = 0
# for i in range(1, number + 1):
#     rez[i] = round((1+1/i)**i, 2)
# print(f'Для N={number} {rez}')
# print(f'Сумма {sum(rez.values())}')

# ЗАДАЧА № 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#             Найдите произведение элементов на указанных позициях. 
#             Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# num = int(input("Ведите число: "))  
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(-num, num))
# print(my_list)


# path = 'file.txt'
# data = open(path, 'w')
# data.write('2\n')
# data.write('4\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# mult = 1
# for line in data:
#     mult*=my_list[int(line)]
    
# print(mult)

# ЗАДАЧА 5. Реализуйте алгоритм перемешивания списка.

def shuffleArr(array):
    #print(array, array[0])      #[1, 2, 3, 4, 5, 6, 7, 8]     1

    print(f'Массив для перемешивания: {array}')

    # Подготовка к работе рандомайзера
    minEl = 0                # миним. индексМассива = 0
    maxEl = len(array)-1     # макс. индексМассива

    print(f'Мин.индекс: {minEl} , макс. индекс: {maxEl}')    # стартМассива: 1 конецМассива:8

    import random   # Импорт модуля для рандомайзера
    for i in array:
        idxRndm = random.randint(minEl, maxEl)  # создание рандомного индекса
        #print(idxRndm, end=' | ')  # рандомн.знач. индексов от 0 до 7

        #print(i, array[i-1])    # 1,1   2,2 ...  7,7    8,8

        tmp = i     # сохр.текущее значение во временн.переменную
        print(f'TMP: {tmp} => индекс для {array[i-1]}: { array.index(i) }')

        print(f'Рандом. индекс {idxRndm}: значение массива { array[idxRndm] }')

        print(f'i ДО замены = {i} ')
        i = array[idxRndm]
        print(f'i ПОСЛЕ замены = {i} \n')

        #print(array.index(idxRndm))

        # array.index(i) = tmp

        print(array)







shuffleArr([1,2,3,4,5,6,7,8])