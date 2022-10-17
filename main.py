def food_book():
    with open('book.txt', 'r', encoding = 'utf8') as cook_book:
        global book
        book = {}
        for line in cook_book:
            dish_name = line.strip()
            book[dish_name] = []
            ingredient_count = cook_book.readline()
            for i in range(int(ingredient_count)):
                emp = cook_book.readline()
                ingredient, quantity, measure = emp.split('|')
                dinner = {'ingredient': ingredient, 'quantity': int(quantity), 'measure': measure.strip()}
                book[dish_name].append(dinner)
            cook_book.readline()
    print(book)
    return book
food_book()

def get_shop_list_by_dishes(dishes, person_count):
    for dish in book:
        return dish




print(get_shop_list_by_dishes(['Утка по-пекински'], 2))



dct = {1:[1, 2, 3, 4], 4: [6, 7, 8]}
res = list(dct)
print(res)


























