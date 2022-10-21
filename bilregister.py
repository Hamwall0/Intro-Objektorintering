class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        self.brand = new_brand

        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
    def set_color(self, new_color):
        self.color = new_color
        
            
       
a_car = Car("Fiat", "råsa", 10)
b_car = Car("volvo", "grön", 5)
a_car.get_brand()#det skriver ut bil märket 
b_car.get_brand()
b_car.set_color("råsa")
b_car.get_color()
