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
        file = open(self.__file_name, 'r', encoding='utf-8')
        file.read()
        file.close()
        # return file.read()


    def add(self, *products):
        existing_products = set()
        file_name = self.get_products().strip().splitlines()

        for line in file_name:
            if line:
                name = line.split(', ')[0]
                existing_products.add(name)
        file_all = open(self.__file_name, 'a', encoding='utf-8')

        # # file_all.close()
        file_all = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name not in existing_products:
                file_all.write(f"{product}\n")
                existing_products.add(product.name)
                # file_all.close()
            else:
                print(f"Продукт {product.name} уже есть в магазине")

        file_all.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
