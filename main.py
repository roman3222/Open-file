def food_book():
    with open('book.txt', 'r', encoding = 'utf8') as cook_book:
        global book
        book = {}
        for line in cook_book:
            dish_name = line
            book = {dish_name: []}
            ingredient_count = cook_book.readline()
            for i in range(int(ingredient_count)):
                emp = cook_book.readline()
                ingredient, quantity, measure = emp.split('|')
                dinner = {'ingredient': ingredient, 'quantity': int(quantity), 'measure': measure}
                book[dish_name].append(dinner)
            cook_book.readline()
            print(book)
    return
food_book()

for i in book:
    print(i['Омлет'])



















