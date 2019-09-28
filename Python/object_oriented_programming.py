"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 11-Sep-19 at 19:23
"""

class Computer:
    # For every object init gets called once
    def __init__(self, *special):
        self.special = special
        print ("From __init__")

    # Attributes -> Variables
    # Behaviours -> Methods
    def latitude3400(self):
        print("Features of : {}".format(self.special))

    def optiplex3070(self):
        print("Features of : {}".format(self.special))

# Constructor
comp1 = Computer("Dell Latitude 3400 (New 2019)",'Touch',"Core i7, 16GB DDR4, 2GB GeForce MX130 Graphics, 256GB M.2 SSD, 1TB 5400 RPM, 42 Watt Hr, Backlit Keyboard")
comp2 = Computer('Dell Optiplex 3070','WiFi', "24\" Display, Core i5, 2GB Nvidia GTX, 1x8GB DDR4, 1TB 7200 RPM")
print ("Type of com1 : " + str(type(comp1)))
print ("Configurations : ")
#comp1.config()

Computer.latitude3400(comp1)
comp2.optiplex3070()

