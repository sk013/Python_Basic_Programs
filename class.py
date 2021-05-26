class laptop:
    sale_discount = 50
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    def apply_discount(self):
        return self.price - (laptop.sale_discount/100)*self.price


laptop1 = laptop("dell", "inspiron15" , 32000)
print(laptop1.brand_name)
print(laptop1.model_name)
print(laptop1.price)
print(laptop1.apply_discount())