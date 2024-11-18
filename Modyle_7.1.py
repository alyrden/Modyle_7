
from pprint import pprint

class Product:

    def __init__(self, name, weigth, category):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weigth}, {self.category}"

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
         file_all = open(self.__file_name, 'r', encoding='utf-8')
         return file_all.read()
    def add(self, *products):

        current_products = set(self.get_products().splitlines())

        new_product = []
        for product in products:
            product_str = str(product)
            if product_str in current_products:
                print(f"Продукт {product_str} уже есть в магазине")
            else:
                new_product.append(product_str)
                current_products.add(product_str)

        if new_product:
            file_a = open(self.__file_name, 'a', encoding='utf-8')
            file_a.write('\n'.join(new_product) + '\n')
            file_a.close()
            
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
