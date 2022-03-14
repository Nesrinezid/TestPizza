from cmath import e


class CartePizza:

    def __init__(self, pizza=[]):
        self.pizza=pizza

    # def is_empty(self):
    # # checking the length
    # if len(list) == 0:
    #     # returning true as length is 0
    #     return True
    # # returning false as length is greater than 0
    # return False

    def nb_pizzas(self):
     return len(self.pizza)    

    def is_empty(self):
        return len(self.pizza)==0 

    def add_pizzas(self,pizza):
        self.pizza.append(pizza)


    def delete(self,pizza):
        self.pizza.remove(pizza)


