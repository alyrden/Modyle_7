from pprint import pprint


class Product:

  def __init__(self, name, weigth, category):
      self.name = name
      self.weigth = weigth
      self.category = category

  def __str__(self):
      return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    # def get_products(self):
name = 'products.txt'
file = open(name, 'a')
file.write('\n345')
file.close()
print(file)
        # return
#
# s1 = Shop()
# p1 = Product('Potato', 50.5, 'Vegetables')
# p2 = Product('Spaghetti', 3.4, 'Groceries')
# # p3 = Product('Potato', 5.5, 'Vegetables')
# #
# print(p2)  # __str__
#
# s1.add(p1, p2, p3)
#
# print(s1.get_products())
