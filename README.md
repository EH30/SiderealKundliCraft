# SiderealKundliCraft

SidreakKundliCraft helps generate kundli.     
SiderealKundliCraff is a simple Python package designed for astrology enthusiasts. This package empowers users to calculate Lagna Kundli (also known as birth charts) and determine planetary positions within the zodiac signs, adhering to the sidereal system.   

# Example
```
from SiderealKundliCraft import SiderealKundli, chart

if __name__ == "__main__":
    data = SiderealKundli.Kundli(2009, 3, 30, 9, 30, 0, 5, 30, 19.0760, 72.8777, ayan="ay_lahiri")
    kundli = chart.Chart(data.planets_rashi()).lagnaChart()
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
        print("house: {0} sign_num: {1} planet: {2}".format(house+1, kundli[house].sign_num, kundli[house].planet))

```   
#       
```   
# Output: 
# Asc Signlon:  6
# Asc minute:  2
# Asc sec:  30
# Asc: 6:2:30
# house: 1 sign_num: 2 planet: {'MOON': {'signlon': 0, 'minute': 22, 'second': 26, 'lon': 30.374020847229794, 'retrograde': False}}
# house: 2 sign_num: 3 planet: {}
# house: 3 sign_num: 4 planet: {'KETU': {'signlon': 12, 'minute': 18, 'second': 14, 'lon': 102.30407210529324, 'retrograde': True}}
# house: 4 sign_num: 5 planet: {'SATURN': {'signlon': 22, 'minute': 45, 'second': 33, 'lon': 142.75927901924277, 'retrograde': True}}
# house: 5 sign_num: 6 planet: {}
# house: 6 sign_num: 7 planet: {}
# house: 7 sign_num: 8 planet: {}
# house: 8 sign_num: 9 planet: {'PLUTO': {'signlon': 9, 'minute': 18, 'second': 8, 'lon': 249.30235776590413, 'retrograde': False}}
# house: 9 sign_num: 10 planet: {'JUPITER': {'signlon': 24, 'minute': 45, 'second': 55, 'lon': 294.7652798639882, 'retrograde': False}, 'RAHU': {'signlon': 12, 'minute': 18, 'second': 14, 'lon': 282.30407210529324, 'retrograde': True}}
# house: 10 sign_num: 11 planet: {'MARS': {'signlon': 17, 'minute': 46, 'second': 34, 'lon': 317.77631081211916, 'retrograde': False}, 'URANUS': {'signlon': 29, 'minute': 35, 'second': 7, 'lon': 329.5853325776043, 'retrograde': False}, 'NEPTUNE': {'signlon': 1, 'minute': 32, 'second': 57, 'lon': 301.54924666197826, 'retrograde': False}}
# house: 11 sign_num: 12 planet: {'SUN': {'signlon': 15, 'minute': 36, 'second': 6, 'lon': 345.60193267617626, 'retrograde': False}, 'MERCURY': {'signlon': 14, 'minute': 35, 'second': 13, 'lon': 344.58717542538943, 'retrograde': False}, 'VENUS': {'signlon': 11, 'minute': 47, 'second': 46, 'lon': 341.7961896197394, 'retrograde': True}}
# house: 12 sign_num: 1 planet: {}

```   
   
#  
```  
SiderealKundli.Kundli(year, month, day, hour, minute, second, 
                 utc_offset_hours, utc_offset_minutes, latitude, longitude, ayan="lahiri")   
```
returns a list with all the houses.   
example:   
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
```kundli[0].asc_signlon```: returns the ascendant degree    
```kundli[0].asc_minute```: returns the ascendant minute    
```kundli[0].asc_second```: returns the ascendant second   

```kundli[0].sign_num```: returns sign number in the first house    
```kundli[0].planet```:   returns dict with planet information in the first house   
#
``` chart.Chart```:    
- ```chart.Chart(data.planets_rashi()).lagnaChart()```: returns Lagna Chart    
- ```chart.Chart(data.planets_rashi()).moonChart()```: returns Moon Chart   
#
   
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
