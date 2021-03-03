from datetime import datetime
from random import randint


"#######################CLASS########################"
class city:
    def __init__(self,name):
        self.__name = name
        self.__temperature = randint(18,30)
        self.__weather = ["Clean","Cloudy","Windy","Stormy"] [randint(0,3)]

    def getName(self):
        return self.__name

    def getTemperature(self):
        return self.__temperature

    def getWeather(self):
        return self.__weather

    def setTemperature(self,temperature:int):
        self.__temperature = temperature

    def setWeather(self,status):
        if status not in ["Clean","Cloudy","Windy","Stormy"]:
            pass
        else:
            self.__weather = status
    def __str__(self):
        return self.__name

class fly:
    def __init__(self,wherefrom:city,where:city,date:datetime):
        self.__date = date
        self.__where = where
        self.__wherefrom = wherefrom


    def delay(self,minutes:int):
        day = self.__date.day
        hour = self.__date.hour     # 7
        minute = self.__date.minute # 40

        if (minute + minutes) >= 60:
            hour += int((minute+minutes)/60)
            minute = (minute + minutes ) % 60

            if hour >= 24:
                day += int(hour / 24)
                hour = hour % 24

                newDate = datetime(self.__date.year,self.__date.month,day,hour,minute)
                self.__date = newDate

        newDate = datetime(self.__date.year,self.__date.month,day,hour,minute)
        self.__date = newDate

    def getDate(self):
        return self.__date
    def getWhere(self):
        return self.__where
    def getWherefrom(self):
        return self.__wherefrom

class Passenger:
    def __init__(self,name:str,surname:str,id:int):
        self.__name = name
        self.__surname = surname
        self.__id = id

    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname
    def getId(self):
        return self.__id

class ticket:
    def __init__(self,passenger:Passenger,flight:fly,seat:str):
        self.__passenger = passenger
        self.__flight = flight
        self.__seatno = seat
    def __str__(self):
        string = """
        Name:           {}
        Surname:        {}
        Id:             {}
        Fly Date:       {}
        Fly Hour:       {}
        Where:      {}
        Where From: {}      Weather: {}
        Seat No:        {}
        """.format(self.__passenger.getName(), self.__passenger.getSurname(),self.__passenger.getId(),self.__flight.getDate().date(),self.__flight.getDate().time(),self.__flight.getWhere().getName(),self.__flight.getWherefrom().getName(),self.__flight.getWherefrom().getWeather(),self.__seatno)
        return string

    def getFly(self):
        return self.__flight

class Pegasus:
    def __init__(self):
        self.__activeticket = list()
        self.__passiveticket = list()
        self.__activeflights = list()
        self.__passiveflights = list()

    def buyTicket(self, passanger:Passenger, flight:fly, seat:str):
        if flight in self.__activeflights:
            Ticket = ticket(passanger,flight,seat)
            self.__activeticket.append(Ticket)
            return Ticket

    def makeFlight(self, where:city, wherefrom:city, date:datetime):
        flight = fly(wherefrom,where,date)
        self.__activeflights.append(flight)
        return flight

    def ticketCancel(self,Ticket: ticket):
        if Ticket in self.__activeticket:
            self.__activeticket.remove(Ticket)
            print("Ticket has cancelled!")
        else:
            print("None Ticket!")

    def flyTook(self,flight:fly):
        for ticket in self.__activeticket:
            if ticket.getFly() == flight:
                self.__activeticket.remove(ticket)
                self.__passiveticket.append(ticket)
        self.__activeflights.remove(flight)
        self.__passiveflights.append(flight)

    def delay(self,flight:fly, minute:int):
        flight.delay(minute)


"#####################################################"

def Main():
    s = """Adana
    Adıyaman
    Afyonkarahisar
    Ağrı
    Aksaray
    Amasya
    Ankara
    Antalya
    Ardahan
    Artvin
    Aydın
    Balıkesir
    Bartın
    Batman
    Bayburt
    Bilecik
    Bingöl
    Bitlis
    Bolu
    Burdur
    Bursa
    Çanakkale
    Çankırı
    Çorum
    Denizli
    Diyarbakır
    Düzce
    Edirne
    Elazığ
    Erzincan
    Erzurum
    Eskişehir
    Gaziantep
    Giresun
    Gümüşhane
    Hakkari
    Hatay
    Iğdır
    Isparta
    İstanbul
    İzmir
    Kahramanmaraş
    Karabük
    Karaman
    Kars
    Kastamonu
    Kayseri
    Kırıkkale
    Kırklareli
    Kırşehir
    Kilis
    Kocaeli
    Konya
    Kütahya
    Malatya
    Manisa
    Mardin
    Mersin
    Muğla
    Muş
    Nevşehir
    Niğde
    Ordu
    Osmaniye
    Rize
    Sakarya
    Samsun
    Siirt
    Sinop
    Sivas
    Şırnak
    Tekirdağ
    Tokat
    Trabzon
    Tunceli
    Şanlıurfa
    Uşak
    Van
    Yalova
    Yozgat
    Zonguldak"""
    cities = list()
    for i in s.split("\n"):
        cities.append(city(i))

    pegasus = Pegasus()
    can = Passenger("Can", "Çınar", 123456789)
    flight1 = pegasus.makeFlight(cities[5], cities[67], datetime(2018,5,6,12,30))
    canticket = pegasus.buyTicket(can,flight1, "C2")
    print(canticket)
    pegasus.delay(flight1,40)
    print(canticket)
    flight2 = pegasus.makeFlight(cities[4],cities[5],datetime(2018,5,7,5,45))
    x = ticket(can,flight2,"C1")
    pegasus.ticketCancel(x)


if __name__ == "__main__":
    Main()