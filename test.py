def apply_discount(product,discount):
    price = int(product['цена']*(1.0 - discount))
    assert 0<=price<=product['цена']
    return price


shoes = {'имя': 'Модные туфли', 'цена': 14900}

if __name__ == '__main__':
    print(apply_discount(shoes,0.9))