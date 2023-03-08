import time
class Kraj:
    def __init__(self, nazwa, ekonomia=50, wojsko=50, ludnosc=50, ekologia=50, satysfakcja=50):
        self.nazwa = nazwa
        self.ekonomia = ekonomia
        self.wojsko = wojsko
        self.ludnosc = ludnosc
        self.ekologia = ekologia
        self.satysfakcja = satysfakcja
        
    def checker(self):
        if self.ekonomia <= 0:
            time.sleep(1)
            print("jesteś w wielkim jak piwniczak sasinowym długu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    def koniec(self):
        if self.satysfakcja <= 0:
            time.sleep(1)
            print("Ludność się zbuntowała bo jesteś słabym pszyfudcom i zostałeś ukrzyżowany za swoje grzechy")
            time.sleep(1)
            print("https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing")
            time.sleep(1)
            exit()
        if self.wojsko <= 0:
            time.sleep(1)
            print("Twoje wojsko jest zbyt słabe i Kim Jong Un podarował ci uzbrojoną handmade atomic bomb")
            time.sleep(1)
            print("https://drive.google.com/file/d/17GAollhLRgM22b8HepU3msyuvP6AW8ja/view?usp=sharing")
            time.sleep(1)
            exit()
        if self.ludnosc <= 0:
            time.sleep(1)
            print("Byłeś mega samotny i pociąłeś się mydłem w płynie a potem skoczyłeś z dywanu.")
            time.sleep(1)
            print("https://drive.google.com/file/d/10VleoghoIasBFFJCI836n7PloeMiWynK/view?usp=sharing")
            time.sleep(1)
            exit()

    def __str__(self):
        return f"{self.nazwa} - ekonomia: {self.ekonomia}, wojsko: {self.wojsko}, ludnosc: {self.ludnosc}, ekologia: {self.ekologia}, satysfakcja ludności: {self.satysfakcja}"