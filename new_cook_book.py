from pprint import pprint
import os

# Задача №1
def create_cook_book(filename, encoding='utf-8'):
    cook_book = {}

    try:
        with open(filename, encoding='utf-8') as f:
            lst = [line.strip() for line in f]
        for i, c in enumerate(lst):
            if c.isdigit():
                cook_book[lst[i-1]] = []

                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {filename} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'

filename = 'recipes.txt'
# data = cook_book(filename)
# print(data)    
    

# Задача №2
# в качестве второго аргумента решил передавать результат работы функции
def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ing_dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    # пробежимся по ключам словаря
                    ing_name = dictionary['ingredient_name']

                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}

    return ing_dict

def create_combined_list(directory):
  file_list = os.listdir(directory)
  combined_list = []
    
  for file in file_list:
    with open(directory + "/" + file, encoding='utf-8') as cur_file:
      combined_list.append([file, 0 , []])
      for line in cur_file:
        combined_list[-1][2].append(line.strip())
        combined_list[-1][1] += 1

  return sorted(combined_list, key= lambda x: x[2], reverse = True)

def create_file_from_directory(directory, filename):
  with open (filename + '.txt', 'w+', encoding='utf-8') as newfile:
      for file in create_combined_list(directory):
        newfile.write(f'Файл: {file[0]}\n')
        newfile.write(f'Длинна: {file[1]} строк\n')
        for string in file[2]:
          newfile.write(string + '\n')
        newfile.write('-------------------\n')

create_file_from_directory('text', 'new_text')

print('Задача №1:\n')
print(create_cook_book(filename))
print('\n' * 1)

print('Задача №2:\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], create_cook_book(filename), 2))
print('\n' * 1)

print('Задача №3:\n')
with open("new_text.txt", encoding='utf-8') as f:
     print(f.read())
  