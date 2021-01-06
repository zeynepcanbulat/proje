class Terrorism():
    "Bu sınıf terör aktivitelerine göre bölgelerin tehlike seviyesini ve kullanılması gereken ekipmanı temsil eder. Zeynep"
    def __init__(self,location_name):
        self.location_name = location_name
    
    def degree_of_the_danger(self,danger=0): #tehlikeyi 10 üzerinden alır.
        "Bölgenin tehlike seviyesini değişken olarak giriniz."#kırmızı yüksek tehlike seviyesini, mavi orta tehlike seviyesini, 
        if danger >= 5 and danger < 7:         # yeşil düşük tehlike seviyesini, beyaz beklenen bir tehlike olmadığını temsil eder.
            return "Mavi Bölge"
           
        if danger >= 7 and danger <= 10:
            return "Kırmızı Bölge"
           
        if danger < 5 and danger >= 3:
            return "Yeşil Bölge"
           
        if danger >= 0 and danger < 3:
            return "Beyaz Bölge"
            
        else:
            print("Lütfen belirtilen sayı aralığında değerlendirme yapın!")

    def recommended_variations(self,danger):
        "Bölgenin tehlike seviyesini değişken olarak giriniz"
        a = self.degree_of_the_danger(danger)
        if a == "Beyaz Bölge":
            return "Sadece personel öneriliyor ve bir çeşit araç"

        elif a == "Kırmızı Bölge":
            return"Bölgeye uygun tüm ekipman çeşitleri ve personel öneriliyor"

        elif a == "Yeşil Bölge":
            return "Personel ve o bölgeye uygun üç çeşit ekipman öneriliyor"

        elif a == "Mavi Bölge":
            return "Personel ve o bölgeye uygun beş çeşit ekipman öneriliyor"               
                                                                     

    def equipment_selection(self,iklim=0,deniz_kenari=0,engebeli=0):
        "iklim 'agir' veya 'hafif', deniz_kenari ve engebeli True/False şeklinde seçilmelidir."
                                                                     #bölgenin belirleyici özelliğine göre ekipman
        if deniz_kenari == False and iklim == "agir":                #seçimi yapılır. İklim agir/hafif şeklinde
            if engebeli == True:                                     #Deniz Kenarı True/False şeklinde
                return ["Jet",  "personel", "İHA","roket"]                   #engebeli True/False şeklinde girilmelidir.
            if engebeli == False:
                return ["Jet",  "personel", "tank", "İHA","roket"]                        

        elif deniz_kenari == False and iklim == "hafif":
            if engebeli == True:                                           
                return ["Jet",  "personel", "helikopter","İHA","roket"]                                 
            if engebeli == False:
                return ["Jet",  "personel", "helikopter", "tank","İHA","roket" ]                       

        elif deniz_kenari == True and iklim == "hafif":
            if engebeli == True:                                           
                return ["Jet",  "personel", "helikopter", "denizaltı","İHA","roket" ] 
            if engebeli == False:
                return ["Jet", "personel","tank", "helikopter", "denizaltı","İHA","roket"]
        elif deniz_kenari == True and iklim == "agir":
            if engebeli == True:                                           
                return ["Jet", "personel","denizaltı","İHA","roket"] 
            if engebeli == False:
                return ["Jet", "personel", "tank" ,"denizaltı","İHA","roket" ]

