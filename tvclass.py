#n= int(input(""))
#ns=int(input(""))
#for i in range(1,ns+1):
 #   print(n)
#a=int(input(""))
#n=int(input(""))
#s=a**n
#print(s)
class TV:
    def __init__(self,brand):
        self.brand=brand
        self.channel=1
        self.volume=50
        self.inches=None
        self.price=None
        self.on=False
    def increase_volume(self):
        if self.volume<100:
            self.volume+=1
    def decrease_volume(self):
        if self.volume>0:
            self.volume-=1
    def set_channel(self,channel):
        if 1 <= channel <= 50:
            self.channel=channel
    def reset_tv(self):
        self.channel=1
        self.volume=50
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
class LedTv(TV):
    def __init__(self,brand):
        super().__init__(brand)
        self.screen_thickness=None
        self.energy_usage=None
        self.lifespan=None
        self.refresh_rate=None
        self.viewing_angle=None
        self.backlight=None
        self.display_details=None
        
class PlasmaTv(TV):
    def __init__(self,brand):
        super().__init__(brand)
        self.screen_thickness=None
        self.energy_usage=None
        self.lifespan=None
        self.refresh_rate=None
        self.viewing_angle=None
        self.backlight=None
        self.display_details=None
led_tv=LedTv("MI")
led_tv.set_channel(5)
led_tv.increase_volume()
led_tv.decrease_volume()
print(led_tv.status()) 

    
    
           
          
