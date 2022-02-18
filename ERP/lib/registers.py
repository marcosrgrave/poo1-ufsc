class Fornecedor:
    def __init__(self, name=None, email=None, phone=None, website=None, address=None) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
    
    def add_produto():
        pass


class Produto:
    def __init__(
                self, 
                name=None, 
                description=None, 
                category=None, 
                supplier=None, 
                purchase_cost=None, 
                sale_price=None
                ) -> None:
        
        self.name = name
        self.description = description
        self.category = category
        self.supplier = supplier
        self.purchase_cost = purchase_cost
        self.sale_price = sale_price
    
    def recebimento_produto(self, date=None, time=None, amount=None):
        pass

