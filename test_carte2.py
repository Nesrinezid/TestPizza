from unittest.mock import Mock
from CartePizza import CartePizza


def test_init_cp():
    cp = CartePizza()
    assert cp.pizzas == []

def test_is_empty_success():
    cp = CartePizza()
    cp.pizzas=[]
    assert cp.is_empty()


def test_is_empty_failure():
    cp = CartePizza()
    pizza = Mock()
    cp.pizzas=[pizza]
    assert cp.is_empty()

def test_nb_pizza():
    pizza= Mock()
    cp=CartePizza()
#on a une pizza 
    cp.pizzas = [pizza]  
# tester si y'a une pizza      
    assert cp.nb_pizzas()==1

def test_remove_pizza():
    pizza=Mock()    #si on a besoin de l'objet pizza on fait mock
    pizza2 = Mock()

    cp = CartePizza()
    cp.pizzas = [pizza, pizza2]
    cp.remove_pizza(pizza)

    assert cp.pizzas == [pizza2]
