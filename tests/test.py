from SiderealKundliCraft import SiderealKundli

if __name__ == "__main__":
    kundli = SiderealKundli.Kundli(2009, 3, 30, 9, 30, 0, 5, 30, 19.0760, 72.8777, ayan="ay_lahiri").lagnaChart()
    
    for house in range(len(kundli)):
        if house == 0:
            print("Asc Signlon: ", kundli[house].asc_signlon)
            print("Asc minute: ", kundli[house].asc_minute)
            print("Asc sec: ", kundli[house].asc_second)
            print("Asc: {0}:{1}:{2}".format(kundli[house].asc_signlon, kundli[house].asc_minute, kundli[house].asc_second))
        print("house: {0} sign_num: {1} planet: {2}".format(house+1, kundli[house].sign_num, kundli[house].planet))


