
def isLeapYear(year):
    # Hier müssen Sie erweitern ...
    if ( year % 4 == 0  and year % 100 != 0 ):
        return True
    elif ( year % 400 == 0 ):
        return True
    else: 
        return False

def main():
    isLeapYear(2025)

if __name__ == "__main__":
    main()
