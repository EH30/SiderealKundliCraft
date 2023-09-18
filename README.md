# SiderealKundliCraft
     
SiderealKundliCraft is a simple Python package designed for astrology enthusiasts. This package empowers users to calculate charts and determine planetary positions within the zodiac signs, adhering to the sidereal system.   

# Example
```
from SiderealKundliCraft import SiderealAstroData, chart

if __name__ == "__main__":
    # Example UTC: +5:30 which is used by India
    # Example Location Mumbai India latitude: 19.0760 and Longitude: 72.8777 
    # Year: 2009 Month: 3  Day: 30 Hour: 9 Minute: 36 Second: 0 utc_hour: 5 utc_minute: 30 latitude: 19.0760 Longitude: 72.8777 ayanamsa: ay_lahiri 
    year  = 2009
    month = 3
    day = 30
    hour = 9
    minute = 36
    second = 0
    utc_hour = 5
    utc_minute = 30
    latitude = 19.0760
    longitude =  72.8777
    ayanamsa = "ay_lahiri"
    data = SiderealAstroData.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayan=ayanamsa)
    kundli = chart.Chart(data.planets_rashi()).lagnaChart() # returns list with all the houses in Lagna Chart
    # kundli[0] = house 1      
    # kundli[1] = house 2   
    # ...   
    # ...   
    # kundli[11] = house 12

    # kundli[0].sign_num returns rashi sign in first house.   
    # kundli[0].planets returns dict with all the planet information in first house.   
    for house in range(len(kundli)):
        if kundli[house].is_ascendant == True:
            print("Asc Signlon: ", kundli[house].asc_signlon)
            print("Asc minute: ", kundli[house].asc_minute)
            print("Asc sec: ", kundli[house].asc_second)
            print("Asc: {0}:{1}:{2}".format(kundli[house].asc_signlon, kundli[house].asc_minute, kundli[house].asc_second))
        print("house: {0} sign_num: {1} planet: {2}".format(house+1, kundli[house].sign_num, kundli[house].planets))
```   
#       
```   
# Output: 
# Asc Signlon:  7
# Asc minute:  36
# Asc sec:  23
# Asc: 7:36:23
# house: 1 sign_num: 2 planet: {'moon': {'signlon': 0, 'minute': 25, 'second': 57, 'lon': 30.43269224654518, 'retrograde': False}}
# house: 2 sign_num: 3 planet: {}
# house: 3 sign_num: 4 planet: {'ketu': {'signlon': 12, 'minute': 18, 'second': 13, 'lon': 102.30385130530328, 'retrograde': True}}
# house: 4 sign_num: 5 planet: {'saturn': {'signlon': 22, 'minute': 45, 'second': 32, 'lon': 142.75898718206952, 'retrograde': True}}
# house: 5 sign_num: 6 planet: {}
# house: 6 sign_num: 7 planet: {}
# house: 7 sign_num: 8 planet: {}
# house: 8 sign_num: 9 planet: {'pluto': {'signlon': 9, 'minute': 18, 'second': 8, 'lon': 249.30237002216532, 'retrograde': False}}
# house: 9 sign_num: 10 planet: {'jupiter': {'signlon': 24, 'minute': 45, 'second': 57, 'lon': 294.76607252592436, 'retrograde': False}, 'rahu': {'signlon': 12, 'minute': 18, 'second': 13, 'lon': 282.3038513053033, 'retrograde': True}}
# house: 10 sign_num: 11 planet: {'mars': {'signlon': 17, 'minute': 46, 'second': 46, 'lon': 317.77956968504066, 'retrograde': False}, 'uranus': {'signlon': 29, 'minute': 35, 'second': 8, 'lon': 329.5855638533189, 'retrograde': False}, 'neptune': {'signlon': 1, 'minute': 32, 'second': 57, 'lon': 301.54936905595946, 'retrograde': False}}
# house: 11 sign_num: 12 planet: {'sun': {'signlon': 15, 'minute': 36, 'second': 21, 'lon': 345.6060505603411, 'retrograde': False}, 'mercury': {'signlon': 14, 'minute': 35, 'second': 44, 'lon': 344.59557987848166, 'retrograde': False}, 'venus': {'signlon': 11, 'minute': 47, 'second': 37, 'lon': 341.7936220400737, 'retrograde': True}}
# house: 12 sign_num: 1 planet: {}

```   


#   
kundli[0] = house 1      
kundli[1] = house 2  
...   
...   
kundli[11] = house 12

kundli[0].sign_num returns rashi sign number in first house.   
kundli[0].planets returns dict with all the planet information in first house.

ayanamsa you can use:   
"ay_fagan_bradley"   
"ay_lahiri"   
"ay_deluce"   
"ay_raman"   
"ay_krishnamurti"  
"ay_sassanian"   
"ay_aldebaran_15tau"  
"ay_galcenter_5sag"      
   
# 
```kundli[0].sign_num```: returns sign number in the first house    
```kundli[0].asc_signlon```: returns the ascendant degree    
```kundli[0].asc_minute```: returns the ascendant minute    
```kundli[0].asc_second```: returns the ascendant second   
```kundli[0].planets```:   returns dict with planet information in the first house   
#
``` chart.Chart```:    
- ```chart.Chart(data.planets_rashi()).lagnaChart()```: returns Lagna Chart    
- ```chart.Chart(data.planets_rashi()).moonChart()```: returns Moon Chart   
#

   
```  
# Example  
data = SiderealAstroData.AstroData(year, month, day, hour, minute, second, utc_hour, utc_minute, latitude, longitude, ayan=ayanamsa)
kundli = chart.Chart(data.planets_rashi()).lagnaChart() # returns list with all the houses in Lagna Chart
```

# Installl
```   
pip install SiderealKundliCraft
```   
or    
download the files from https://github.com/EH30/SiderealKundliCraft   
then cd to the folder and enter the command:    

```   
pip install .
```   
