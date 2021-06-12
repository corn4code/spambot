import random

auto_marke = ["apollo", "ariel", "ats", "audi", "bentley", "bmw", "bugatti", "chevrolet", "ferrari", "ford", "hoonigan",
              "hyundai", "koenigsegg", "lamborghini", "lego", "lexus", "mclaren", "mercedes-amg", "mercedes-benz",
              "mosler", "pagani", "peel", "porsche", "quadra", "quartz", "raesr", "rimac", "rj anderson", "volkswagen",
              "w motors", "zenvo"]

if __name__ == '__main__':
    while True:
        user_input = input("Want a new car? (y/n) ")
        if user_input == "y" or user_input == "Y":
            car_to_drive = random.choice(auto_marke)
            print(f"Fahr ein Auto von {car_to_drive}")
        elif user_input == "n" or user_input == "N":
            print("Ok, by")
            break
        else:
            print("invalid input")
