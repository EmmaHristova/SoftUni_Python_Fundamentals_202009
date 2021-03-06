# 06-02. OBJECTS AND CLASSES [Exercise]
# 03. Catalogue

class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        sub_products = [p for p in self.products if p[0] == first_letter]
        return sub_products

    def __repr__(self):
        info = f'Items in the {self.name} catalogue:\n'
        info += '\n'.join(sorted(self.products))
        return info


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
