print("Witamy w PKP")


def destination():
    station = ["Warszawa", "Poznań", "Kraków", "Wrocław", "Gdańsk"]
    print(station)
    print("Wybierz stacje odjazdu z listy")
    x = input("")
    print('Wybrałeś: ' + x)
    station.remove(x)
    print(station)

    print("Wybierz stacje przyjazdu z listy")
    y = input("")
    print("Wybrałeś trasę z " + x + " do " + y)
    station.remove(y)


def time_travel():
    print("dostępne godziny odjazdu:")
    travel_start_time = ("10.00", "12.00", "14.30", "18.00", "20.00")
    print(travel_start_time)
    start_time = input("")
    print("wybrałeś godzinę: " + start_time)
    if start_time != '0':
        if start_time == '10.00':
            print("Podróz zajmie ci 3 godziny i przyjedziesz o godzinie 13.00 do miejsca docelowego.")
        elif start_time == "12.00":
            print("Podróz zajmie ci 3 godziny i przyjedziesz o godzinie 15.00 do miejsca docelowego.")
        elif start_time == "14.30":
            print("Podróz zajmie ci 3 godziny i przyjedziesz o godzinie 17.30 do miejsca docelowego.")
        elif start_time == "18.00":
            print("Podróz zajmie ci 3 godziny i przyjedziesz o godzinie 21.00 do miejsca docelowego.")
        elif start_time == "20.00":
            print("Podróz zajmie ci 3 godziny i przyjedziesz o godzinie 23.00 do miejsca docelowego.")
        else:
            print("Niestety nie ma pociągu o takiej godzinie. Spróbuj na nowo wybrać godzinę wyjazdu")


def discount():
    x = 130
    y = 80
    print("1. Znizka studencka 51%")
    print("2. Znizka inwalidzka 30%")
    print("3. Znizka seniorska 25%")
    user_choice = input("")
    if user_choice != '0':
        if user_choice == '1':
            print(x * 0.49)
            if user_choice == '2':
                print( x * 0.7)
            elif user_choice == '3':
                print( x * 0.75)

def price():
    print("Cena biletu za 1 klase to 130 zł")
    print("Cena biletu za 2 klase to 80 zł")
    print("Wybierz która klasa cię interesuje")
    price_of_travel = input()
    if price_of_travel == '1':
        print("Wybrałeś 1 klasę, rodzaje znizek ponizej:")
        discount()
        if price_of_travel == '2':
            print("Wybrałeś 2 klasę, rodzaje znizek ponizej:")
            discount()
    else:
        print("Niestety nie rozpoznano komendy.")
def tickets():
    print("Czy chcesz zakupić więcej biletów?")
    quantity = input("")
    if quantity == "tak":
        price()
        if quantity == "nie":
            print("dziękujemy za skorzystanie z usług PKP")
        while quantity == "tak":
            tickets()
            if "nie":
                break

    
        
        
        




        
        

destination()
time_travel()
price()
tickets()