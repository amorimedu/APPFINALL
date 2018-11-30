

class Cars:

    def __init__(self, model, brand, year, price, plate):

        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.plate = plate


    def get_model(self):

        return self.model

    def get_plate(self):

        return self.plate

    def get_sale(self):

        return 'Comprador: '+ self.purchaser.get_purchaser_name() + '/ Vendedor: '+ self.seller.get_seller_name()

    def register_sale(self, seller, purchaser):

        self.seller = seller
        self.purchaser = purchaser

    def get_data(self):

        return self.model, self.brand, self.year, self.price, self.plate

    def get_price(self):

        return self.price