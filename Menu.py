def calc_menu():
    stop_work = False
    while(stop_work != True):
        print("Выберите операцию:")
        print("1 +; 2 -; 3 *; 4 /; 5 выход")
        user_input = int(input())
        if(user_input == 1 ):
            from Addition import Addit
            ad = Addit
            print(ad)
            print('')
        elif(user_input == 2):
            from Substraction import Substract
            sub = Substract
            print(sub)
            print('')
        elif(user_input == 3):
            from Multiplication import Multi
            mult = Multi
            print(mult)
            print('')
        elif(user_input == 4):
            from Division import Divi
            di = Divi
            print(di)
            print('')
        elif(user_input == 5):
            print("Работа закончена")
            stop_work = True
        else:
            print("Некорректное значение")
calc_menu()