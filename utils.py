typesOfPizza = {
    "Margherita": {
        "medium": {
            "price": 28.90
        },
        "big": {
            "price": 38.20
        }
    },
    "Funghi": {
        "medium": {
            "price": 29.75
        },
        "big": {
            "price": 39.10
        }
    },
    "Salami": {
        "medium": {
            "price": 30
        },
        "big": {
            "price": 41.10
        }
    },
    "Hawajska": {
        "medium": {
            "price": 31.20
        },
        "big": {
            "price": 42.40
        }
    },
    "Capricciosa": {
        "medium": {
            "price": 29.50
        },
        "big": {
            "price": 38.90
        }
    },
}

def getPriceOfPizza(type,size):
    return typesOfPizza[type][size]["price"]