print('Здравствуйте!')
# date=input('Какое сегодня число? ') # 22.06.2024
# print('Сегодня',date,'Let us get started!')
print('Тема занятия','Списки. Индексация и методы списков')

food=['apple','coconut','banana']
print(food) # the entire list
print(food[0]) # select first element
# replace element
food[0]='peach' # replace the first element
print(food) # display the list with the replacement
# add element
food.append('True') # adds at the end
print(food) # ['peach', 'coconut', 'banana', 'True'] может хранить разные типы
food.extend('False')
print(food)
food.extend(['Fraud'])
print(food)
# remove element
food.remove('banana')
print(food)
# проверка наличия элеметнов в списке
print('banana' in food)
print('banana' not in food)
# вывод элементов списка
print(food[0])
print(food[0:2])
print(food[0:4:2]) # ['peach', 'True'] - справа, 4 элемента, каждый второй начиная с первого
print(food[-1]) # Fraud - последний элемент
print(food[::-1]) # наоборот
print(food[:-1]) # с конца, но без первого элемента