class DataHouse:
    def __init__(self):
        self.sign_num        = None
        self.is_ascendant    = False
        self.asc_signlon     = None
        self.asc_minute      = None
        self.asc_second      = None
        self.planet          = {}

class Chart:
    def __init__(self, data:dict) :
        self.data = data
    
    def degree_minute_second(self, lon:float):
        """calculate degree minute and second"""
        deg = lon % 30
        minutes = int((lon - int(lon)) * 60)
        seconds = (lon - int(lon) - minutes / 60) * 3600
        return {"signlon": int(deg), "minute": minutes, "second": int(seconds)}
    
    def lagnaChart(self):
        """calculate lagna chart"""
        houses = []
        planets = self.data
        temp = planets["Asc"]["sign_num"]
        for _ in range (0, 12):
            if temp > 12:
                temp = 1
            
            data = DataHouse()
            data.sign_num = temp
            houses.append(data)
            temp += 1
        
        lagna = self.degree_minute_second(planets["Asc"]["lon"])
        houses[0].is_ascendant = True
        houses[0].asc_signlon  = lagna["signlon"]
        houses[0].asc_minute   = lagna["minute"]
        houses[0].asc_second   = lagna["second"]

        for house in range(len(houses)):
            for planet in planets:
                if planet == "Asc":
                    continue
                if planets[planet]["sign_num"] == houses[house].sign_num:
                    temp = self.degree_minute_second(planets[planet]["lon"])
                    houses[house].planet[planet] = temp
                    houses[house].planet[planet]["lon"] = planets[planet]["lon"]
                    houses[house].planet[planet]["retrograde"] = planets[planet]["retrograde"]
        
        return houses
    
    def moonChart(self):
        """calculate moon chart"""
        houses  = []
        planets = self.data
        temp    = planets["MOON"]["sign_num"]
        asc_house = 0
        for _ in range (0, 12):
            if temp > 12:
                temp = 1

            if temp == planets["Asc"]["sign_num"]:
                asc_house = len(houses)
            data = DataHouse()
            data.sign_num = temp
            houses.append(data)
            temp += 1
        
        lagna = self.degree_minute_second(planets["Asc"]["lon"])
        houses[asc_house].is_ascendant = True
        houses[asc_house].asc_signlon  = lagna["signlon"]
        houses[asc_house].asc_minute   = lagna["minute"]
        houses[asc_house].asc_second   = lagna["second"]

        for house in range(len(houses)):
            for planet in planets:
                if planet == "Asc":
                    continue
                if planets[planet]["sign_num"] == houses[house].sign_num:
                    temp = self.degree_minute_second(planets[planet]["lon"])
                    houses[house].planet[planet] = temp
                    houses[house].planet[planet]["lon"] = planets[planet]["lon"]
                    houses[house].planet[planet]["retrograde"] = planets[planet]["retrograde"]
        
        return houses


