favourite_foods = []

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favourite foods")
    
    choice = input("Choose an Option: ")
    
    if choice == "0":
        print("Thanks for using Favourite Food Manager!")
        break
    elif choice == "1":
        food = input("Enter your favourite food: ")
        favourite_foods.append(food)
        print(f"{food} added succesfully!")
    elif choice == "2":
        food = input("Enter food name: ")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} removed succesfully!")
        else:
            print(f"{food} doesn't exist in the list")
    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index,food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food} ")      
        else:
            print("Food list is empty!") 
    else:
        print("Invalid Choice")