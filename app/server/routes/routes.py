from app.classes.eshop.operations_module import basket

routes = [
    {
        'method': 'GET',
        'path': 'basket/checkout',
        'call': basket.checkout()
    }
]

